import { useParams, Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, Package, FileText, CheckCircle } from 'lucide-react';
import { motion } from 'framer-motion';
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

function ProductDetail() {
  const { productId } = useParams<{ productId: string }>();
  const navigate = useNavigate();
  const product = products.find(p => p.sku === productId);

  if (!product) {
    return (
      <motion.div 
        className="min-h-screen bg-background flex items-center justify-center"
        initial="initial"
        animate="animate"
        variants={fadeInScale}
      >
        <div className="text-center">
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
            <Package className="w-16 h-16 text-text-subtle mx-auto mb-4" />
          </motion.div>
          <h2 className="text-2xl font-bold text-text mb-2">Product Not Found</h2>
          <p className="text-text-muted mb-6">The product you're looking for doesn't exist.</p>
            <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
              <Link to="/products" className="btn-primary">
              <ArrowLeft className="inline w-5 h-5 mr-2" />
              Back to Products
            </Link>
          </motion.div>
        </div>
      </motion.div>
    );
  }

  const relatedProducts = products
    .filter(p => p.category === product.category && p.sku !== product.sku && p.status === 'Active')
    .slice(0, 3);

  return (
    <motion.div 
      className="min-h-screen bg-background"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageVariants}
    >
      {/* Header */}
      <div className="bg-surface border-b border-border">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <motion.button
            onClick={() => navigate(-1)}
            className="flex items-center text-text-muted hover:text-primary-300 transition-colors mb-4 font-medium"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            whileHover={{ x: -2 }}
            whileTap={{ scale: 0.95 }}
          >
            <ArrowLeft className="w-5 h-5 mr-2" />
            Back
          </motion.button>
          <div className="flex items-center gap-2 text-sm text-text-muted">
            <Link to="/" className="hover:text-primary-300">Home</Link>
            <span>/</span>
            <Link to="/products" className="hover:text-primary-300">Products</Link>
            <span>/</span>
            <span className="text-text font-medium">{product.product_name}</span>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="max-w-4xl mx-auto">
          {/* Product Info */}
          <motion.div 
            className="space-y-6"
            variants={fadeInUp}
          >
            <div>
              <span className="inline-block px-3 py-1 bg-primary-800/50 text-primary-300 rounded-full text-sm font-semibold mb-4 border border-primary-600/40 shadow-sm">
                {product.category}
              </span>
              <h1 className="text-4xl font-bold font-bold text-text mb-4">
                {product.product_name}
              </h1>
              <p className="text-lg text-text-muted leading-relaxed">
                {product.description}
              </p>
            </div>

            {/* Price */}
            <div className="bg-primary-800/30 rounded-xl p-6 border border-primary-600/40 shadow-sm">
              <div className="flex items-baseline gap-2 mb-2">
                <span className="text-4xl font-bold text-primary-300">
                  ${product.msrp.toLocaleString()}
                </span>
                <span className="text-text-muted">USD</span>
              </div>
              <div className="flex items-center gap-2 text-sm">
                {product.inventory_on_hand > 0 ? (
                  <>
                    <CheckCircle className="w-4 h-4 text-secondary-300" />
                    <span className="text-secondary-300 font-semibold">In Stock ({product.inventory_on_hand} units)</span>
                  </>
                ) : (
                  <span className="text-accent-300 font-semibold">Contact for Availability</span>
                )}
              </div>
            </div>

            {/* Actions */}
            <div className="flex gap-4">
              <motion.div 
                className="flex-1"
                whileHover={{ scale: 1.01 }}
                whileTap={{ scale: 0.98 }}
              >
                <Link to="/support" className="block btn-primary text-center">
                  Request Quote
                </Link>
              </motion.div>
              <motion.div 
                className="flex-1"
                whileHover={{ scale: 1.01 }}
                whileTap={{ scale: 0.98 }}
              >
                <Link to="/customer-portal" className="block btn-outline text-center">
                  Contact Sales
                </Link>
              </motion.div>
            </div>

            {/* Additional Info */}
            <div className="grid grid-cols-2 gap-4 pt-6 border-t border-border">
              <div>
                <div className="text-sm text-text-muted mb-1">Supplier</div>
                <div className="font-semibold text-text">{product.supplier}</div>
              </div>
              <div>
                <div className="text-sm text-text-muted mb-1">Warranty</div>
                <div className="font-semibold text-text">{product.warranty_years} years</div>
              </div>
              <div>
                <div className="text-sm text-text-muted mb-1">Launch Date</div>
                <div className="font-semibold text-text">
                  {new Date(product.release_date).toLocaleDateString()}
                </div>
              </div>
              <div>
                <div className="text-sm text-text-muted mb-1">Status</div>
                <div className="font-semibold text-secondary-300">{product.status}</div>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Specifications */}
        <motion.div 
          className="mt-12 bg-surface rounded-2xl shadow-lg p-8 border border-border"
          variants={fadeInUp}
          transition={{ delay: 0.3 }}
        >
          <h2 className="text-2xl font-bold font-bold text-text mb-6 flex items-center">
            <FileText className="w-6 h-6 mr-3 text-primary-300" />
            Technical Specifications
          </h2>
          <motion.div 
            className="grid md:grid-cols-2 gap-6"
            variants={staggerContainer}
            initial="initial"
            animate="animate"
          >
            {product.weight_kg && (
              <motion.div 
                className="flex justify-between items-center py-3 border-b border-border"
                variants={staggerItem}
              >
                <span className="font-medium text-text-muted">Weight</span>
                <span className="text-text">{product.weight_kg} kg</span>
              </motion.div>
            )}
            {product.payload_capacity && (
              <div className="flex justify-between items-center py-3 border-b border-border">
                <span className="font-medium text-text-muted">Payload Capacity</span>
                <span className="text-text">{product.payload_capacity}</span>
              </div>
            )}
            {product.reach_mm && (
              <div className="flex justify-between items-center py-3 border-b border-border">
                <span className="font-medium text-text-muted">Reach</span>
                <span className="text-text">{product.reach_mm}</span>
              </div>
            )}
            {product.color_options && (
              <div className="flex justify-between items-center py-3 border-b border-border">
                <span className="font-medium text-text-muted">Color Options</span>
                <span className="text-text">{product.color_options}</span>
              </div>
            )}
            {product.configurations_available && (
              <div className="flex justify-between items-center py-3 border-b border-border">
                <span className="font-medium text-text-muted">Configurations</span>
                <span className="text-text">{product.configurations_available}</span>
              </div>
            )}
            {product.lead_time_days && (
              <div className="flex justify-between items-center py-3 border-b border-border">
                <span className="font-medium text-text-muted">Lead Time</span>
                <span className="text-text">{product.lead_time_days} days</span>
              </div>
            )}
          </motion.div>
        </motion.div>

        {/* Documentation Link */}
        <motion.div 
          className="mt-8 bg-gradient-to-r from-primary-600 to-primary-700 rounded-2xl p-8 text-text"
          variants={fadeInScale}
          initial="initial"
          animate="animate"
          transition={{ delay: 0.4 }}
          whileHover={{ scale: 1.01 }}
        >
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-2xl font-bold font-bold mb-2 text-text">Need Documentation?</h3>
              <p className="text-text/95 font-normal">
                Access technical specifications, user guides, and installation manuals
              </p>
            </div>
            <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }}>
              <Link
                to="/documentation"
                className="btn-primary bg-gradient-to-r from-accent-500 to-accent-600 text-background hover:from-accent-600 hover:to-accent-700 whitespace-nowrap"
              >
                View Docs
              </Link>
            </motion.div>
          </div>
        </motion.div>

        {/* Related Products */}
        {relatedProducts.length > 0 && (
          <motion.div 
            className="mt-16"
            variants={fadeInUp}
            initial="initial"
            animate="animate"
            transition={{ delay: 0.5 }}
          >
            <h2 className="text-3xl font-bold font-bold text-text mb-8">Related Products</h2>
            <motion.div 
              className="grid md:grid-cols-3 gap-6"
              variants={staggerContainer}
              initial="initial"
              animate="animate"
            >
              {relatedProducts.map((relatedProduct) => (
                <motion.div
                  key={relatedProduct.sku}
                  variants={staggerItem}
                >
                  <Link
                    to={`/products/${relatedProduct.sku}`}
                    className="block"
                  >
                    <motion.div
                      className="card-hover"
                      whileHover={{ scale: 1.01, y: -3 }}
                      transition={{ duration: 0.2 }}
                    >
                  <div className="mb-4">
                    <span className="inline-block px-3 py-1 bg-primary-800/50 text-primary-300 rounded-full text-sm font-semibold border border-primary-600/40 shadow-sm">
                      {relatedProduct.category}
                    </span>
                  </div>
                  <h3 className="text-lg font-semibold text-text mb-2">{relatedProduct.product_name}</h3>
                  <p className="text-text-muted text-sm mb-4 line-clamp-2">{relatedProduct.description}</p>
                  <div className="flex justify-between items-center pt-4 border-t border-border">
                    <span className="text-xl font-bold text-primary-300">
                      ${relatedProduct.msrp.toLocaleString()}
                    </span>
                      <span className="text-primary-300 text-sm font-semibold">View Details →</span>
                    </div>
                    </motion.div>
                  </Link>
                </motion.div>
              ))}
            </motion.div>
          </motion.div>
        )}
      </div>
    </motion.div>
  );
}

export default ProductDetail;

