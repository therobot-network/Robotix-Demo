import { useState, useMemo } from 'react';
import { User, ShoppingCart, AlertCircle, TrendingUp, DollarSign } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line } from 'recharts';
import customersData from '../data/customers.json';
import ordersData from '../data/orders.json';
import supportTicketsData from '../data/support_tickets.json';
import { Customer, Order, SupportTicket } from '../types';

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
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-center">
          <User className="w-16 h-16 text-text-subtle mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-text mb-2">No Customer Data</h2>
          <p className="text-text-muted">Please select a customer to view their portal.</p>
        </div>
      </div>
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
    <div className="min-h-screen bg-background">
      {/* Header */}
      <div className="gradient-primary text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-4xl font-bold mb-4">Customer Portal</h1>
          <p className="text-xl text-white/95 font-normal">Access your orders, support tickets, and account information</p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Customer Selector */}
        <div className="mb-8 card">
          <label className="block text-sm font-medium text-text mb-2">
            Select Customer Account
          </label>
          <select
            value={selectedCustomerId}
            onChange={(e) => setSelectedCustomerId(e.target.value)}
            className="w-full md:w-96 input-field"
          >
            {customers.slice(0, 50).map((c) => (
              <option key={c.customer_id} value={c.customer_id}>
                {c.company_name} - {c.contact_first_name} {c.contact_last_name}
              </option>
            ))}
          </select>
        </div>

        {/* Customer Info */}
        <div className="card mb-8">
          <div className="flex items-start justify-between mb-6">
            <div>
              <h2 className="text-2xl font-bold text-text mb-2">{customer.company_name}</h2>
              <p className="text-text-muted">{customer.contact_first_name} {customer.contact_last_name}</p>
              <p className="text-sm text-text-subtle">{customer.email} • {customer.phone}</p>
            </div>
            <span className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(customer.status)}`}>
              {customer.status}
            </span>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4 border-t border-border">
            <div>
              <div className="text-sm text-text-muted mb-1">Customer Type</div>
              <div className="font-semibold text-text">{customer.customer_type}</div>
            </div>
            <div>
              <div className="text-sm text-text-muted mb-1">Industry</div>
              <div className="font-semibold text-text">{customer.industry}</div>
            </div>
            <div>
              <div className="text-sm text-text-muted mb-1">Account Manager</div>
              <div className="font-semibold text-text">{customer.account_manager}</div>
            </div>
            <div>
              <div className="text-sm text-text-muted mb-1">Member Since</div>
              <div className="font-semibold text-text">
                {new Date(customer.signup_date).toLocaleDateString()}
              </div>
            </div>
          </div>
        </div>

        {/* Stats */}
        <div className="grid md:grid-cols-4 gap-6 mb-8">
          <div className="card">
            <div className="flex items-center justify-between mb-2">
              <ShoppingCart className="w-10 h-10 text-primary-500" />
              <span className="text-3xl font-bold text-text">{stats.totalOrders}</span>
            </div>
            <div className="text-sm text-text-muted">Total Orders</div>
          </div>
          <div className="card">
            <div className="flex items-center justify-between mb-2">
              <DollarSign className="w-10 h-10 text-green-500" />
              <span className="text-3xl font-bold text-text">${Math.round(stats.totalSpent).toLocaleString()}</span>
            </div>
            <div className="text-sm text-text-muted">Total Spent</div>
          </div>
          <div className="card">
            <div className="flex items-center justify-between mb-2">
              <TrendingUp className="w-10 h-10 text-blue-500" />
              <span className="text-3xl font-bold text-text">${Math.round(stats.avgOrderValue).toLocaleString()}</span>
            </div>
            <div className="text-sm text-text-muted">Avg Order Value</div>
          </div>
          <div className="card">
            <div className="flex items-center justify-between mb-2">
              <AlertCircle className="w-10 h-10 text-orange-500" />
              <span className="text-3xl font-bold text-text">{stats.openTickets}</span>
            </div>
            <div className="text-sm text-text-muted">Open Tickets</div>
          </div>
        </div>

        {/* Charts */}
        {ordersByMonth.length > 0 && (
          <div className="grid md:grid-cols-2 gap-6 mb-8">
            <div className="card">
              <h3 className="text-lg font-semibold text-text mb-4">Orders Over Time</h3>
              <ResponsiveContainer width="100%" height={200}>
                <LineChart data={ordersByMonth}>
                  <CartesianGrid strokeDasharray="3 3" stroke="oklch(0.35 0.03 195)" />
                  <XAxis dataKey="month" style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                  <YAxis style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                  <Tooltip contentStyle={{ backgroundColor: 'oklch(0.18 0.02 195)', border: '1px solid oklch(0.35 0.03 195)', color: 'oklch(0.98 0.005 195)' }} />
                  <Line type="monotone" dataKey="orders" stroke="oklch(0.62 0.12 195)" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </div>
            <div className="card">
              <h3 className="text-lg font-semibold text-text mb-4">Revenue Over Time</h3>
              <ResponsiveContainer width="100%" height={200}>
                <BarChart data={ordersByMonth}>
                  <CartesianGrid strokeDasharray="3 3" stroke="oklch(0.35 0.03 195)" />
                  <XAxis dataKey="month" style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                  <YAxis style={{ fontSize: '12px', fill: 'oklch(0.78 0.015 195)' }} />
                  <Tooltip contentStyle={{ backgroundColor: 'oklch(0.18 0.02 195)', border: '1px solid oklch(0.35 0.03 195)', color: 'oklch(0.98 0.005 195)' }} />
                  <Bar dataKey="revenue" fill="oklch(0.62 0.12 195)" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}

        {/* Orders */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-text mb-4">Recent Orders</h2>
          <div className="card overflow-hidden">
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-surface-elevated border-b border-border">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-text-muted uppercase tracking-wider">Order ID</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-text-muted uppercase tracking-wider">Date</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-text-muted uppercase tracking-wider">Status</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-text-muted uppercase tracking-wider">Payment</th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-text-muted uppercase tracking-wider">Amount</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-border">
                  {customerOrders.slice(0, 10).map((order) => (
                    <tr key={order.order_id} className="hover:bg-surface-elevated transition-colors">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-text">{order.order_id}</td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-text-muted">
                        {new Date(order.order_date).toLocaleDateString()}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusColor(order.order_status)}`}>
                          {order.order_status}
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusColor(order.payment_terms)}`}>
                          {order.payment_terms}
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-semibold text-text">
                        ${order.total.toLocaleString()}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        {/* Support Tickets */}
        <div>
          <h2 className="text-2xl font-bold text-text mb-4">Support Tickets</h2>
          <div className="space-y-4">
            {customerTickets.slice(0, 10).map((ticket) => (
                <div key={ticket.ticket_id} className="card-hover">
                  <div className="flex items-start justify-between mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h3 className="text-lg font-semibold text-text">{ticket.subject}</h3>
                        <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusColor(ticket.status)}`}>
                          {ticket.status}
                        </span>
                        <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusColor(ticket.priority)}`}>
                          {ticket.priority}
                        </span>
                      </div>
                      <p className="text-sm text-text-muted mb-2">Category: {ticket.category}</p>
                    </div>
                  </div>
                  <div className="flex items-center justify-between text-sm text-text-subtle pt-3 border-t border-border">
                    <div className="flex items-center gap-4">
                      <span>Ticket: {ticket.ticket_id}</span>
                      <span>Assigned to: {ticket.assigned_to}</span>
                    </div>
                    <div className="flex items-center gap-4">
                      <span>Created: {new Date(ticket.created_date).toLocaleDateString()}</span>
                      {ticket.satisfaction_rating && (
                        <span>Rating: {ticket.satisfaction_rating}/5 ⭐</span>
                      )}
                    </div>
                  </div>
                </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default CustomerPortal;

