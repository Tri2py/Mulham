# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Enhance Code Editor container
old_editor = '''        .code-editor {
            background: #161b22;
            border-radius: 12px;
            border: 1px solid #30363d;
            overflow: hidden;
            box-shadow: 0 16px 70px rgba(0, 0, 0, 0.5);
        }'''

new_editor = '''        .code-editor {
            background: rgba(14, 8, 20, 0.6);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 16px;
            border: 1px solid rgba(140, 45, 246, 0.2);
            box-shadow: 0 30px 100px rgba(0, 0, 0, 0.8), inset 0 0 40px rgba(140, 45, 246, 0.05);
            overflow: hidden;
        }'''

# Enhance Editor Header
old_header = '''        .editor-header {
            background: #21262d;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid #30363d;
        }'''

new_header = '''        .editor-header {
            background: rgba(255, 255, 255, 0.02);
            padding: 14px 20px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }'''

# Fix CV Section Title margin
old_cv_title = '<section id="cv-preview" class="cv-preview-section" style="margin-top: 10vh; margin-bottom: 10vh;">'
new_cv_title = '<section id="cv-preview" class="cv-preview-section" style="margin-top: 20vh; margin-bottom: 15vh;">'

content = content.replace(old_editor, new_editor)
content = content.replace(old_header, new_header)
content = content.replace(old_cv_title, new_cv_title)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Taste-skill applied to CV editor!")
