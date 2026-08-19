# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

text_to_remove = '''**Co-Founder & Booking Assistant | TikiTaka Gaming Club**
- Co-managed operational workflows and strategic development.
- Improved booking coordination and customer scheduling systems.
- Supported customer experience and operational management.

'''

new_content = content.replace(text_to_remove, '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed successfully!")
