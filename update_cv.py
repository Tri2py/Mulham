# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_cv = '''# MULHAM IBRAHIM
Digital Marketing Strategist & Full-Stack Web Designer
Damascus, Syria | +963 992 318 066 | mulhamlol790@gmail.com

---

## PROFESSIONAL SUMMARY

Business Administration student with hands-on experience in digital marketing, AI-generated content creation, full-stack web design, and business operations. Specialized in scaling social media brands for dental clinics, medical centers, and commercial businesses through short-form content strategy, AI-assisted production workflows, and UI/UX optimization.

---

## EDUCATION

**Bachelor of Business Administration**
Higher Institute of Business Administration (HIBA) - 3rd Year
Focus: Business Operations, Marketing Principles, Organizational Strategy

---

## CORE SKILLS & TECHNOLOGIES

- **Marketing:** Short-Form Video Production, Social Media Strategy, AI Content Generation, Campaign Optimization, Product Positioning
- **Development:** UI/UX Design, Full-Stack Web Design, Responsive Design, Database Management
- **AI Tools:** Cursor, Claude Models, Google AI Studio, Codex, Anthropic Tools
- **Design Software:** Adobe Illustrator, Adobe Photoshop, Affinity Suite, Canva
- **Business Tools:** Microsoft Office Suite, Workflow Coordination, Operations Management

---

## PROFESSIONAL EXPERIENCE

**Digital Marketing & Content Strategist | Freelance & Agency Projects**
- Managed and scaled social media presence for dental clinics, medical centers, and consumer brands.
- Produced high-engagement short-form video campaigns using AI tools for scripting, visual generation, and editing.
- Optimized content performance through analytics and audience targeting strategies.

**Head of Design (Marketing Department) | Cureox Medical Applications**
- Led visual direction and execution for advertising and social media campaigns.
- Designed high-converting creative assets tailored for medical and corporate audiences.
- Maintained brand consistency across digital marketing materials.

**Full-Stack Web Designer & Developer | Ghiath Bourhani Trading Co.**
- Designed and developed full-stack web applications using AI-assisted development workflows.
- Managed UI/UX systems and database structures for usability and performance.
- Optimized responsive behavior across multiple devices.

**Co-Founder & Booking Assistant | TikiTaka Gaming Club**
- Co-managed operational workflows and strategic development.
- Improved booking coordination and customer scheduling systems.
- Supported customer experience and operational management.

**Pre-Press Designer | Apparel Print Houses & Factories**
- Prepared vector artwork and executed color separation for textile printing.
- Collaborated with manufacturing teams to minimize print errors.
- Supervised pre-production proofing for accurate final output.

---

## LANGUAGES

- Arabic: Native
- English: Full Professional Proficiency'''

# Regex to replace the content of cvMarkdownContent
pattern = re.compile(r'(const cvMarkdownContent = ).*?(;)', re.DOTALL)
new_content = pattern.sub(rf'\g<1>{new_cv}\g<2>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CV Updated!")
