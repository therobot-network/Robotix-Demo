export interface Product {
  sku: string;
  product_name: string;
  category: string;
  description: string;
  msrp: number;
  cost: number;
  margin: number;
  margin_pct: number;
  weight_kg: number;
  payload_capacity: string;
  reach_mm: string;
  color_options: string;
  configurations_available: string;
  inventory_on_hand: number;
  inventory_location: string;
  reorder_point: number;
  supplier: string;
  lead_time_days: number;
  status: string;
  release_date: string;
  warranty_years: number;
}

export interface Customer {
  customer_id: string;
  company_name: string;
  contact_first_name: string;
  contact_last_name: string;
  email: string;
  phone: string;
  address: string;
  city: string;
  state: string;
  zip_code: string;
  signup_date: string;
  customer_type: string;
  industry: string;
  account_manager: string;
  lifetime_value: number;
  total_orders: number;
  status: string;
}

export interface Order {
  order_id: string;
  customer_id: string;
  order_date: string;
  subtotal: number;
  discount: number;
  tax: number;
  shipping: number;
  total: number;
  payment_method: string;
  payment_terms: string;
  order_status: string;
  shipping_address: string;
  shipping_city: string;
  shipping_state: string;
  shipping_zip: string;
  sales_channel: string;
  sales_rep: string;
}

export interface OrderItem {
  order_item_id: string;
  order_id: string;
  product_sku: string;
  product_name: string;
  quantity: number;
  unit_price: number;
  line_total: number;
  discount_applied: number;
}

export interface SupportTicket {
  ticket_id: string;
  customer_id: string;
  customer_email: string;
  company_name: string;
  subject: string;
  priority: string;
  status: string;
  created_date: string;
  resolved_date: string | null;
  assigned_to: string;
  category: string;
  satisfaction_rating: number | null;
}

export interface Employee {
  employee_id: string;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  department: string;
  position: string;
  hire_date: string;
  salary: number;
  manager_id: string | null;
  status: string;
}

export interface DocumentMetadata {
  id: string;
  title: string;
  category: string;
  type: string;
  path: string;
  description?: string;
}

