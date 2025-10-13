"""
Document Generator
Creates synthetic HR, Product, and Legal documents
AI-FIRST approach - generates all content using Claude for Robotix (robotics company)
"""

import random
import os
from datetime import datetime
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
    print("⚠️  LangChain not installed for document generation.")

class DocumentGenerator:
    
    def __init__(self, use_ai=True):
        self.generated_docs = []
        self.use_ai = use_ai and AI_AVAILABLE
        
        # Initialize AI model if available
        if self.use_ai:
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key:
                self.llm = ChatAnthropic(
                    model="claude-3-5-sonnet-20241022",
                    temperature=0.7,
                    max_tokens=8000
                )
                print("✅ AI content generation enabled for HTML documents (Claude 3.5 Sonnet)")
            else:
                self.use_ai = False
                print("⚠️  ANTHROPIC_API_KEY not found for document generation.")
    
    def _generate_ai_document(self, doc_type, context):
        """Generate document using AI with structured context"""
        if not self.use_ai:
            return f"<p>AI generation not available. {doc_type} content would go here.</p>"
        
        try:
            prompt = f"""Generate a comprehensive, realistic {doc_type} document for Robotix.

Company Context:
{context}

Requirements:
- Professional business tone appropriate for {doc_type}
- Realistic, specific details, metrics, and technical specifications
- Well-structured with clear sections using HTML tags (h2, h3, p, ul, li, strong, em, table)
- 800-1500 words for policy documents, 600-1000 for product/technical docs
- Include concrete examples and actionable information
- Use proper HTML formatting (but NO <h1> tag - that's added separately)
- Make it feel authentic and comprehensive for a robotics company

Generate ONLY the HTML content body (no document headers, no <html> or <body> tags)."""

            response = self.llm.invoke(prompt)
            content = response.content.strip()
            
            # Ensure no h1 tags in content
            content = content.replace('<h1>', '<h2>').replace('</h1>', '</h2>')
            
            return content
        except Exception as e:
            print(f"   ⚠️  AI generation failed for {doc_type}: {str(e)}")
            return f"<p>Content generation failed. {doc_type} content would go here.</p>"
    
    # ===== HR DOCUMENTS =====
    
    def generate_employee_handbook(self):
        """Generate comprehensive employee handbook using AI"""
        author = get_employees_by_dept("Human Resources")[0]
        
        context = f"""
Company: {COMPANY['name']} - {COMPANY['tagline']}
Industry: {COMPANY['industry']} (robotics manufacturing and sales)
Founded: {COMPANY['founded']}
Headquarters: {COMPANY['headquarters']}
Employees: {COMPANY['employees']}
Revenue: {COMPANY['revenue']}

Document Type: Employee Handbook 2024
Author: {author['name']}, {author['title']}
Effective Date: January 1, 2024

Generate a comprehensive employee handbook covering:
- Welcome message and company mission/values (innovation, quality, sustainability)
- Employment basics (work schedule, attendance, dress code, manufacturing safety)
- Compensation and benefits overview (401k with 4% match, insurance, PTO)
- Time off policies (15 days PTO, 10 sick days, 8 holidays)
- Workplace conduct and expectations
- Performance reviews and professional development ($1,000 annual budget)
- Safety policies (critical for robot manufacturing)
- Remote work eligibility (office staff only, not manufacturing)
- Employee discount (40% off Robotix products)
- Contact information for HR

Include specific, realistic details for a robotics company.
"""
        
        content = self._generate_ai_document("Employee Handbook", context)
        
        doc = {
            "title": "Employee Handbook 2024",
            "category": "HR",
            "type": "Policy",
            "date": "January 1, 2024",
            "author": author["name"],
            "content": f"<h1>Robotix Employee Handbook</h1>\n<p><em>Effective Date: January 1, 2024</em></p>\n\n{content}"
        }
        self.generated_docs.append(doc)
        return doc
    
    def generate_remote_work_policy(self):
        """Generate remote work policy using AI"""
        author = get_employees_by_dept("Human Resources")[0]
        
        context = f"""
Company: {COMPANY['name']} - Robotics manufacturer
Author: {author['name']}, {author['title']}
Document Type: Remote Work Policy
Effective Date: March 15, 2024

Generate a comprehensive remote work policy covering:
- Purpose and eligibility (90-day probation complete, manager approval)
- Remote work options (hybrid up to 3 days/week, full remote case-by-case)
- Requirements (home office setup, reliable internet 25+ Mbps, VPN)
- Technology and security requirements
- Availability expectations (core hours 10 AM - 3 PM Pacific, 2-hour response time)
- Equipment and expenses ($500 home office stipend, $50/month internet reimbursement)
- Communication expectations (cameras on for meetings, weekly check-ins)
- Performance standards
- In-office requirements for key events
- Policy violations and enforcement
- Department exceptions (Manufacturing/Warehouse require on-site presence)
- Application process

Note: Manufacturing and hardware roles require on-site presence due to equipment.
"""
        
        content = self._generate_ai_document("Remote Work Policy", context)
        
        doc = {
            "title": "Remote Work Policy",
            "category": "HR",
            "type": "Policy",
            "date": "March 15, 2024",
            "author": author["name"],
            "content": f"<h1>Remote Work Policy</h1>\n<p><em>Last Updated: March 15, 2024</em></p>\n<p><em>Policy Owner: {author['name']}, {author['title']}</em></p>\n\n{content}"
        }
        self.generated_docs.append(doc)
        return doc
    
    def generate_benefits_overview(self):
        """Generate benefits overview using AI"""
        author = get_employees_by_dept("Human Resources")[1]
        
        context = f"""
Company: {COMPANY['name']} - Robotics company
Document Type: Employee Benefits Overview 2024
Effective Date: January 1, 2024

Generate comprehensive benefits overview covering:

Health & Wellness:
- Medical insurance (3 plan options, company pays 80% employee premium)
- Dental insurance (Delta Dental, preventive care 100%)
- Vision insurance (company pays 100% employee premium)
- Wellness programs (on-site fitness, $50/month gym reimbursement)
- Mental health resources and EAP

Financial Benefits:
- 401(k) retirement (immediate eligibility, 4% company match, 3-year vesting)
- Life insurance (1x salary company-paid, up to 5x available)
- Disability insurance (short-term and long-term company-paid)

Time Off:
- PTO (15-25 days based on tenure, accrues each pay period, 40 hours rollover)
- Sick leave (10 days per year, non-rollover)
- Paid holidays (8 company holidays + 1 floating)
- Parental leave (12 weeks primary caregiver, 4 weeks secondary, $5k adoption assistance)

Professional Development:
- Education assistance ($5,000 annually for job-related courses)
- Professional development ($1,000 annual budget for conferences/certifications)
- LinkedIn Learning access

Work-Life Benefits:
- Employee product discount (40% off all Robotix products, 25% friends/family events)
- Commuter benefits (pre-tax transit, $20/month bike-to-work, free parking, EV charging)
- Flexible work arrangements (hybrid work up to 3 days remote)
- EAP (24/7 confidential counseling, financial/legal consultation)

Additional Perks:
- Company events (summer picnic, holiday party)
- Anniversary recognition
- Volunteer time off (16 hours per year)
- Casual dress code
- Free coffee and snacks

Enrollment periods and contact information.
"""
        
        content = self._generate_ai_document("Benefits Overview", context)
        
        doc = {
            "title": "Benefits Overview 2024",
            "category": "HR",
            "type": "Benefits",
            "date": "January 1, 2024",
            "author": author["name"],
            "content": f"<h1>Employee Benefits Overview 2024</h1>\n<p><em>Your Complete Guide to Robotix Benefits</em></p>\n\n{content}"
        }
        self.generated_docs.append(doc)
        return doc
    
    # ===== PRODUCT DOCUMENTS =====
    
    def generate_product_spec(self, product_name, category):
        """Generate product specification using AI"""
        pm = random.choice([e for e in EMPLOYEES if "Product Manager" in e["title"]])
        engineer = get_employees_by_dept("Product Development")[-1]
        
        context = f"""
Company: {COMPANY['name']} - Leading robotics manufacturer
Product: {product_name}
Category: {category}
Document Type: Technical Specification
Author: {pm['name']}, {pm['title']}
Technical Review: {engineer['name']}, {engineer['title']}
Date: {format_date(get_random_date(2024, 2024))}

Generate a comprehensive technical specification document covering:

Product Overview:
- Purpose and target applications
- Key innovations and differentiators
- Target customers/industries

Technical Specifications:
- Chassis/Frame (materials, construction, weight capacity)
- Actuators/Motors (type, specifications, precision)
- Control System (controller type, programming interfaces, connectivity)
- Sensors (vision systems, force sensing, positioning)
- Reach/Workspace dimensions
- Payload capacity
- Power requirements
- Operating environment specifications
- Sizes/configurations available
- Color/finish options

Performance Metrics:
- Speed and acceleration
- Repeatability and accuracy
- Cycle time
- Duty cycle
- Safety ratings

Manufacturing Details:
- Production location (Minneapolis Manufacturing Facility)
- Quality standards (ISO 9001:2015)
- Testing protocols (safety compliance, endurance testing)

Warranty & Support:
- Warranty terms (frame/chassis: lifetime limited, components: 2 years)
- Technical support availability
- Maintenance requirements

Pricing & SKU:
- MSRP: Generate realistic price based on category
  * Industrial Robots: $25,000-$50,000
  * Collaborative Robots: $20,000-$35,000
  * Mobile Robots: $15,000-$30,000
  * Components: $500-$5,000
  * Software: $500-$2,000/year
- SKU format: RBX-XXX-#### (category prefix and 4-digit number)

Packaging:
- Shipping dimensions and weight
- Assembly requirements
- Included accessories

Include realistic technical specifications for a {category} robot.
"""
        
        content = self._generate_ai_document(f"Technical Specification for {product_name}", context)
        
        doc = {
            "title": f"{product_name} - Technical Specification",
            "category": "Product",
            "type": "Technical Spec",
            "date": format_date(get_random_date(2024, 2024)),
            "author": pm["name"],
            "content": f"<h1>{product_name}</h1>\n<h2>Technical Specification Document</h2>\n<p><em>Product Category: {category}</em></p>\n<p><em>Document Owner: {pm['name']}, {pm['title']}</em></p>\n<p><em>Technical Review: {engineer['name']}, {engineer['title']}</em></p>\n\n{content}"
        }
        self.generated_docs.append(doc)
        return doc
    
    def generate_product_user_guide(self, product_name):
        """Generate product user guide using AI"""
        
        context = f"""
Company: {COMPANY['name']} - Robotics manufacturer
Product: {product_name}
Document Type: User Guide & Setup Instructions
Audience: End users, system integrators, maintenance technicians

Generate a comprehensive user guide covering:

Introduction:
- Congratulations message
- Safety warnings (robotic systems carry inherent risks)
- Regulatory compliance notices (ISO, OSHA, CE marking)

What's In The Box:
- Main robot unit components
- Controller/computer
- Cables and connectors
- Power supply
- Safety equipment
- Documentation and warranty card
- Mounting hardware
- Setup tools

Tools Required:
- Torque wrench
- Allen keys/hex keys
- Multimeter
- Safety equipment
- Cable management tools

Installation Instructions:
Step 1: Unpack and inspect
Step 2: Mounting/base installation
Step 3: Electrical connections (power, emergency stop, safety circuits)
Step 4: Controller setup
Step 5: Software installation and configuration
Step 6: Network connectivity setup
Step 7: Calibration procedures

Pre-Operation Safety Check:
- Emergency stop functionality
- Safety circuit verification
- Work envelope clearance
- Sensor calibration
- Power supply checks

Programming & Operation:
- Basic programming interface overview
- Teaching/programming modes
- Running programs
- Monitoring operation
- Error codes and troubleshooting

Regular Maintenance Schedule:
- Daily checks
- Weekly maintenance
- Monthly inspections
- Annual servicing
- Lubrication points
- Parts replacement intervals

Basic Maintenance:
- Cleaning procedures
- Lubrication
- Cable inspection
- Sensor cleaning
- Backup procedures

Troubleshooting Common Issues:
- Won't power on
- Communication errors
- Position errors
- Safety system activated
- Performance issues

Technical Specifications Table:
- Operating parameters
- Maintenance torque specs
- Electrical specifications
- Environmental requirements

Warranty Information:
- Coverage details (lifetime chassis, 2-year components)
- What's not covered
- Claim process

Need Help:
- Customer service contact (1-800-555-ROBO)
- Technical support email
- Website resources
- Registration link

Include safety warnings and realistic technical details for a robotics system.
"""
        
        content = self._generate_ai_document(f"User Guide for {product_name}", context)
        
        doc = {
            "title": f"{product_name} - User Guide",
            "category": "Product",
            "type": "User Guide",
            "date": format_date(get_random_date(2024, 2024)),
            "author": "Product Documentation Team",
            "content": f"<h1>{product_name}</h1>\n<h2>User Guide & Setup Instructions</h2>\n\n{content}"
        }
        self.generated_docs.append(doc)
        return doc
    
    # ===== LEGAL DOCUMENTS =====
    
    def generate_privacy_policy(self):
        """Generate privacy policy using AI"""
        legal_counsel = get_employees_by_dept("Legal & Compliance")[0]
        
        context = f"""
Company: {COMPANY['name']} - Robotics manufacturer and retailer
Location: {COMPANY['headquarters']}
Document Type: Privacy Policy
Effective Date: January 1, 2024
Contact: {legal_counsel['name']}, {legal_counsel['email']}

Generate a comprehensive privacy policy covering:

Introduction:
- Company commitment to privacy
- Scope (website, mobile app, products, services)
- Agreement to terms

Information We Collect:
- Personal information (name, contact, payment, purchase history)
- Automatically collected (IP, device info, cookies, location)
- From third parties (social media, payment processors, partners)
- Robot telemetry data (usage patterns, performance metrics)

How We Use Your Information:
- Service delivery (orders, account management, support)
- Business operations (analytics, fraud prevention, compliance)
- Marketing and communications (newsletters, promotions)
- Product improvement (telemetry analysis, R&D)

Information Sharing:
- Service providers (payment, shipping, email, analytics)
- Business transfers (mergers, acquisitions)
- Legal requirements (compliance, law enforcement)
- With consent

Cookies and Tracking:
- Types of cookies (essential, performance, functional, marketing)
- Browser controls

Data Security:
- SSL/TLS encryption
- Secure storage
- Access controls
- Employee training
- Incident response

Privacy Rights:
- Access and portability
- Correction and deletion
- Objection and restriction
- Opt-out of marketing
- Contact information for requests

California Privacy Rights (CCPA):
- Right to know
- Right to delete
- Right to opt-out of sale (we don't sell data)
- Non-discrimination

Children's Privacy:
- Not directed to children under 13
- Parent contact information

Third-Party Links:
- No responsibility for external sites

International Data Transfers:
- Cross-border processing
- EEA safeguards (Standard Contractual Clauses)

Data Retention:
- Account info: 7 years after closure
- Purchase records: 7 years
- Marketing data: Until opt-out or 3 years inactivity
- Analytics: 26 months
- Robot telemetry: 2 years

Updates to Policy:
- Notification procedures
- Continued use = acceptance

Contact Information:
- Privacy officer contact
- Phone: 1-800-555-ROBO
- Email: privacy@robotix.com

Include realistic legal language for a robotics company with e-commerce and IoT devices.
"""
        
        content = self._generate_ai_document("Privacy Policy", context)
        
        doc = {
            "title": "Privacy Policy",
            "category": "Legal",
            "type": "Policy",
            "date": "January 1, 2024",
            "author": legal_counsel["name"],
            "content": f"<h1>Privacy Policy</h1>\n<p><em>Effective Date: January 1, 2024</em></p>\n<p><em>Last Updated: January 1, 2024</em></p>\n\n{content}"
        }
        self.generated_docs.append(doc)
        return doc
    
    def generate_warranty_policy(self):
        """Generate warranty and return policy using AI"""
        
        context = f"""
Company: {COMPANY['name']} - Robotics manufacturer
Location: {COMPANY['headquarters']}
Document Type: Warranty and Return Policy
Effective Date: January 1, 2024

Generate a comprehensive warranty and return policy covering:

Limited Warranty Coverage:
- Company warranty statement
- Original purchaser only, non-transferable

Warranty Terms by Product Category:
- Robot Chassis/Frames: Lifetime limited warranty
- Electronic Components: 2-year limited warranty
- Software: 1-year limited warranty
- Accessories: 1-year limited warranty
- Wear items excluded (cables, sensors subject to wear, consumables)

What is NOT Covered:
- Normal wear and tear
- Damage from misuse, accidents, or improper installation
- Lack of maintenance
- Unauthorized modifications
- Environmental damage
- Commercial misuse beyond specifications
- Theft or vandalism
- Consequential damages

Warranty Claims Process:
Step 1: Contact customer service (warranty@robotix.com, 1-800-555-ROBO)
Step 2: Provide required information (proof of purchase, serial number, description, photos)
Step 3: Evaluation (3-5 business days review)
Step 4: Resolution (repair, replacement, or credit)
- Processing time: 10-15 business days
- We cover shipping for warranty replacements

Equipment Replacement Program:
- If robot chassis damaged in first year: 50% discount on replacement
- One-time per customer
- Must provide incident documentation
- Original equipment must be returned
- $199 processing fee

Return Policy:
30-Day Satisfaction Guarantee:
- Return most items within 30 days for full refund
- Must be unused, original condition, original packaging

Return Eligibility:
Eligible:
- Unused items with tags
- Original packaging
- Within 30 days
- Proof of purchase

NOT Eligible:
- Used/operated equipment
- Custom or configured systems
- Clearance/final sale items
- Software licenses (opened)
- Items without packaging

How to Return:
Step 1: Initiate return (online account or call support)
Step 2: Pack securely (original packaging, all accessories)
Step 3: Ship (use provided label, insurance recommended)

Return Shipping Costs:
- Free return shipping: defective, wrong item, quality issues
- Customer pays: change of mind, wrong size/model ordered
- Shipping cost deducted from refund unless defective

Refunds:
- Processed within 5-7 business days of receiving return
- Refunded to original payment method
- 5-10 business days to appear
- Shipping non-refundable unless our error
- Damaged returns may receive partial refund

Exchanges:
- Processed as return + new order
- Free exchange shipping for defects within 30 days
- Subject to availability

Robots & Large Equipment:
- Must be uninstalled and in original packaging
- Equipment that has been installed or operated not eligible
- Test run policy: Initial setup and 1-hour test period allowed
- Return shipping: Customer responsible unless defective (freight costs may apply)
- Restocking fee: 15% for opened/installed equipment

International Orders:
- 30-day policy applies
- Customer responsible for return shipping and customs
- Refund excludes international shipping and duties

Disclaimer of Warranties:
- Except as expressly provided, no other warranties implied
- State-specific limitations may apply

Limitation of Liability:
- Liability limited to repair, replacement, or refund
- Not liable for consequential, incidental, special damages
- Includes injury, property damage, lost production, lost profits

Legal Rights:
- This warranty provides specific legal rights
- Additional rights may vary by state/jurisdiction

Contact Information:
- Warranty Claims: warranty@robotix.com, 1-800-555-ROBO option 2
- Returns: returns@robotix.com, 1-800-555-ROBO option 3
- Return Portal: robotix.com/returns
- Mailing address: {COMPANY['headquarters']}

Include realistic legal language for industrial robotics equipment.
"""
        
        content = self._generate_ai_document("Warranty and Return Policy", context)
        
        doc = {
            "title": "Warranty and Return Policy",
            "category": "Legal",
            "type": "Policy",
            "date": "January 1, 2024",
            "author": "Legal Department",
            "content": f"<h1>Warranty and Return Policy</h1>\n<p><em>Effective Date: January 1, 2024</em></p>\n\n{content}"
        }
        self.generated_docs.append(doc)
        return doc

    def get_all_documents(self):
        """Return all generated documents"""
        return self.generated_docs
