# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Fix hero margin-bottom
content = content.replace('margin-bottom: 20vh;', 'margin-bottom: 5vh;')

# 2. Add ID to services section
content = content.replace('<section style="margin-top: 10vh;">', '<section id="about" style="margin-top: 5vh; position: relative;">')

# 3. Add the connection line and glowing overlap effect to the wrapper
wrapper_find = '''<div class="page-content-wrapper" style="position: relative; z-index: 10; background: #000000; margin-left: calc(50% - 50vw); width: 100vw; padding-top: 8vh; padding-bottom: 8vh; border-top-left-radius: 50px; border-top-right-radius: 50px; box-shadow: 0 -30px 100px rgba(0,0,0,0.9); border-top: 1px solid rgba(255,255,255,0.06); transform: translate3d(0,0,0);">'''

wrapper_replace = '''<div class="page-content-wrapper" style="position: relative; z-index: 10; background: #000000; margin-left: calc(50% - 50vw); width: 100vw; padding-top: 12vh; padding-bottom: 8vh; border-top-left-radius: 60px; border-top-right-radius: 60px; box-shadow: 0 -40px 100px rgba(140, 45, 246, 0.15), 0 -10px 40px rgba(0,0,0,0.9); border-top: 1px solid rgba(140, 45, 246, 0.3); transform: translate3d(0,0,0);">
                
                <!-- Animated Connection Line -->
                <div style="position: absolute; top: -100px; left: 50%; transform: translateX(-50%); width: 2px; height: 180px; z-index: 11;">
                    <div style="width: 100%; height: 100%; background: linear-gradient(to bottom, transparent, #8C2DF6, transparent); animation: dropLine 2.5s infinite ease-in-out;"></div>
                </div>
                <style>
                    @keyframes dropLine {
                        0% { transform: translateY(-100%) scaleY(0); opacity: 0; }
                        50% { transform: translateY(0) scaleY(1); opacity: 1; }
                        100% { transform: translateY(100%) scaleY(0); opacity: 0; }
                    }
                </style>
'''

content = content.replace(wrapper_find, wrapper_replace)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Connection animation added!")
