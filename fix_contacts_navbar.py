# -*- coding: utf-8 -*-
import re

# 1. Grab the correct header from index.html
with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    index_content = f.read()

header_match = re.search(r'(<header id="bringer-header".*?</header>)', index_content, re.DOTALL)
if header_match:
    correct_header = header_match.group(1)
    
    # Let's adjust the 'current-menu-item' class for the Contacts page
    # First, remove current-menu-item from Home
    correct_header = correct_header.replace('<li class="current-menu-item">\n                            <a href="index.html">Home</a>', '<li>\n                            <a href="index.html">Home</a>')
    # Add current-menu-item to Contacts
    correct_header = correct_header.replace('<li>\n                            <a href="contacts.html">Contacts</a>', '<li class="current-menu-item">\n                            <a href="contacts.html">Contacts</a>')

    # 2. Inject it into contacts.html
    with open('contacts.html', 'r', encoding='windows-1252', errors='ignore') as f:
        contacts_content = f.read()
        
    contacts_content = re.sub(r'<header id="bringer-header".*?</header>', correct_header, contacts_content, flags=re.DOTALL)
    
    with open('contacts.html', 'w', encoding='windows-1252') as f:
        f.write(contacts_content)
    
    print("Contacts navbar fixed successfully!")
else:
    print("Could not find header in index.html")

