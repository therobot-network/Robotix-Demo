import { Link } from 'react-router-dom';
import { Bot, ArrowRight, Sparkles, Rocket, Package, Cpu, Factory } from 'lucide-react';
import { motion } from 'framer-motion';
import { useState, useEffect, useMemo } from 'react';
import productsData from '../data/products.json';
import { Product } from '../types';
import { 
  pageVariants, 
  fadeInUp, 
  staggerContainer, 
  staggerItem 
} from '../utils/animations';
import NeuralBackground, { ExclusionZone } from '../components/NeuralBackground';

const products = productsData as Product[];

function Home() {
  // Memoize filtered products to avoid recalculating on every render
  const activeProducts = useMemo(() => products.filter(p => p.status === 'Active'), []);
  const featuredProducts = useMemo(() => activeProducts.slice(0, 3), [activeProducts]);
  const activeProductCount = useMemo(() => activeProducts.length, [activeProducts]);
  const industrialRobotsCount = useMemo(() => activeProducts.filter(p => p.category === 'Industrial Robots').length, [activeProducts]);
  const collaborativeRobotsCount = useMemo(() => activeProducts.filter(p => p.category === 'Collaborative Robots').length, [activeProducts]);
  const mobileRobotsCount = useMemo(() => activeProducts.filter(p => p.category === 'Mobile Robots').length, [activeProducts]);
  
  const [exclusionZones, setExclusionZones] = useState<ExclusionZone[]>([]);

  useEffect(() => {
    let resizeTimer: number | undefined;
    
    const updateZones = () => {
      // Get the actual hero section dimensions
      const heroSection = document.querySelector('section.relative.min-h-\\[85vh\\]') as HTMLElement;
      if (!heroSection) return;
      
      const rect = heroSection.getBoundingClientRect();
      const width = rect.width;
      const height = rect.height;
      
      // Early exit if dimensions haven't changed significantly (avoid unnecessary recalc)
      const lastWidth = exclusionZones[0]?.width ? exclusionZones[0].width / 0.38 : 0;
      if (Math.abs(lastWidth - width) < 10) return;
      
      const zones: ExclusionZone[] = [];
      const isDesktop = window.innerWidth >= 1024;

      // Left content area - only text and subtext, NOT buttons
      if (isDesktop) {
        // Desktop: two column layout (pre-calculate multiplications)
        zones.push({
          x: width * 0.15,      // Where text actually starts
          y: height * 0.12,      // Start at badge
          width: width * 0.38,   // Cover heading text width
          height: height * 0.56, // Taller to cover badge + heading + subtext paragraph
          strength: 1.0 
        });

        // Right category cards zone on desktop
        zones.push({
          x: width * 0.55,      // Right column start
          y: height * 0.18,      // Start at cards top
          width: width * 0.32,   // Card container width
          height: height * 0.58, // Cover all cards including stats
          strength: 1.0
        });
      } else {
        // Mobile: single column, just cover the main text
        zones.push({
          x: width * 0.05, 
          y: height * 0.20, 
          width: width * 0.90, 
          height: height * 0.45, 
          strength: 1.0 
        });
      }

      setExclusionZones(zones);
    };

    // Debounced resize handler for better performance
    const handleResize = () => {
      if (resizeTimer) clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(updateZones, 150);
    };

    // Initial update with delay to ensure DOM is ready
    const timer = setTimeout(updateZones, 100);
    window.addEventListener('resize', handleResize);
    return () => {
      clearTimeout(timer);
      if (resizeTimer) clearTimeout(resizeTimer);
      window.removeEventListener('resize', handleResize);
    };
  }, [exclusionZones]);

  return (
    <motion.div 
      className="overflow-hidden"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageVariants}
    >
      {/* Hero Section - Neural Network Background */}
      <section className="relative min-h-[85vh] flex items-center overflow-hidden">
        {/* Neural Network Background Layer */}
        <div className="absolute inset-0">
          {/* Base gradient foundation */}
          <div className="absolute inset-0 bg-gradient-to-br from-primary-900 via-primary-950 to-background" 
               style={{ clipPath: 'polygon(0 0, 100% 0, 100% 85%, 0 100%)' }}>
            {/* Subtle radial glows for depth */}
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_40%,rgba(14,116,144,0.15),transparent_60%)]"></div>
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(139,92,246,0.08),transparent_50%)]"></div>
          </div>
          
          {/* Interactive Neural Network Canvas */}
          <div 
            className="absolute inset-0" 
            style={{ clipPath: 'polygon(0 0, 100% 0, 100% 85%, 0 100%)' }}
          >
            <NeuralBackground 
              nodeCount={50}
              particleCount={1000}
              connectionDistance={180}
              interactive={true}
              intensity="medium"
              exclusionZones={exclusionZones}
              debugZones={false}
            />
          </div>
          
          {/* Subtle accent glows */}
          <div className="absolute top-[15%] right-[20%] w-64 h-64 bg-primary-500/10 rounded-full blur-[100px] animate-blob"></div>
          <div className="absolute bottom-[25%] left-[15%] w-80 h-80 bg-accent-500/8 rounded-full blur-[120px] animate-blob" style={{ animationDelay: '3s' }}></div>
          
          {/* Bottom section gradient */}
          <div className="absolute inset-0 bg-gradient-to-tr from-surface to-surface-elevated" 
               style={{ clipPath: 'polygon(0 85%, 100% 70%, 100% 100%, 0 100%)' }}></div>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-28 w-full">
          <div className="grid lg:grid-cols-2 gap-16 lg:gap-24 items-start">
            {/* Left: Content */}
            <motion.div 
              className="z-10"
              variants={staggerContainer}
              initial="initial"
              animate="animate"
            >
              <motion.div 
                className="inline-flex items-center gap-2 px-4 py-2 bg-white/20 backdrop-blur-xl rounded-full border border-white/30 shadow-lg shadow-black/20 group hover:bg-white/30 hover:scale-[1.02] transition-all duration-500 cursor-default mb-6"
                variants={staggerItem}
                whileHover={{ scale: 1.02 }}
              >
                <Sparkles className="w-3.5 h-3.5 text-accent-300 animate-pulse-slow" />
                <span className="text-[11px] font-bold text-white tracking-wide">Leading Innovation Since 2015</span>
              </motion.div>
              
              <div className="flex flex-col justify-between min-h-[445px]" style={{ paddingTop: '10px' }}>
                <div className="space-y-6">
                  <motion.h1 
                    className="relative text-3xl md:text-4xl lg:text-5xl font-display font-black leading-[1.05] tracking-tight"
                    variants={staggerItem}
                    style={{
                      color: 'transparent',
                      background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.25) 100%)',
                      WebkitBackgroundClip: 'text',
                      backgroundClip: 'text',
                      textShadow: '0 0 15px rgba(255, 255, 255, 0.3), 0 2px 4px rgba(0, 0, 0, 0.8)',
                      WebkitTextStroke: '1.5px rgba(255, 255, 255, 0.6)',
                      filter: 'drop-shadow(0 0 10px rgba(255, 255, 255, 0.2))'
                    }}
                  >
                    Revolutionizing<br />
                    <span style={{
                      background: 'linear-gradient(135deg, rgba(255, 200, 150, 0.2) 0%, rgba(255, 220, 180, 0.3) 50%, rgba(255, 200, 150, 0.2) 100%)',
                      WebkitBackgroundClip: 'text',
                      backgroundClip: 'text',
                      color: 'transparent',
                      textShadow: '0 0 20px rgba(255, 200, 150, 0.4), 0 4px 8px rgba(0, 0, 0, 0.8)',
                      WebkitTextStroke: '1.5px rgba(255, 200, 150, 0.7)',
                      filter: 'drop-shadow(0 0 12px rgba(255, 200, 150, 0.3))'
                    }}>
                      Industrial Automation
                    </span>
                  </motion.h1>
                  
                  <motion.p 
                    className="relative text-sm md:text-base leading-relaxed max-w-xl"
                    variants={staggerItem}
                    style={{
                      color: 'transparent',
                      background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.18) 100%)',
                      WebkitBackgroundClip: 'text',
                      backgroundClip: 'text',
                      textShadow: '0 0 10px rgba(255, 255, 255, 0.25), 0 1px 3px rgba(0, 0, 0, 0.6)',
                      WebkitTextStroke: '0.8px rgba(255, 255, 255, 0.5)',
                      filter: 'drop-shadow(0 0 8px rgba(255, 255, 255, 0.15))'
                    }}
                  >
                    Transform production with AI-driven robotics and intelligent automation systems.
                  </motion.p>
                </div>
                
                <motion.div 
                  className="flex flex-wrap gap-4"
                  variants={staggerItem}
                >
                <Link to="/products" 
                  className="group relative px-5 py-2.5 bg-white text-primary-900 rounded-[12px] font-bold text-sm inline-flex items-center shadow-xl shadow-black/20 hover:shadow-2xl hover:shadow-accent-400/30 hover:-translate-y-1 hover:scale-[1.02] transition-all duration-300 overflow-hidden border border-white/50"
                  style={{ 
                    letterSpacing: '0.02em',
                    boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.8), 0 10px 20px rgba(0, 0, 0, 0.2)'
                  }}>
                  <span className="relative z-10">Explore Products</span>
                  <ArrowRight className="w-4 h-4 ml-1.5 relative z-10 group-hover:translate-x-1 transition-transform duration-300" strokeWidth={2.5} />
                  <div className="absolute inset-0 bg-gradient-to-r from-accent-400 to-accent-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <span className="absolute inset-0 bg-gradient-to-r from-accent-400/0 to-accent-400/0 group-hover:from-accent-400/20 group-hover:to-accent-500/20 transition-all duration-300"></span>
                </Link>
                <Link to="/customer-portal" 
                  className="group relative px-5 py-2.5 border-2 border-white/80 text-white rounded-[12px] font-bold text-sm inline-flex items-center backdrop-blur-sm bg-white/10 hover:bg-white hover:text-primary-900 hover:border-white hover:-translate-y-1 hover:scale-[1.02] transition-all duration-300 shadow-xl shadow-black/20"
                  style={{ 
                    letterSpacing: '0.02em',
                    boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.15), 0 10px 20px rgba(0, 0, 0, 0.2)'
                  }}>
                  <span>Get Started</span>
                  <Rocket className="w-4 h-4 ml-1.5 group-hover:rotate-12 group-hover:scale-110 transition-transform duration-300" strokeWidth={2.5} />
                </Link>
              </motion.div>
              </div>
            </motion.div>
            
            {/* Right: Product Category Navigator */}
            <motion.div 
              className="relative lg:block hidden"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.4, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
              style={{ paddingTop: '80px' }}
            >
              <div className="max-w-md ml-auto space-y-4">
                {/* Header Card */}
                <div className="group relative bg-white/[0.08] backdrop-blur-3xl p-5 rounded-[16px] border border-white/30 shadow-2xl overflow-hidden"
                     style={{
                       boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.37), inset 0 1px 0 0 rgba(255, 255, 255, 0.5), inset 0 -1px 0 0 rgba(255, 255, 255, 0.1), inset 2px 0 4px rgba(255, 255, 255, 0.1)',
                       background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.03) 100%)',
                       backdropFilter: 'blur(40px) saturate(180%)'
                     }}>
                  {/* Light refraction gradient overlay with glitch */}
                  <div className="absolute inset-0 bg-gradient-to-br from-white/30 via-transparent to-white/5 pointer-events-none mix-blend-overlay"
                       style={{ animation: 'glassGlitch 15s ease-in-out infinite' }}></div>
                  
                  {/* Shimmer sweep effect - only on hover */}
                  <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                       style={{
                         background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.15) 50%, transparent 60%)',
                         backgroundSize: '200% 100%',
                         animation: 'glassShimmer 1.5s ease-in-out'
                       }}></div>
                  
                  {/* Dynamic distortion light spots */}
                  <div className="absolute top-0 right-0 w-32 h-32 bg-white/20 rounded-full blur-3xl pointer-events-none"
                       style={{ animation: 'lightCaustic 6s ease-in-out infinite', animationDelay: '1s' }}></div>
                  
                  <div className="relative flex items-center gap-2.5 mb-1">
                    <div className="w-8 h-8 bg-gradient-to-br from-primary-500 to-primary-700 rounded-[10px] flex items-center justify-center shadow-lg">
                      <Package className="w-5 h-5 text-white" strokeWidth={2} />
                    </div>
                    <div>
                      <div className="text-xs font-bold text-white tracking-wide drop-shadow-lg">Explore Categories</div>
                      <div className="text-[11px] text-white/80 drop-shadow">{activeProductCount} active products</div>
                    </div>
                  </div>
                </div>

                {/* Category Cards - Only showing categories with products */}
                <Link to="/products?category=Industrial+Robots" className="group relative block bg-white/[0.08] backdrop-blur-3xl p-4 rounded-[14px] border border-white/30 hover:border-primary-300/60 hover:shadow-2xl transition-all duration-300 overflow-hidden"
                      style={{
                        boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.37), inset 0 1px 0 0 rgba(255, 255, 255, 0.4), inset 0 -1px 0 0 rgba(255, 255, 255, 0.1), inset 2px 0 4px rgba(255, 255, 255, 0.1)',
                        background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.03) 100%)',
                        backdropFilter: 'blur(40px) saturate(180%)'
                      }}>
                  {/* Light refraction gradient overlay with glitch */}
                  <div className="absolute inset-0 bg-gradient-to-br from-white/25 via-transparent to-primary-400/10 pointer-events-none mix-blend-overlay"
                       style={{ animation: 'glassGlitch 15s ease-in-out infinite' }}></div>
                  
                  {/* Shimmer sweep effect - only on hover */}
                  <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                       style={{
                         background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.15) 50%, transparent 60%)',
                         backgroundSize: '200% 100%',
                         animation: 'glassShimmer 1.5s ease-in-out'
                       }}></div>
                  
                  {/* Dynamic distortion light spots */}
                  <div className="absolute -top-8 -right-8 w-24 h-24 bg-white/20 rounded-full blur-2xl pointer-events-none group-hover:bg-primary-300/30 transition-all duration-500"
                       style={{ animation: 'lightCaustic 6s ease-in-out infinite', animationDelay: '1s' }}></div>
                  
                  <div className="relative flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-gradient-to-br from-primary-400 to-primary-600 rounded-[12px] flex items-center justify-center group-hover:scale-[1.03] transition-all duration-300 shadow-lg">
                        <Factory className="w-5 h-5 text-white" strokeWidth={2} />
                      </div>
                      <div>
                        <div className="text-sm font-bold text-white drop-shadow-lg group-hover:text-primary-200 transition-colors">Industrial Robots</div>
                        <div className="text-[11px] text-white/80 font-medium drop-shadow">{industrialRobotsCount} models</div>
                      </div>
                    </div>
                    <ArrowRight className="w-4 h-4 text-white/80 opacity-0 group-hover:opacity-100 group-hover:translate-x-0.5 transition-all duration-300 drop-shadow" />
                  </div>
                </Link>

                <Link to="/products?category=Collaborative+Robots" className="group relative block bg-white/[0.08] backdrop-blur-3xl p-4 rounded-[14px] border border-white/30 hover:border-accent-300/60 hover:shadow-2xl transition-all duration-300 overflow-hidden"
                      style={{
                        boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.37), inset 0 1px 0 0 rgba(255, 255, 255, 0.4), inset 0 -1px 0 0 rgba(255, 255, 255, 0.1), inset 2px 0 4px rgba(255, 255, 255, 0.1)',
                        background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.03) 100%)',
                        backdropFilter: 'blur(40px) saturate(180%)'
                      }}>
                  {/* Light refraction gradient overlay with glitch */}
                  <div className="absolute inset-0 bg-gradient-to-br from-white/25 via-transparent to-accent-400/10 pointer-events-none mix-blend-overlay"
                       style={{ animation: 'glassGlitch 15s ease-in-out infinite', animationDelay: '2s' }}></div>
                  
                  {/* Shimmer sweep effect - only on hover */}
                  <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                       style={{
                         background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.15) 50%, transparent 60%)',
                         backgroundSize: '200% 100%',
                         animation: 'glassShimmer 1.5s ease-in-out'
                       }}></div>
                  
                  {/* Dynamic distortion light spots */}
                  <div className="absolute -top-8 -right-8 w-24 h-24 bg-white/20 rounded-full blur-2xl pointer-events-none group-hover:bg-accent-300/30 transition-all duration-500"
                       style={{ animation: 'lightCaustic 6s ease-in-out infinite', animationDelay: '1.5s' }}></div>
                  
                  <div className="relative flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-gradient-to-br from-accent-400 to-accent-600 rounded-[12px] flex items-center justify-center group-hover:scale-[1.03] transition-all duration-300 shadow-lg">
                        <Bot className="w-5 h-5 text-white" strokeWidth={2} />
                      </div>
                      <div>
                        <div className="text-sm font-bold text-white drop-shadow-lg group-hover:text-accent-200 transition-colors">Collaborative Robots</div>
                        <div className="text-[11px] text-white/80 font-medium drop-shadow">{collaborativeRobotsCount} models</div>
                      </div>
                    </div>
                    <ArrowRight className="w-4 h-4 text-white/80 opacity-0 group-hover:opacity-100 group-hover:translate-x-0.5 transition-all duration-300 drop-shadow" />
                  </div>
                </Link>

                <Link to="/products?category=Mobile+Robots" className="group relative block bg-white/[0.08] backdrop-blur-3xl p-4 rounded-[14px] border border-white/30 hover:border-secondary-300/60 hover:shadow-2xl transition-all duration-300 overflow-hidden"
                      style={{
                        boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.37), inset 0 1px 0 0 rgba(255, 255, 255, 0.4), inset 0 -1px 0 0 rgba(255, 255, 255, 0.1), inset 2px 0 4px rgba(255, 255, 255, 0.1)',
                        background: 'linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.03) 100%)',
                        backdropFilter: 'blur(40px) saturate(180%)'
                      }}>
                  {/* Light refraction gradient overlay with glitch */}
                  <div className="absolute inset-0 bg-gradient-to-br from-white/25 via-transparent to-secondary-400/10 pointer-events-none mix-blend-overlay"
                       style={{ animation: 'glassGlitch 15s ease-in-out infinite', animationDelay: '4s' }}></div>
                  
                  {/* Shimmer sweep effect - only on hover */}
                  <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                       style={{
                         background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.15) 50%, transparent 60%)',
                         backgroundSize: '200% 100%',
                         animation: 'glassShimmer 1.5s ease-in-out'
                       }}></div>
                  
                  {/* Dynamic distortion light spots */}
                  <div className="absolute -top-8 -right-8 w-24 h-24 bg-white/20 rounded-full blur-2xl pointer-events-none group-hover:bg-secondary-300/30 transition-all duration-500"
                       style={{ animation: 'lightCaustic 6s ease-in-out infinite', animationDelay: '2s' }}></div>
                  
                  <div className="relative flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-gradient-to-br from-secondary-400 to-secondary-600 rounded-[12px] flex items-center justify-center group-hover:scale-105 transition-all duration-300 shadow-lg">
                        <Cpu className="w-5 h-5 text-white" strokeWidth={2} />
                      </div>
                      <div>
                        <div className="text-sm font-bold text-white drop-shadow-lg group-hover:text-secondary-200 transition-colors">Mobile Robots</div>
                        <div className="text-[11px] text-white/80 font-medium drop-shadow">{mobileRobotsCount} models</div>
                      </div>
                    </div>
                    <ArrowRight className="w-4 h-4 text-white/80 opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all duration-300 drop-shadow" />
                  </div>
                </Link>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Features + Products Combined Section - Asymmetric Bento */}
      <section className="py-24 bg-gradient-to-b from-background via-surface-muted to-background relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          
          {/* Featured Products Header */}
          <motion.div 
            className="grid lg:grid-cols-3 gap-6"
            variants={staggerContainer}
            initial="initial"
            whileInView="animate"
            viewport={{ once: true, margin: "-80px" }}
          >
            <motion.div 
              className="lg:col-span-3 mb-6 flex justify-between items-end"
              variants={fadeInUp}
            >
              <div>
                <div className="inline-flex items-center gap-2.5 px-5 py-2 bg-gradient-to-r from-primary-600 to-secondary-600 text-background rounded-full text-xs font-black mb-3 shadow-lg shadow-primary-600/30">
                  <Package className="w-4 h-4" strokeWidth={2.5} />
                  <span className="tracking-wide">Featured Products</span>
                </div>
                <h2 className="text-3xl md:text-4xl font-display font-black text-text tracking-tight">
                  <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-400 via-primary-300 to-accent-400">
                    Popular Solutions
                  </span>
                </h2>
              </div>
              <Link to="/products" 
                className="group px-6 py-2.5 bg-gradient-to-r from-primary-600 to-primary-700 text-background rounded-[14px] font-bold text-sm inline-flex items-center shadow-lg shadow-primary-600/30 hover:shadow-xl hover:shadow-primary-500/40 hover:-translate-y-1 hover:scale-[1.02] transition-all duration-300 border border-primary-500/30"
                style={{ 
                  letterSpacing: '0.025em',
                  boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.1), 0 4px 8px rgba(14, 116, 144, 0.3)'
                }}>
                View All
                <ArrowRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform duration-300" strokeWidth={2.5} />
              </Link>
            </motion.div>

            {/* Product Cards - Compact */}
            {featuredProducts.map((product) => (
              <motion.div
                key={product.sku}
                variants={staggerItem}
              >
                <motion.div
                  whileHover={{ y: -8, scale: 1.02 }}
                  transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
                >
                  <Link 
                    to={`/products/${product.sku}`}
                    className="group relative bg-surface rounded-[20px] p-7 shadow-lg border border-border hover:shadow-2xl hover:shadow-primary-500/20 hover:border-primary-500/50 transition-all duration-500 block h-full"
                  >
                  <div className="absolute inset-0 bg-gradient-to-br from-primary-900/10 to-accent-900/10 opacity-0 group-hover:opacity-100 rounded-[20px] transition-opacity duration-500"></div>
                
                <div className="relative">
                  <div className="flex items-start justify-between mb-4">
                    <span className="px-3.5 py-1.5 bg-primary-800/50 text-primary-300 rounded-lg text-[11px] font-bold border border-primary-600/40 shadow-sm tracking-wide">
                      {product.category}
                    </span>
                    <div className="w-9 h-9 bg-gradient-to-br from-primary-400 to-accent-400 rounded-[12px] flex items-center justify-center opacity-0 group-hover:opacity-100 group-hover:scale-[1.05] group-hover:rotate-6 transition-all duration-500 shadow-lg shadow-primary-500/30">
                      <ArrowRight className="w-5 h-5 text-background" strokeWidth={2.5} />
                    </div>
                  </div>
                  
                  <h3 className="text-lg font-display font-bold text-text mb-2.5 group-hover:text-primary-300 transition-colors duration-300 line-clamp-2 tracking-tight">
                    {product.product_name}
                  </h3>
                  <p className="text-sm text-text-muted mb-5 line-clamp-2 leading-relaxed">
                    {product.description}
                  </p>
                  
                  <div className="flex justify-between items-center pt-4 border-t border-border">
                    <div>
                      <div className="text-[10px] text-text-muted font-bold mb-1 uppercase tracking-wider">Starting at</div>
                      <span className="text-2xl font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-primary-300 to-accent-300 tracking-tight">
                        ${product.msrp.toLocaleString()}
                      </span>
                    </div>
                    <div className="text-primary-300 font-bold text-sm flex items-center gap-1 group-hover:gap-2 transition-all duration-300">
                      Learn More
                      <ArrowRight className="w-4 h-4" strokeWidth={2.5} />
                    </div>
                  </div>
                </div>
                  </Link>
                </motion.div>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* CTA Section - Enhanced with Animated Background */}
      <section className="relative py-32 overflow-hidden">
        {/* Rich Animated Background Layer */}
        <div className="absolute inset-0">
          {/* Base gradient with multiple color stops for depth */}
          <div className="absolute inset-0 bg-gradient-to-br from-primary-600 via-primary-700 via-primary-800 to-primary-950">
            {/* Radial gradient overlay for center glow */}
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(14,116,144,0.25),transparent_50%)]"></div>
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_80%,rgba(139,92,246,0.08),transparent_40%)]"></div>
            
            {/* Subtle directional light streaks */}
            <div className="absolute inset-0 bg-[linear-gradient(135deg,transparent_30%,rgba(14,116,144,0.08)_50%,transparent_70%)]"></div>
            <div className="absolute inset-0 bg-[linear-gradient(200deg,transparent_40%,rgba(139,92,246,0.05)_60%,transparent_80%)]"></div>
          </div>
          
          {/* Subtle grid pattern overlay */}
          <div className="absolute inset-0 opacity-[0.03]"
               style={{ 
                 backgroundImage: 'linear-gradient(rgba(255,255,255,0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.5) 1px, transparent 1px)',
                 backgroundSize: '60px 60px'
               }}></div>
          
          {/* Diagonal accent lines */}
          <div className="absolute top-0 left-1/4 w-px h-[40%] bg-gradient-to-b from-transparent via-primary-400/20 to-transparent rotate-[20deg]"></div>
          <div className="absolute top-1/4 right-1/3 w-px h-[30%] bg-gradient-to-b from-transparent via-primary-300/15 to-transparent rotate-[-15deg]"></div>
          
          {/* Animated geometric accents */}
          <div className="absolute top-[15%] left-[10%] w-[300px] h-[300px] border border-white/5 rounded-full animate-blob"></div>
          <div className="absolute top-[25%] right-[15%] w-[200px] h-[200px] border border-accent-400/10 rounded-full animate-blob" style={{ animationDelay: '3s' }}></div>
          
          {/* Soft glow spots for depth */}
          <div className="absolute top-[10%] right-[20%] w-32 h-32 bg-primary-500/5 rounded-full blur-[60px]"></div>
          <div className="absolute bottom-[30%] left-[15%] w-40 h-40 bg-purple-400/5 rounded-full blur-[70px]"></div>
          
          {/* Enhanced Animated Gradient Orbs */}
          <div className="absolute top-20 right-1/4 w-[450px] h-[450px] bg-gradient-to-br from-accent-400/15 to-primary-400/10 rounded-full blur-[130px] animate-blob"></div>
          <div className="absolute bottom-20 left-1/4 w-[32rem] h-[32rem] bg-gradient-to-tl from-secondary-400/12 to-accent-400/8 rounded-full blur-[150px] animate-blob" style={{ animationDelay: '2s' }}></div>
          <div className="absolute top-1/2 right-1/3 w-72 h-72 bg-gradient-to-br from-primary-300/12 to-transparent rounded-full blur-[110px] animate-blob" style={{ animationDelay: '4s' }}></div>
        </div>
        
        <div className="relative max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center"
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="inline-flex items-center gap-2.5 px-4 py-2 bg-white/20 backdrop-blur-xl rounded-full border border-white/30 shadow-lg shadow-black/20 mb-6">
              <Sparkles className="w-3.5 h-3.5 text-accent-300 animate-pulse-slow" />
              <span className="text-xs font-semibold text-white tracking-wide">Transform Your Business</span>
            </div>
            
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-display font-black mb-6 leading-tight tracking-tight text-white">
              Ready to Transform
              <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-accent-200 via-white to-accent-100 drop-shadow-2xl">Your Manufacturing?</span>
            </h2>
            
            <p className="text-lg text-white/95 mb-10 max-w-2xl mx-auto leading-relaxed">
              Join <span className="font-semibold text-accent-200">500+</span> industry leaders who trust Robotix.
            </p>
            
            <div className="flex flex-wrap justify-center gap-5 mb-16">
              <motion.div
                whileHover={{ scale: 1.05, y: -4 }}
                whileTap={{ scale: 0.98 }}
              >
                <Link to="/customer-portal" 
                  className="group relative px-8 py-4 bg-white text-primary-900 rounded-[14px] font-bold text-base inline-flex items-center shadow-xl shadow-black/20 hover:shadow-2xl hover:shadow-accent-400/30 transition-all duration-300 overflow-hidden border border-white/50"
                  style={{ 
                    letterSpacing: '0.02em',
                    boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.8), 0 10px 20px rgba(0, 0, 0, 0.2)'
                  }}>
                  <span className="relative z-10">Get Started Free</span>
                  <Rocket className="w-4 h-4 ml-2 relative z-10 group-hover:rotate-12 group-hover:scale-110 transition-transform duration-300" strokeWidth={2.5} />
                  <div className="absolute inset-0 bg-gradient-to-r from-accent-400 to-accent-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                </Link>
              </motion.div>
              <motion.div
                whileHover={{ scale: 1.05, y: -4 }}
                whileTap={{ scale: 0.98 }}
              >
                <Link to="/support" 
                  className="group relative px-8 py-4 border-2 border-white/80 text-white rounded-[14px] font-bold text-base inline-flex items-center backdrop-blur-sm bg-white/10 hover:bg-white hover:text-primary-900 hover:border-white transition-all duration-300 shadow-xl shadow-black/20"
                  style={{ 
                    letterSpacing: '0.02em',
                    boxShadow: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.15), 0 10px 20px rgba(0, 0, 0, 0.2)'
                  }}>
                  <span>Contact Sales</span>
                  <ArrowRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform duration-300" strokeWidth={2.5} />
                </Link>
              </motion.div>
            </div>
          </motion.div>
        </div>
      </section>
    </motion.div>
  );
}

export default Home;

