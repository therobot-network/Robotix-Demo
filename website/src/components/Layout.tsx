import { ReactNode, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Menu, X } from 'lucide-react';
import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface LayoutProps {
  children: ReactNode;
}

function Layout({ children }: LayoutProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [logoHovered, setLogoHovered] = useState(false);
  const location = useLocation();

  const navigation = [
    { name: 'Home', href: '/' },
    { name: 'Products', href: '/products' },
    { name: 'Documentation', href: '/documentation' },
    { name: 'Support', href: '/support' },
    { name: 'Company', href: '/company' },
  ];

  const isActive = (href: string) => {
    if (href === '/') return location.pathname === '/';
    return location.pathname.startsWith(href);
  };

  // Track scroll position for navbar styling
  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Close mobile menu on route change
  useEffect(() => {
    setMobileMenuOpen(false);
  }, [location.pathname]);

  // Add smooth scroll behavior
  useEffect(() => {
    document.documentElement.style.scrollBehavior = 'smooth';
    return () => {
      document.documentElement.style.scrollBehavior = 'auto';
    };
  }, []);

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header - Enhanced with scroll effects */}
      <motion.header 
        className={`sticky top-0 z-50 glass-effect border-b transition-all duration-300 ${
          scrolled 
            ? 'border-border shadow-lg shadow-black/10 bg-surface/95' 
            : 'border-border-subtle bg-surface/80'
        }`}
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
      >
        <nav className="w-full px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo and Demo Files Button */}
            <div className="flex items-center gap-3">
              <Link to="/" className="flex items-center group">
                <motion.div 
                  className="flex items-center px-5 py-2.5 rounded-[12px] border border-white/20 bg-white/5 backdrop-blur-xl relative overflow-hidden"
                  whileTap={{ scale: 0.97 }}
                  onMouseEnter={() => setLogoHovered(true)}
                  onMouseLeave={() => setLogoHovered(false)}
                  style={{
                    boxShadow: '0 4px 16px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.1)'
                  }}
                >
                  {/* Subtle gradient overlay */}
                  <div className="absolute inset-0 bg-gradient-to-br from-primary-400/10 via-transparent to-accent-400/5 pointer-events-none"></div>
                  
                  {/* Text - Animated expansion */}
                  <span 
                    className="text-base font-display font-black relative flex items-center"
                    style={{
                      letterSpacing: '0.02em',
                      background: 'linear-gradient(180deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.85) 100%)',
                      WebkitBackgroundClip: 'text',
                      backgroundClip: 'text',
                      color: 'transparent',
                      textShadow: '0 1px 3px rgba(0, 0, 0, 0.3), 0 0 8px rgba(14, 116, 144, 0.15)',
                      filter: 'drop-shadow(0 0 1px rgba(14, 116, 144, 0.2))'
                    }}
                  >
                    <span>R</span>
                    <motion.span
                      animate={{ 
                        width: logoHovered ? 'auto' : 0, 
                        opacity: logoHovered ? 1 : 0 
                      }}
                      className="inline-block overflow-hidden"
                      transition={{ 
                        duration: logoHovered ? 0.3 : 0.4, 
                        ease: [0.16, 1, 0.3, 1] 
                      }}
                    >
                      <span className="inline-block">O</span>
                    </motion.span>
                    <span>B</span>
                    <motion.span
                      animate={{ 
                        width: logoHovered ? 'auto' : 0, 
                        opacity: logoHovered ? 1 : 0 
                      }}
                      className="inline-block overflow-hidden"
                      transition={{ 
                        duration: logoHovered ? 0.3 : 0.4, 
                        ease: [0.16, 1, 0.3, 1], 
                        delay: logoHovered ? 0.05 : 0.03 
                      }}
                    >
                      <span className="inline-block">O</span>
                    </motion.span>
                    <span>T</span>
                    <motion.span
                      animate={{ 
                        width: logoHovered ? 'auto' : 0, 
                        opacity: logoHovered ? 1 : 0 
                      }}
                      className="inline-block overflow-hidden"
                      transition={{ 
                        duration: logoHovered ? 0.3 : 0.4, 
                        ease: [0.16, 1, 0.3, 1], 
                        delay: logoHovered ? 0.1 : 0.06 
                      }}
                    >
                      <span className="inline-block">I</span>
                    </motion.span>
                    <span>X</span>
                  </span>
                  
                </motion.div>
              </Link>
              
              {/* Demo Files Button */}
              <Link
                to="/demo-files"
                className="hidden md:block px-5 py-2.5 bg-gradient-to-r from-accent-600 to-accent-700 text-background rounded-lg font-bold text-sm border border-accent-500/30 relative overflow-hidden"
                style={{ 
                  letterSpacing: '0.025em',
                  boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.1), 0 4px 6px -1px rgba(245, 158, 11, 0.3)',
                  outline: 'none'
                }}
                onMouseDown={(e) => {
                  e.preventDefault();
                }}
                onClick={(e) => {
                  (e.currentTarget as HTMLAnchorElement).blur();
                }}
              >
                Demo Files
              </Link>
            </div>

            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-1">
              {navigation.map((item) => (
                <div key={item.name}>
                  <Link
                    to={item.href}
                    className={`relative px-4 py-2.5 rounded-lg font-bold text-sm ${
                      isActive(item.href)
                        ? 'bg-gradient-to-r from-primary-800/60 to-primary-700/50 text-primary-300 border border-primary-600/50 shadow-md shadow-primary-500/25'
                        : 'text-text-muted'
                    }`}
                    style={isActive(item.href) ? { 
                      letterSpacing: '0.015em',
                      boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.05)',
                      outline: 'none'
                    } : { outline: 'none' }}
                    onMouseDown={(e) => {
                      e.preventDefault();
                    }}
                    onClick={(e) => {
                      (e.currentTarget as HTMLAnchorElement).blur();
                    }}
                  >
                    {item.name}
                  </Link>
                </div>
              ))}
              <div>
                <Link
                  to="/customer-portal"
                  className="ml-3 px-5 py-2.5 bg-gradient-to-r from-primary-600 to-primary-700 text-background rounded-lg font-bold text-sm border border-primary-500/30 relative overflow-hidden"
                  style={{ 
                    letterSpacing: '0.025em',
                    boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.1), 0 4px 6px -1px rgba(14, 116, 144, 0.3)',
                    outline: 'none'
                  }}
                  onMouseDown={(e) => {
                    e.preventDefault();
                  }}
                  onClick={(e) => {
                    (e.currentTarget as HTMLAnchorElement).blur();
                  }}
                >
                  Customer Portal
                </Link>
              </div>
            </div>

            {/* Mobile menu button */}
            <motion.button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 rounded-lg hover:bg-surface-elevated transition-all"
              whileTap={{ scale: 0.9 }}
            >
              <AnimatePresence mode="wait">
                {mobileMenuOpen ? (
                  <motion.div
                    key="close"
                    initial={{ rotate: -90, opacity: 0 }}
                    animate={{ rotate: 0, opacity: 1 }}
                    exit={{ rotate: 90, opacity: 0 }}
                    transition={{ duration: 0.2 }}
                  >
                    <X className="w-5 h-5 text-text" />
                  </motion.div>
                ) : (
                  <motion.div
                    key="menu"
                    initial={{ rotate: 90, opacity: 0 }}
                    animate={{ rotate: 0, opacity: 1 }}
                    exit={{ rotate: -90, opacity: 0 }}
                    transition={{ duration: 0.2 }}
                  >
                    <Menu className="w-5 h-5 text-text" />
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.button>
          </div>

          {/* Mobile Navigation */}
          <AnimatePresence>
            {mobileMenuOpen && (
              <motion.div 
                className="md:hidden py-4 border-t border-border overflow-hidden"
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: 'auto', opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
              >
                <div className="flex flex-col space-y-2">
                  {navigation.map((item, index) => (
                    <motion.div
                      key={item.name}
                      initial={{ x: -20, opacity: 0 }}
                      animate={{ x: 0, opacity: 1 }}
                      transition={{ delay: index * 0.05 }}
                    >
                      <Link
                        to={item.href}
                        className={`block px-4 py-3 rounded-lg font-bold text-sm transition-all duration-300 ${
                          isActive(item.href)
                            ? 'bg-gradient-to-r from-primary-800/60 to-primary-700/50 text-primary-300 border border-primary-600/50 shadow-md shadow-primary-500/25'
                            : 'text-text-muted hover:bg-surface-elevated hover:text-primary-300 hover:border hover:border-border/50'
                        }`}
                        style={isActive(item.href) ? { 
                          letterSpacing: '0.015em',
                          boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.05)',
                          outline: 'none'
                        } : { outline: 'none' }}
                        onMouseDown={(e) => {
                          e.preventDefault();
                        }}
                        onClick={(e) => {
                          (e.currentTarget as HTMLAnchorElement).blur();
                        }}
                      >
                        {item.name}
                      </Link>
                    </motion.div>
                  ))}
                  <motion.div
                    initial={{ x: -20, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    transition={{ delay: navigation.length * 0.05 }}
                  >
                    <Link
                      to="/demo-files"
                      className="block px-4 py-3 bg-gradient-to-r from-accent-600 to-accent-700 text-background rounded-lg font-bold text-sm text-center border border-accent-500/30 shadow-md shadow-accent-500/30"
                      style={{ 
                        letterSpacing: '0.025em',
                        boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.1), 0 4px 6px -1px rgba(245, 158, 11, 0.3)',
                        outline: 'none'
                      }}
                      onMouseDown={(e) => {
                        e.preventDefault();
                      }}
                      onClick={(e) => {
                        (e.currentTarget as HTMLAnchorElement).blur();
                      }}
                    >
                      Demo Files
                    </Link>
                  </motion.div>
                  <motion.div
                    initial={{ x: -20, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    transition={{ delay: (navigation.length + 1) * 0.05 }}
                  >
                    <Link
                      to="/customer-portal"
                      className="block px-4 py-3 bg-gradient-to-r from-primary-600 to-primary-700 text-background rounded-lg font-bold text-sm text-center border border-primary-500/30 shadow-md shadow-primary-500/30"
                      style={{ 
                        letterSpacing: '0.025em',
                        boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.1), 0 4px 6px -1px rgba(14, 116, 144, 0.3)',
                        outline: 'none'
                      }}
                      onMouseDown={(e) => {
                        e.preventDefault();
                      }}
                      onClick={(e) => {
                        (e.currentTarget as HTMLAnchorElement).blur();
                      }}
                    >
                      Customer Portal
                    </Link>
                  </motion.div>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </nav>
      </motion.header>

      {/* Main Content */}
      <main className="flex-grow">
        {children}
      </main>

      {/* Footer - Enhanced */}
      <footer className="relative bg-gradient-to-br from-surface-muted via-background to-surface-muted text-text-muted mt-16 overflow-hidden border-t border-border">
        <div className="absolute inset-0">
          <motion.div 
            className="absolute top-0 left-0 w-64 h-64 bg-primary-500/10 rounded-full blur-3xl"
            animate={{ 
              scale: [1, 1.2, 1],
              opacity: [0.1, 0.15, 0.1]
            }}
            transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
          />
          <motion.div 
            className="absolute bottom-0 right-0 w-64 h-64 bg-secondary-500/10 rounded-full blur-3xl"
            animate={{ 
              scale: [1, 1.3, 1],
              opacity: [0.1, 0.15, 0.1]
            }}
            transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 1 }}
          />
        </div>
        
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            {/* Company Info */}
            <div className="col-span-1 md:col-span-2">
              <div className="flex items-center space-x-2 mb-4">
                <span className="text-lg font-display font-black"
                  style={{
                    letterSpacing: '0.02em',
                    color: 'transparent',
                    background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.20) 100%)',
                    WebkitBackgroundClip: 'text',
                    backgroundClip: 'text',
                    textShadow: '0 0 12px rgba(255, 255, 255, 0.25), 0 2px 4px rgba(0, 0, 0, 0.6)',
                    WebkitTextStroke: '1px rgba(255, 255, 255, 0.5)',
                    filter: 'drop-shadow(0 0 8px rgba(255, 255, 255, 0.15))'
                  }}>
                  Robotix
                </span>
              </div>
              <p className="text-text-muted mb-4 max-w-md text-sm leading-relaxed">
                Leading industrial automation with innovative robotics solutions since 2015.
              </p>
              <div className="text-xs text-text-subtle font-medium">
                © 2025 Robotix. All rights reserved.
              </div>
            </div>

            {/* Products */}
            <div>
              <h3 className="text-text font-bold text-sm mb-4 tracking-wide relative inline-block">
                Products
                <span className="absolute -bottom-1 left-0 w-8 h-0.5 bg-gradient-to-r from-primary-500 to-transparent"></span>
              </h3>
              <ul className="space-y-2">
                <li><Link to="/products?category=Collaborative+Robots" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Collaborative Robots
                </Link></li>
                <li><Link to="/products?category=Autonomous+Mobile+Robots" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Mobile Robots
                </Link></li>
                <li><Link to="/products?category=Industrial+Robots" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Industrial Robots
                </Link></li>
                <li><Link to="/products?category=Software" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Software Solutions
                </Link></li>
              </ul>
            </div>

            {/* Company */}
            <div>
              <h3 className="text-text font-bold text-sm mb-4 tracking-wide relative inline-block">
                Company
                <span className="absolute -bottom-1 left-0 w-8 h-0.5 bg-gradient-to-r from-primary-500 to-transparent"></span>
              </h3>
              <ul className="space-y-2">
                <li><Link to="/company" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  About Us
                </Link></li>
                <li><Link to="/support" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Support
                </Link></li>
                <li><Link to="/documentation" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Documentation
                </Link></li>
                <li><Link to="/demo-files" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Demo Files
                </Link></li>
                <li><Link to="/customer-portal" className="text-text-muted hover:text-primary-300 transition-all duration-200 text-xs font-medium hover:translate-x-0.5 inline-block">
                  Customer Portal
                </Link></li>
              </ul>
            </div>
          </div>
          
          {/* Bottom Bar */}
          <div className="pt-6 border-t border-border/70">
            <div className="flex flex-col md:flex-row justify-between items-center gap-3 text-xs text-text-subtle">
              <p className="font-medium">Built with ❤️ for manufacturing excellence</p>
              <div className="flex gap-4">
                <Link to="/company" className="hover:text-primary-300 transition-all duration-200 font-medium hover:translate-y-[-1px]">Privacy</Link>
                <Link to="/company" className="hover:text-primary-300 transition-all duration-200 font-medium hover:translate-y-[-1px]">Terms</Link>
                <Link to="/support" className="hover:text-primary-300 transition-all duration-200 font-medium hover:translate-y-[-1px]">Contact</Link>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Layout;

