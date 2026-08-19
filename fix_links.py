import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with open(file, 'r', encoding='windows-1252', errors='ignore') as f:
            content = f.read()
        
        # Replace hrefs in links (preventing changing strings that might be inside other contexts)
        content = content.replace('href="index.html"', 'href="/home"')
        content = content.replace('href="contacts.html"', 'href="/contact"')
        content = content.replace('href="portfolio.html"', 'href="/portfolio"')
        
        with open(file, 'w', encoding='windows-1252') as f:
            f.write(content)
        print(f"Fixed links in {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
