#!/usr/bin/env python3
"""
Generate Product Guides and Benefits Documents
Generates 5 product guides and 5 benefits documents for Robotix
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# Color scheme
COLORS = {
    "primary": "\033[94m",
    "success": "\033[92m",
    "warning": "\033[93m",
    "error": "\033[91m",
    "reset": "\033[0m",
    "bold": "\033[1m",
}


def print_status(message, status="info"):
    """Print colored status message"""
    color = COLORS.get(status, COLORS["reset"])
    print(f"{color}{message}{COLORS['reset']}")


# Product Guide Templates
PRODUCT_GUIDE_TYPES = [
    {
        "title": "Safety and Compliance Guide",
        "focus": "safety",
        "sections": [
            "Safety Overview",
            "Regulatory Compliance",
            "Risk Assessment",
            "Safety Features",
            "Emergency Procedures",
            "Lockout/Tagout Procedures",
            "Personal Protective Equipment",
            "Safety Training Requirements",
        ],
    },
    {
        "title": "Maintenance Best Practices Guide",
        "focus": "maintenance",
        "sections": [
            "Preventive Maintenance Schedule",
            "Daily Inspection Checklist",
            "Monthly Maintenance Tasks",
            "Quarterly Service Requirements",
            "Annual Inspections",
            "Troubleshooting Common Issues",
            "Spare Parts Recommendations",
            "Service Contact Information",
        ],
    },
    {
        "title": "Integration Guide",
        "focus": "integration",
        "sections": [
            "System Requirements",
            "Network Configuration",
            "PLC Integration",
            "I/O Signal Mapping",
            "Communication Protocols",
            "Third-Party Software Integration",
            "API Reference",
            "Integration Examples",
        ],
    },
    {
        "title": "Programming Quick Start Guide",
        "focus": "programming",
        "sections": [
            "Getting Started",
            "Teaching Pendant Basics",
            "Creating Your First Program",
            "Motion Commands",
            "Logic and Variables",
            "Subroutines and Functions",
            "Testing and Debugging",
            "Program Optimization Tips",
        ],
    },
    {
        "title": "Advanced Operations Guide",
        "focus": "advanced",
        "sections": [
            "Advanced Motion Control",
            "Path Planning Optimization",
            "Force Control Applications",
            "Vision System Integration",
            "Multi-Robot Coordination",
            "Performance Tuning",
            "Advanced Diagnostics",
            "Custom Application Development",
        ],
    },
]

BENEFITS_TEMPLATES = [
    {
        "title": "Retirement Plans Guide 2025",
        "category": "Retirement",
        "sections": {
            "401(k) Plan": [
                "Plan overview and eligibility",
                "Employer matching: 100% of first 6% contributed",
                "Immediate vesting for employee contributions",
                "3-year graded vesting for employer match",
                "Investment options: 15 fund choices including target-date funds",
                "Contribution limits: $23,500 annually (2025)",
                "Catch-up contributions: $7,500 for age 50+ (2025)",
                "Roth 401(k) option available",
            ],
            "Retirement Planning Resources": [
                "Free financial planning consultations",
                "Online retirement calculators",
                "Quarterly retirement planning webinars",
                "One-on-one sessions with financial advisors",
                "Access to Fidelity planning tools",
            ],
            "Social Security Planning": [
                "Educational workshops on Social Security optimization",
                "Medicare enrollment assistance",
                "Retirement transition planning support",
            ],
        },
    },
    {
        "title": "Professional Development Benefits 2025",
        "category": "Professional Development",
        "sections": {
            "Tuition Reimbursement": [
                "Up to $7,500 annually for approved degree programs",
                "Covers undergraduate and graduate courses",
                "Must maintain B grade or better",
                "Reimbursement upon course completion",
                "Requires 1-year commitment after completion",
            ],
            "Professional Certifications": [
                "100% coverage for job-related certifications",
                "PMP, Six Sigma, Robotics certifications supported",
                "Exam fees and study materials covered",
                "Paid study time for approved certifications",
            ],
            "Conference and Training": [
                "$2,500 annual budget for conferences",
                "Internal training programs at no cost",
                "Leadership development programs",
                "Technical skills workshops",
                "Soft skills training (communication, management)",
            ],
            "LinkedIn Learning": [
                "Free access to entire LinkedIn Learning platform",
                "10,000+ courses available",
                "Personalized learning paths",
                "Progress tracking and certificates",
            ],
        },
    },
    {
        "title": "Work-Life Balance Programs 2025",
        "category": "Work-Life Balance",
        "sections": {
            "Flexible Work Arrangements": [
                "Hybrid work options: 2-3 days remote per week",
                "Flexible start times: 7 AM - 10 AM window",
                "Compressed work week options (4x10)",
                "Summer Fridays: Half-day Fridays June-August",
                "Results-focused culture",
            ],
            "Paid Time Off": [
                "15 days PTO (0-3 years of service)",
                "20 days PTO (4-7 years of service)",
                "25 days PTO (8+ years of service)",
                "11 paid holidays",
                "Birthday day off",
                "Volunteer time off: 2 days annually",
            ],
            "Parental Leave": [
                "12 weeks paid leave for primary caregiver",
                "6 weeks paid leave for secondary caregiver",
                "Adoption assistance: $5,000 reimbursement",
                "Phased return-to-work program",
                "Lactation rooms at all facilities",
            ],
            "Sabbatical Program": [
                "4-week paid sabbatical after 5 years",
                "8-week paid sabbatical after 10 years",
                "Sabbatical grant: $2,000 for approved purposes",
                "No work contact during sabbatical",
            ],
        },
    },
    {
        "title": "Financial Wellness Benefits 2025",
        "category": "Financial Wellness",
        "sections": {
            "Employee Stock Purchase Plan": [
                "Purchase company stock at 15% discount",
                "Contribute up to 15% of salary",
                "6-month offering periods",
                "No holding period requirement",
                "Immediate equity ownership",
            ],
            "Health Savings Account (HSA)": [
                "Available with HDHP medical plan",
                "Employer contribution: $1,500 (single) / $3,000 (family)",
                "Tax-advantaged savings for medical expenses",
                "Investment options after $2,000 balance",
                "Portable account - take it with you",
            ],
            "Student Loan Repayment Assistance": [
                "$200 monthly contribution to student loans",
                "Up to $2,400 annually",
                "5-year maximum benefit ($12,000 total)",
                "No tax penalty (through 2025)",
                "Direct payment to loan servicer",
            ],
            "Financial Planning Services": [
                "Free financial planning consultations",
                "Estate planning assistance",
                "Tax preparation support",
                "Debt management counseling",
                "Home buying workshops",
            ],
            "Emergency Savings Fund": [
                "Company-sponsored emergency savings account",
                "Automatic payroll deductions",
                "Employer match: $0.50 per $1 up to $500 annually",
                "Access funds anytime without penalty",
            ],
        },
    },
    {
        "title": "Health and Wellness Programs 2025",
        "category": "Health & Wellness",
        "sections": {
            "Mental Health Support": [
                "Employee Assistance Program (EAP): 8 free sessions",
                "24/7 crisis support hotline",
                "Teletherapy options through Talkspace",
                "Stress management workshops",
                "Meditation app subscriptions (Calm, Headspace)",
                "Mental health days included in PTO",
            ],
            "Physical Wellness": [
                "On-site fitness center (HQ location)",
                "$75 monthly gym membership reimbursement",
                "Fitness class subsidies (yoga, CrossFit, etc.)",
                "Annual fitness challenge with prizes",
                "Standing desks available upon request",
                "Ergonomic assessments and equipment",
            ],
            "Preventive Care": [
                "Annual health screenings at no cost",
                "Flu shots provided on-site",
                "Biometric screening incentives",
                "Health coaching programs",
                "Chronic condition management support",
                "Nutrition counseling",
            ],
            "Wellness Incentives": [
                "Up to $500 wellness rewards annually",
                "Points for healthy behaviors",
                "Quarterly wellness challenges",
                "Team-based fitness competitions",
                "Redeemable for gift cards, PTO, charitable donations",
            ],
        },
    },
]


def generate_product_guide(guide_type, product_name, output_dir):
    """Generate a product guide HTML document"""

    date = datetime.now().strftime("%B %d, %Y")
    authors = [
        "Product Documentation Team",
        "Technical Writing Team",
        "Engineering Team",
    ]
    author = random.choice(authors)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name} - {guide_type['title']} - Robotix</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #1a365d;
            border-bottom: 3px solid #2563eb;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2563eb;
            margin-top: 30px;
            border-left: 4px solid #2563eb;
            padding-left: 15px;
        }}
        h3 {{
            color: #0ea5e9;
            margin-top: 20px;
        }}
        .metadata {{
            background: #f1f5f9;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #2563eb;
        }}
        .warning {{
            background: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .info {{
            background: #dbeafe;
            border-left: 4px solid #2563eb;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .success {{
            background: #d1fae5;
            border-left: 4px solid #10b981;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #cbd5e1;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #2563eb;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f8fafc;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        code {{
            background: #f1f5f9;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <h1>{product_name}<br>{guide_type['title']}</h1>
    
    <div class="metadata">
        <strong>Category:</strong> Product Guide | 
        <strong>Type:</strong> {guide_type['focus'].title()} | 
        <strong>Date:</strong> {date} | 
        <strong>Author:</strong> {author}
    </div>
    
    <hr>
    
    <h2>Overview</h2>
    <p>This guide provides comprehensive information about {guide_type['title'].lower()} for the {product_name}. 
    Whether you're a new user or an experienced operator, this document will help you understand and implement 
    best practices for {guide_type['focus']} operations.</p>
    
    <div class="info">
        <strong>📘 Note:</strong> This guide should be used in conjunction with the main product manual. 
        For basic operation instructions, please refer to the {product_name} User Guide.
    </div>
"""

    # Generate content based on guide type
    for i, section in enumerate(guide_type["sections"], 1):
        html_content += f"\n    <h2>{i}. {section}</h2>\n"

        if guide_type["focus"] == "safety":
            html_content += generate_safety_content(section)
        elif guide_type["focus"] == "maintenance":
            html_content += generate_maintenance_content(section)
        elif guide_type["focus"] == "integration":
            html_content += generate_integration_content(section)
        elif guide_type["focus"] == "programming":
            html_content += generate_programming_content(section)
        elif guide_type["focus"] == "advanced":
            html_content += generate_advanced_content(section)

    # Add footer
    html_content += (
        """
    <hr>
    
    <h2>Additional Resources</h2>
    <ul>
        <li><strong>Technical Support:</strong> support@robotix.com | 1-800-ROBOTIX</li>
        <li><strong>Training Portal:</strong> training.robotix.com</li>
        <li><strong>Knowledge Base:</strong> kb.robotix.com</li>
        <li><strong>Video Tutorials:</strong> youtube.com/robotixinc</li>
    </ul>
    
    <div class="info">
        <strong>Document Version:</strong> 1.0<br>
        <strong>Last Updated:</strong> """
        + date
        + """<br>
        <strong>Next Review:</strong> """
        + (datetime.now() + timedelta(days=365)).strftime("%B %Y")
        + """
    </div>
    
    <p><em>© 2025 Robotix. All rights reserved. This document is proprietary and confidential.</em></p>
    
</body>
</html>
"""
    )

    # Save file
    filename = f"{product_name.lower().replace(' ', '-')}---{guide_type['title'].lower().replace(' ', '-')}.html"
    filepath = output_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filename


def generate_safety_content(section):
    """Generate safety-specific content"""
    contents = {
        "Safety Overview": """
    <p>The Robotix robotic system is designed with multiple layers of safety protection. Understanding and following 
    all safety protocols is essential to prevent injury and equipment damage.</p>
    
    <div class="warning">
        <strong>⚠️ WARNING:</strong> Industrial robots can cause serious injury or death. Only qualified personnel 
        should operate, program, or maintain this equipment.
    </div>
    
    <ul>
        <li>All operators must complete certified safety training</li>
        <li>Safety equipment must be worn at all times in the work cell</li>
        <li>Emergency stop buttons must be within easy reach</li>
        <li>Never enter the work envelope during operation</li>
        <li>Follow lockout/tagout procedures for all maintenance</li>
    </ul>
""",
        "Regulatory Compliance": """
    <p>This robotic system complies with the following safety standards and regulations:</p>
    
    <table>
        <tr>
            <th>Standard</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>ISO 10218-1:2011</td>
            <td>Robot safety requirements for industrial robots</td>
        </tr>
        <tr>
            <td>ISO/TS 15066:2016</td>
            <td>Collaborative robots safety requirements</td>
        </tr>
        <tr>
            <td>ANSI/RIA R15.06</td>
            <td>American National Standard for Industrial Robots</td>
        </tr>
        <tr>
            <td>EN ISO 13849-1</td>
            <td>Safety-related parts of control systems</td>
        </tr>
        <tr>
            <td>OSHA 1910.212</td>
            <td>General requirements for all machines</td>
        </tr>
    </table>
""",
        "Emergency Procedures": """
    <p>In case of emergency, follow these procedures:</p>
    
    <h3>Emergency Stop</h3>
    <ol>
        <li>Press any emergency stop button immediately</li>
        <li>Ensure the robot has come to a complete stop</li>
        <li>Do not reset until the cause is identified and resolved</li>
        <li>Report the incident to your supervisor</li>
        <li>Document the event in the safety log</li>
    </ol>
    
    <h3>Emergency Contacts</h3>
    <ul>
        <li><strong>On-site Emergency:</strong> Call 911</li>
        <li><strong>Safety Manager:</strong> Extension 5555</li>
        <li><strong>Technical Support:</strong> 1-800-ROBOTIX (24/7)</li>
        <li><strong>Supervisor:</strong> Per facility directory</li>
    </ul>
""",
    }
    return contents.get(section, f"    <p>Content for {section} section...</p>\n")


def generate_maintenance_content(section):
    """Generate maintenance-specific content"""
    contents = {
        "Preventive Maintenance Schedule": """
    <p>Following the preventive maintenance schedule ensures optimal performance and extends equipment life.</p>
    
    <table>
        <tr>
            <th>Frequency</th>
            <th>Task</th>
            <th>Duration</th>
        </tr>
        <tr>
            <td>Daily</td>
            <td>Visual inspection, clean work area</td>
            <td>10 minutes</td>
        </tr>
        <tr>
            <td>Weekly</td>
            <td>Check cable conditions, clean sensors</td>
            <td>20 minutes</td>
        </tr>
        <tr>
            <td>Monthly</td>
            <td>Lubrication, check bolt torque</td>
            <td>45 minutes</td>
        </tr>
        <tr>
            <td>Quarterly</td>
            <td>Detailed inspection, calibration check</td>
            <td>2 hours</td>
        </tr>
        <tr>
            <td>Annually</td>
            <td>Complete system overhaul, replace wear items</td>
            <td>4-6 hours</td>
        </tr>
    </table>
""",
        "Daily Inspection Checklist": """
    <p>Perform these checks at the start of each shift:</p>
    
    <ul>
        <li>☐ Check emergency stop functionality</li>
        <li>☐ Inspect cables for damage or wear</li>
        <li>☐ Verify all safety guards are in place</li>
        <li>☐ Check for unusual noises or vibrations</li>
        <li>☐ Inspect end effector and tooling</li>
        <li>☐ Clean sensors and cameras</li>
        <li>☐ Check for fluid leaks (if applicable)</li>
        <li>☐ Verify controller display shows no errors</li>
        <li>☐ Test teach pendant functionality</li>
        <li>☐ Clean work area and remove debris</li>
    </ul>
    
    <div class="info">
        <strong>📝 Note:</strong> Log all inspections in the maintenance record book. Report any issues immediately.
    </div>
""",
        "Troubleshooting Common Issues": """
    <p>Common issues and their solutions:</p>
    
    <h3>Robot Won't Start</h3>
    <ul>
        <li>Check power supply and circuit breakers</li>
        <li>Verify emergency stop is not engaged</li>
        <li>Check controller display for error codes</li>
        <li>Inspect all safety interlocks</li>
    </ul>
    
    <h3>Position Errors</h3>
    <ul>
        <li>Perform home position calibration</li>
        <li>Check encoder batteries</li>
        <li>Verify mechanical backlash is within spec</li>
        <li>Inspect for loose mounting bolts</li>
    </ul>
    
    <h3>Jerky Motion</h3>
    <ul>
        <li>Check lubrication levels</li>
        <li>Inspect cables for damage</li>
        <li>Verify payload is within specifications</li>
        <li>Review acceleration/deceleration settings</li>
    </ul>
""",
    }
    return contents.get(section, f"    <p>Content for {section} section...</p>\n")


def generate_integration_content(section):
    """Generate integration-specific content"""
    contents = {
        "System Requirements": """
    <p>Minimum system requirements for integration:</p>
    
    <table>
        <tr>
            <th>Component</th>
            <th>Requirement</th>
        </tr>
        <tr>
            <td>Network</td>
            <td>Ethernet 100Mbps minimum, 1Gbps recommended</td>
        </tr>
        <tr>
            <td>PLC</td>
            <td>Modbus TCP, EtherNet/IP, or PROFINET compatible</td>
        </tr>
        <tr>
            <td>PC (Programming)</td>
            <td>Windows 10/11, 8GB RAM, 50GB storage</td>
        </tr>
        <tr>
            <td>Safety Controller</td>
            <td>Category 3, PLd or higher per ISO 13849-1</td>
        </tr>
    </table>
""",
        "Communication Protocols": """
    <p>Supported communication protocols:</p>
    
    <h3>Industrial Ethernet</h3>
    <ul>
        <li><strong>Modbus TCP:</strong> Port 502, slave mode</li>
        <li><strong>EtherNet/IP:</strong> Scanner/Adapter modes</li>
        <li><strong>PROFINET:</strong> IO-Device mode, RT/IRT</li>
        <li><strong>OPC UA:</strong> Server implementation</li>
    </ul>
    
    <h3>Digital I/O</h3>
    <ul>
        <li>24 configurable digital inputs</li>
        <li>16 configurable digital outputs</li>
        <li>24VDC, sourcing/sinking configurable</li>
        <li>Response time: < 1ms</li>
    </ul>
    
    <h3>Analog I/O</h3>
    <ul>
        <li>8 analog inputs: ±10V, 0-10V, 4-20mA</li>
        <li>4 analog outputs: ±10V, 0-10V</li>
        <li>16-bit resolution</li>
    </ul>
""",
        "API Reference": """
    <p>REST API endpoints for external system integration:</p>
    
    <h3>Authentication</h3>
    <code>POST /api/v1/auth/login</code>
    <p>Authenticate and receive JWT token</p>
    
    <h3>Robot Control</h3>
    <code>GET /api/v1/robot/status</code>
    <p>Retrieve current robot status</p>
    
    <code>POST /api/v1/robot/move</code>
    <p>Execute movement command</p>
    
    <code>POST /api/v1/robot/program/start</code>
    <p>Start program execution</p>
    
    <h3>Data Monitoring</h3>
    <code>GET /api/v1/robot/position</code>
    <p>Get current position (X, Y, Z, Rx, Ry, Rz)</p>
    
    <code>GET /api/v1/robot/io</code>
    <p>Read I/O status</p>
""",
    }
    return contents.get(section, f"    <p>Content for {section} section...</p>\n")


def generate_programming_content(section):
    """Generate programming-specific content"""
    contents = {
        "Getting Started": """
    <p>Begin programming your robot in three easy steps:</p>
    
    <ol>
        <li><strong>Power On:</strong> Turn on the controller and wait for initialization (30-45 seconds)</li>
        <li><strong>Home Position:</strong> Navigate to Setup > Calibration > Home Robot</li>
        <li><strong>Create Program:</strong> Press PROG > NEW > Enter program name</li>
    </ol>
    
    <div class="success">
        <strong>✓ Best Practice:</strong> Always test new programs in T1 (reduced speed) mode first.
    </div>
""",
        "Motion Commands": """
    <p>Basic motion command syntax:</p>
    
    <h3>Linear Movement (MoveL)</h3>
    <code>MoveL P1, v100, fine</code>
    <p>Move linearly to position P1 at 100mm/s with fine positioning</p>
    
    <h3>Joint Movement (MoveJ)</h3>
    <code>MoveJ P2, v50, z10</code>
    <p>Move in joint space to P2 at 50% speed with 10mm zone</p>
    
    <h3>Circular Movement (MoveC)</h3>
    <code>MoveC P3, P4, v200, fine</code>
    <p>Circular movement through P3 to P4 at 200mm/s</p>
    
    <table>
        <tr>
            <th>Speed Parameter</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>v100</td>
            <td>100mm/s TCP speed</td>
        </tr>
        <tr>
            <td>v50</td>
            <td>50% of maximum joint speed</td>
        </tr>
    </table>
""",
        "Logic and Variables": """
    <p>Programming logic and variable handling:</p>
    
    <h3>Variable Types</h3>
    <ul>
        <li><code>num</code> - Numeric values (integer or float)</li>
        <li><code>bool</code> - Boolean (TRUE/FALSE)</li>
        <li><code>pos</code> - Position data (X, Y, Z, Rx, Ry, Rz)</code>
        <li><code>string</code> - Text strings</li>
    </ul>
    
    <h3>Conditional Statements</h3>
    <code>IF DI[1] = TRUE THEN</code><br>
    <code>&nbsp;&nbsp;MoveL P1, v100, fine</code><br>
    <code>ELSE</code><br>
    <code>&nbsp;&nbsp;MoveL P2, v100, fine</code><br>
    <code>ENDIF</code>
    
    <h3>Loops</h3>
    <code>FOR i:=1 TO 10 DO</code><br>
    <code>&nbsp;&nbsp;MoveL PickPos[i], v100, fine</code><br>
    <code>&nbsp;&nbsp;GripperClose()</code><br>
    <code>&nbsp;&nbsp;MoveL PlacePos[i], v100, fine</code><br>
    <code>&nbsp;&nbsp;GripperOpen()</code><br>
    <code>ENDFOR</code>
""",
    }
    return contents.get(section, f"    <p>Content for {section} section...</p>\n")


def generate_advanced_content(section):
    """Generate advanced operations content"""
    contents = {
        "Advanced Motion Control": """
    <p>Advanced motion control features for optimized performance:</p>
    
    <h3>Trajectory Blending</h3>
    <p>Use zone parameters to blend motions for smoother paths:</p>
    <ul>
        <li><code>z1</code> - 1mm radius blend (tight corners)</li>
        <li><code>z10</code> - 10mm radius blend (balanced)</li>
        <li><code>z50</code> - 50mm radius blend (high speed)</li>
        <li><code>fine</code> - No blending (precise stop)</li>
    </ul>
    
    <div class="info">
        <strong>💡 Tip:</strong> Using zone parameters instead of fine positioning can reduce cycle time by 20-40%.
    </div>
""",
        "Force Control Applications": """
    <p>Implement force-controlled operations for delicate tasks:</p>
    
    <h3>Contact Detection</h3>
    <code>ForceMode(TCP, [0,0,1,0,0,0], [0,0,20,0,0,0], 2, [.1,.1,.1,.1,.1,.1])</code>
    
    <p>Parameters:</p>
    <ul>
        <li>Reference frame: TCP</li>
        <li>Selection vector: Z-axis only</li>
        <li>Force limits: 20N in Z-direction</li>
        <li>Type: 2 (compliant mode)</li>
        <li>Limits: Motion limits per axis</li>
    </ul>
    
    <h3>Applications</h3>
    <ul>
        <li>Part insertion and assembly</li>
        <li>Surface following and deburring</li>
        <li>Quality inspection with probing</li>
        <li>Delicate material handling</li>
    </ul>
""",
        "Performance Tuning": """
    <p>Optimize robot performance for your application:</p>
    
    <table>
        <tr>
            <th>Parameter</th>
            <th>Default</th>
            <th>Tuning Guide</th>
        </tr>
        <tr>
            <td>Acceleration</td>
            <td>100%</td>
            <td>Reduce for delicate payloads (50-75%)</td>
        </tr>
        <tr>
            <td>Jerk Limiting</td>
            <td>Enabled</td>
            <td>Disable for maximum speed in simple motions</td>
        </tr>
        <tr>
            <td>Look-ahead</td>
            <td>5 points</td>
            <td>Increase to 10-20 for complex paths</td>
        </tr>
        <tr>
            <td>Servo Gain</td>
            <td>Medium</td>
            <td>Increase for high precision, decrease if oscillating</td>
        </tr>
    </table>
""",
    }
    return contents.get(section, f"    <p>Content for {section} section...</p>\n")


def generate_benefits_document(benefit_template, output_dir):
    """Generate a benefits HTML document"""

    date = datetime.now().strftime("%B %d, %Y")
    authors = [
        "HR Benefits Team",
        "Amanda Foster - HR Director",
        "People Operations Team",
    ]
    author = random.choice(authors)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{benefit_template['title']} - Robotix</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #1e40af;
            border-bottom: 3px solid #3b82f6;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #3b82f6;
            margin-top: 30px;
            border-left: 4px solid #3b82f6;
            padding-left: 15px;
        }}
        h3 {{
            color: #60a5fa;
            margin-top: 20px;
        }}
        .metadata {{
            background: #eff6ff;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #3b82f6;
        }}
        .highlight {{
            background: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .info {{
            background: #dbeafe;
            border-left: 4px solid #3b82f6;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .benefit-box {{
            background: #f0fdf4;
            border: 2px solid #10b981;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        ul {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 10px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #cbd5e1;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #3b82f6;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f8fafc;
        }}
    </style>
</head>
<body>
    <h1>{benefit_template['title']}</h1>
    
    <div class="metadata">
        <strong>Category:</strong> {benefit_template['category']} | 
        <strong>Type:</strong> Employee Benefits | 
        <strong>Effective Date:</strong> January 1, 2025 | 
        <strong>Author:</strong> {author}
    </div>
    
    <hr>
    
    <div class="info">
        <strong>📋 Important:</strong> This document outlines benefits available to eligible Robotix employees. 
        Eligibility requirements and specific terms may vary. Please contact HR at benefits@robotix.com or 
        call 1-800-ROBOTIX ext. 4200 for personalized benefits consultation.
    </div>
    
    <h2>Overview</h2>
    <p>At Robotix, we're committed to providing comprehensive benefits that support your {benefit_template['category'].lower()} 
    needs. This guide outlines the programs and resources available to help you and your family thrive.</p>
"""

    # Generate sections
    for section_title, section_items in benefit_template["sections"].items():
        html_content += f"\n    <h2>{section_title}</h2>\n"
        html_content += '    <div class="benefit-box">\n'
        html_content += "    <ul>\n"
        for item in section_items:
            html_content += f"        <li>{item}</li>\n"
        html_content += "    </ul>\n"
        html_content += "    </div>\n"

    # Add enrollment information
    html_content += (
        """
    <hr>
    
    <h2>Enrollment Information</h2>
    
    <h3>When Can I Enroll?</h3>
    <ul>
        <li><strong>New Hire Enrollment:</strong> Within 30 days of hire date</li>
        <li><strong>Annual Open Enrollment:</strong> November 1-30 each year</li>
        <li><strong>Qualifying Life Events:</strong> 30 days from event (marriage, birth, etc.)</li>
    </ul>
    
    <h3>How to Enroll</h3>
    <ol>
        <li>Log into the benefits portal: <strong>benefits.robotix.com</strong></li>
        <li>Review plan options and costs</li>
        <li>Select your benefits</li>
        <li>Designate beneficiaries</li>
        <li>Review and submit enrollment</li>
    </ol>
    
    <div class="highlight">
        <strong>⏰ Enrollment Deadline:</strong> If you don't enroll during your eligibility period, 
        you'll need to wait until the next open enrollment period unless you experience a qualifying life event.
    </div>
    
    <h2>Contact Information</h2>
    <table>
        <tr>
            <th>Resource</th>
            <th>Contact</th>
        </tr>
        <tr>
            <td>Benefits Team</td>
            <td>benefits@robotix.com | Ext. 4200</td>
        </tr>
        <tr>
            <td>HR Service Center</td>
            <td>hr@robotix.com | 1-800-ROBOTIX</td>
        </tr>
        <tr>
            <td>Benefits Portal</td>
            <td>benefits.robotix.com</td>
        </tr>
        <tr>
            <td>Employee Assistance Program</td>
            <td>1-888-EAP-HELP (24/7)</td>
        </tr>
    </table>
    
    <h2>Important Reminders</h2>
    <ul>
        <li>Review your benefits selections annually during open enrollment</li>
        <li>Update beneficiary information after major life events</li>
        <li>Keep personal information current in the HR system</li>
        <li>Take advantage of preventive care services</li>
        <li>Contact HR with questions - we're here to help!</li>
    </ul>
    
    <div class="info">
        <strong>Document Information:</strong><br>
        Version: 1.0<br>
        Last Updated: """
        + date
        + """<br>
        Next Review: January """
        + str(datetime.now().year + 1)
        + """
    </div>
    
    <p><em>© 2025 Robotix. All rights reserved. This document contains confidential employee benefit information.</em></p>
    
</body>
</html>
"""
    )

    # Save file
    filename = (
        benefit_template["title"].lower().replace(" ", "-").replace("/", "-") + ".html"
    )
    filepath = output_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filename


def main():
    """Main execution function"""
    print_status("\n" + "=" * 60, "primary")
    print_status("  ROBOTIX - PRODUCT GUIDES & BENEFITS GENERATOR", "bold")
    print_status("=" * 60 + "\n", "primary")

    # Define output directories
    base_dir = Path(__file__).parent.parent
    product_guides_dir = base_dir / "data" / "public" / "product-guides"
    benefits_dir = base_dir / "data" / "hr-legal" / "benefits"

    # Create directories if they don't exist
    product_guides_dir.mkdir(parents=True, exist_ok=True)
    benefits_dir.mkdir(parents=True, exist_ok=True)

    # Product names for guides
    products = [
        "PrecisionArm 6-Axis",
        "CoBot Precision 10kg",
        "AutoNav AGV 500",
        "Welding Robot Pro",
        "SmartCart AMR 1000",
    ]

    # Generate Product Guides
    print_status("📚 Generating Product Guides...\n", "primary")
    product_files = []

    for i, guide_type in enumerate(PRODUCT_GUIDE_TYPES, 1):
        product = products[i - 1]
        print_status(f"  [{i}/5] Creating {product} - {guide_type['title']}...", "info")
        filename = generate_product_guide(guide_type, product, product_guides_dir)
        product_files.append(filename)
        print_status(f"        ✓ {filename}", "success")

    # Generate Benefits Documents
    print_status("\n💼 Generating Benefits Documents...\n", "primary")
    benefits_files = []

    for i, benefit_template in enumerate(BENEFITS_TEMPLATES, 1):
        print_status(f"  [{i}/5] Creating {benefit_template['title']}...", "info")
        filename = generate_benefits_document(benefit_template, benefits_dir)
        benefits_files.append(filename)
        print_status(f"        ✓ {filename}", "success")

    # Summary
    print_status("\n" + "=" * 60, "primary")
    print_status("  GENERATION COMPLETE!", "bold")
    print_status("=" * 60, "primary")
    print_status(f"\n✅ Generated {len(product_files)} Product Guides:", "success")
    for f in product_files:
        print_status(f"   • {f}", "info")

    print_status(f"\n✅ Generated {len(benefits_files)} Benefits Documents:", "success")
    for f in benefits_files:
        print_status(f"   • {f}", "info")

    print_status(f"\n📁 Output Directories:", "primary")
    print_status(f"   • Product Guides: {product_guides_dir}", "info")
    print_status(f"   • Benefits: {benefits_dir}", "info")

    print_status("\n✨ All documents generated successfully!\n", "success")


if __name__ == "__main__":
    main()
