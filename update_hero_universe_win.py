# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='replace') as f:
    content = f.read()

new_hero = '''    <!-- Another Universe UI-UX-PRO-MAX Hero -->
    <section class="bringer-hero-section" id="universe-hero" style="position: relative; width: 100%; min-height: 120vh; display: flex; flex-direction: column; align-items: center; justify-content: center; overflow: hidden; padding-top: 80px; padding-bottom: 10vh; margin: 0; background: #010103;">

        <!-- Universe Background Layers -->
        <div style="position: absolute; inset: 0; z-index: 1; pointer-events: none; overflow: hidden;">
            
            <!-- Massive Glowing Orbs (Aurora) -->
            <div style="position: absolute; top: -10%; left: 10%; width: 50vw; height: 50vw; min-width: 600px; min-height: 600px; background: radial-gradient(circle, rgba(140,45,246,0.25) 0%, transparent 60%); filter: blur(90px); animation: floatOrb 20s ease-in-out infinite alternate; mix-blend-mode: screen;"></div>
            
            <div style="position: absolute; bottom: -20%; right: 5%; width: 60vw; height: 60vw; min-width: 700px; min-height: 700px; background: radial-gradient(circle, rgba(64,15,138,0.35) 0%, transparent 60%); filter: blur(120px); animation: floatOrb 25s ease-in-out infinite alternate-reverse; mix-blend-mode: screen;"></div>

            <!-- Deep Starfield / Noise -->
            <div style="position: absolute; inset: 0; background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 400 400%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noise%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.9%22 numOctaves=%224%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noise)%22/%3E%3C/svg%3E'); opacity: 0.05; mix-blend-mode: color-dodge;"></div>
            
            <!-- Interactive Cursor Glow (Controlled via JS) -->
            <div id="universe-cursor-glow" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 30vw; height: 30vw; min-width: 400px; min-height: 400px; background: radial-gradient(circle, rgba(255,255,255,0.06) 0%, transparent 50%); filter: blur(50px); transition: opacity 0.5s ease; opacity: 0;"></div>
        </div>

        <!-- Giant Kinetic Marquee Typography (Background) -->
        <div style="position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%); z-index: 2; width: 300%; pointer-events: none; opacity: 0.12; mix-blend-mode: overlay;">
            <h1 style="font-family: 'Inter', sans-serif; font-size: 25vw; font-weight: 900; line-height: 0.8; margin: 0; white-space: nowrap; color: transparent; -webkit-text-stroke: 3px #fff; text-transform: uppercase; letter-spacing: -0.02em; animation: scrollText 50s linear infinite;">
                CREATIVITY &amp; INNOVATION &bull; CREATIVITY &amp; INNOVATION &bull; 
            </h1>
        </div>

        <!-- Floating Glassmorphism Core -->
        <div data-appear="zoom-in" data-delay="100" style="position: relative; z-index: 10; width: 92%; max-width: 900px; padding: 5rem 2rem; background: rgba(10, 5, 20, 0.35); border: 1px solid rgba(255,255,255,0.05); border-radius: 40px; backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px); box-shadow: 0 40px 80px rgba(0,0,0,0.8), inset 0 0 0 1px rgba(255,255,255,0.02); text-align: center; overflow: hidden;">
            
            <!-- Internal Glass Highlight -->
            <div style="position: absolute; top: 0; left: 10%; right: 10%; height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);"></div>

            <!-- Glowing Availability Pill -->
            <div style="display: inline-flex; align-items: center; gap: 12px; padding: 6px 18px; background: rgba(255,255,255,0.02); border: 1px solid rgba(140,45,246,0.4); border-radius: 100px; margin-bottom: 2.5rem; backdrop-filter: blur(10px);">
                <div style="width: 6px; height: 6px; background: #8C2DF6; border-radius: 50%; box-shadow: 0 0 12px #8C2DF6; animation: pulseCore 2s infinite;"></div>
                <span style="font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: 0.25em; font-size: 0.65rem; color: #e0c8ff; font-weight: 600;">System Online &mdash; Available</span>
            </div>
            
            <!-- Surreal Headline -->
            <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(3rem, 7vw, 6.5rem); font-weight: 500; line-height: 1.1; letter-spacing: -0.02em; color: #ffffff; margin-bottom: 1.5rem; text-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                Architect of the <br>
                <span style="font-style: italic; background: linear-gradient(135deg, #ffffff 0%, #8C2DF6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">digital universe.</span>
            </h1>
            
            <!-- Futuristic Subheadline -->
            <p style="font-family: 'Inter', sans-serif; font-size: clamp(1rem, 1.5vw, 1.15rem); color: rgba(255,255,255,0.6); max-width: 550px; margin: 0 auto 3.5rem; line-height: 1.7; font-weight: 300;">
                Fusing high-end UI/UX design with data-driven marketing to build immersive, conversion-focused digital experiences.
            </p>
            
            <!-- Ethereal CTAs -->
            <div style="display: flex; gap: 24px; align-items: center; justify-content: center; flex-wrap: wrap;">
                <a href="#cv-preview" onclick="document.getElementById('cv-preview').scrollIntoView({behavior: 'smooth'}); return false;" style="position: relative; background: linear-gradient(135deg, #8C2DF6, #5b10b3); color: #ffffff; padding: 18px 40px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.85rem; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 0.15em; overflow: hidden; transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1); box-shadow: 0 10px 30px rgba(140,45,246,0.4);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 20px 40px rgba(140,45,246,0.6)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(140,45,246,0.4)';">
                    <span style="position: relative; z-index: 2;">Initialize CV</span>
                </a>
                
                <a href="contacts.html" style="background: transparent; color: #ffffff; border: 1px solid rgba(255,255,255,0.2); padding: 18px 40px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.85rem; font-weight: 700; text-decoration: none; text-transform: uppercase; letter-spacing: 0.15em; transition: all 0.4s ease;" onmouseover="this.style.background='rgba(255,255,255,0.1)'; this.style.borderColor='rgba(255,255,255,0.4)';" onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(255,255,255,0.2)';">
                    Connect
                </a>
            </div>
        </div>

        <style>
            @keyframes floatOrb {
                0% { transform: translate(0, 0) scale(1); }
                33% { transform: translate(5%, 10%) scale(1.1); }
                66% { transform: translate(-5%, 5%) scale(0.9); }
                100% { transform: translate(0, 0) scale(1); }
            }
            @keyframes scrollText {
                0% { transform: translate(0, -50%); }
                100% { transform: translate(-50%, -50%); }
            }
            @keyframes pulseCore {
                0% { box-shadow: 0 0 0 0 rgba(140, 45, 246, 0.6); }
                70% { box-shadow: 0 0 0 8px rgba(140, 45, 246, 0); }
                100% { box-shadow: 0 0 0 0 rgba(140, 45, 246, 0); }
            }
        </style>
        <script>
            // Advanced Mouse follower for the universe hero
            document.addEventListener('DOMContentLoaded', () => {
                const hero = document.getElementById('universe-hero');
                const glow = document.getElementById('universe-cursor-glow');
                if(hero && glow) {
                    hero.addEventListener('mousemove', (e) => {
                        const rect = hero.getBoundingClientRect();
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        glow.style.opacity = '1';
                        // Center the glow orb on cursor
                        glow.style.left = x + 'px';
                        glow.style.top = y + 'px';
                        glow.style.transform = 'translate(-50%, -50%)';
                    });
                    hero.addEventListener('mouseleave', () => {
                        glow.style.opacity = '0';
                    });
                }
            });
        </script>
    </section>'''

# Regex to replace the hero
pattern = re.compile(r'<!-- Professional Premium Hero Section -->.*?</section>', re.DOTALL)
new_content = pattern.sub(new_hero, content, count=1)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(new_content)

print("Universe Hero Updated!")
