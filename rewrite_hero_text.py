# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

find_block = re.search(r'<div class="hero-blend-text".*?Explore\s*</a>', content, re.DOTALL)

if find_block:
    new_hero_html = '''<div class="hero-blend-text" style="position: absolute; inset: 0; display: flex; flex-direction: column; justify-content: center; align-items: center; pointer-events: none; z-index: 10;">
            
            <!-- Rotating Badge (Top Right) -->
            <div class="hero-badge" style="position: absolute; top: 15vh; right: 8vw; width: 140px; height: 140px; animation: spinBadge 20s linear infinite;">
                <svg viewBox="0 0 100 100" width="100%" height="100%">
                    <path id="circlePath" d="M 50, 50 m -35, 0 a 35,35 0 1,1 70,0 a 35,35 0 1,1 -70,0" fill="transparent" />
                    <text fill="rgba(255,255,255,0.7)" font-size="10.5" font-family="'Inter', sans-serif" font-weight="600" letter-spacing="0.15em">
                        <textPath href="#circlePath">CREATIVE DEVELOPER + UI/UX DESIGNER +</textPath>
                    </text>
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 24px; color: #8C2DF6;">+</div>
            </div>

            <!-- Vertical Editorial Text (Left) -->
            <div class="vertical-text" style="position: absolute; left: 4vw; top: 50%; transform: translateY(-50%) rotate(-90deg); transform-origin: left center; font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.3em; color: rgba(255,255,255,0.4); white-space: nowrap;">
                EST. 2026 - Damascus, Syria - Available Worldwide
            </div>

            <!-- Main Typography -->
            <div class="hero-main-title" style="text-align: center; position: relative; z-index: 5;">
                <div style="font-family: 'Inter', sans-serif; font-size: clamp(0.7rem, 1vw, 1rem); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5em; color: #8C2DF6; margin-bottom: 2vh; text-shadow: 0 0 20px rgba(140,45,246,0.5);">
                    Independent
                </div>
                
                <h1 style="margin: 0; line-height: 1.1; display: flex; flex-direction: column; align-items: center;">
                    <span style="font-family: 'Inter', sans-serif; font-size: clamp(4rem, 9vw, 8rem); font-weight: 900; letter-spacing: -0.04em; color: #ffffff; text-shadow: 0 10px 40px rgba(0,0,0,0.8);">MULHAM</span>
                    <span style="font-family: 'Playfair Display', serif; font-size: clamp(4.5rem, 10vw, 9rem); font-weight: 400; font-style: italic; letter-spacing: -0.02em; color: #ffffff; text-shadow: 0 10px 40px rgba(0,0,0,0.8); margin-top: -2vw;">IBRAHIM</span>
                </h1>
                
                <div style="font-family: 'Inter', sans-serif; font-size: clamp(0.8rem, 1.1vw, 1.2rem); font-weight: 400; text-transform: uppercase; letter-spacing: 0.3em; color: rgba(255,255,255,0.8); margin-top: 3vh;">
                    Digital Experience Architect
                </div>
            </div>

            <!-- Floating Glass Pills -->
            <div class="glass-pill pill-1" style="position: absolute; top: 25%; left: 15%; animation: floatPill1 8s ease-in-out infinite alternate;">
                [ Front-End Engineering ]
            </div>
            <div class="glass-pill pill-2" style="position: absolute; bottom: 35%; right: 12%; animation: floatPill2 10s ease-in-out infinite alternate;">
                [ Brand Identity ]
            </div>
            <div class="glass-pill pill-3" style="position: absolute; bottom: 25%; left: 22%; animation: floatPill3 12s ease-in-out infinite alternate;">
                [ UI/UX Design ]
            </div>

            <!-- Editorial Description -->
            <div class="hero-desc" style="position: absolute; bottom: 15vh; left: 6vw; max-width: 280px; text-align: left; border-left: 2px solid #8C2DF6; padding-left: 20px;">
                <p style="font-family: 'Inter', sans-serif; font-size: 0.8rem; font-weight: 400; line-height: 1.6; color: rgba(255,255,255,0.7); margin: 0; text-shadow: 0 2px 10px rgba(0,0,0,0.8);">
                    Bridging the gap between highly aesthetic design and robust engineering. I build digital products that leave a lasting impression.
                </p>
            </div>
            
        </div>

        <!-- Interactive Scroll Button -->
        <a href="#about" onclick="document.getElementById('about').scrollIntoView({behavior: 'smooth'}); return false;" class="hero-scroll-btn" style="position: absolute; bottom: 8vh; right: 5vw; z-index: 20; width: 100px; height: 100px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.15); display: flex; align-items: center; justify-content: center; color: #fff; text-decoration: none; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1); font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; background: rgba(255,255,255,0.03);">
            Explore
        </a>'''

    content = content.replace(find_block.group(0), new_hero_html)

    css_addition = '''
            /* New Hero Elements CSS */
            @keyframes spinBadge { 100% { transform: rotate(360deg); } }
            
            .glass-pill {
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
            }

            @keyframes floatPill1 { 0% { transform: translateY(0) rotate(-4deg); } 100% { transform: translateY(-25px) rotate(4deg); } }
            @keyframes floatPill2 { 0% { transform: translateY(0) rotate(3deg); } 100% { transform: translateY(20px) rotate(-3deg); } }
            @keyframes floatPill3 { 0% { transform: translateY(0) rotate(-2deg); } 100% { transform: translateY(-15px) rotate(5deg); } }
            
            /* Responsive Overrides for new layout */
            @media (max-width: 900px) {
                .hero-badge { display: none !important; }
                .vertical-text { display: none !important; }
                .glass-pill { display: none !important; }
                .hero-desc { display: none !important; }
                .hero-main-title h1 span { font-size: 15vw !important; }
                .hero-main-title h1 span:last-child { margin-top: 0 !important; }
                .hero-scroll-btn { width: 80px !important; height: 80px !important; bottom: 4vh !important; }
            }
'''
    
    style_idx = content.find('/* The image track styles */')
    if style_idx != -1:
        content = content[:style_idx] + css_addition + content[style_idx:]

    content = re.sub(r'\.hero-blend-text h1:first-of-type {.*?}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.hero-blend-text h1:last-of-type {.*?}', '', content, flags=re.DOTALL)
    content = re.sub(r'\.hero-blend-text > div:first-child.*?}', '', content, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='windows-1252') as f:
        f.write(content)
        print("Successfully rebuilt the hero typography and elements!")
else:
    print("Could not find the block to replace.")

