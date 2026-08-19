# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Fix the Orbs: Use radial-gradient instead of expensive filter: blur()
old_orb_style = '''                .orb {
                    position: absolute;
                    border-radius: 50%;
                    filter: blur(90px);
                    animation: drift ease-in-out infinite alternate;
                    pointer-events: none;
                }
                .orb-1 {
                    width: 60vw; height: 60vw;
                    background: rgba(140, 45, 246, 0.25);
                    top: -15%; left: -10%;
                    animation-duration: 20s;
                }
                .orb-2 {
                    width: 50vw; height: 50vw;
                    background: rgba(80, 20, 150, 0.35);
                    bottom: -15%; right: -10%;
                    animation-duration: 25s;
                }
                .orb-3 {
                    width: 45vw; height: 45vw;
                    background: rgba(140, 45, 246, 0.2);
                    top: 20%; right: -5%;
                    animation-duration: 22s;
                }'''

new_orb_style = '''                .orb {
                    position: absolute;
                    border-radius: 50%;
                    animation: drift ease-in-out infinite alternate;
                    pointer-events: none;
                    will-change: transform;
                }
                .orb-1 {
                    width: 80vw; height: 80vw;
                    background: radial-gradient(circle, rgba(140, 45, 246, 0.3) 0%, transparent 60%);
                    top: -25%; left: -20%;
                    animation-duration: 20s;
                }
                .orb-2 {
                    width: 70vw; height: 70vw;
                    background: radial-gradient(circle, rgba(80, 20, 150, 0.35) 0%, transparent 60%);
                    bottom: -25%; right: -20%;
                    animation-duration: 25s;
                }
                .orb-3 {
                    width: 60vw; height: 60vw;
                    background: radial-gradient(circle, rgba(140, 45, 246, 0.25) 0%, transparent 60%);
                    top: 10%; right: -15%;
                    animation-duration: 22s;
                }'''
content = content.replace(old_orb_style, new_orb_style)

# 2. Fix the Glass Pills: Remove backdrop-filter
old_pill_css = '''            .glass-pill {
                background: rgba(255, 255, 255, 0.02);
                border: 1px solid rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                padding: 12px 24px;
                border-radius: 100px;
                font-family: 'Inter', sans-serif;
                font-size: 0.75rem;
                font-weight: 500;
                color: #fff;
                letter-spacing: 0.15em;
                text-transform: uppercase;
                box-shadow: 0 15px 35px rgba(0,0,0,0.4);
            }'''
new_pill_css = '''            .glass-pill {
                background: rgba(14, 8, 20, 0.7);
                border: 1px solid rgba(140, 45, 246, 0.15);
                padding: 12px 24px;
                border-radius: 100px;
                font-family: 'Inter', sans-serif;
                font-size: 0.75rem;
                font-weight: 500;
                color: #fff;
                letter-spacing: 0.15em;
                text-transform: uppercase;
                box-shadow: 0 15px 35px rgba(0,0,0,0.4);
                will-change: transform;
            }'''
content = content.replace(old_pill_css, new_pill_css)

# Also fix the mobile pills
old_mobile_pill = '''                .glass-pill { 
                    font-size: 0.55rem !important; 
                    padding: 8px 16px !important; 
                    backdrop-filter: blur(5px) !important;
                }'''
new_mobile_pill = '''                .glass-pill { 
                    font-size: 0.55rem !important; 
                    padding: 8px 16px !important; 
                }'''
content = content.replace(old_mobile_pill, new_mobile_pill)

# 3. Add will-change to the wrapper
content = content.replace('transform: translate3d(0,0,0);"', 'transform: translate3d(0,0,0); will-change: transform;"')

# 4. Reduce particles count
content = content.replace('const particleCount = 45;', 'const particleCount = 20;')

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Performance fixes applied!")
