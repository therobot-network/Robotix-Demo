"""
Unstructured Data Generator
Creates markdown files, memos, meeting notes, emails, and other unstructured content
AI-FIRST approach for Robotix robotics company
"""

import os
import random
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
    print("⚠️  LangChain not installed for unstructured data generation.")


class UnstructuredDataGenerator:

    def __init__(self, output_dir="data/unstructured", use_ai=True):
        self.output_dir = output_dir
        self.use_ai = use_ai and AI_AVAILABLE

        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(f"{output_dir}/memos", exist_ok=True)
        os.makedirs(f"{output_dir}/meetings", exist_ok=True)
        os.makedirs(f"{output_dir}/projects", exist_ok=True)

        # Initialize AI model if available
        if self.use_ai:
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if api_key:
                self.llm = ChatAnthropic(
                    model="claude-3-5-sonnet-20241022",
                    temperature=0.8,  # Higher for creative content
                    max_tokens=6000,
                )
                print(
                    "✅ AI content generation enabled for unstructured docs (Claude 3.5 Sonnet)"
                )
            else:
                self.use_ai = False
                print("⚠️  ANTHROPIC_API_KEY not found for unstructured generation.")

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

    def _generate_ai_content(self, content_type, context):
        """Generate content using AI"""
        if not self.use_ai:
            return f"AI generation not available. {content_type} content would go here."

        try:
            prompt = f"""Generate realistic business content for Robotix (robotics manufacturer, 290 employees, $42M revenue).

Content Type: {content_type}
Context:
{context}

Requirements:
- Professional business tone appropriate for {content_type}
- Specific data, metrics, and technical details relevant to robotics/automation
- 500-800 words
- Include concrete examples and actionable information
- Use realistic business language
- Format as markdown with clear sections

Generate ONLY the content body (I'll add the header separately)."""

            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            print(f"   ⚠️  AI generation failed for {content_type}: {str(e)}")
            return f"Content generation failed. {content_type} content would go here."

    def generate_internal_memo(self, subject, from_person, to_people, date, content):
        """Format an internal memo in markdown"""
        memo = f"""# INTERNAL MEMORANDUM

**TO:** {to_people}  
**FROM:** {from_person['name']}, {from_person['title']}  
**DATE:** {date}  
**RE:** {subject}

---

{content}

---

For questions regarding this memo, please contact {from_person['name']} at {from_person['email']}.
"""
        return memo

    def generate_meeting_notes(self, meeting_title, attendees, date, content):
        """Format meeting notes in markdown"""
        meeting_doc = f"""# {meeting_title}

**Date:** {date}  
**Location:** Conference Room / Zoom  
**Attendees:** {', '.join(attendees)}

{content}

---
*Notes compiled by {random.choice(attendees)}*
"""
        return meeting_doc

    def generate_project_document(self, project_name, owner, date, content):
        """Format project documentation"""
        doc = f"""# Project: {project_name}

**Project Owner:** {owner['name']}  
**Department:** {owner['dept']}  
**Last Updated:** {date}

{content}
"""
        return doc

    def generate_all_memos(self):
        """Generate various internal memos using AI"""
        memos = []

        # Define memo topics
        memo_topics = [
            {
                "subject": "Q1 2024 Sales Performance Summary",
                "dept": "Sales & Marketing",
                "to": "All Sales Team Members",
                "context": """Generate a Q1 2024 sales performance memo covering:
- Overall revenue achievement ($12.3M, 18% YoY growth)
- Product category performance (Industrial Robots up 25%, Collaborative Robots growth, Software subscriptions)
- Regional performance breakdown
- Top performing products
- Major wins (large manufacturing clients, system integrations)
- Q2 outlook and targets
Include realistic metrics for robotics sales.""",
            },
            {
                "subject": "New CoBot Product Line Launch Announcement",
                "dept": "Product Development",
                "to": "All Departments",
                "context": """Generate a product launch announcement for new collaborative robot line:
- Product innovations (improved safety features, easier programming, higher payload)
- Development timeline and testing results
- Launch date and marketing campaign
- Sales team preparation and training
- Manufacturing readiness
- Competitive positioning in cobot market
- Launch events and demonstrations
Include technical details relevant to robotics.""",
            },
            {
                "subject": "Updated Remote Work Policy - Effective April 1, 2024",
                "dept": "Human Resources",
                "to": "All Employees",
                "context": """Generate remote work policy update memo covering:
- Expanded flexibility (3 days/week remote for eligible roles)
- Core in-office days (Tuesday/Thursday for collaboration)
- Increased home office stipend ($750 one-time, $200 annual refresh)
- Technology support improvements
- Eligibility criteria
- Department-specific policies (Manufacturing/Production require on-site)
- Implementation timeline
- Employee feedback data supporting change
Note: Robotics manufacturing roles require on-site presence.""",
            },
            {
                "subject": "Manufacturing Process Improvement Initiative - Phase 1 Results",
                "dept": "Manufacturing",
                "to": "Manufacturing Team, Quality Assurance, Executive Leadership",
                "context": """Generate manufacturing improvement results memo covering:
- Quality improvements (defect rate reduction, yield improvements)
- Efficiency gains (throughput increase, cycle time reduction)
- Safety enhancements (accident-free days, improved protocols)
- Lean manufacturing implementation
- Employee training program results
- Equipment upgrades (automation in production)
- Phase 2 plans (additional automation, capacity expansion)
- Financial impact
Include specific metrics for robot manufacturing facility.""",
            },
            {
                "subject": "Sustainability Initiative - Carbon Neutral Manufacturing Goal",
                "dept": "Manufacturing",
                "to": "All Employees",
                "context": """Generate sustainability initiative memo covering:
- Carbon neutral manufacturing goal by 2028
- Current baseline emissions assessment
- Renewable energy transition plan
- Manufacturing efficiency improvements
- Sustainable materials sourcing
- Waste reduction targets
- Employee engagement programs
- Cost-benefit analysis
- Industry leadership position
Make it relevant to robotics/electronics manufacturing.""",
            },
            {
                "subject": "Customer Satisfaction Survey Results - Q1 2024",
                "dept": "Customer Service",
                "to": "All Departments",
                "context": """Generate customer satisfaction survey results memo covering:
- Overall satisfaction scores (Net Promoter Score, CSAT)
- Product quality ratings
- Technical support performance
- Installation and training feedback
- Areas of strength (reliability, performance, support)
- Areas for improvement (documentation, response times)
- Action plans based on feedback
- Competitive benchmarking
Focus on B2B robotics customers.""",
            },
            {
                "subject": "IT Security Policy Updates and Mandatory Training",
                "dept": "IT & Systems",
                "to": "All Employees",
                "context": """Generate IT security policy update memo covering:
- New security threats relevant to robotics/industrial companies
- Updated password requirements
- Multi-factor authentication rollout
- VPN and remote access security
- Phishing awareness
- Data classification and handling
- Incident reporting procedures
- Mandatory security training (deadline, format)
- Compliance requirements
Include specifics for industrial IoT and connected robot systems.""",
            },
            {
                "subject": "New System Integrator Partnership Program Launch",
                "dept": "Sales & Marketing",
                "to": "Sales Team, Product Development",
                "context": """Generate partnership program launch memo covering:
- Program overview and goals
- Partner tiers (Silver/Gold/Platinum)
- Benefits for each tier (margins, support, training)
- Technical certification requirements
- Marketing support and co-op funds
- Target partner profile
- Application process
- Expected business impact
- Competitive advantage in robotics integration market.""",
            },
            {
                "subject": "Employee Wellness Program Expansion Announcement",
                "dept": "Human Resources",
                "to": "All Employees",
                "context": """Generate wellness program expansion memo covering:
- New wellness initiatives
- Mental health resources expansion
- Fitness reimbursement increase
- Ergonomics assessments (important for manufacturing workers)
- Health screening programs
- Wellness challenges and incentives
- Employee Assistance Program enhancements
- Participation details and enrollment
- Cost savings and ROI for employees.""",
            },
        ]

        print(f"   [{self._get_timestamp()}] Generating AI-powered memos...")
        total = len(memo_topics)
        for idx, memo_def in enumerate(memo_topics, 1):
            from_person = random.choice(get_employees_by_dept(memo_def["dept"]))
            date = format_date(get_random_date(2024, 2024))

            self._print_progress_bar(idx - 0.5, total, "Memo Progress")
            content = self._generate_ai_content(
                f"Internal Memo - {memo_def['subject']}", memo_def["context"]
            )

            memo = self.generate_internal_memo(
                subject=memo_def["subject"],
                from_person=from_person,
                to_people=memo_def["to"],
                date=date,
                content=content,
            )

            filename = (
                memo_def["subject"].split("-")[0].strip().replace(" ", "-")[:50] + ".md"
            )
            memos.append((filename, memo))
            self._print_progress_bar(idx, total, "Memo Progress")

        # Save all memos
        print(f"\n   [{self._get_timestamp()}] Saving memos to disk...")
        for filename, content in memos:
            filepath = f"{self.output_dir}/memos/{filename}"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

        return memos

    def generate_all_meeting_notes(self):
        """Generate various meeting notes using AI"""
        meetings = []

        meeting_topics = [
            {
                "title": "Q2 2024 Product Planning Meeting",
                "attendees": [
                    "Emily Thompson",
                    "Nicole Sanders",
                    "Marcus Johnson",
                    "Rachel Green",
                    "Sarah Chen",
                ],
                "context": """Generate product planning meeting notes covering:
- Q1 product performance review (best sellers, challenges)
- Q2 product launches (new cobot models, software updates)
- R&D pipeline (next-gen industrial robots, AI integration)
- Budget allocation for new projects
- Competitive landscape analysis (other robotics companies)
- Supply chain updates (semiconductor availability, lead times)
- Market opportunities (emerging applications, industries)
Include action items and next steps.""",
            },
            {
                "title": "Sales Strategy Session - Manufacturing Sector Growth",
                "attendees": [
                    "David Martinez",
                    "Jessica Martinez",
                    "Chris Patel",
                    "Sarah Chen",
                ],
                "context": """Generate sales strategy meeting notes covering:
- Current manufacturing sector penetration
- Target industries (automotive, electronics, food processing)
- System integrator partnership expansion
- Pricing strategy for large accounts
- Marketing support for sales team
- Competitive threats and response
- Demo and proof-of-concept programs
- Sales training needs
- Revenue targets and quotas
Include specific action items for team members.""",
            },
            {
                "title": "Manufacturing Automation Investment Discussion",
                "attendees": [
                    "James Wilson",
                    "Sarah Chen",
                    "Michael Rodriguez",
                    "Emily Thompson",
                ],
                "context": """Generate executive meeting notes covering:
- Proposal for additional production automation
- Capital investment requirements ($2M-$5M range)
- ROI analysis and payback period
- Capacity increase projections
- Quality improvements expected
- Labor impact and retraining
- Timeline for implementation
- Risk assessment
- Decision and next steps.""",
            },
            {
                "title": "Customer Advisory Board - Product Feedback Session",
                "attendees": [
                    "David Martinez",
                    "Emily Thompson",
                    "Nicole Sanders",
                    "Marcus Johnson",
                ],
                "context": """Generate customer advisory board meeting notes covering:
- Customer feedback on current products
- Feature requests and improvements
- Pain points in deployment and integration
- Training and documentation needs
- Support experience feedback
- Future product direction input
- Industry trends and needs
- Competitive comparisons
- Action items for product team.""",
            },
        ]

        print(f"   [{self._get_timestamp()}] Generating AI-powered meeting notes...")
        total = len(meeting_topics)
        for idx, meeting_def in enumerate(meeting_topics, 1):
            date = format_date(get_random_date(2024, 2024))

            self._print_progress_bar(idx - 0.5, total, "Meeting Progress")
            content = self._generate_ai_content(
                f"Meeting Notes - {meeting_def['title']}", meeting_def["context"]
            )

            meeting_doc = self.generate_meeting_notes(
                meeting_title=meeting_def["title"],
                attendees=meeting_def["attendees"],
                date=date,
                content=content,
            )

            filename = meeting_def["title"].replace(" ", "-")[:60] + ".md"
            meetings.append((filename, meeting_doc))
            self._print_progress_bar(idx, total, "Meeting Progress")

        # Save all meeting notes
        print(f"\n   [{self._get_timestamp()}] Saving meeting notes to disk...")
        for filename, content in meetings:
            filepath = f"{self.output_dir}/meetings/{filename}"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

        return meetings

    def generate_project_docs(self):
        """Generate project documentation using AI"""
        projects = []

        project_topics = [
            {
                "name": "E-Commerce Platform Modernization (Phase 2)",
                "owner_dept": "IT & Systems",
                "context": """Generate project documentation covering:
- Overview: Phase 2 of e-commerce platform upgrade for B2B robotics sales
- Objectives: Mobile optimization, quote generation, CAD model downloads, configurator tool
- Timeline: April-September 2024, phased rollout
- Status: 20% complete, design phase
- Team: IT team, external developers, UX agency, product liaisons
- Resources: $350K budget, React/Node.js stack, integration with ERP
- Success metrics: Conversion rate increase, quote generation efficiency, customer satisfaction
- Risks and mitigation strategies.""",
            },
            {
                "name": "Next-Generation Industrial Robot Development",
                "owner_dept": "Product Development",
                "context": """Generate project documentation covering:
- Overview: Develop next-gen 6-axis industrial robot with AI capabilities
- Objectives: Higher payload, improved precision, vision integration, easier programming
- Timeline: 18-month development cycle, Q4 2025 launch target
- Status: 30% complete, prototype testing phase
- Team: Engineering team, software developers, manufacturing liaison
- Resources: $3M R&D budget, simulation software, testing facilities
- Technical milestones and deliverables
- Market opportunity and competitive positioning.""",
            },
            {
                "name": "Manufacturing Facility Expansion - Minneapolis",
                "owner_dept": "Manufacturing",
                "context": """Generate project documentation covering:
- Overview: Expand Minneapolis facility to increase production capacity 40%
- Objectives: Add 15,000 sq ft, install automated assembly lines, hire 25 workers
- Timeline: Construction starts Q2 2024, operational Q1 2025
- Status: 10% complete, design and permitting phase
- Team: Facilities manager, manufacturing director, HR, finance
- Resources: $8M capital investment, construction contractor, equipment vendors
- Capacity analysis and production projections
- Impact on delivery times and revenue.""",
            },
            {
                "name": "AI-Powered Predictive Maintenance Platform",
                "owner_dept": "Product Development",
                "context": """Generate project documentation covering:
- Overview: Develop cloud-based AI platform for robot fleet maintenance prediction
- Objectives: Reduce downtime, predictive alerts, usage analytics, OTA updates
- Timeline: 12-month development, Q3 2024 beta launch
- Status: 45% complete, ML model training phase
- Team: Software engineers, data scientists, customer success
- Resources: $500K budget, AWS infrastructure, ML tools
- Technical architecture and data requirements
- Revenue model (subscription SaaS) and business case.""",
            },
        ]

        print(
            f"   [{self._get_timestamp()}] Generating AI-powered project documents..."
        )
        total = len(project_topics)
        for idx, project_def in enumerate(project_topics, 1):
            owner = random.choice(get_employees_by_dept(project_def["owner_dept"]))
            date = format_date(get_random_date(2024, 2024))

            self._print_progress_bar(idx - 0.5, total, "Project Progress")
            content = self._generate_ai_content(
                f"Project Documentation - {project_def['name']}", project_def["context"]
            )

            project_doc = self.generate_project_document(
                project_name=project_def["name"],
                owner=owner,
                date=date,
                content=content,
            )

            filename = (
                project_def["name"].split("-")[0].strip().replace(" ", "-")[:50] + ".md"
            )
            projects.append((filename, project_doc))
            self._print_progress_bar(idx, total, "Project Progress")

        # Save project docs
        print(f"\n   [{self._get_timestamp()}] Saving project documents to disk...")
        for filename, content in projects:
            filepath = f"{self.output_dir}/projects/{filename}"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

        return projects

    def generate_all(self):
        """Generate all unstructured content using AI"""
        print(f"\n[{self._get_timestamp()}] 📝 Generating unstructured documents...")

        memos = self.generate_all_memos()
        print(f"  ✓ [{self._get_timestamp()}] Generated {len(memos)} internal memos\n")

        meetings = self.generate_all_meeting_notes()
        print(
            f"  ✓ [{self._get_timestamp()}] Generated {len(meetings)} meeting notes\n"
        )

        projects = self.generate_project_docs()
        print(
            f"  ✓ [{self._get_timestamp()}] Generated {len(projects)} project documents\n"
        )

        total = len(memos) + len(meetings) + len(projects)
        print(f"✅ Total unstructured documents: {total}")
        print(f"   Location: {self.output_dir}/")

        return {"memos": memos, "meetings": meetings, "projects": projects}
