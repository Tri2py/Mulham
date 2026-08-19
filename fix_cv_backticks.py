# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I will find 'const cvMarkdownContent = # MULHAM' and add backticks
content = content.replace('const cvMarkdownContent = # MULHAM', 'const cvMarkdownContent = # MULHAM')

# I will find '- English: Full Professional Proficiency' and add 
content = content.replace('- English: Full Professional Proficiency\n\n# Regex to replace', '- English: Full Professional Proficiency;\n\n# Regex to replace')

# Let's just do a smarter replace. 
# We know where it starts and where it ends.
