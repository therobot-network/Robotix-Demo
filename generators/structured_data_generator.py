"""
Structured Data Generator
Creates CSV/JSON exports for enterprise datasets
AI-FIRST approach for Robotix robotics company
"""

import csv
import json
import random
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from company_data import *

# Load environment variables from .env file
load_dotenv()

# AI Integration
try:
    from langchain_anthropic import ChatAnthropic

    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    print("⚠️  LangChain not installed. Run: pip install langchain langchain-anthropic")


class StructuredDataGenerator:

    def __init__(self, output_dir="data", use_ai=True):
        self.output_dir = output_dir
        self.data = {}
        self.use_ai = use_ai and AI_AVAILABLE

        # Initialize AI model if available
        if self.use_ai:
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key:
                self.llm = ChatAnthropic(
                    model="claude-3-5-sonnet-20241022", temperature=0.7, max_tokens=2000
                )
                print("✅ AI content generation enabled (Claude 3.5 Sonnet)")
            else:
                self.use_ai = False
                print("⚠️  ANTHROPIC_API_KEY not found. Set it for AI generation.")

    def _get_timestamp(self):
        """Get formatted timestamp"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _print_progress_bar(self, current, total, label="Progress", width=40):
        """Print a progress bar"""
        percent = current / total
        filled = int(width * percent)
        bar = "█" * filled + "░" * (width - filled)
        print(
            f"   {label}: [{bar}] {int(percent * 100)}% ({current}/{total})", end="\r"
        )
        if current == total:
            print()  # New line when complete

    def generate_employee_data(self):
        """Generate detailed employee dataset"""
        employees = []

        for emp in EMPLOYEES:
            hire_date = get_random_date(2015, 2023)
            salary_ranges = {
                "Executive Leadership": (150000, 250000),
                "Human Resources": (60000, 95000),
                "Sales & Marketing": (55000, 120000),
                "Product Development": (75000, 130000),
                "Manufacturing": (45000, 75000),
                "Quality Assurance": (55000, 85000),
                "Customer Service": (40000, 65000),
                "Finance": (65000, 110000),
                "IT & Systems": (70000, 120000),
                "Legal & Compliance": (90000, 150000),
            }

            salary_range = salary_ranges.get(emp["dept"], (50000, 80000))
            salary = random.randint(salary_range[0], salary_range[1])

            employee_data = {
                "employee_id": f"EMP{random.randint(1000, 9999)}",
                "first_name": emp["name"].split()[0],
                "last_name": emp["name"].split()[-1],
                "full_name": emp["name"],
                "email": emp["email"],
                "title": emp["title"],
                "department": emp["dept"],
                "hire_date": hire_date.strftime("%Y-%m-%d"),
                "salary": salary,
                "location": random.choice([loc["city"] for loc in LOCATIONS]),
                "employment_type": random.choice(
                    ["Full-time", "Full-time", "Full-time", "Part-time"]
                ),
                "manager": random.choice(
                    [
                        e["name"]
                        for e in EMPLOYEES
                        if e["dept"] == emp["dept"]
                        and ("VP" in e["title"] or "Director" in e["title"])
                    ]
                    or ["Sarah Chen"]
                ),
                "performance_rating": random.choice([3, 4, 4, 5]),
                "years_of_service": (datetime.now() - hire_date).days // 365,
                "status": "Active",
            }
            employees.append(employee_data)

        self.data["employees"] = employees
        return employees

    def _generate_product_description(self, product_name, category):
        """Generate realistic product description using AI"""
        if not self.use_ai:
            return f"Professional-grade {product_name.lower()} designed for industrial automation"

        try:
            prompt = f"""Generate a compelling 2-3 sentence product description for:
Product: {product_name}
Category: {category}
Company: Robotix (premium robotics manufacturer)

Make it technical yet appealing, mentioning key features and target applications. Be specific and realistic for industrial/collaborative robotics."""

            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            return f"Professional-grade {product_name.lower()} designed for industrial automation"

    def generate_product_data(self):
        """Generate product catalog with SKUs, pricing, inventory"""
        products = []
        sku_counter = 1000

        # Calculate total products
        total_products = sum(len(products) for products in PRODUCT_CATEGORIES.values())
        current_product = 0

        print(
            f"   [{self._get_timestamp()}] Generating product descriptions..."
            + (" (AI-enhanced)" if self.use_ai else "")
        )

        for category, product_list in PRODUCT_CATEGORIES.items():
            for product_name in product_list:
                current_product += 1
                # Pricing by category
                price_ranges = {
                    "Industrial Robots": (25000, 50000),
                    "Collaborative Robots": (20000, 35000),
                    "Mobile Robots": (15000, 30000),
                    "Components": (500, 5000),
                    "Software": (500, 2000),
                }

                price_range = price_ranges.get(category, (1000, 5000))
                if category == "Software":
                    msrp = random.randint(price_range[0], price_range[1])
                    cost = int(msrp * 0.3)  # Higher margin for software
                else:
                    msrp = random.randint(price_range[0], price_range[1])
                    cost = int(msrp * 0.6)  # 40% margin for hardware

                # Generate AI-enhanced description
                self._print_progress_bar(
                    current_product - 0.5, total_products, "Product Catalog"
                )
                description = self._generate_product_description(product_name, category)

                # Weight based on category
                if "Industrial" in category or "Collaborative" in category:
                    weight = random.uniform(20, 150)  # kg for robots
                elif "Mobile" in category:
                    weight = random.uniform(50, 300)  # kg for mobile platforms
                elif "Components" in category:
                    weight = random.uniform(0.5, 10)  # kg for components
                else:
                    weight = 0  # software

                product = {
                    "sku": f"RBX-{category[:3].upper()}-{sku_counter}",
                    "product_name": product_name,
                    "category": category,
                    "description": description,
                    "msrp": msrp,
                    "cost": cost,
                    "margin": msrp - cost,
                    "margin_pct": round((msrp - cost) / msrp * 100, 1),
                    "weight_kg": round(weight, 2) if weight > 0 else "N/A",
                    "payload_capacity": (
                        f"{random.randint(5, 100)} kg"
                        if "Robot" in category and "Mobile" not in category
                        else "N/A"
                    ),
                    "reach_mm": (
                        f"{random.randint(600, 2000)} mm"
                        if "Industrial" in category or "Collaborative" in category
                        else "N/A"
                    ),
                    "color_options": (
                        "Industrial Gray/Safety Yellow"
                        if "Robot" in category
                        else "N/A"
                    ),
                    "configurations_available": random.choice(
                        [
                            "Standard/Extended Reach",
                            "Standard/Heavy Duty",
                            "Single/Dual Arm",
                            "Standard Only",
                        ]
                    ),
                    "inventory_on_hand": (
                        random.randint(5, 50) if category != "Software" else "Digital"
                    ),
                    "inventory_location": (
                        random.choice(
                            [
                                loc["city"]
                                for loc in LOCATIONS
                                if loc["type"]
                                in ["Distribution Center", "Manufacturing"]
                            ]
                        )
                        if category != "Software"
                        else "N/A"
                    ),
                    "reorder_point": 10 if category != "Software" else "N/A",
                    "supplier": random.choice(
                        [
                            "Robotix Manufacturing",
                            "Global Automation Components",
                            "Servo Systems Inc",
                            "Vision Tech Ltd",
                        ]
                    ),
                    "lead_time_days": (
                        random.randint(30, 90)
                        if "Robot" in category
                        else random.randint(14, 45)
                    ),
                    "status": "Active",
                    "release_date": get_random_date(2020, 2024).strftime("%Y-%m-%d"),
                    "warranty_years": 2 if "Robot" in category else 1,
                }
                products.append(product)
                sku_counter += 1
                self._print_progress_bar(
                    current_product, total_products, "Product Catalog"
                )

        print()  # New line after progress bar
        self.data["products"] = products
        return products

    def generate_customer_data(self, num_customers=500):
        """Generate synthetic customer dataset"""
        customers = []

        # Company names for B2B customers
        company_prefixes = [
            "Advanced",
            "Precision",
            "Global",
            "Industrial",
            "Smart",
            "Auto",
            "Tech",
            "Innovative",
            "Quality",
            "Elite",
        ]
        company_types = [
            "Manufacturing",
            "Automation",
            "Systems",
            "Industries",
            "Solutions",
            "Technologies",
            "Robotics",
            "Assembly",
        ]

        first_names = [
            "James",
            "Mary",
            "John",
            "Patricia",
            "Robert",
            "Jennifer",
            "Michael",
            "Linda",
            "William",
            "Barbara",
            "David",
            "Elizabeth",
            "Richard",
            "Susan",
            "Joseph",
            "Jessica",
        ]

        last_names = [
            "Smith",
            "Johnson",
            "Williams",
            "Brown",
            "Jones",
            "Garcia",
            "Miller",
            "Davis",
            "Rodriguez",
            "Martinez",
            "Hernandez",
            "Lopez",
            "Wilson",
            "Anderson",
            "Thomas",
            "Taylor",
        ]

        for i in range(num_customers):
            # 70% B2B, 30% individual
            is_business = random.random() < 0.7

            if is_business:
                company_name = (
                    f"{random.choice(company_prefixes)} {random.choice(company_types)}"
                )
                first = random.choice(first_names)
                last = random.choice(last_names)
                email = f"{first.lower()}.{last.lower()}@{company_name.lower().replace(' ', '')}.com"
            else:
                company_name = "Individual"
                first = random.choice(first_names)
                last = random.choice(last_names)
                email = (
                    f"{first.lower()}.{last.lower()}{random.randint(1, 999)}@email.com"
                )

            signup_date = get_random_date(2020, 2024)

            customer = {
                "customer_id": f"CUST{10000 + i}",
                "company_name": company_name,
                "contact_first_name": first,
                "contact_last_name": last,
                "email": email,
                "phone": f"({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}",
                "address": f"{random.randint(100, 9999)} {random.choice(['Industrial', 'Tech', 'Commerce', 'Business', 'Manufacturing'])} {random.choice(['Blvd', 'Dr', 'Way', 'Parkway'])}",
                "city": random.choice(
                    [
                        "Seattle",
                        "Portland",
                        "Denver",
                        "Austin",
                        "Minneapolis",
                        "Boston",
                        "Detroit",
                        "Chicago",
                    ]
                ),
                "state": random.choice(
                    ["WA", "OR", "CO", "TX", "MN", "MA", "MI", "IL"]
                ),
                "zip_code": f"{random.randint(10000, 99999)}",
                "signup_date": signup_date.strftime("%Y-%m-%d"),
                "customer_type": random.choice(
                    [
                        "Manufacturing",
                        "Warehouse/Logistics",
                        "Research",
                        "System Integrator",
                        "Individual",
                    ]
                ),
                "industry": (
                    random.choice(
                        [
                            "Automotive",
                            "Electronics",
                            "Food & Beverage",
                            "Pharmaceuticals",
                            "Aerospace",
                            "General Manufacturing",
                        ]
                    )
                    if is_business
                    else "N/A"
                ),
                "account_manager": random.choice(
                    [e["name"] for e in EMPLOYEES if e["dept"] == "Sales & Marketing"]
                ),
                "lifetime_value": (
                    random.randint(10000, 500000)
                    if is_business
                    else random.randint(5000, 50000)
                ),
                "total_orders": (
                    random.randint(1, 15) if is_business else random.randint(1, 5)
                ),
                "status": "Active",
            }
            customers.append(customer)

        self.data["customers"] = customers
        return customers

    def generate_sales_data(self, num_orders=1000):
        """Generate sales order transactions"""
        if "customers" not in self.data:
            self.generate_customer_data()
        if "products" not in self.data:
            self.generate_product_data()

        orders = []
        order_items = []

        for i in range(num_orders):
            customer = random.choice(self.data["customers"])
            order_date = get_random_date(2023, 2024)

            # Generate order
            order_id = f"ORD{100000 + i}"

            # B2B orders tend to be larger
            is_large_order = (
                customer["customer_type"] != "Individual" and random.random() < 0.6
            )
            num_items = random.randint(2, 8) if is_large_order else random.randint(1, 3)

            order_total = 0

            # Generate order items
            selected_products = random.sample(
                self.data["products"], min(num_items, len(self.data["products"]))
            )
            for product in selected_products:
                quantity = (
                    random.randint(1, 5)
                    if product["category"] in ["Components", "Software"]
                    else 1
                )
                unit_price = product["msrp"]
                line_total = unit_price * quantity
                order_total += line_total

                order_item = {
                    "order_item_id": f"ITEM{100000 + len(order_items)}",
                    "order_id": order_id,
                    "product_sku": product["sku"],
                    "product_name": product["product_name"],
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "line_total": line_total,
                    "discount_applied": 0,
                }
                order_items.append(order_item)

            # Volume discounts for large orders
            discount = 0
            if order_total > 50000:
                discount = int(
                    order_total * random.choice([0.05, 0.10])
                )  # 5-10% volume discount
            elif order_total > 100000:
                discount = int(
                    order_total * random.choice([0.10, 0.15])
                )  # 10-15% volume discount

            # Shipping free for orders over $10k, otherwise based on weight
            if order_total > 10000:
                shipping = 0
            else:
                shipping = random.randint(50, 500)  # freight shipping

            tax = round(order_total * 0.08, 2)

            order = {
                "order_id": order_id,
                "customer_id": customer["customer_id"],
                "order_date": order_date.strftime("%Y-%m-%d"),
                "subtotal": order_total,
                "discount": discount,
                "tax": tax,
                "shipping": shipping,
                "total": order_total - discount + tax + shipping,
                "payment_method": random.choice(
                    [
                        "Purchase Order",
                        "Purchase Order",
                        "Credit Card",
                        "Wire Transfer",
                        "Financing",
                    ]
                ),
                "payment_terms": (
                    random.choice(
                        ["Net 30", "Net 60", "Prepaid", "50/50", "Financing 24mo"]
                    )
                    if customer["customer_type"] != "Individual"
                    else "Prepaid"
                ),
                "order_status": random.choice(
                    [
                        "Completed",
                        "Completed",
                        "Completed",
                        "Shipped",
                        "In Production",
                        "Cancelled",
                    ]
                ),
                "shipping_address": customer["address"],
                "shipping_city": customer["city"],
                "shipping_state": customer["state"],
                "shipping_zip": customer["zip_code"],
                "sales_channel": random.choice(
                    ["Direct Sales", "Direct Sales", "Partner", "Online", "Phone"]
                ),
                "sales_rep": random.choice(
                    [e["name"] for e in EMPLOYEES if e["dept"] == "Sales & Marketing"]
                ),
            }
            orders.append(order)

        self.data["orders"] = orders
        self.data["order_items"] = order_items
        return orders, order_items

    def generate_support_tickets(self, num_tickets=200):
        """Generate customer support ticket data"""
        if "customers" not in self.data:
            self.generate_customer_data()

        tickets = []

        ticket_subjects = [
            "Robot not responding to commands",
            "Installation and setup assistance",
            "Software integration question",
            "Maintenance and calibration request",
            "Warranty claim - mechanical issue",
            "Programming support needed",
            "Technical specifications question",
            "Sensor calibration issue",
            "Safety system troubleshooting",
            "Replacement parts inquiry",
            "Training and documentation request",
            "Network connectivity issue",
            "Performance optimization question",
        ]

        priorities = ["Low", "Medium", "Medium", "High", "Critical"]
        statuses = ["Open", "In Progress", "Resolved", "Resolved", "Resolved", "Closed"]

        for i in range(num_tickets):
            customer = random.choice(self.data["customers"])
            created_date = get_random_date(2023, 2024)

            status = random.choice(statuses)
            resolved_date = None
            if status in ["Resolved", "Closed"]:
                resolved_date = (
                    created_date + timedelta(days=random.randint(1, 14))
                ).strftime("%Y-%m-%d")

            ticket = {
                "ticket_id": f"TICK{10000 + i}",
                "customer_id": customer["customer_id"],
                "customer_email": customer["email"],
                "company_name": customer["company_name"],
                "subject": random.choice(ticket_subjects),
                "priority": random.choice(priorities),
                "status": status,
                "created_date": created_date.strftime("%Y-%m-%d"),
                "resolved_date": resolved_date,
                "assigned_to": random.choice(
                    [e["name"] for e in EMPLOYEES if e["dept"] == "Customer Service"]
                ),
                "category": random.choice(
                    [
                        "Technical Support",
                        "Installation",
                        "Programming",
                        "Maintenance",
                        "Warranty",
                        "Training",
                    ]
                ),
                "satisfaction_rating": (
                    random.choice([None, None, 3, 4, 4, 5])
                    if status in ["Resolved", "Closed"]
                    else None
                ),
            }
            tickets.append(ticket)

        self.data["support_tickets"] = tickets
        return tickets

    def export_csv(self, dataset_name, data, filename):
        """Export data to CSV"""
        if not data:
            return

        os.makedirs(self.output_dir, exist_ok=True)
        filepath = f"{self.output_dir}/{filename}"

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(
            f"  ✓ [{self._get_timestamp()}] Exported {len(data)} records to {filename}"
        )

    def export_json(self, dataset_name, data, filename):
        """Export data to JSON"""
        if not data:
            return

        os.makedirs(self.output_dir, exist_ok=True)
        filepath = f"{self.output_dir}/{filename}"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print(
            f"  ✓ [{self._get_timestamp()}] Exported {len(data)} records to {filename}"
        )

    def export_all(self):
        """Export all datasets to CSV and JSON"""
        print("\nExporting structured data...")

        for dataset_name, dataset in self.data.items():
            self.export_csv(dataset_name, dataset, f"{dataset_name}.csv")
            self.export_json(dataset_name, dataset, f"{dataset_name}.json")

        # Create summary metadata
        metadata = {
            "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "company": COMPANY,
            "datasets": {
                name: {
                    "record_count": len(data),
                    "fields": list(data[0].keys()) if data else [],
                }
                for name, data in self.data.items()
            },
        }

        with open(f"{self.output_dir}/metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        print(f"  ✓ Exported metadata.json")
        print(f"\n✅ All structured data exported to: {self.output_dir}/")
