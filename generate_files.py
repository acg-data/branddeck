import re
import os

# Define sections with their titles and descriptions
sections = [
    {
        'id': 'brand-archetype',
        'title': 'Brand Archetype',
        'desc': 'Analysis of Deel\'s brand personality using archetypal frameworks and strategic positioning.'
    },
    {
        'id': 'brand-book',
        'title': 'Brand Book',
        'desc': 'Comprehensive brand identity and guidelines for Deel.'
    },
    {
        'id': 'market-research',
        'title': 'Market Research',
        'desc': 'Data-driven insights into the HR tech and global payroll market.'
    },
    {
        'id': 'gap-analysis',
        'title': 'Gap Analysis',
        'desc': 'SWOT analysis and competitive positioning for Deel.'
    },
    {
        'id': 'market-size',
        'title': 'Market Size',
        'desc': 'TAM, SAM, and SOM analysis for the global HR and payroll market.'
    },
    {
        'id': 'customer-profiles',
        'title': 'Customer Profiles',
        'desc': 'Detailed personas of Deel\'s target customers and their pain points.'
    },
    {
        'id': 'competitors',
        'title': 'Competitor Analysis',
        'desc': 'Track how AI models mention competitors versus your brand.'
    },
    {
        'id': 'legal-compliance',
        'title': 'Legal & Compliance',
        'desc': 'Regulatory framework and compliance requirements for Deel\'s global operations.'
    },
    {
        'id': 'go-to-market',
        'title': 'Go To Market',
        'desc': 'Strategic launch plan and market expansion roadmap for Deel.'
    },
    {
        'id': 'business-plan',
        'title': 'Business Plan',
        'desc': 'Comprehensive operational and strategic plan for Deel\'s growth.'
    },
    {
        'id': 'financial-model',
        'title': 'Financial Model',
        'desc': 'Revenue projections, expense analysis, and financial metrics for Deel.'
    },
    {
        'id': 'team',
        'title': 'Team',
        'desc': 'Key leadership and organizational structure for Deel.'
    },
    {
        'id': 'pitch-deck',
        'title': 'Pitch Deck',
        'desc': 'Investor presentation deck highlighting Deel\'s opportunity and traction.'
    }
]

# Sidebar HTML template with navigation
sidebar_template = '''        <div class="sidebar">
            <div class="mac-dots">
                <div class="dot red"></div>
                <div class="dot yellow"></div>
                <div class="dot green"></div>
            </div>

            <div class="company-select">
                <div class="avatar-box">D</div>
                <span style="font-weight: 500; font-size: 14px;">Deel</span>
                <svg class="icon" style="margin-left: auto; color: #9ca3af;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
            </div>

            <nav class="nav-menu">
                <a href="executive-summary.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Executive Summary
                </a>
                <a href="brand-archetype.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Brand Archetype
                </a>
                <a href="brand-book.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Brand Book
                </a>
                <a href="market-research.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Market Research
                </a>
                <a href="gap-analysis.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Gap Analysis
                </a>
                <a href="market-size.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Market Size
                </a>
                <a href="customer-profiles.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Customer Profiles
                </a>
                <a href="competitors.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Competitors
                </a>
                <a href="legal-compliance.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Legal & Compliance
                </a>
                <a href="go-to-market.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Go To Market
                </a>
                <a href="business-plan.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Business Plan
                </a>
                <a href="financial-model.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Financial Model
                </a>
                <a href="team.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Team
                </a>
                <a href="pitch-deck.html" class="nav-item">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Pitch Deck
                </a>
            </nav>
        </div>'''

# HTML template for each page
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Competitor Analysis Dashboard</title>
    <link rel="stylesheet" href="../components/common.css">
    <script>
        function setActiveLink() {{
            const currentPath = window.location.pathname.split('/').pop();
            document.querySelectorAll('.nav-item').forEach(item => {{
                item.classList.remove('active');
                if (item.getAttribute('href').includes('{id}')) {{
                    item.classList.add('active');
                }}
            }});
        }}
        document.addEventListener('DOMContentLoaded', setActiveLink);
    </script>
</head>
<body>

    <div class="window-frame">
{sidebar}
        <div class="main-content">
{content}
        </div>
    </div>

</body>
</html>'''

# Read the original HTML file to extract section contents
with open('C:/Users/Justin Abrams/analysis.html', 'r', encoding='utf-8') as f:
    original_content = f.read()

# Extract content for each section
for section in sections:
    section_id = section['id']
    pattern = rf'<div id="{section_id}" class="section[^"]*">(.*?)</div>\s*</div>\s*(?=<div id="|$)'

    match = re.search(pattern, original_content, re.DOTALL)
    if match:
        section_content = match.group(1)

        # Set active class for this section's nav item
        sidebar_with_active = sidebar_template.replace(
            f'<a href="{section_id}.html" class="nav-item">',
            f'<a href="{section_id}.html" class="nav-item active">'
        )

        # Generate complete HTML
        html = html_template.format(
            title=section['title'],
            id=section_id,
            sidebar=sidebar_with_active,
            content=section_content
        )

        # Write to file
        output_path = f'C:/Users/Justin Abrams/analysis/pages/{section_id}.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f'Created {output_path}')
    else:
        print(f'Warning: Could not find content for {section_id}')

print('\nAll HTML files created successfully!')
