import { useState } from 'react';
import { Mail, Phone, MessageCircle, HelpCircle, Send, CheckCircle } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import supportTicketsData from '../data/support_tickets.json';
import { SupportTicket } from '../types';
import { 
  pageVariants, 
  fadeInUp, 
  staggerContainer, 
  staggerItem,
  fadeInScale,
  successAnimation 
} from '../utils/animations';

const supportTickets = supportTicketsData as SupportTicket[];

function Support() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
    priority: 'Medium',
  });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      setFormData({ name: '', email: '', subject: '', message: '', priority: 'Medium' });
    }, 3000);
  };

  const stats = {
    open: supportTickets.filter(t => t.status === 'Open').length,
    inProgress: supportTickets.filter(t => t.status === 'In Progress').length,
    closed: supportTickets.filter(t => t.status === 'Closed').length,
    avgSatisfaction: (
      supportTickets
        .filter(t => t.satisfaction_rating !== null)
        .reduce((sum, t) => sum + (t.satisfaction_rating || 0), 0) /
      supportTickets.filter(t => t.satisfaction_rating !== null).length
    ).toFixed(1),
  };

  return (
    <motion.div 
      className="min-h-screen bg-background"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageVariants}
    >
      {/* Hero Header - Enhanced */}
      <section className="relative py-20 overflow-hidden">
        {/* Background Layer */}
        <div className="absolute inset-0 bg-black">
          {/* Subtle accent lines */}
          <div className="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-white/20 to-transparent"></div>
          <div className="absolute bottom-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-white/10 to-transparent"></div>
          <div className="absolute top-1/4 left-0 w-32 h-px bg-gradient-to-r from-accent-500/30 to-transparent"></div>
          <div className="absolute top-1/3 right-0 w-24 h-px bg-gradient-to-l from-secondary-500/30 to-transparent"></div>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            className="inline-flex items-center gap-2.5 px-5 py-2.5 bg-white/10 backdrop-blur-xl rounded-full border border-white/20 mb-8"
            variants={fadeInUp}
          >
            <HelpCircle className="w-4 h-4 text-accent-400" />
            <span className="text-xs font-semibold text-white/90 tracking-wider uppercase">24/7 Support</span>
          </motion.div>
          
          <motion.h1 
            className="text-5xl md:text-6xl lg:text-7xl font-display font-black mb-6 tracking-tight leading-[1.1]"
            variants={fadeInUp}
          >
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-white via-white to-white/80">
              Support
            </span>
            <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-accent-300 via-accent-200 to-secondary-300">
              Center
            </span>
          </motion.h1>
          <motion.p 
            className="text-base md:text-lg text-white/60 max-w-2xl leading-relaxed font-light"
            variants={fadeInUp}
            transition={{ delay: 0.1 }}
          >
            We're here to help. Get in touch with our support team for assistance with products, orders, and technical issues.
          </motion.p>
        </div>
      </section>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Stats - Enhanced Cards */}
        <motion.div 
          className="grid md:grid-cols-4 gap-6 mb-12"
          variants={staggerContainer}
          initial="initial"
          animate="animate"
        >
          <motion.div 
            className="relative bg-surface rounded-[20px] p-6 shadow-lg border border-border hover:shadow-2xl hover:shadow-primary-500/20 hover:border-primary-500/50 transition-all duration-500 text-center group"
            variants={staggerItem}
            whileHover={{ y: -8, scale: 1.02 }}
          >
            <div className="absolute inset-0 bg-gradient-to-br from-primary-900/10 to-accent-900/10 opacity-0 group-hover:opacity-100 rounded-[20px] transition-opacity duration-500"></div>
            <div className="relative">
              <div className="text-4xl font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-text to-text-muted mb-2">{stats.open}</div>
              <div className="text-text-muted font-medium text-sm">Open Tickets</div>
            </div>
          </motion.div>
          <motion.div 
            className="relative bg-surface rounded-[20px] p-6 shadow-lg border border-border hover:shadow-2xl hover:shadow-primary-500/20 hover:border-primary-500/50 transition-all duration-500 text-center group"
            variants={staggerItem}
            whileHover={{ y: -8, scale: 1.02 }}
          >
            <div className="absolute inset-0 bg-gradient-to-br from-primary-900/10 to-accent-900/10 opacity-0 group-hover:opacity-100 rounded-[20px] transition-opacity duration-500"></div>
            <div className="relative">
              <div className="text-4xl font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-primary-300 to-primary-400 mb-2">{stats.inProgress}</div>
              <div className="text-text-muted font-medium text-sm">In Progress</div>
            </div>
          </motion.div>
          <motion.div 
            className="relative bg-surface rounded-[20px] p-6 shadow-lg border border-border hover:shadow-2xl hover:shadow-secondary-500/20 hover:border-secondary-500/50 transition-all duration-500 text-center group"
            variants={staggerItem}
            whileHover={{ y: -8, scale: 1.02 }}
          >
            <div className="absolute inset-0 bg-gradient-to-br from-secondary-900/10 to-accent-900/10 opacity-0 group-hover:opacity-100 rounded-[20px] transition-opacity duration-500"></div>
            <div className="relative">
              <div className="text-4xl font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-secondary-300 to-secondary-400 mb-2">{stats.closed}</div>
              <div className="text-text-muted font-medium text-sm">Resolved</div>
            </div>
          </motion.div>
          <motion.div 
            className="relative bg-surface rounded-[20px] p-6 shadow-lg border border-border hover:shadow-2xl hover:shadow-accent-500/20 hover:border-accent-500/50 transition-all duration-500 text-center group"
            variants={staggerItem}
            whileHover={{ y: -8, scale: 1.02 }}
          >
            <div className="absolute inset-0 bg-gradient-to-br from-accent-900/10 to-primary-900/10 opacity-0 group-hover:opacity-100 rounded-[20px] transition-opacity duration-500"></div>
            <div className="relative">
              <div className="text-4xl font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-accent-300 to-accent-400 mb-2">{stats.avgSatisfaction} ⭐</div>
              <div className="text-text-muted font-medium text-sm">Avg. Satisfaction</div>
            </div>
          </motion.div>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-8">
          {/* Contact Form */}
          <motion.div 
            className="relative bg-surface rounded-[20px] p-8 shadow-lg border border-border"
            variants={fadeInScale}
            initial="initial"
            animate="animate"
            transition={{ delay: 0.3 }}
          >
            <div className="flex items-center gap-3 mb-6">
              <div className="w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-700 rounded-[14px] flex items-center justify-center shadow-lg">
                <MessageCircle className="w-6 h-6 text-white" strokeWidth={2} />
              </div>
              <h2 className="text-2xl font-display font-bold text-text">Submit a Support Request</h2>
            </div>
            
            <AnimatePresence mode="wait">
              {submitted ? (
                <motion.div 
                  className="text-center py-12"
                  variants={successAnimation}
                  initial="initial"
                  animate="animate"
                  exit="exit"
                  key="success"
                >
                  <motion.div
                    animate={{ 
                      scale: [1, 1.2, 1],
                      rotate: [0, 360, 360]
                    }}
                    transition={{
                      duration: 0.6,
                      ease: "easeOut"
                    }}
                  >
                    <CheckCircle className="w-16 h-16 text-secondary-400 mx-auto mb-4" />
                  </motion.div>
                  <h3 className="text-xl font-semibold text-text mb-2">Request Submitted!</h3>
                  <p className="text-text-muted">
                    We've received your support request and will get back to you within 24 hours.
                  </p>
                </motion.div>
              ) : (
                <motion.div
                  key="form"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                >
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label className="block text-sm font-semibold text-text mb-2">
                    Name *
                  </label>
                  <input
                    type="text"
                    required
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                    className="input-field"
                    placeholder="John Doe"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-text mb-2">
                    Email *
                  </label>
                  <input
                    type="email"
                    required
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    className="input-field"
                    placeholder="john@example.com"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-text mb-2">
                    Priority
                  </label>
                  <select
                    value={formData.priority}
                    onChange={(e) => setFormData({ ...formData, priority: e.target.value })}
                    className="input-field"
                  >
                    <option value="Low">Low</option>
                    <option value="Medium">Medium</option>
                    <option value="High">High</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-semibold text-text mb-2">
                    Subject *
                  </label>
                  <input
                    type="text"
                    required
                    value={formData.subject}
                    onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                    className="input-field"
                    placeholder="Brief description of your issue"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-text mb-2">
                    Message *
                  </label>
                  <textarea
                    required
                    value={formData.message}
                    onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                    rows={5}
                    className="input-field"
                    placeholder="Please provide details about your issue..."
                  />
                </div>

                  <motion.button 
                    type="submit" 
                    className="w-full btn-primary"
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    <Send className="inline w-5 h-5 mr-2" />
                    Submit Request
                  </motion.button>
                </form>
                </motion.div>
              )}
            </AnimatePresence>
          </motion.div>

          {/* Contact Information & FAQs */}
          <motion.div 
            className="space-y-6"
            variants={fadeInUp}
            initial="initial"
            animate="animate"
            transition={{ delay: 0.4 }}
          >
            {/* Contact Methods */}
            <motion.div 
              className="relative bg-surface rounded-[20px] p-8 shadow-lg border border-border hover:shadow-2xl transition-all duration-500"
              whileHover={{ y: -4 }}
            >
              <div className="flex items-center gap-3 mb-6">
                <div className="w-12 h-12 bg-gradient-to-br from-accent-500 to-accent-700 rounded-[14px] flex items-center justify-center shadow-lg">
                  <Phone className="w-6 h-6 text-white" strokeWidth={2} />
                </div>
                <h2 className="text-2xl font-display font-bold text-text">Contact Us</h2>
              </div>
              <motion.div 
                className="space-y-4"
                variants={staggerContainer}
                initial="initial"
                animate="animate"
              >
                <motion.div 
                  className="flex items-start gap-4 p-4 rounded-[14px] bg-surface-elevated/50 border border-border/50 hover:border-primary-500/50 hover:bg-surface-elevated transition-all duration-300"
                  variants={staggerItem}
                  whileHover={{ x: 4 }}
                >
                  <div className="w-12 h-12 bg-gradient-to-br from-primary-400 to-primary-600 rounded-[12px] flex items-center justify-center flex-shrink-0 shadow-lg">
                    <Phone className="w-6 h-6 text-white" strokeWidth={2} />
                  </div>
                  <div>
                    <h3 className="font-bold text-text mb-1">Phone Support</h3>
                    <p className="text-text-muted text-sm mb-1 font-medium">+1 (800) 555-ROBOT</p>
                    <p className="text-text-subtle text-xs">Mon-Fri, 8am-6pm EST</p>
                  </div>
                </motion.div>

                <motion.div 
                  className="flex items-start gap-4 p-4 rounded-[14px] bg-surface-elevated/50 border border-border/50 hover:border-accent-500/50 hover:bg-surface-elevated transition-all duration-300"
                  variants={staggerItem}
                  whileHover={{ x: 4 }}
                >
                  <div className="w-12 h-12 bg-gradient-to-br from-accent-400 to-accent-600 rounded-[12px] flex items-center justify-center flex-shrink-0 shadow-lg">
                    <Mail className="w-6 h-6 text-white" strokeWidth={2} />
                  </div>
                  <div>
                    <h3 className="font-bold text-text mb-1">Email Support</h3>
                    <p className="text-text-muted text-sm mb-1 font-medium">support@robotechindustries.com</p>
                    <p className="text-text-subtle text-xs">Response within 24 hours</p>
                  </div>
                </motion.div>

                <motion.div 
                  className="flex items-start gap-4 p-4 rounded-[14px] bg-surface-elevated/50 border border-border/50 hover:border-secondary-500/50 hover:bg-surface-elevated transition-all duration-300"
                  variants={staggerItem}
                  whileHover={{ x: 4 }}
                >
                  <div className="w-12 h-12 bg-gradient-to-br from-secondary-400 to-secondary-600 rounded-[12px] flex items-center justify-center flex-shrink-0 shadow-lg">
                    <MessageCircle className="w-6 h-6 text-white" strokeWidth={2} />
                  </div>
                  <div>
                    <h3 className="font-bold text-text mb-1">Live Chat</h3>
                    <p className="text-text-muted text-sm mb-1 font-medium">Available on our website</p>
                    <p className="text-text-subtle text-xs">Mon-Fri, 8am-8pm EST</p>
                  </div>
                </motion.div>
              </motion.div>
            </motion.div>

            {/* FAQs */}
            <motion.div 
              className="relative bg-surface rounded-[20px] p-8 shadow-lg border border-border hover:shadow-2xl transition-all duration-500"
              whileHover={{ y: -4 }}
            >
              <div className="flex items-center gap-3 mb-6">
                <div className="w-12 h-12 bg-gradient-to-br from-secondary-500 to-secondary-700 rounded-[14px] flex items-center justify-center shadow-lg">
                  <HelpCircle className="w-6 h-6 text-white" strokeWidth={2} />
                </div>
                <h2 className="text-2xl font-display font-bold text-text">Common Questions</h2>
              </div>
              <motion.div 
                className="space-y-4"
                variants={staggerContainer}
                initial="initial"
                animate="animate"
              >
                <motion.div 
                  className="p-4 rounded-[14px] bg-surface-elevated/50 border border-border/50 hover:border-primary-500/30 transition-all duration-300"
                  variants={staggerItem}
                  whileHover={{ x: 4 }}
                >
                  <h3 className="font-bold text-text mb-2">How do I track my order?</h3>
                  <p className="text-text-muted text-sm">
                    Visit the Customer Portal and log in to view all your orders and their current status.
                  </p>
                </motion.div>
                <motion.div 
                  className="p-4 rounded-[14px] bg-surface-elevated/50 border border-border/50 hover:border-primary-500/30 transition-all duration-300"
                  variants={staggerItem}
                  whileHover={{ x: 4 }}
                >
                  <h3 className="font-bold text-text mb-2">What's your warranty policy?</h3>
                  <p className="text-text-muted text-sm">
                    Most products come with a 1-2 year warranty. Check individual product pages for specific details.
                  </p>
                </motion.div>
                <motion.div 
                  className="p-4 rounded-[14px] bg-surface-elevated/50 border border-border/50 hover:border-primary-500/30 transition-all duration-300"
                  variants={staggerItem}
                  whileHover={{ x: 4 }}
                >
                  <h3 className="font-bold text-text mb-2">How do I access technical documentation?</h3>
                  <p className="text-text-muted text-sm">
                    All technical specs and user guides are available in our Documentation Center.
                  </p>
                </motion.div>
                <motion.div 
                  className="p-4 rounded-[14px] bg-surface-elevated/50 border border-border/50 hover:border-primary-500/30 transition-all duration-300"
                  variants={staggerItem}
                  whileHover={{ x: 4 }}
                >
                  <h3 className="font-bold text-text mb-2">Do you offer training?</h3>
                  <p className="text-text-muted text-sm">
                    Yes! We provide on-site training and online resources for all our robotics solutions.
                  </p>
                </motion.div>
              </motion.div>
            </motion.div>
          </motion.div>
        </div>
      </div>
    </motion.div>
  );
}

export default Support;

