# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

old_css = '''            /* Responsive Overrides for new layout */
            @media (max-width: 900px) {
                /* Hide things that truly don't fit */
                .hero-badge { display: none !important; }
                .vertical-text { display: none !important; }
                
                /* Keep the pills, but scale them down and arrange them better */
                .glass-pill { 
                    font-size: 0.55rem !important; 
                    padding: 8px 16px !important; 
                }
                .pill-1 { top: 15% !important; left: 5% !important; }
                .pill-2 { bottom: 35% !important; right: 5% !important; }
                .pill-3 { bottom: 25% !important; left: 5% !important; }
                
                /* Fix typography scaling */
                .hero-main-title h1 span { font-size: 16vw !important; }
                .hero-main-title h1 span:last-child { margin-top: -2vw !important; }
                .hero-main-title > div:first-child { font-size: 0.6rem !important; margin-bottom: 3vh !important; }
                .hero-main-title > div:last-child { font-size: 0.65rem !important; margin-top: 3vh !important; }
                
                /* Keep the description, but center it at the bottom */
                .hero-desc { 
                    display: block !important;
                    position: absolute !important; 
                    bottom: 22vh !important; 
                    left: 5vw !important; 
                    right: 5vw !important; 
                    max-width: 100% !important; 
                    text-align: center !important; 
                    border-left: none !important; 
                    border-top: 1px solid rgba(140, 45, 246, 0.5) !important; 
                    padding-left: 0 !important; 
                    padding-top: 15px !important; 
                }
                .hero-desc p { font-size: 0.75rem !important; }
                
                /* Center the scroll button */
                .hero-scroll-btn { 
                    width: 70px !important; 
                    height: 70px !important; 
                    bottom: 6vh !important; 
                    right: 50% !important; 
                    transform: translateX(50%) !important; 
                    font-size: 0.55rem !important;
                    backdrop-filter: none !important;
                    -webkit-backdrop-filter: none !important;
                    background: rgba(14, 8, 20, 0.8) !important;
                }
            }'''

new_css = '''            /* Responsive Overrides for new layout */
            @media (max-width: 900px) {
                /* Hide things that truly don't fit */
                .hero-badge { display: none !important; }
                .vertical-text { display: none !important; }
                .pill-3 { display: none !important; }
                
                /* Keep the pills, but scale them down and arrange them better */
                .glass-pill { 
                    font-size: 0.55rem !important; 
                    padding: 8px 16px !important; 
                }
                .pill-1 { top: 12% !important; left: 5% !important; }
                .pill-2 { top: 18% !important; right: 5% !important; }
                
                /* Fix typography scaling */
                .hero-main-title { transform: translateY(-5vh) !important; }
                .hero-main-title h1 span { font-size: 16vw !important; }
                .hero-main-title h1 span:last-child { margin-top: -2vw !important; }
                .hero-main-title > div:first-child { font-size: 0.6rem !important; margin-bottom: 2vh !important; }
                .hero-main-title > div:last-child { font-size: 0.65rem !important; margin-top: 2vh !important; }
                
                /* Keep the description, but center it at the bottom */
                .hero-desc { 
                    display: block !important;
                    position: absolute !important; 
                    bottom: 18vh !important; 
                    left: 5vw !important; 
                    right: 5vw !important; 
                    max-width: 100% !important; 
                    text-align: center !important; 
                    border-left: none !important; 
                    border-top: 1px solid rgba(140, 45, 246, 0.5) !important; 
                    padding-left: 0 !important; 
                    padding-top: 15px !important; 
                }
                .hero-desc p { font-size: 0.75rem !important; }
                
                /* Center the scroll button */
                .hero-scroll-btn { 
                    width: 70px !important; 
                    height: 70px !important; 
                    bottom: 4vh !important; 
                    right: 50% !important; 
                    transform: translateX(50%) !important; 
                    font-size: 0.55rem !important;
                    backdrop-filter: none !important;
                    -webkit-backdrop-filter: none !important;
                    background: rgba(14, 8, 20, 0.8) !important;
                }
            }'''

# Check if old_css exactly matches to avoid failure
if old_css in content:
    content = content.replace(old_css, new_css)
else:
    # Use regex to do a fuzzy replace if whitespace differs slightly
    print("Warning: exact match failed, trying regex")
    content = re.sub(r'/\* Responsive Overrides for new layout \*/.*?\}\s*\}', new_css, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Mobile layout fixed!")
