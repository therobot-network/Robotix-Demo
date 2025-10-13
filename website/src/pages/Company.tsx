import { Users, Target, Award, TrendingUp, Mail, Linkedin, Sparkles, Building2, Lightbulb, Handshake, Shield, Leaf, CheckCircle2 } from 'lucide-react';
import { motion } from 'framer-motion';
import employeesData from '../data/employees.json';
import customersData from '../data/customers.json';
import { Customer } from '../types';
import { 
  pageVariants, 
  staggerContainer, 
  staggerItem 
} from '../utils/animations';

const employees = employeesData as any[];
const customers = customersData as Customer[];

function Company() {
  const departments = Array.from(new Set(employees.map(e => e.department)));
  const topEmployees = employees
    .filter(e => e.status === 'Active' && (e.department === 'Executive Leadership' || e.manager === e.full_name))
    .slice(0, 8);

  return (
    <motion.div 
      className="overflow-hidden"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageVariants}
    >
      {/* Hero Section - Modern with Animated Background */}
      <section className="relative min-h-[44vh] flex items-center overflow-hidden">
        {/* Animated Gradient Background */}
        <div className="absolute inset-0 bg-black">
          {/* Subtle accent lines */}
          <div className="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-white/20 to-transparent"></div>
          <div className="absolute bottom-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-white/10 to-transparent"></div>
          <div className="absolute top-1/4 left-1/4 w-40 h-px bg-gradient-to-r from-transparent via-accent-500/20 to-transparent rotate-45"></div>
          <div className="absolute top-1/3 right-1/4 w-32 h-px bg-gradient-to-l from-transparent via-secondary-500/20 to-transparent -rotate-45"></div>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 w-full">
          <motion.div 
            className="text-center max-w-4xl mx-auto"
            variants={staggerContainer}
            initial="initial"
            animate="animate"
          >
            <motion.div 
              className="inline-flex items-center gap-2.5 px-5 py-2.5 bg-white/10 backdrop-blur-xl rounded-full border border-white/20 mb-8"
              variants={staggerItem}
            >
              <Building2 className="w-4 h-4 text-accent-400" />
              <span className="text-xs font-semibold text-white/90 tracking-wider uppercase">Est. 2015 · Leading Innovation</span>
            </motion.div>
            
            <motion.h1 
              className="text-5xl md:text-6xl lg:text-7xl font-display font-black mb-6 leading-[1.05] tracking-tight"
              variants={staggerItem}
            >
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-white/90 via-white to-white/80">
                About
              </span>
              <span className="block text-transparent bg-clip-text bg-gradient-to-r from-accent-300 via-primary-200 to-secondary-300 mt-2">
                Robotix
              </span>
            </motion.h1>
            
            <motion.p 
              className="text-base md:text-lg text-white/60 leading-relaxed max-w-3xl mx-auto font-light"
              variants={staggerItem}
            >
              Pioneering the future of industrial automation since 2015. We're on a mission to empower 
              manufacturers worldwide with intelligent robotics solutions that drive productivity and innovation.
            </motion.p>
          </motion.div>
        </div>
      </section>

      {/* Mission & Vision */}
      <section className="py-12 bg-gradient-to-b from-background to-surface-muted relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="grid md:grid-cols-2 gap-8"
            variants={staggerContainer}
            initial="initial"
            whileInView="animate"
            viewport={{ once: true, margin: "-80px" }}
          >
            <motion.div 
              className="glass-card p-8 hover:scale-[1.01] transition-all duration-500 shadow-xl hover:shadow-2xl hover:shadow-primary-500/10 group"
              variants={staggerItem}
            >
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-primary-400/30 blur-2xl group-hover:bg-primary-400/40 transition-all duration-500"></div>
                <div className="relative w-16 h-16 bg-gradient-to-br from-surface-elevated to-surface rounded-[18px] flex items-center justify-center border border-border shadow-lg group-hover:rotate-3 group-hover:scale-[1.05] transition-all duration-500">
                  <Target className="w-9 h-9 text-primary-400" strokeWidth={2} />
                </div>
              </div>
              <h2 className="text-3xl font-display font-black text-text mb-4 tracking-tight group-hover:text-primary-300 transition-colors duration-300">Our Mission</h2>
              <p className="text-text-muted leading-relaxed text-base">
                To revolutionize manufacturing through innovative robotics and automation solutions that enhance 
                productivity, safety, and sustainability. We strive to make advanced automation accessible to 
                businesses of all sizes, empowering them to compete in the global marketplace.
              </p>
            </motion.div>
            <motion.div 
              className="glass-card p-8 hover:scale-[1.01] transition-all duration-500 shadow-xl hover:shadow-2xl hover:shadow-secondary-500/10 group"
              variants={staggerItem}
            >
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-secondary-400/30 blur-2xl group-hover:bg-secondary-400/40 transition-all duration-500"></div>
                <div className="relative w-16 h-16 bg-gradient-to-br from-surface-elevated to-surface rounded-[18px] flex items-center justify-center border border-border shadow-lg group-hover:rotate-3 group-hover:scale-[1.05] transition-all duration-500">
                  <Award className="w-9 h-9 text-secondary-400" strokeWidth={2} />
                </div>
              </div>
              <h2 className="text-3xl font-display font-black text-text mb-4 tracking-tight group-hover:text-secondary-300 transition-colors duration-300">Our Vision</h2>
              <p className="text-text-muted leading-relaxed text-base">
                To be the world's most trusted partner in industrial automation, recognized for innovation, 
                reliability, and customer success. We envision a future where intelligent robotics seamlessly 
                integrate with human workers to create safer, more efficient, and more fulfilling workplaces.
              </p>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-16 bg-surface relative overflow-hidden">
        {/* Subtle animated background */}
        <div className="absolute top-1/2 left-1/4 w-96 h-96 bg-primary-400/5 rounded-full blur-[100px] animate-blob"></div>
        <div className="absolute bottom-1/2 right-1/4 w-96 h-96 bg-accent-400/5 rounded-full blur-[100px] animate-blob" style={{ animationDelay: '3s' }}></div>
        
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-10"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="inline-flex items-center gap-2.5 px-5 py-2 bg-gradient-to-r from-primary-600 to-secondary-600 text-background rounded-full text-xs font-black mb-4 shadow-lg shadow-primary-600/30">
              <TrendingUp className="w-4 h-4" strokeWidth={2.5} />
              <span className="tracking-wide">Company Stats</span>
            </div>
            <h2 className="text-3xl md:text-4xl font-display font-black text-text tracking-tight mb-3">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-400 via-primary-300 to-accent-400">
                By the Numbers
              </span>
            </h2>
            <p className="text-text-muted max-w-2xl mx-auto text-base">
              Our growth and impact in the industrial automation industry
            </p>
          </motion.div>
          <motion.div 
            className="grid grid-cols-2 md:grid-cols-4 gap-6"
            variants={staggerContainer}
            initial="initial"
            whileInView="animate"
            viewport={{ once: true, margin: "-80px" }}
          >
            <motion.div 
              className="glass-card p-6 text-center hover:scale-[1.02] transition-all duration-300 shadow-lg hover:shadow-xl hover:shadow-primary-400/10 group"
              variants={staggerItem}
            >
              <div className="text-4xl md:text-5xl font-display font-black text-text tracking-tight group-hover:text-primary-300 transition-colors duration-300 mb-2">
                {customers.filter(c => c.status === 'Active').length}+
              </div>
              <div className="text-[11px] text-text-muted font-bold uppercase tracking-wider">Active Customers</div>
            </motion.div>
            <motion.div 
              className="glass-card p-6 text-center hover:scale-[1.02] transition-all duration-300 shadow-lg hover:shadow-xl hover:shadow-secondary-400/10 group"
              variants={staggerItem}
            >
              <div className="text-4xl md:text-5xl font-display font-black text-text tracking-tight group-hover:text-secondary-300 transition-colors duration-300 mb-2">
                {employees.filter(e => e.status === 'Active').length}
              </div>
              <div className="text-[11px] text-text-muted font-bold uppercase tracking-wider">Team Members</div>
            </motion.div>
            <motion.div 
              className="glass-card p-6 text-center hover:scale-[1.02] transition-all duration-300 shadow-lg hover:shadow-xl hover:shadow-accent-400/10 group"
              variants={staggerItem}
            >
              <div className="text-4xl md:text-5xl font-display font-black text-text tracking-tight group-hover:text-accent-300 transition-colors duration-300 mb-2">45+</div>
              <div className="text-[11px] text-text-muted font-bold uppercase tracking-wider">Countries Served</div>
            </motion.div>
            <motion.div 
              className="glass-card p-6 text-center hover:scale-[1.02] transition-all duration-300 shadow-lg hover:shadow-xl hover:shadow-primary-400/10 group"
              variants={staggerItem}
            >
              <div className="text-4xl md:text-5xl font-display font-black text-text tracking-tight group-hover:text-primary-300 transition-colors duration-300 mb-2">98%</div>
              <div className="text-[11px] text-text-muted font-bold uppercase tracking-wider">Customer Satisfaction</div>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* Values */}
      <section className="py-16 bg-gradient-to-b from-background via-surface-muted to-background relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-10"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="inline-flex items-center gap-2.5 px-5 py-2 bg-gradient-to-r from-secondary-600 to-primary-600 text-background rounded-full text-xs font-black mb-4 shadow-lg shadow-secondary-600/30">
              <Sparkles className="w-4 h-4" strokeWidth={2.5} />
              <span className="tracking-wide">Our Values</span>
            </div>
            <h2 className="text-3xl md:text-4xl font-display font-black text-text tracking-tight mb-3">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-secondary-400 via-primary-300 to-accent-400">
                Core Values
              </span>
            </h2>
            <p className="text-text-muted max-w-2xl mx-auto text-base">
              The principles that guide everything we do
            </p>
          </motion.div>
          <motion.div 
            className="grid md:grid-cols-2 lg:grid-cols-3 gap-6"
            variants={staggerContainer}
            initial="initial"
            whileInView="animate"
            viewport={{ once: true, margin: "-80px" }}
          >
            {[
              {
                icon: Lightbulb,
                title: 'Innovation',
                description: 'We continuously push boundaries, embracing new technologies and creative solutions to solve complex manufacturing challenges.',
                color: 'primary'
              },
              {
                icon: CheckCircle2,
                title: 'Quality',
                description: 'Excellence is not negotiable. Every product we deliver meets the highest standards of performance and reliability.',
                color: 'accent'
              },
              {
                icon: Handshake,
                title: 'Partnership',
                description: 'We build lasting relationships with our customers, working as true partners to achieve their business objectives.',
                color: 'secondary'
              },
              {
                icon: Shield,
                title: 'Integrity',
                description: 'We operate with honesty and transparency in all our business dealings, building trust through consistent ethical behavior.',
                color: 'primary'
              },
              {
                icon: Shield,
                title: 'Safety',
                description: 'Worker safety is paramount. Our solutions are designed to create safer working environments for all.',
                color: 'accent'
              },
              {
                icon: Leaf,
                title: 'Sustainability',
                description: 'We\'re committed to environmental responsibility, creating solutions that reduce waste and energy consumption.',
                color: 'secondary'
              },
            ].map((value, index) => {
              const Icon = value.icon;
              const colorClasses = {
                primary: 'bg-gradient-to-br from-primary-400 to-primary-600 shadow-primary-600/30',
                secondary: 'bg-gradient-to-br from-secondary-400 to-secondary-600 shadow-secondary-600/30',
                accent: 'bg-gradient-to-br from-accent-400 to-accent-600 shadow-accent-600/30'
              };
              return (
                <motion.div 
                  key={index} 
                  className="glass-card p-6 hover:scale-[1.01] transition-all duration-300 shadow-lg hover:shadow-xl hover:shadow-primary-500/10 group"
                  variants={staggerItem}
                >
                  <div className={`w-12 h-12 rounded-[14px] flex items-center justify-center mb-4 shadow-lg group-hover:scale-[1.05] group-hover:rotate-3 transition-transform duration-300 ${colorClasses[value.color as keyof typeof colorClasses]}`}>
                    <Icon className="w-6 h-6 text-background" strokeWidth={2.5} />
                  </div>
                  <h3 className="text-xl font-display font-bold text-text mb-3 tracking-tight">{value.title}</h3>
                  <p className="text-text-muted leading-relaxed text-sm">{value.description}</p>
                </motion.div>
              );
            })}
          </motion.div>
        </div>
      </section>

      {/* Departments */}
      <section className="py-16 bg-surface relative overflow-hidden">
        <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-secondary-400/5 rounded-full blur-[100px] animate-blob"></div>
        
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-10"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="inline-flex items-center gap-2.5 px-5 py-2 bg-gradient-to-r from-accent-600 to-primary-600 text-background rounded-full text-xs font-black mb-4 shadow-lg shadow-accent-600/30">
              <Users className="w-4 h-4" strokeWidth={2.5} />
              <span className="tracking-wide">Our Team</span>
            </div>
            <h2 className="text-3xl md:text-4xl font-display font-black text-text tracking-tight mb-3">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-accent-400 via-secondary-300 to-primary-400">
                Our Departments
              </span>
            </h2>
            <p className="text-text-muted max-w-2xl mx-auto text-base">
              Diverse teams working together to deliver excellence
            </p>
          </motion.div>
          <motion.div 
            className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"
            variants={staggerContainer}
            initial="initial"
            whileInView="animate"
            viewport={{ once: true, margin: "-80px" }}
          >
            {departments.map((dept, index) => {
              const deptCount = employees.filter(e => e.department === dept && e.status === 'Active').length;
              const colorClasses = [
                'bg-gradient-to-br from-primary-400 to-primary-600 shadow-primary-600/30',
                'bg-gradient-to-br from-secondary-400 to-secondary-600 shadow-secondary-600/30',
                'bg-gradient-to-br from-accent-400 to-accent-600 shadow-accent-600/30'
              ];
              const colorClass = colorClasses[index % colorClasses.length];
              return (
                <motion.div 
                  key={dept} 
                  className="glass-card p-5 text-center hover:scale-[1.02] transition-all duration-300 shadow-lg hover:shadow-xl hover:shadow-primary-400/10 group"
                  variants={staggerItem}
                >
                  <div className={`w-12 h-12 rounded-[14px] flex items-center justify-center mx-auto mb-3 shadow-lg group-hover:scale-[1.05] group-hover:rotate-3 transition-transform duration-300 ${colorClass}`}>
                    <Users className="w-6 h-6 text-background" strokeWidth={2.5} />
                  </div>
                  <h3 className="font-display font-bold text-text mb-1 text-sm tracking-tight">{dept}</h3>
                  <p className="text-xs text-text-muted font-medium">{deptCount} members</p>
                </motion.div>
              );
            })}
          </motion.div>
        </div>
      </section>

      {/* Leadership */}
      <section className="py-16 bg-gradient-to-b from-background to-surface-muted relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div 
            className="text-center mb-10"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-80px" }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="inline-flex items-center gap-2.5 px-5 py-2 bg-gradient-to-r from-primary-600 to-accent-600 text-background rounded-full text-xs font-black mb-4 shadow-lg shadow-primary-600/30">
              <Award className="w-4 h-4" strokeWidth={2.5} />
              <span className="tracking-wide">Leadership</span>
            </div>
            <h2 className="text-3xl md:text-4xl font-display font-black text-text tracking-tight mb-3">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary-400 via-accent-300 to-secondary-400">
                Leadership Team
              </span>
            </h2>
            <p className="text-text-muted max-w-2xl mx-auto text-base">
              Meet the experts driving our vision forward
            </p>
          </motion.div>
          <motion.div 
            className="grid md:grid-cols-2 lg:grid-cols-4 gap-6"
            variants={staggerContainer}
            initial="initial"
            whileInView="animate"
            viewport={{ once: true, margin: "-80px" }}
          >
            {topEmployees.map((employee, index) => {
              const colorStyles = [
                {
                  bg: 'bg-gradient-to-br from-primary-400 to-primary-600 shadow-primary-600/30',
                  text: 'text-primary-300',
                  hover: 'hover:text-primary-400'
                },
                {
                  bg: 'bg-gradient-to-br from-secondary-400 to-secondary-600 shadow-secondary-600/30',
                  text: 'text-secondary-300',
                  hover: 'hover:text-secondary-400'
                },
                {
                  bg: 'bg-gradient-to-br from-accent-400 to-accent-600 shadow-accent-600/30',
                  text: 'text-accent-300',
                  hover: 'hover:text-accent-400'
                }
              ];
              const style = colorStyles[index % colorStyles.length];
              return (
                <motion.div 
                  key={employee.employee_id} 
                  className="glass-card p-6 text-center hover:scale-[1.01] transition-all duration-300 shadow-lg hover:shadow-xl hover:shadow-primary-500/10 group"
                  variants={staggerItem}
                >
                  <div className={`w-24 h-24 rounded-full mx-auto mb-4 flex items-center justify-center shadow-xl group-hover:scale-[1.05] transition-transform duration-300 ${style.bg}`}>
                    <Users className="w-12 h-12 text-background" strokeWidth={2} />
                  </div>
                  <h3 className="text-lg font-display font-bold text-text mb-1 tracking-tight">
                    {employee.first_name} {employee.last_name}
                  </h3>
                  <p className={`text-sm font-bold mb-2 ${style.text}`}>{employee.title}</p>
                  <p className="text-xs text-text-muted font-medium mb-4">{employee.department}</p>
                  <div className="flex justify-center gap-3 pt-3 border-t border-border">
                    <a href="#" className={`text-text-subtle transition-colors duration-300 ${style.hover}`}>
                      <Mail className="w-4 h-4" />
                    </a>
                    <a href="#" className={`text-text-subtle transition-colors duration-300 ${style.hover}`}>
                      <Linkedin className="w-4 h-4" />
                    </a>
                  </div>
                </motion.div>
              );
            })}
          </motion.div>
        </div>
      </section>

      {/* CTA Section - Enhanced with Rich Animated Background */}
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
              <span className="text-xs font-semibold text-white tracking-wide">Join Our Team</span>
            </div>
            
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-display font-black mb-6 leading-tight tracking-tight text-white">
              Join Our
              <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-accent-200 via-white to-accent-100 drop-shadow-2xl">Journey</span>
            </h2>
            
            <p className="text-lg text-white/95 mb-10 max-w-2xl mx-auto leading-relaxed">
              We're always looking for <span className="font-semibold text-accent-200">talented individuals</span> passionate about robotics and automation.
            </p>
            
            <motion.div
              whileHover={{ scale: 1.05, y: -4 }}
              whileTap={{ scale: 0.98 }}
            >
              <button className="group relative px-8 py-4 bg-white text-primary-900 rounded-[14px] font-bold text-base inline-flex items-center shadow-xl shadow-black/20 hover:shadow-2xl hover:shadow-accent-400/30 transition-all duration-300 overflow-hidden">
                <span className="relative z-10">View Open Positions</span>
                <Award className="w-4 h-4 ml-2 relative z-10 group-hover:rotate-6 transition-transform duration-300" />
                <div className="absolute inset-0 bg-gradient-to-r from-accent-400 to-accent-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
              </button>
            </motion.div>
          </motion.div>
        </div>
      </section>
    </motion.div>
  );
}

export default Company;

