# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

old_css = '''            /* Responsive Overrides for new layout */
            @media (max-width: 900px) {
                .hero-badge { display: none !important; }
                .vertical-text { display: none !important; }
                .glass-pill { display: none !important; }
                .hero-desc { display: none !important; }
                .hero-main-title h1 span { font-size: 15vw !important; }
                .hero-main-title h1 span:last-child { margin-top: 0 !important; }
                .hero-scroll-btn { width: 80px !important; height: 80px !important; bottom: 4vh !important; }
            }'''

new_css = '''            /* Responsive Overrides for new layout */
            @media (max-width: 900px) {
                /* Hide things that truly don't fit */
                .hero-badge { display: none !important; }
                .vertical-text { display: none !important; }
                
                /* Keep the pills, but scale them down and arrange them better */
                .glass-pill { 
                    font-size: 0.55rem !important; 
                    padding: 8px 16px !important; 
                    backdrop-filter: blur(5px) !important;
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
                }

                /* Fix curtain corner radius for mobile */
                .page-content-wrapper {
                    border-top-left-radius: 30px !important;
                    border-top-right-radius: 30px !important;
                    padding-top: 8vh !important;
                }
            }'''

if old_css in content:
    content = content.replace(old_css, new_css)
    with open('index.html', 'w', encoding='windows-1252') as f:
        f.write(content)
    print("Fixed mobile layout in index.html!")
else:
    print("Could not find the old CSS block.")
