# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Make the section height larger
content = content.replace('height: 100vh;', 'height: 115vh;')

# 2. Make the text bigger
content = content.replace('font-size: 16vw;', 'font-size: 18.5vw;')
content = content.replace('font-size: 15.5vw;', 'font-size: 17.5vw;')

# 3. Make the orbs bigger to match the new scale
content = content.replace('width: 45vw; height: 45vw;', 'width: 60vw; height: 60vw;')
content = content.replace('width: 35vw; height: 35vw;', 'width: 50vw; height: 50vw;')
content = content.replace('width: 30vw; height: 30vw;', 'width: 45vw; height: 45vw;')

# 4. Make the text vertically centered more perfectly within the new 115vh container
# We can adjust the padding on hero-blend-text if needed, but flex center handles it automatically.

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Hero made bigger!")
