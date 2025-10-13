import { useState, useMemo } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { Search, Filter, ArrowRight, Package } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import productsData from '../data/products.json';
import { Product } from '../types';
import { 
  pageVariants, 
  fadeInUp, 
  staggerContainer, 
  staggerItem,
  fadeInScale
} from '../utils/animations';

const products = productsData as Product[];

function Products() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [searchTerm, setSearchTerm] = useState(searchParams.get('search') || '');
  const [selectedCategory, setSelectedCategory] = useState(searchParams.get('category') || 'All');
  const [sortBy, setSortBy] = useState(searchParams.get('sort') || 'name');

  const categories = ['All', ...Array.from(new Set(products.map(p => p.category)))];

  const filteredProducts = useMemo(() => {
    let filtered = products.filter(p => p.status === 'Active');

    // Filter by category
    if (selectedCategory !== 'All') {
      filtered = filtered.filter(p => p.category === selectedCategory);
    }

    // Filter by search term
    if (searchTerm) {
      const term = searchTerm.toLowerCase();
      filtered = filtered.filter(p =>
        p.product_name.toLowerCase().includes(term) ||
        p.description.toLowerCase().includes(term) ||
        p.category.toLowerCase().includes(term)
      );
    }

    // Sort
    filtered.sort((a, b) => {
      switch (sortBy) {
        case 'name':
          return a.product_name.localeCompare(b.product_name);
        case 'price-low':
          return a.msrp - b.msrp;
        case 'price-high':
          return b.msrp - a.msrp;
        case 'newest':
          return new Date(b.release_date).getTime() - new Date(a.release_date).getTime();
        default:
          return 0;
      }
    });

    return filtered;
  }, [selectedCategory, searchTerm, sortBy]);

  const handleCategoryChange = (category: string) => {
    setSelectedCategory(category);
    const params = new URLSearchParams(searchParams);
    if (category === 'All') {
      params.delete('category');
    } else {
      params.set('category', category);
    }
    setSearchParams(params);
  };

  const handleSearchChange = (value: string) => {
    setSearchTerm(value);
    const params = new URLSearchParams(searchParams);
    if (value) {
      params.set('search', value);
    } else {
      params.delete('search');
    }
    setSearchParams(params);
  };

  const handleSortChange = (value: string) => {
    setSortBy(value);
    const params = new URLSearchParams(searchParams);
    params.set('sort', value);
    setSearchParams(params);
  };

  return (
    <motion.div 
      className="min-h-screen bg-background"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageVariants}
    >
      {/* Header - More refined and integrated */}
      <div className="relative bg-gradient-to-br from-primary-900/40 via-background to-background text-text pt-32 pb-8 overflow-hidden">
        {/* Subtle background effects */}
        <div className="absolute inset-0">
          <motion.div 
            className="absolute top-10 right-1/4 w-[300px] h-[300px] bg-primary-400/8 rounded-full blur-[120px]"
            animate={{ scale: [1, 1.2, 1], opacity: [0.08, 0.12, 0.08] }}
            transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
          />
          <motion.div 
            className="absolute bottom-10 left-1/4 w-[250px] h-[250px] bg-accent-400/6 rounded-full blur-[100px]"
            animate={{ scale: [1, 1.3, 1], opacity: [0.06, 0.1, 0.06] }}
            transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 2 }}
          />
        </div>
        
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="inline-flex items-center gap-2 px-4 py-1.5 bg-gradient-to-r from-primary-600 to-secondary-600 text-background rounded-full text-[11px] font-black mb-5 shadow-lg shadow-primary-600/30"
            variants={fadeInUp}
          >
            <Package className="w-3.5 h-3.5" strokeWidth={2.5} />
            <span className="tracking-wide">Product Catalog</span>
          </motion.div>
          
          <motion.h1 
            className="text-2xl md:text-3xl lg:text-4xl font-display font-black mb-4 tracking-tight"
            variants={fadeInUp}
          >
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-300 via-text to-accent-300">
              Our Products
            </span>
          </motion.h1>
          <motion.p 
            className="text-sm md:text-base text-text-muted max-w-3xl leading-relaxed"
            variants={fadeInUp}
            transition={{ delay: 0.1 }}
          >
            Discover our comprehensive range of industrial automation solutions, designed to enhance productivity and efficiency.
          </motion.p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Filters and Search - Enhanced Design */}
        <motion.div 
          className="mb-12 space-y-6"
          variants={fadeInUp}
          transition={{ delay: 0.2 }}
        >
          {/* Search Bar */}
          <div className="flex flex-col md:flex-row gap-4">
            <motion.div 
              className="flex-1 relative group"
              variants={fadeInScale}
              whileHover={{ scale: 1.005 }}
            >
              <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 w-4 h-4 text-text-subtle group-hover:text-primary-400 transition-colors duration-300" />
              <input
                type="text"
                placeholder="Search products by name, category, or description..."
                value={searchTerm}
                onChange={(e) => handleSearchChange(e.target.value)}
                className="w-full pl-11 pr-5 py-2.5 border-2 border-border rounded-2xl focus:ring-2 focus:ring-primary-500/50 focus:border-primary-500/70 outline-none transition-all duration-300 bg-surface/80 backdrop-blur-sm hover:border-primary-500/50 hover:bg-surface text-text text-sm placeholder:text-text-subtle shadow-lg hover:shadow-xl"
              />
            </motion.div>
            <motion.div
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              <select
                value={sortBy}
                onChange={(e) => handleSortChange(e.target.value)}
                className="w-full md:w-auto px-5 py-2.5 border-2 border-border rounded-2xl focus:ring-2 focus:ring-primary-500/50 focus:border-primary-500/70 outline-none bg-surface text-text text-sm font-semibold cursor-pointer hover:border-primary-500/50 hover:bg-surface-elevated transition-all duration-300 shadow-lg hover:shadow-xl"
              >
                <option value="name">Sort by Name</option>
                <option value="price-low">Price: Low to High</option>
                <option value="price-high">Price: High to Low</option>
                <option value="newest">Newest First</option>
              </select>
            </motion.div>
          </div>

          {/* Category Filters */}
          <motion.div 
            className="flex items-center gap-2.5 flex-wrap bg-surface/60 backdrop-blur-sm p-4 rounded-2xl border border-border/60 shadow-lg"
            variants={staggerContainer}
            initial="initial"
            animate="animate"
          >
            <div className="flex items-center gap-2 mr-2">
              <div className="w-7 h-7 bg-gradient-to-br from-primary-500 to-primary-700 rounded-xl flex items-center justify-center shadow-md">
                <Filter className="w-4 h-4 text-white" strokeWidth={2.5} />
              </div>
              <span className="text-xs font-bold text-text">Filter by Category</span>
            </div>
            {categories.map((category) => (
              <motion.button
                key={category}
                onClick={() => handleCategoryChange(category)}
                className={`px-4 py-2 rounded-xl font-bold text-xs transition-all duration-300 ${
                  selectedCategory === category
                    ? 'bg-gradient-to-r from-primary-600 to-primary-700 text-background shadow-lg shadow-primary-500/40 border-2 border-primary-500'
                    : 'bg-surface-elevated text-text-muted hover:bg-surface hover:text-primary-300 hover:border-primary-600/40 border-2 border-border/40 hover:shadow-md'
                }`}
                variants={staggerItem}
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
                layout
              >
                {category}
              </motion.button>
            ))}
          </motion.div>

          {/* Results Count */}
          <motion.div 
            className="flex items-center gap-2 text-text-muted font-medium"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4 }}
          >
            <span className="text-xs">Showing</span>
            <motion.span 
              key={filteredProducts.length}
              className="px-3 py-1 bg-gradient-to-r from-primary-600/20 to-accent-600/20 text-primary-300 rounded-lg font-bold text-xs border border-primary-600/30 shadow-sm"
              initial={{ scale: 1.15, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.3 }}
            >
              {filteredProducts.length}
            </motion.span>
            <span className="text-xs">
              {filteredProducts.length === 1 ? 'product' : 'products'}
            </span>
          </motion.div>
        </motion.div>

        {/* Products Grid - Enhanced Cards */}
        {filteredProducts.length > 0 ? (
          <motion.div 
            className="grid md:grid-cols-2 lg:grid-cols-3 gap-8"
            variants={staggerContainer}
            initial="initial"
            animate="animate"
          >
            <AnimatePresence mode="popLayout">
              {filteredProducts.map((product, index) => (
                <motion.div
                  key={product.sku}
                  variants={staggerItem}
                  layout
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.9, transition: { duration: 0.2 } }}
                  transition={{ delay: index * 0.05, duration: 0.4 }}
                >
                  <Link
                    to={`/products/${product.sku}`}
                    className="block h-full"
                  >
                    <motion.div
                      className="bg-surface/90 backdrop-blur-sm rounded-[16px] p-5 shadow-xl border border-border hover:shadow-2xl hover:shadow-primary-500/25 hover:border-primary-500/50 transition-all duration-500 h-full group relative overflow-hidden"
                      whileHover={{ y: -8, scale: 1.015 }}
                      transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
                    >
                      {/* Hover gradient overlay */}
                      <div className="absolute inset-0 bg-gradient-to-br from-primary-900/5 to-accent-900/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-[16px]"></div>
                      
                      <div className="relative">
                        {/* Header with category badge and hover icon */}
                        <div className="mb-4 flex items-start justify-between">
                          <span className="inline-block px-3 py-1 bg-gradient-to-r from-primary-600/30 to-primary-700/30 text-primary-300 rounded-xl text-[10px] font-bold border border-primary-500/40 shadow-sm tracking-wide backdrop-blur-sm">
                            {product.category}
                          </span>
                          <div className="w-8 h-8 bg-gradient-to-br from-primary-500/20 to-accent-500/20 border border-primary-500/30 rounded-[12px] flex items-center justify-center opacity-0 group-hover:opacity-100 group-hover:scale-[1.05] transition-all duration-500 shadow-md">
                            <ArrowRight className="w-4 h-4 text-primary-300" strokeWidth={2.5} />
                          </div>
                        </div>
                
                        <h3 className="text-base font-display font-bold text-text mb-2.5 group-hover:text-primary-300 transition-colors tracking-tight leading-tight">
                          {product.product_name}
                        </h3>
                        
                        <p className="text-text-muted mb-5 line-clamp-3 text-xs leading-relaxed">
                          {product.description}
                        </p>

                        {/* Specifications Preview */}
                        {(product.payload_capacity || product.reach_mm) && (
                          <div className="mb-6 p-3 bg-surface-elevated/60 backdrop-blur-sm rounded-xl border border-border/50 space-y-2">
                            {product.payload_capacity && (
                              <div className="text-xs text-text-subtle flex items-center justify-between">
                                <span className="font-bold text-text-muted">Payload</span>
                                <span className="text-text">{product.payload_capacity}</span>
                              </div>
                            )}
                            {product.reach_mm && (
                              <div className="text-xs text-text-subtle flex items-center justify-between">
                                <span className="font-bold text-text-muted">Reach</span>
                                <span className="text-text">{product.reach_mm}</span>
                              </div>
                            )}
                          </div>
                        )}

                        {/* Price and action footer */}
                        <div className="flex justify-between items-center pt-5 border-t border-border/70">
                          <div>
                            <div className="text-[10px] text-text-muted font-bold mb-1 uppercase tracking-wider">Starting at</div>
                            <div className="text-xl font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-primary-300 to-accent-300 tracking-tight">
                              ${product.msrp.toLocaleString()}
                            </div>
                            <div className={`text-[10px] font-bold mt-1.5 ${product.inventory_on_hand > 0 ? 'text-accent-400' : 'text-text-subtle'}`}>
                              {product.inventory_on_hand > 0 ? '● In Stock' : 'Contact for Availability'}
                            </div>
                          </div>
                          <div className="text-primary-300 font-bold text-sm flex items-center gap-1 group-hover:gap-2 transition-all duration-300">
                            View
                            <ArrowRight className="w-4 h-4" strokeWidth={2.5} />
                          </div>
                        </div>
                      </div>
                    </motion.div>
                  </Link>
                </motion.div>
              ))}
            </AnimatePresence>
          </motion.div>
        ) : (
          <motion.div 
            className="text-center py-24 px-4"
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.4 }}
          >
            <div className="max-w-md mx-auto bg-surface/60 backdrop-blur-sm rounded-[24px] border border-border/60 shadow-xl p-12">
              <motion.div
                className="mb-8"
                animate={{ 
                  y: [0, -12, 0],
                }}
                transition={{
                  duration: 2.5,
                  repeat: Infinity,
                  ease: "easeInOut"
                }}
              >
                <div className="w-20 h-20 mx-auto bg-gradient-to-br from-primary-500/20 to-accent-500/20 rounded-[20px] flex items-center justify-center border border-primary-500/30 shadow-lg">
                  <Package className="w-10 h-10 text-primary-400" strokeWidth={2} />
                </div>
              </motion.div>
              <h3 className="text-2xl font-display font-bold text-text mb-3 tracking-tight">No products found</h3>
              <p className="text-text-muted mb-10 leading-relaxed">Try adjusting your search or filter criteria to find what you're looking for</p>
              <motion.button
                onClick={() => {
                  setSearchTerm('');
                  setSelectedCategory('All');
                  setSearchParams({});
                }}
                className="px-8 py-4 bg-gradient-to-r from-primary-600 to-primary-700 text-background rounded-[14px] font-bold shadow-xl hover:shadow-2xl hover:shadow-primary-500/40 transition-all duration-300 inline-flex items-center gap-2 group"
                whileHover={{ scale: 1.05, y: -3 }}
                whileTap={{ scale: 0.95 }}
              >
                <span>Clear All Filters</span>
                <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform duration-300" strokeWidth={2.5} />
              </motion.button>
            </div>
          </motion.div>
        )}
      </div>
    </motion.div>
  );
}

export default Products;

