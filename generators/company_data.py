"""
Company Data Structures and Synthetic Data Generator
Defines the fictional company universe based on Robotix
"""

import random
from datetime import datetime, timedelta
from typing import List, Dict

# Company Profile
COMPANY = {
    "name": "Robotix",
    "tagline": "Automate Your Future",
    "industry": "Robotics & Automation",
    "founded": 1998,
    "headquarters": "Bothell, Washington",
    "employees": 290,
    "revenue": "$42M (2024)",
    "description": "Leading manufacturer and integrator of industrial robots, collaborative robots, and automation solutions."
}

# Departments
DEPARTMENTS = [
    "Executive Leadership",
    "Human Resources",
    "Sales & Marketing",
    "Product Development",
    "Manufacturing",
    "Quality Assurance",
    "Customer Service",
    "Finance",
    "IT & Systems",
    "Legal & Compliance"
]

# Locations
LOCATIONS = [
    {"city": "Bothell", "state": "WA", "type": "Headquarters"},
    {"city": "Seattle", "state": "WA", "type": "Solutions Center"},
    {"city": "Portland", "state": "OR", "type": "Distribution Center"},
    {"city": "Denver", "state": "CO", "type": "Regional Office"},
    {"city": "Austin", "state": "TX", "type": "R&D Center"},
    {"city": "Minneapolis", "state": "MN", "type": "Manufacturing"},
]

# Employee Names (synthetic)
EMPLOYEES = [
    {"name": "Sarah Chen", "title": "Chief Executive Officer", "dept": "Executive Leadership", "email": "sarah.chen@robotix.com"},
    {"name": "Michael Rodriguez", "title": "Chief Financial Officer", "dept": "Executive Leadership", "email": "michael.rodriguez@robotix.com"},
    {"name": "Jennifer Park", "title": "VP of Human Resources", "dept": "Human Resources", "email": "jennifer.park@robotix.com"},
    {"name": "David Martinez", "title": "VP of Sales", "dept": "Sales & Marketing", "email": "david.martinez@robotix.com"},
    {"name": "Emily Thompson", "title": "VP of Product Development", "dept": "Product Development", "email": "emily.thompson@robotix.com"},
    {"name": "James Wilson", "title": "Director of Manufacturing", "dept": "Manufacturing", "email": "james.wilson@robotix.com"},
    {"name": "Lisa Anderson", "title": "Director of Quality Assurance", "dept": "Quality Assurance", "email": "lisa.anderson@robotix.com"},
    {"name": "Robert Kim", "title": "Director of Customer Service", "dept": "Customer Service", "email": "robert.kim@robotix.com"},
    {"name": "Amanda Foster", "title": "HR Manager", "dept": "Human Resources", "email": "amanda.foster@robotix.com"},
    {"name": "Chris Patel", "title": "Marketing Manager", "dept": "Sales & Marketing", "email": "chris.patel@robotix.com"},
    {"name": "Nicole Sanders", "title": "Product Manager - Industrial Robots", "dept": "Product Development", "email": "nicole.sanders@robotix.com"},
    {"name": "Marcus Johnson", "title": "Product Manager - Collaborative Robots", "dept": "Product Development", "email": "marcus.johnson@robotix.com"},
    {"name": "Rachel Green", "title": "Senior Engineer", "dept": "Product Development", "email": "rachel.green@robotix.com"},
    {"name": "Tom Bradley", "title": "Quality Control Specialist", "dept": "Quality Assurance", "email": "tom.bradley@robotix.com"},
    {"name": "Diana Lopez", "title": "Customer Support Lead", "dept": "Customer Service", "email": "diana.lopez@robotix.com"},
    {"name": "Kevin O'Brien", "title": "IT Manager", "dept": "IT & Systems", "email": "kevin.obrien@robotix.com"},
    {"name": "Sophia Nguyen", "title": "Finance Manager", "dept": "Finance", "email": "sophia.nguyen@robotix.com"},
    {"name": "Daniel Wright", "title": "Legal Counsel", "dept": "Legal & Compliance", "email": "daniel.wright@robotix.com"},
    {"name": "Jessica Martinez", "title": "Sales Representative", "dept": "Sales & Marketing", "email": "jessica.martinez@robotix.com"},
    {"name": "Brian Cooper", "title": "Manufacturing Supervisor", "dept": "Manufacturing", "email": "brian.cooper@robotix.com"},
]

# Product Categories
PRODUCT_CATEGORIES = {
    "Industrial Robots": [
        "PrecisionArm 6-Axis",
        "HeavyDuty Articulated Robot",
        "HighSpeed Assembly Robot",
        "Welding Robot Pro"
    ],
    "Collaborative Robots": [
        "CoBot Assistant 5kg",
        "CoBot Precision 10kg",
        "CoBot Mobile Platform",
        "CoBot Dual-Arm System"
    ],
    "Mobile Robots": [
        "AutoNav AGV-500",
        "SmartCart AMR-1000",
        "PalletMover Robot",
        "Inspection Rover"
    ],
    "Components": [
        "6-Axis Force Sensor",
        "High-Precision Gripper",
        "Vision System Pro",
        "End-Effector Kit",
        "Safety Scanner System"
    ],
    "Software": [
        "RobotOS Control Suite",
        "Fleet Management Platform",
        "Simulation & Programming Tool",
        "Predictive Maintenance AI"
    ]
}

# Common HR Policy Topics
HR_TOPICS = [
    "Employee Handbook",
    "Code of Conduct",
    "Remote Work Policy",
    "Time Off and Leave",
    "Benefits Overview",
    "Performance Review Process",
    "Workplace Safety",
    "Anti-Harassment Policy",
    "Professional Development",
    "Onboarding Guide"
]

# Legal Document Types
LEGAL_TOPICS = [
    "Privacy Policy",
    "Terms of Service",
    "Warranty and Return Policy",
    "System Integration Agreement",
    "Employee Confidentiality Agreement",
    "Data Protection Compliance",
    "Product Liability Terms",
    "Service Contract Template"
]

def get_random_employee(exclude_dept=None):
    """Get a random employee, optionally excluding a department"""
    if exclude_dept:
        filtered = [e for e in EMPLOYEES if e['dept'] != exclude_dept]
        return random.choice(filtered)
    return random.choice(EMPLOYEES)

def get_employees_by_dept(dept):
    """Get all employees in a department"""
    return [e for e in EMPLOYEES if e['dept'] == dept]

def get_random_date(start_year=2023, end_year=2024):
    """Generate a random date within range"""
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def format_date(date):
    """Format date consistently"""
    return date.strftime("%B %d, %Y")
