import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ChevronRight, File, Folder, FileText, FileSpreadsheet, Code, Image as ImageIcon, FileJson, X, Download, Search } from 'lucide-react';
import fileTreeData from '../data/file_tree.json';

interface FileNode {
  name: string;
  type: 'file' | 'directory';
  path: string;
  extension?: string;
  size?: number;
  children?: FileNode[];
}

function DemoFiles() {
  const [expandedFolders, setExpandedFolders] = useState<Set<string>>(new Set(['']));
  const [selectedFile, setSelectedFile] = useState<FileNode | null>(null);
  const [fileContent, setFileContent] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  const toggleFolder = (path: string) => {
    setExpandedFolders(prev => {
      const newSet = new Set(prev);
      if (newSet.has(path)) {
        newSet.delete(path);
      } else {
        newSet.add(path);
      }
      return newSet;
    });
  };

  const getFileIcon = (extension: string) => {
    const ext = extension.toLowerCase();
    if (ext === '.json') return <FileJson className="w-4 h-4 text-yellow-400" />;
    if (ext === '.csv') return <FileSpreadsheet className="w-4 h-4 text-green-400" />;
    if (ext === '.md') return <FileText className="w-4 h-4 text-blue-400" />;
    if (ext === '.html') return <Code className="w-4 h-4 text-orange-400" />;
    if (['.jpg', '.jpeg', '.png', '.gif', '.svg'].includes(ext)) return <ImageIcon className="w-4 h-4 text-purple-400" />;
    return <File className="w-4 h-4 text-gray-400" />;
  };

  const formatFileSize = (bytes: number) => {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
  };

  const loadFileContent = async (file: FileNode) => {
    setLoading(true);
    setSelectedFile(file);
    
    try {
      const response = await fetch(`/data/${file.path}`);
      const text = await response.text();
      setFileContent(text);
    } catch (error) {
      console.error('Error loading file:', error);
      setFileContent('Error loading file content.');
    } finally {
      setLoading(false);
    }
  };

  const filterTree = (node: FileNode, query: string): FileNode | null => {
    if (!query) return node;
    
    const lowerQuery = query.toLowerCase();
    
    if (node.type === 'file') {
      return node.name.toLowerCase().includes(lowerQuery) ? node : null;
    }
    
    const filteredChildren = node.children
      ?.map(child => filterTree(child, query))
      .filter(child => child !== null) as FileNode[] | undefined;
    
    if (filteredChildren && filteredChildren.length > 0) {
      return { ...node, children: filteredChildren };
    }
    
    return node.name.toLowerCase().includes(lowerQuery) ? node : null;
  };

  const renderFileTree = (node: FileNode, level: number = 0) => {
    if (node.type === 'directory') {
      const isExpanded = expandedFolders.has(node.path);
      const hasChildren = node.children && node.children.length > 0;
      
      return (
        <div key={node.path}>
          <motion.div
            className="flex items-center gap-2 py-2 px-3 hover:bg-surface-elevated rounded-lg cursor-pointer group transition-all"
            style={{ paddingLeft: `${level * 1.5 + 0.75}rem` }}
            onClick={() => toggleFolder(node.path)}
            whileHover={{ x: 2 }}
          >
            {hasChildren && (
              <motion.div
                animate={{ rotate: isExpanded ? 90 : 0 }}
                transition={{ duration: 0.2 }}
              >
                <ChevronRight className="w-4 h-4 text-text-muted" />
              </motion.div>
            )}
            {!hasChildren && <div className="w-4" />}
            <Folder className={`w-4 h-4 ${isExpanded ? 'text-primary-400' : 'text-text-muted'}`} />
            <span className="text-sm font-medium text-text group-hover:text-primary-300 transition-colors">
              {node.name}
            </span>
            {node.children && (
              <span className="text-xs text-text-subtle ml-auto">
                {node.children.length} {node.children.length === 1 ? 'item' : 'items'}
              </span>
            )}
          </motion.div>
          
          <AnimatePresence>
            {isExpanded && node.children && (
              <motion.div
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: 'auto', opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.2 }}
                className="overflow-hidden"
              >
                {node.children.map(child => renderFileTree(child, level + 1))}
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      );
    } else {
      return (
        <motion.div
          key={node.path}
          className={`flex items-center gap-2 py-2 px-3 hover:bg-surface-elevated rounded-lg cursor-pointer group transition-all ${
            selectedFile?.path === node.path ? 'bg-primary-900/30 border border-primary-600/30' : ''
          }`}
          style={{ paddingLeft: `${level * 1.5 + 2.25}rem` }}
          onClick={() => loadFileContent(node)}
          whileHover={{ x: 2 }}
        >
          {getFileIcon(node.extension || '')}
          <span className="text-sm text-text-muted group-hover:text-text transition-colors flex-1">
            {node.name}
          </span>
          {node.size !== undefined && (
            <span className="text-xs text-text-subtle">
              {formatFileSize(node.size)}
            </span>
          )}
        </motion.div>
      );
    }
  };

  const filteredTree = filterTree(fileTreeData as FileNode, searchQuery);

  // Count total files
  const countFiles = (node: FileNode): number => {
    if (node.type === 'file') return 1;
    return node.children?.reduce((acc, child) => acc + countFiles(child), 0) || 0;
  };
  const totalFiles = countFiles(fileTreeData as FileNode);

  return (
    <div className="min-h-screen bg-background">
      {/* Hero Section */}
      <section className="relative pt-24 pb-16 overflow-hidden">
        {/* Background Effects */}
        <div className="absolute inset-0 pointer-events-none">
          <motion.div
            className="absolute top-20 left-10 w-96 h-96 bg-primary-500/20 rounded-full blur-3xl"
            animate={{
              scale: [1, 1.2, 1],
              opacity: [0.3, 0.5, 0.3],
            }}
            transition={{ duration: 8, repeat: Infinity, ease: 'easeInOut' }}
          />
          <motion.div
            className="absolute bottom-20 right-10 w-96 h-96 bg-accent-500/20 rounded-full blur-3xl"
            animate={{
              scale: [1, 1.3, 1],
              opacity: [0.3, 0.5, 0.3],
            }}
            transition={{ duration: 10, repeat: Infinity, ease: 'easeInOut', delay: 1 }}
          />
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-center"
          >
            <h1 className="text-5xl md:text-6xl font-display font-black mb-6">
              <span className="bg-gradient-to-r from-primary-400 via-primary-300 to-accent-400 bg-clip-text text-transparent">
                Demo Files
              </span>
            </h1>
            <p className="text-xl text-text-muted max-w-3xl mx-auto mb-8">
              Browse and explore all company data files including internal documents, reports, and more.
            </p>
            <div className="flex items-center justify-center gap-4 text-sm text-text-subtle">
              <div className="flex items-center gap-2 px-4 py-2 bg-surface-elevated rounded-lg border border-border">
                <File className="w-4 h-4" />
                <span>{totalFiles} Files</span>
              </div>
              <div className="flex items-center gap-2 px-4 py-2 bg-surface-elevated rounded-lg border border-border">
                <Folder className="w-4 h-4" />
                <span>5 Departments</span>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Main Content */}
      <section className="relative pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
            {/* File Browser */}
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="lg:col-span-4"
            >
              <div className="glass-effect rounded-2xl border border-border p-6 sticky top-24">
                <div className="mb-4">
                  <h2 className="text-xl font-bold text-text mb-4">File Browser</h2>
                  
                  {/* Search */}
                  <div className="relative">
                    <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-text-muted" />
                    <input
                      type="text"
                      placeholder="Search files..."
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      className="w-full pl-10 pr-4 py-2 bg-surface-elevated border border-border rounded-lg text-sm text-text placeholder-text-subtle focus:outline-none focus:ring-2 focus:ring-primary-500/50 focus:border-primary-500/50 transition-all"
                    />
                  </div>
                </div>

                <div className="overflow-y-auto max-h-[calc(100vh-300px)] scrollbar-thin scrollbar-thumb-border scrollbar-track-transparent">
                  {filteredTree ? renderFileTree(filteredTree) : (
                    <div className="text-center py-8 text-text-muted">
                      No files found
                    </div>
                  )}
                </div>
              </div>
            </motion.div>

            {/* File Viewer */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.4 }}
              className="lg:col-span-8"
            >
              <div className="glass-effect rounded-2xl border border-border overflow-hidden">
                {selectedFile ? (
                  <>
                    {/* File Header */}
                    <div className="bg-surface-elevated border-b border-border p-6">
                      <div className="flex items-start justify-between">
                        <div className="flex items-start gap-3">
                          {getFileIcon(selectedFile.extension || '')}
                          <div>
                            <h3 className="text-lg font-bold text-text">{selectedFile.name}</h3>
                            <p className="text-sm text-text-muted mt-1">
                              {selectedFile.path}
                              {selectedFile.size !== undefined && (
                                <span className="ml-2 text-text-subtle">
                                  • {formatFileSize(selectedFile.size)}
                                </span>
                              )}
                            </p>
                          </div>
                        </div>
                        <div className="flex gap-2">
                          <a
                            href={`/data/${selectedFile.path}`}
                            download
                            className="p-2 hover:bg-surface rounded-lg transition-colors"
                            title="Download file"
                          >
                            <Download className="w-4 h-4 text-text-muted" />
                          </a>
                          <button
                            onClick={() => setSelectedFile(null)}
                            className="p-2 hover:bg-surface rounded-lg transition-colors"
                            title="Close file"
                          >
                            <X className="w-4 h-4 text-text-muted" />
                          </button>
                        </div>
                      </div>
                    </div>

                    {/* File Content */}
                    <div className="p-6">
                      {loading ? (
                        <div className="flex items-center justify-center py-20">
                          <motion.div
                            className="w-12 h-12 border-4 border-primary-500/30 border-t-primary-500 rounded-full"
                            animate={{ rotate: 360 }}
                            transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
                          />
                        </div>
                      ) : (
                        <div className="bg-surface rounded-xl p-6 overflow-x-auto">
                          <pre className="text-xs text-text-muted font-mono whitespace-pre-wrap break-words">
                            {fileContent}
                          </pre>
                        </div>
                      )}
                    </div>
                  </>
                ) : (
                  <div className="flex flex-col items-center justify-center py-20 px-6 text-center">
                    <div className="w-16 h-16 bg-surface-elevated rounded-2xl flex items-center justify-center mb-4">
                      <FileText className="w-8 h-8 text-text-muted" />
                    </div>
                    <h3 className="text-xl font-bold text-text mb-2">No File Selected</h3>
                    <p className="text-text-muted max-w-md">
                      Select a file from the browser on the left to view its contents.
                    </p>
                  </div>
                )}
              </div>
            </motion.div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default DemoFiles;

