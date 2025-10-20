import { useState, useMemo } from 'react';
import { User, ShoppingCart, AlertCircle, TrendingUp, DollarSign, Package, Mail, Phone, Building2, Calendar } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line } from 'recharts';
import { motion, AnimatePresence } from 'framer-motion';
import customersData from '../data/customers.json';
import ordersData from '../data/orders.json';
import supportTicketsData from '../data/support_tickets.json';
import { Customer, Order, SupportTicket } from '../types';
import { 
  pageVariants, 
  fadeInUp, 
  staggerContainer, 
  staggerItem,
  fadeInScale 
} from '../utils/animations';

const customers = customersData as Customer[];
const orders = ordersData as Order[];
const supportTickets = supportTicketsData as SupportTicket[];

function CustomerPortal() {
  const [selectedCustomerId, setSelectedCustomerId] = useState(customers[0]?.customer_id || '');
  const customer = customers.find(c => c.customer_id === selectedCustomerId);

  const customerOrders = useMemo(() => {
    return orders
      .filter(o => o.customer_id === selectedCustomerId)
      .sort((a, b) => new Date(b.order_date).getTime() - new Date(a.order_date).getTime());
  }, [selectedCustomerId]);

  const customerTickets = useMemo(() => {
    return supportTickets
      .filter(t => t.customer_id === selectedCustomerId)
      .sort((a, b) => new Date(b.created_date).getTime() - new Date(a.created_date).getTime());
  }, [selectedCustomerId]);

  const stats = useMemo(() => {
    const totalOrders = customerOrders.length;
    const totalSpent = customerOrders.reduce((sum, order) => sum + order.total, 0);
    const openTickets = customerTickets.filter(t => t.status !== 'Closed').length;
    const avgOrderValue = totalOrders > 0 ? totalSpent / totalOrders : 0;

    return { totalOrders, totalSpent, openTickets, avgOrderValue };
  }, [customerOrders, customerTickets]);

  const ordersByMonth = useMemo(() => {
    const monthlyData: { [key: string]: { month: string; orders: number; revenue: number } } = {};
    
    customerOrders.forEach(order => {
      const date = new Date(order.order_date);
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
      const monthName = date.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });
      
      if (!monthlyData[monthKey]) {
        monthlyData[monthKey] = { month: monthName, orders: 0, revenue: 0 };
      }
      monthlyData[monthKey].orders += 1;
      monthlyData[monthKey].revenue += order.total;
    });

    return Object.values(monthlyData).slice(-6);
  }, [customerOrders]);

  if (!customer) {
    return (
      <motion.div 
        className="min-h-screen bg-background flex items-center justify-center"
        initial="initial"
        animate="animate"
        exit="exit"
        variants={pageVariants}
      >
        <motion.div 
          className="text-center max-w-md mx-auto bg-surface/60 backdrop-blur-sm rounded-[24px] border border-border/60 shadow-xl p-12"
          variants={fadeInScale}
        >
          <motion.div
            className="mb-6"
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
              <User className="w-10 h-10 text-primary-400" strokeWidth={2} />
            </div>
          </motion.div>
          <h2 className="text-2xl font-display font-bold text-text mb-3 tracking-tight">No Customer Data</h2>
          <p className="text-text-muted leading-relaxed">Please select a customer to view their portal.</p>
        </motion.div>
      </motion.div>
    );
  }

  const getStatusColor = (status: string) => {
    const statusColors: { [key: string]: string } = {
      'Completed': 'bg-green-500/20 text-green-400 border border-green-500/30',
      'Shipped': 'bg-blue-500/20 text-blue-400 border border-blue-500/30',
      'Processing': 'bg-yellow-500/20 text-yellow-400 border border-yellow-500/30',
      'Pending': 'bg-orange-500/20 text-orange-400 border border-orange-500/30',
      'Cancelled': 'bg-red-500/20 text-red-400 border border-red-500/30',
      'Open': 'bg-yellow-500/20 text-yellow-400 border border-yellow-500/30',
      'In Progress': 'bg-blue-500/20 text-blue-400 border border-blue-500/30',
      'Closed': 'bg-green-500/20 text-green-400 border border-green-500/30',
      'High': 'bg-red-500/20 text-red-400 border border-red-500/30',
      'Medium': 'bg-orange-500/20 text-orange-400 border border-orange-500/30',
      'Low': 'bg-green-500/20 text-green-400 border border-green-500/30',
      'Active': 'bg-green-500/20 text-green-400 border border-green-500/30',
    };
    return statusColors[status] || 'bg-surface-elevated text-text-muted border border-border';
  };

  return (
    <motion.div 
      className="min-h-screen bg-background"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageVariants}
    >
      {/* Hero Header - Enhanced with animations */}
      <section className="relative bg-gradient-to-br from-primary-900/40 via-background to-background text-text pt-32 pb-8 overflow-hidden">
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
            <User className="w-3.5 h-3.5" strokeWidth={2.5} />
            <span className="tracking-wide">Customer Portal</span>
          </motion.div>
          
          <motion.h1 
            className="text-2xl md:text-3xl lg:text-4xl font-display font-black mb-4 tracking-tight"
            variants={fadeInUp}
          >
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-300 via-text to-accent-300">
              Customer Portal
            </span>
          </motion.h1>
          <motion.p 
            className="text-sm md:text-base text-text-muted max-w-3xl leading-relaxed"
            variants={fadeInUp}
            transition={{ delay: 0.1 }}
          >
            Access your orders, support tickets, and account information
          </motion.p>
        </div>
      </section>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Customer Selector - Enhanced Design */}
        <motion.div 
          className="mb-12"
          variants={fadeInUp}
          transition={{ delay: 0.2 }}
        >
          <div className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border">
            <div className="absolute inset-0 bg-gradient-to-br from-primary-900/5 to-accent-900/5 rounded-[20px]"></div>
            <div className="relative">
              <label className="flex items-center gap-2 text-sm font-bold text-text mb-4">
                <div className="w-8 h-8 bg-gradient-to-br from-primary-500 to-primary-700 rounded-[10px] flex items-center justify-center shadow-md">
                  <Building2 className="w-4 h-4 text-white" strokeWidth={2.5} />
                </div>
                Select Customer Account
              </label>
              <motion.select
                value={selectedCustomerId}
                onChange={(e) => setSelectedCustomerId(e.target.value)}
                className="w-full px-5 py-3 border-2 border-border rounded-[16px] focus:ring-2 focus:ring-primary-500/50 focus:border-primary-500/70 outline-none bg-surface text-text text-sm font-semibold cursor-pointer hover:border-primary-500/50 hover:bg-surface-elevated transition-all duration-300 shadow-lg"
                whileHover={{ scale: 1.005 }}
                whileTap={{ scale: 0.998 }}
              >
                {customers.slice(0, 50).map((c) => (
                  <option key={c.customer_id} value={c.customer_id}>
                    {c.company_name} - {c.contact_first_name} {c.contact_last_name}
                  </option>
                ))}
              </motion.select>
            </div>
          </div>
        </motion.div>

        {/* Customer Info - Enhanced Design */}
        <motion.div 
          className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-8 shadow-xl border border-border mb-12 overflow-hidden group"
          variants={fadeInUp}
          transition={{ delay: 0.3 }}
          whileHover={{ y: -4 }}
        >
          <div className="absolute inset-0 bg-gradient-to-br from-primary-900/5 to-accent-900/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div className="relative">
            <div className="flex flex-col md:flex-row md:items-start justify-between mb-6 gap-4">
              <div className="flex-1">
                <div className="flex items-start gap-4 mb-4">
                  <div className="w-16 h-16 bg-gradient-to-br from-primary-400 to-primary-600 rounded-[16px] flex items-center justify-center shadow-lg flex-shrink-0">
                    <Building2 className="w-8 h-8 text-white" strokeWidth={2} />
                  </div>
                  <div>
                    <h2 className="text-2xl font-display font-black text-text mb-2 tracking-tight">{customer.company_name}</h2>
                    <div className="flex items-center gap-2 text-text-muted mb-2">
                      <User className="w-4 h-4" />
                      <p className="font-semibold">{customer.contact_first_name} {customer.contact_last_name}</p>
                    </div>
                    <div className="flex flex-col gap-1.5 text-sm text-text-subtle">
                      <div className="flex items-center gap-2">
                        <Mail className="w-3.5 h-3.5" />
                        <span>{customer.email}</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <Phone className="w-3.5 h-3.5" />
                        <span>{customer.phone}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <motion.span 
                className={`px-4 py-2 rounded-[12px] text-sm font-bold ${getStatusColor(customer.status)} shadow-md flex-shrink-0 h-fit`}
                whileHover={{ scale: 1.05 }}
              >
                {customer.status}
              </motion.span>
            </div>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-6 border-t border-border">
              <div className="p-4 bg-surface-elevated/50 rounded-[14px] border border-border/50">
                <div className="text-xs font-bold text-text-muted mb-2 uppercase tracking-wider flex items-center gap-1.5">
                  <Package className="w-3.5 h-3.5" />
                  Customer Type
                </div>
                <div className="font-bold text-text text-base">{customer.customer_type}</div>
              </div>
              <div className="p-4 bg-surface-elevated/50 rounded-[14px] border border-border/50">
                <div className="text-xs font-bold text-text-muted mb-2 uppercase tracking-wider flex items-center gap-1.5">
                  <Building2 className="w-3.5 h-3.5" />
                  Industry
                </div>
                <div className="font-bold text-text text-base">{customer.industry}</div>
              </div>
              <div className="p-4 bg-surface-elevated/50 rounded-[14px] border border-border/50">
                <div className="text-xs font-bold text-text-muted mb-2 uppercase tracking-wider flex items-center gap-1.5">
                  <User className="w-3.5 h-3.5" />
                  Account Manager
                </div>
                <div className="font-bold text-text text-base">{customer.account_manager}</div>
              </div>
              <div className="p-4 bg-surface-elevated/50 rounded-[14px] border border-border/50">
                <div className="text-xs font-bold text-text-muted mb-2 uppercase tracking-wider flex items-center gap-1.5">
                  <Calendar className="w-3.5 h-3.5" />
                  Member Since
                </div>
                <div className="font-bold text-text text-base">
                  {new Date(customer.signup_date).toLocaleDateString()}
                </div>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Stats - Enhanced with animations and better styling */}
        <motion.div 
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12"
          variants={staggerContainer}
          initial="initial"
          whileInView="animate"
          viewport={{ once: true, margin: "-80px" }}
        >
          <motion.div 
            className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border overflow-hidden group cursor-pointer"
            variants={staggerItem}
            whileHover={{ y: -12, scale: 1.03 }}
            whileTap={{ scale: 0.98 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Animated gradient overlay */}
            <div className="absolute inset-0 bg-gradient-to-br from-primary-400/20 via-primary-500/10 to-primary-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            
            {/* Shimmer effect on hover */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                 style={{
                   background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.1) 50%, transparent 60%)',
                   backgroundSize: '200% 100%',
                   animation: 'shimmer 1.5s ease-in-out infinite'
                 }}></div>
            
            {/* Glow effect */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-500 bg-gradient-to-br from-primary-400/30 to-transparent"></div>
            
            <div className="relative">
              <div className="flex items-center justify-between mb-4">
                <motion.div 
                  className="w-12 h-12 bg-gradient-to-br from-primary-400 to-primary-600 rounded-[14px] flex items-center justify-center shadow-lg relative"
                  whileHover={{ rotate: [0, -10, 10, -10, 0], scale: 1.15 }}
                  transition={{ duration: 0.5 }}
                >
                  {/* Icon glow on hover */}
                  <div className="absolute inset-0 bg-primary-300 rounded-[14px] blur-md opacity-0 group-hover:opacity-60 transition-opacity duration-300"></div>
                  <ShoppingCart className="w-6 h-6 text-white relative z-10" strokeWidth={2.5} />
                </motion.div>
                <motion.span 
                  className="text-3xl font-display font-black text-transparent bg-clip-text bg-gradient-to-br from-primary-300 to-primary-400"
                  whileHover={{ scale: 1.1 }}
                  transition={{ duration: 0.3 }}
                >
                  {stats.totalOrders}
                </motion.span>
              </div>
              <div className="text-xs font-bold text-text-muted uppercase tracking-wider group-hover:text-primary-300 transition-colors duration-300">Total Orders</div>
            </div>
          </motion.div>

          <motion.div 
            className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border overflow-hidden group cursor-pointer"
            variants={staggerItem}
            whileHover={{ y: -12, scale: 1.03 }}
            whileTap={{ scale: 0.98 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Animated gradient overlay */}
            <div className="absolute inset-0 bg-gradient-to-br from-green-400/20 via-green-500/10 to-green-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            
            {/* Shimmer effect on hover */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                 style={{
                   background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.1) 50%, transparent 60%)',
                   backgroundSize: '200% 100%',
                   animation: 'shimmer 1.5s ease-in-out infinite'
                 }}></div>
            
            {/* Glow effect */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-500 bg-gradient-to-br from-green-400/30 to-transparent"></div>
            
            <div className="relative">
              <div className="flex items-center justify-between mb-4">
                <motion.div 
                  className="w-12 h-12 bg-gradient-to-br from-green-400 to-green-600 rounded-[14px] flex items-center justify-center shadow-lg relative"
                  whileHover={{ rotate: [0, -10, 10, -10, 0], scale: 1.15 }}
                  transition={{ duration: 0.5 }}
                >
                  {/* Icon glow on hover */}
                  <div className="absolute inset-0 bg-green-300 rounded-[14px] blur-md opacity-0 group-hover:opacity-60 transition-opacity duration-300"></div>
                  <DollarSign className="w-6 h-6 text-white relative z-10" strokeWidth={2.5} />
                </motion.div>
                <motion.span 
                  className="text-3xl font-display font-black text-transparent bg-clip-text bg-gradient-to-br from-green-300 to-green-400"
                  whileHover={{ scale: 1.1 }}
                  transition={{ duration: 0.3 }}
                >
                  ${Math.round(stats.totalSpent).toLocaleString()}
                </motion.span>
              </div>
              <div className="text-xs font-bold text-text-muted uppercase tracking-wider group-hover:text-green-300 transition-colors duration-300">Total Spent</div>
            </div>
          </motion.div>

          <motion.div 
            className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border overflow-hidden group cursor-pointer"
            variants={staggerItem}
            whileHover={{ y: -12, scale: 1.03 }}
            whileTap={{ scale: 0.98 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Animated gradient overlay */}
            <div className="absolute inset-0 bg-gradient-to-br from-blue-400/20 via-blue-500/10 to-blue-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            
            {/* Shimmer effect on hover */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                 style={{
                   background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.1) 50%, transparent 60%)',
                   backgroundSize: '200% 100%',
                   animation: 'shimmer 1.5s ease-in-out infinite'
                 }}></div>
            
            {/* Glow effect */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-500 bg-gradient-to-br from-blue-400/30 to-transparent"></div>
            
            <div className="relative">
              <div className="flex items-center justify-between mb-4">
                <motion.div 
                  className="w-12 h-12 bg-gradient-to-br from-blue-400 to-blue-600 rounded-[14px] flex items-center justify-center shadow-lg relative"
                  whileHover={{ rotate: [0, -10, 10, -10, 0], scale: 1.15 }}
                  transition={{ duration: 0.5 }}
                >
                  {/* Icon glow on hover */}
                  <div className="absolute inset-0 bg-blue-300 rounded-[14px] blur-md opacity-0 group-hover:opacity-60 transition-opacity duration-300"></div>
                  <TrendingUp className="w-6 h-6 text-white relative z-10" strokeWidth={2.5} />
                </motion.div>
                <motion.span 
                  className="text-3xl font-display font-black text-transparent bg-clip-text bg-gradient-to-br from-blue-300 to-blue-400"
                  whileHover={{ scale: 1.1 }}
                  transition={{ duration: 0.3 }}
                >
                  ${Math.round(stats.avgOrderValue).toLocaleString()}
                </motion.span>
              </div>
              <div className="text-xs font-bold text-text-muted uppercase tracking-wider group-hover:text-blue-300 transition-colors duration-300">Avg Order Value</div>
            </div>
          </motion.div>

          <motion.div 
            className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border overflow-hidden group cursor-pointer"
            variants={staggerItem}
            whileHover={{ y: -12, scale: 1.03 }}
            whileTap={{ scale: 0.98 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Animated gradient overlay */}
            <div className="absolute inset-0 bg-gradient-to-br from-orange-400/20 via-orange-500/10 to-orange-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            
            {/* Shimmer effect on hover */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-300"
                 style={{
                   background: 'linear-gradient(110deg, transparent 40%, rgba(255, 255, 255, 0.1) 50%, transparent 60%)',
                   backgroundSize: '200% 100%',
                   animation: 'shimmer 1.5s ease-in-out infinite'
                 }}></div>
            
            {/* Glow effect */}
            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 blur-xl transition-opacity duration-500 bg-gradient-to-br from-orange-400/30 to-transparent"></div>
            
            <div className="relative">
              <div className="flex items-center justify-between mb-4">
                <motion.div 
                  className="w-12 h-12 bg-gradient-to-br from-orange-400 to-orange-600 rounded-[14px] flex items-center justify-center shadow-lg relative"
                  whileHover={{ rotate: [0, -10, 10, -10, 0], scale: 1.15 }}
                  transition={{ duration: 0.5 }}
                >
                  {/* Icon glow on hover */}
                  <div className="absolute inset-0 bg-orange-300 rounded-[14px] blur-md opacity-0 group-hover:opacity-60 transition-opacity duration-300"></div>
                  <AlertCircle className="w-6 h-6 text-white relative z-10" strokeWidth={2.5} />
                </motion.div>
                <motion.span 
                  className="text-3xl font-display font-black text-transparent bg-clip-text bg-gradient-to-br from-orange-300 to-orange-400"
                  whileHover={{ scale: 1.1 }}
                  transition={{ duration: 0.3 }}
                >
                  {stats.openTickets}
                </motion.span>
              </div>
              <div className="text-xs font-bold text-text-muted uppercase tracking-wider group-hover:text-orange-300 transition-colors duration-300">Open Tickets</div>
            </div>
          </motion.div>
        </motion.div>

        {/* Charts - Enhanced Design */}
        {ordersByMonth.length > 0 && (
          <motion.div 
            className="grid md:grid-cols-2 gap-6 mb-12"
            variants={staggerContainer}
            initial="initial"
            whileInView="animate"
            viewport={{ once: true, margin: "-80px" }}
          >
            <motion.div 
              className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border overflow-hidden"
              variants={staggerItem}
            >
              <div className="absolute inset-0 bg-gradient-to-br from-primary-900/5 to-blue-900/5"></div>
              <div className="relative">
                <div className="flex items-center gap-3 mb-6">
                  <div className="w-10 h-10 bg-gradient-to-br from-blue-400 to-blue-600 rounded-[12px] flex items-center justify-center shadow-lg">
                    <TrendingUp className="w-5 h-5 text-white" strokeWidth={2.5} />
                  </div>
                  <h3 className="text-lg font-display font-bold text-text tracking-tight">Orders Over Time</h3>
                </div>
                <ResponsiveContainer width="100%" height={200}>
                  <LineChart data={ordersByMonth}>
                    <CartesianGrid strokeDasharray="3 3" stroke="oklch(0.35 0.03 195)" />
                    <XAxis dataKey="month" style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                    <YAxis style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: 'oklch(0.18 0.02 195)', 
                        border: '1px solid oklch(0.35 0.03 195)', 
                        color: 'oklch(0.98 0.005 195)',
                        borderRadius: '12px',
                        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
                      }} 
                    />
                    <Line type="monotone" dataKey="orders" stroke="oklch(0.62 0.12 195)" strokeWidth={3} dot={{ fill: 'oklch(0.62 0.12 195)', r: 4 }} />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </motion.div>
            
            <motion.div 
              className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border overflow-hidden"
              variants={staggerItem}
            >
              <div className="absolute inset-0 bg-gradient-to-br from-primary-900/5 to-green-900/5"></div>
              <div className="relative">
                <div className="flex items-center gap-3 mb-6">
                  <div className="w-10 h-10 bg-gradient-to-br from-green-400 to-green-600 rounded-[12px] flex items-center justify-center shadow-lg">
                    <DollarSign className="w-5 h-5 text-white" strokeWidth={2.5} />
                  </div>
                  <h3 className="text-lg font-display font-bold text-text tracking-tight">Revenue Over Time</h3>
                </div>
                <ResponsiveContainer width="100%" height={200}>
                  <BarChart data={ordersByMonth}>
                    <CartesianGrid strokeDasharray="3 3" stroke="oklch(0.35 0.03 195)" />
                    <XAxis dataKey="month" style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                    <YAxis style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: 'oklch(0.18 0.02 195)', 
                        border: '1px solid oklch(0.35 0.03 195)', 
                        color: 'oklch(0.98 0.005 195)',
                        borderRadius: '12px',
                        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)'
                      }} 
                    />
                    <Bar dataKey="revenue" fill="oklch(0.62 0.12 195)" radius={[8, 8, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </motion.div>
          </motion.div>
        )}

        {/* Orders - Enhanced Design */}
        <motion.div 
          className="mb-12"
          variants={fadeInUp}
          initial="initial"
          whileInView="animate"
          viewport={{ once: true, margin: "-80px" }}
        >
          <div className="flex items-center gap-3 mb-6">
            <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-700 rounded-[12px] flex items-center justify-center shadow-lg">
              <ShoppingCart className="w-5 h-5 text-white" strokeWidth={2.5} />
            </div>
            <h2 className="text-2xl font-display font-black text-text tracking-tight">Recent Orders</h2>
          </div>
          
          <div className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] shadow-xl border border-border overflow-hidden">
            <div className="absolute inset-0 bg-gradient-to-br from-primary-900/5 to-accent-900/5"></div>
            <div className="relative overflow-x-auto">
              <table className="w-full">
                <thead className="bg-surface-elevated/80 backdrop-blur-sm border-b-2 border-border">
                  <tr>
                    <th className="px-6 py-4 text-left text-xs font-black text-text-muted uppercase tracking-wider">Order ID</th>
                    <th className="px-6 py-4 text-left text-xs font-black text-text-muted uppercase tracking-wider">Date</th>
                    <th className="px-6 py-4 text-left text-xs font-black text-text-muted uppercase tracking-wider">Status</th>
                    <th className="px-6 py-4 text-left text-xs font-black text-text-muted uppercase tracking-wider">Payment</th>
                    <th className="px-6 py-4 text-left text-xs font-black text-text-muted uppercase tracking-wider">Amount</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-border/50">
                  <AnimatePresence>
                    {customerOrders.slice(0, 10).map((order, index) => (
                      <motion.tr 
                        key={order.order_id} 
                        className="hover:bg-surface-elevated/60 transition-all duration-200 group"
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.05 }}
                      >
                        <td className="px-6 py-4 whitespace-nowrap text-sm font-bold text-text group-hover:text-primary-300 transition-colors">
                          {order.order_id}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-text-muted font-medium">
                          {new Date(order.order_date).toLocaleDateString()}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className={`px-3 py-1.5 text-xs font-bold rounded-[10px] ${getStatusColor(order.order_status)} shadow-sm`}>
                            {order.order_status}
                          </span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className={`px-3 py-1.5 text-xs font-bold rounded-[10px] ${getStatusColor(order.payment_terms)} shadow-sm`}>
                            {order.payment_terms}
                          </span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-base font-display font-black text-transparent bg-clip-text bg-gradient-to-r from-primary-300 to-accent-300">
                          ${order.total.toLocaleString()}
                        </td>
                      </motion.tr>
                    ))}
                  </AnimatePresence>
                </tbody>
              </table>
            </div>
          </div>
        </motion.div>

        {/* Support Tickets - Enhanced Design */}
        <motion.div
          variants={fadeInUp}
          initial="initial"
          whileInView="animate"
          viewport={{ once: true, margin: "-80px" }}
        >
          <div className="flex items-center gap-3 mb-6">
            <div className="w-10 h-10 bg-gradient-to-br from-orange-400 to-orange-600 rounded-[12px] flex items-center justify-center shadow-lg">
              <AlertCircle className="w-5 h-5 text-white" strokeWidth={2.5} />
            </div>
            <h2 className="text-2xl font-display font-black text-text tracking-tight">Support Tickets</h2>
          </div>
          
          <motion.div 
            className="space-y-4"
            variants={staggerContainer}
            initial="initial"
            animate="animate"
          >
            {customerTickets.slice(0, 10).map((ticket) => (
              <motion.div 
                key={ticket.ticket_id} 
                className="relative bg-surface/90 backdrop-blur-sm rounded-[20px] p-6 shadow-xl border border-border overflow-hidden group hover:shadow-2xl transition-all duration-500"
                variants={staggerItem}
                whileHover={{ y: -4, scale: 1.01 }}
                transition={{ duration: 0.3 }}
              >
                <div className="absolute inset-0 bg-gradient-to-br from-primary-900/5 to-accent-900/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                
                <div className="relative">
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <div className="flex flex-wrap items-center gap-3 mb-3">
                        <h3 className="text-lg font-display font-bold text-text group-hover:text-primary-300 transition-colors tracking-tight">
                          {ticket.subject}
                        </h3>
                        <span className={`px-3 py-1.5 text-xs font-bold rounded-[10px] ${getStatusColor(ticket.status)} shadow-md`}>
                          {ticket.status}
                        </span>
                        <span className={`px-3 py-1.5 text-xs font-bold rounded-[10px] ${getStatusColor(ticket.priority)} shadow-md`}>
                          {ticket.priority}
                        </span>
                      </div>
                      <div className="flex items-center gap-2 text-sm text-text-muted font-medium">
                        <Package className="w-4 h-4" />
                        <span>Category: <span className="text-text font-bold">{ticket.category}</span></span>
                      </div>
                    </div>
                  </div>
                  
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-4 border-t border-border/50">
                    <div className="flex flex-col">
                      <span className="text-xs font-bold text-text-muted uppercase tracking-wider mb-1">Ticket ID</span>
                      <span className="text-sm font-bold text-text">{ticket.ticket_id}</span>
                    </div>
                    <div className="flex flex-col">
                      <span className="text-xs font-bold text-text-muted uppercase tracking-wider mb-1">Assigned To</span>
                      <span className="text-sm font-bold text-text">{ticket.assigned_to}</span>
                    </div>
                    <div className="flex flex-col">
                      <span className="text-xs font-bold text-text-muted uppercase tracking-wider mb-1">Created</span>
                      <span className="text-sm font-bold text-text">{new Date(ticket.created_date).toLocaleDateString()}</span>
                    </div>
                    {ticket.satisfaction_rating && (
                      <div className="flex flex-col">
                        <span className="text-xs font-bold text-text-muted uppercase tracking-wider mb-1">Rating</span>
                        <span className="text-sm font-bold text-accent-300">{ticket.satisfaction_rating}/5 ⭐</span>
                      </div>
                    )}
                  </div>
                </div>
              </motion.div>
            ))}
          </motion.div>
        </motion.div>
      </div>
    </motion.div>
  );
}

export default CustomerPortal;

