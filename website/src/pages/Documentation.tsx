import { useState, useEffect } from 'react';
import { useParams, Link, useNavigate, useSearchParams } from 'react-router-dom';
import { FileText, Book, Search, ChevronRight } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import documentsData from '../data/documents.json';
import { DocumentMetadata } from '../types';
import { 
  pageVariants, 
  fadeInUp, 
  staggerContainer, 
  staggerItem,
  fadeInScale,
  slideInLeft,
  scaleIn 
} from '../utils/animations';

const documents = documentsData as DocumentMetadata[];

function Documentation() {
  const { docId } = useParams<{ docId?: string }>();
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const [searchTerm, setSearchTerm] = useState('');
  const [documentContent, setDocumentContent] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const categories = ['All', 'Product', 'HR', 'Legal'];
  
  // Get selected category from URL params, default to 'All'
  const selectedCategory = searchParams.get('category') || 'All';

  const filteredDocs = documents.filter(doc => {
    const matchesCategory = selectedCategory === 'All' || doc.category.toLowerCase() === selectedCategory.toLowerCase();
    const matchesSearch = !searchTerm || 
      doc.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      doc.description?.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const selectedDoc = docId ? documents.find(d => d.id === docId) : null;

  const handleCategoryChange = (category: string) => {
    // Navigate back to main documentation list with the selected category
    if (docId) {
      navigate(`/documentation?category=${category}`);
    } else {
      setSearchParams(category === 'All' ? {} : { category });
    }
  };

  // Fetch document content when a document is selected
  useEffect(() => {
    if (selectedDoc) {
      setIsLoading(true);
      setDocumentContent('');
      
      fetch(selectedDoc.path)
        .then(response => response.text())
        .then(html => {
          setDocumentContent(html);
          setIsLoading(false);
        })
        .catch(error => {
          console.error('Error loading document:', error);
          setDocumentContent('<p>Error loading document content.</p>');
          setIsLoading(false);
        });
    }
  }, [selectedDoc]);

  return (
    <motion.div 
      className="min-h-screen bg-background"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageVariants}
    >
      {/* Hero Header - Enhanced */}
      <section className="relative pt-20 pb-8 overflow-hidden">
        {/* Background Layer */}
        <div className="absolute inset-0 bg-black">
          {/* Subtle accent lines */}
          <div className="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-white/20 to-transparent"></div>
          <div className="absolute bottom-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-white/10 to-transparent"></div>
          <div className="absolute top-1/4 left-0 w-32 h-px bg-gradient-to-r from-primary-500/30 to-transparent"></div>
          <div className="absolute top-1/3 right-0 w-24 h-px bg-gradient-to-l from-accent-500/30 to-transparent"></div>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            className="inline-flex items-center gap-2.5 px-5 py-2.5 bg-white/10 backdrop-blur-xl rounded-full border border-white/20 mb-8"
            variants={fadeInUp}
          >
            <Book className="w-4 h-4 text-primary-400" />
            <span className="text-xs font-semibold text-white/90 tracking-wider uppercase">Documentation Library</span>
          </motion.div>
          
          <motion.h1 
            className="text-5xl md:text-6xl lg:text-7xl font-display font-black mb-6 tracking-tight leading-[1.1]"
            variants={fadeInUp}
          >
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-white via-white to-white/80">
              Documentation
            </span>
            <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-300 via-primary-200 to-accent-300">
              Center
            </span>
          </motion.h1>
          <motion.p 
            className="text-base md:text-lg text-white/60 max-w-2xl leading-relaxed font-light"
            variants={fadeInUp}
            transition={{ delay: 0.1 }}
          >
            Access technical specifications, user guides, policies, and other important documents
          </motion.p>
        </div>
      </section>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid lg:grid-cols-4 gap-8">
          {/* Sidebar */}
          <motion.div 
            className="lg:col-span-1"
            variants={slideInLeft}
          >
            <div className="bg-surface rounded-[20px] shadow-lg p-6 border border-border sticky top-24">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-700 rounded-[12px] flex items-center justify-center shadow-lg">
                  <FileText className="w-5 h-5 text-white" strokeWidth={2} />
                </div>
                <h3 className="font-bold text-text">Categories</h3>
              </div>
              <motion.div 
                className="space-y-2"
                variants={staggerContainer}
                initial="initial"
                animate="animate"
              >
                {categories.map((category) => (
                  <motion.button
                    key={category}
                    onClick={() => handleCategoryChange(category)}
                    className={`w-full text-left px-4 py-3 rounded-[12px] transition-all duration-300 font-medium ${
                      selectedCategory === category
                        ? 'bg-gradient-to-r from-primary-800/60 to-primary-900/40 text-primary-200 font-bold border border-primary-600/60 shadow-lg shadow-primary-500/20'
                        : 'text-text-muted hover:bg-surface-elevated hover:text-primary-300 border border-transparent'
                    }`}
                    variants={staggerItem}
                    whileHover={{ scale: 1.02, x: 4 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    {category}
                  </motion.button>
                ))}
              </motion.div>

              <div className="mt-6 pt-6 border-t border-border">
                <h3 className="font-bold text-text mb-4 flex items-center gap-2">
                  <div className="w-2 h-2 bg-accent-400 rounded-full"></div>
                  Quick Stats
                </h3>
                <div className="space-y-3 text-sm">
                  <div className="flex justify-between items-center p-2 rounded-lg bg-surface-elevated/50">
                    <span className="text-text-muted">Total Documents</span>
                    <span className="font-bold text-primary-300 text-base">{documents.length}</span>
                  </div>
                  <div className="flex justify-between items-center p-2 rounded-lg bg-surface-elevated/50">
                    <span className="text-text-muted">Product Docs</span>
                    <span className="font-bold text-accent-300 text-base">
                      {documents.filter(d => d.category === 'Product').length}
                    </span>
                  </div>
                  <div className="flex justify-between items-center p-2 rounded-lg bg-surface-elevated/50">
                    <span className="text-text-muted">HR Policies</span>
                    <span className="font-bold text-secondary-300 text-base">
                      {documents.filter(d => d.category === 'HR').length}
                    </span>
                  </div>
                  <div className="flex justify-between items-center p-2 rounded-lg bg-surface-elevated/50">
                    <span className="text-text-muted">Legal Docs</span>
                    <span className="font-bold text-text text-base">
                      {documents.filter(d => d.category === 'Legal').length}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Main Content */}
          <motion.div 
            className="lg:col-span-3"
            variants={fadeInUp}
            transition={{ delay: 0.2 }}
          >
            {!selectedDoc ? (
              <>
                {/* Search */}
                <motion.div 
                  className="mb-8"
                  variants={fadeInScale}
                >
                  <div className="relative group">
                    <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-text-subtle group-focus-within:text-primary-400 transition-colors" />
                    <input
                      type="text"
                      placeholder="Search documentation..."
                      value={searchTerm}
                      onChange={(e) => setSearchTerm(e.target.value)}
                      className="w-full pl-12 pr-4 py-4 bg-surface rounded-[16px] border border-border text-text placeholder-text-subtle focus:outline-none focus:ring-2 focus:ring-primary-500/50 focus:border-primary-500 transition-all duration-300 shadow-lg"
                    />
                  </div>
                </motion.div>

                {/* Results */}
                <motion.div 
                  className="mb-6 flex items-center gap-2 px-4 py-2 bg-surface-elevated/50 rounded-[12px] border border-border/50 w-fit"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: 0.3 }}
                >
                  <FileText className="w-4 h-4 text-primary-400" />
                  <span className="text-text-muted text-sm">
                    Showing <span className="font-bold text-primary-300">{filteredDocs.length}</span> documents
                  </span>
                </motion.div>

                <motion.div 
                  key={selectedCategory}
                  className="space-y-4"
                  variants={staggerContainer}
                  initial="initial"
                  animate="animate"
                >
                  <AnimatePresence mode="popLayout">
                    {filteredDocs.map((doc) => (
                      <motion.div
                        key={doc.id}
                        variants={staggerItem}
                        initial="initial"
                        animate="animate"
                        layout
                        exit={{ opacity: 0, scale: 0.95 }}
                      >
                        <Link to={`/documentation/${doc.id}`} className="block">
                          <motion.div 
                            className="relative bg-surface rounded-[20px] p-6 shadow-lg border border-border hover:shadow-2xl hover:shadow-primary-500/20 hover:border-primary-500/50 transition-all duration-500 group"
                            whileHover={{ y: -6, scale: 1.01 }}
                            transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
                          >
                            <div className="absolute inset-0 bg-gradient-to-br from-primary-900/10 to-accent-900/10 opacity-0 group-hover:opacity-100 rounded-[20px] transition-opacity duration-500"></div>
                            
                            <div className="relative flex items-start justify-between">
                              <div className="flex-1">
                                <div className="flex items-center gap-4 mb-3">
                                  <div className="w-12 h-12 bg-gradient-to-br from-primary-400 to-primary-600 rounded-[14px] flex items-center justify-center shadow-lg group-hover:scale-[1.05] group-hover:rotate-3 transition-all duration-300">
                                    {doc.type === 'Technical Specification' ? (
                                      <FileText className="w-6 h-6 text-white" strokeWidth={2} />
                                    ) : (
                                      <Book className="w-6 h-6 text-white" strokeWidth={2} />
                                    )}
                                  </div>
                                  <div className="flex-1">
                                    <h3 className="text-lg font-bold text-text group-hover:text-primary-300 transition-colors mb-2 tracking-tight">
                                      {doc.title}
                                    </h3>
                                    <div className="flex items-center gap-2 text-sm text-text-muted">
                                      <span className="px-3 py-1 bg-primary-800/40 rounded-lg text-xs font-bold border border-primary-600/40 text-primary-300">
                                        {doc.category}
                                      </span>
                                      <span className="text-text-subtle">•</span>
                                      <span className="text-xs">{doc.type}</span>
                                    </div>
                                  </div>
                                </div>
                                {doc.description && (
                                  <p className="text-text-muted text-sm mt-3 ml-16 leading-relaxed">{doc.description}</p>
                                )}
                              </div>
                              <div className="w-10 h-10 bg-primary-800/30 rounded-[12px] flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all duration-300 ml-4">
                                <ChevronRight className="w-5 h-5 text-primary-300 group-hover:translate-x-0.5 transition-transform" strokeWidth={2.5} />
                              </div>
                            </div>
                          </motion.div>
                        </Link>
                      </motion.div>
                    ))}
                  </AnimatePresence>
                </motion.div>

                {filteredDocs.length === 0 && (
                  <motion.div 
                    className="text-center py-16"
                    variants={scaleIn}
                    initial="initial"
                    animate="animate"
                  >
                    <motion.div
                      animate={{ 
                        y: [0, -10, 0],
                      }}
                      transition={{
                        duration: 2,
                        repeat: Infinity,
                        ease: "easeInOut"
                      }}
                    >
                      <FileText className="w-16 h-16 text-text-subtle mx-auto mb-4" />
                    </motion.div>
                    <h3 className="text-xl font-semibold text-text mb-2">No documents found</h3>
                    <p className="text-text-muted mb-6">Try adjusting your search or filter criteria</p>
                    <motion.button
                      onClick={() => {
                        setSearchTerm('');
                        setSearchParams({});
                      }}
                      className="btn-primary"
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                    >
                      Clear Filters
                    </motion.button>
                  </motion.div>
                )}
              </>
            ) : (
              <>
                {/* Document View */}
                <motion.div
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.3 }}
                >
                  <Link
                    to="/documentation"
                    className="inline-flex items-center gap-2 px-4 py-2 bg-surface-elevated rounded-[12px] border border-border hover:border-primary-500/50 text-primary-300 hover:text-primary-200 mb-6 font-medium transition-all duration-300 hover:-translate-x-1"
                  >
                    <ChevronRight className="w-4 h-4 rotate-180" />
                    Back to Documentation
                  </Link>
                </motion.div>
                <motion.div 
                  className="relative bg-surface rounded-[20px] p-8 shadow-lg border border-border"
                  variants={fadeInScale}
                  initial="initial"
                  animate="animate"
                >
                  {isLoading ? (
                    <div className="text-center py-12">
                      <motion.div
                        className="inline-block rounded-full h-12 w-12 border-b-2 border-primary-300"
                        animate={{ rotate: 360 }}
                        transition={{
                          duration: 1,
                          repeat: Infinity,
                          ease: "linear"
                        }}
                      />
                      <motion.p 
                        className="mt-4 text-text-muted"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.2 }}
                      >
                        Loading document...
                      </motion.p>
                    </div>
                  ) : (
                    <motion.div 
                      className="prose max-w-none"
                      dangerouslySetInnerHTML={{ __html: documentContent }}
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ delay: 0.2, duration: 0.4 }}
                    />
                  )}
                </motion.div>
              </>
            )}
          </motion.div>
        </div>
      </div>
    </motion.div>
  );
}

export default Documentation;

