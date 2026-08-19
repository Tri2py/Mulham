# -*- coding: utf-8 -*-
import re

with open('portfolio-post03.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# We need to completely rewrite the <main> block.
new_main = '''    <main id="bringer-main">
        <!-- 10/10 Case Study Hero -->
        <section class="bringer-hero-section" style="position: relative; width: 100vw; min-height: 100dvh; overflow: hidden; background: #06020A; margin-left: calc(50% - 50vw); margin-top: -120px; display: flex; flex-direction: column; justify-content: flex-end; padding-bottom: 10vh;">
            
            <!-- Immersive Hero Background -->
            <div style="position: absolute; inset: 0; z-index: 1;">
                <img src="img/portfolio/portfolio03/slider01.jpg" alt="Gaming Power" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.4; filter: grayscale(100%) contrast(1.2);">
                <div style="position: absolute; inset: 0; background: linear-gradient(to top, #06020A 0%, rgba(6,2,10,0.8) 40%, transparent 100%);"></div>
            </div>

            <div class="stg-container" style="position: relative; z-index: 5;">
                <!-- Glass Metadata Pills -->
                <div style="display: flex; gap: 15px; margin-bottom: 4vh; flex-wrap: wrap;">
                    <div class="glass-pill" style="padding: 10px 20px; background: rgba(14,8,20,0.8); border: 1px solid rgba(140,45,246,0.3); border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #fff; letter-spacing: 0.15em; text-transform: uppercase;">Client: Xbox</div>
                    <div class="glass-pill" style="padding: 10px 20px; background: rgba(14,8,20,0.8); border: 1px solid rgba(140,45,246,0.3); border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #fff; letter-spacing: 0.15em; text-transform: uppercase;">Role: UI/UX & Strategy</div>
                    <div class="glass-pill" style="padding: 10px 20px; background: rgba(14,8,20,0.8); border: 1px solid rgba(140,45,246,0.3); border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.75rem; color: #fff; letter-spacing: 0.15em; text-transform: uppercase;">Year: 2026</div>
                </div>

                <!-- Massive Title -->
                <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(4rem, 10vw, 8rem); font-weight: 400; font-style: italic; letter-spacing: -0.03em; color: #ffffff; line-height: 1; margin: 0; text-shadow: 0 10px 40px rgba(0,0,0,0.8);">Gaming <br><span style="font-family: 'Inter', sans-serif; font-weight: 900; font-style: normal; letter-spacing: -0.05em; color: #8C2DF6;">POWER.</span></h1>
            </div>
        </section>

        <div class="stg-container" style="padding-top: 10vh; padding-bottom: 10vh;">
            <!-- The Overview -->
            <div class="stg-row stg-bottom-gap-l" style="margin-bottom: 15vh;">
                <div class="stg-col-4">
                    <h2 style="font-family: 'Inter', sans-serif; font-size: 1rem; font-weight: 600; letter-spacing: 0.3em; text-transform: uppercase; color: #8C2DF6;">The Overview</h2>
                </div>
                <div class="stg-col-8">
                    <p style="font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 3vw, 2.5rem); line-height: 1.4; color: #fff; font-style: italic; text-wrap: balance;">Dive into the electrifying journey where strategic gameplay and creative firepower elevated the platform to the pinnacle of the gaming arena.</p>
                </div>
            </div>

            <!-- Massive Image Break -->
            <div style="width: 100%; border-radius: 30px; overflow: hidden; margin-bottom: 15vh; border: 1px solid rgba(140,45,246,0.2); box-shadow: 0 20px 60px rgba(0,0,0,0.5);">
                <img src="img/portfolio/portfolio03/slider02.jpg" alt="Gameplay UI" style="width: 100%; height: auto; display: block; filter: contrast(1.1);">
            </div>

            <!-- The Strategy Bento Grid -->
            <div class="stg-row" style="margin-bottom: 15vh;">
                <div class="stg-col-4">
                    <h2 style="font-family: 'Inter', sans-serif; font-size: 1rem; font-weight: 600; letter-spacing: 0.3em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 4vh;">The Strategy</h2>
                </div>
                <div class="stg-col-8">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                        <div style="background: rgba(14,8,20,0.6); border: 1px solid rgba(140,45,246,0.15); padding: 40px; border-radius: 20px; box-shadow: inset 0 0 30px rgba(140,45,246,0.05);">
                            <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; font-weight: 600; letter-spacing: -0.03em; margin-bottom: 15px; color: #fff;">01. Immersion</h3>
                            <p style="color: rgba(255,255,255,0.6); line-height: 1.6; text-wrap: balance;">Creating a fluid interface that disappears, letting the gameplay dominate the screen.</p>
                        </div>
                        <div style="background: rgba(14,8,20,0.6); border: 1px solid rgba(140,45,246,0.15); padding: 40px; border-radius: 20px; box-shadow: inset 0 0 30px rgba(140,45,246,0.05); transform: translateY(30px);">
                            <h3 style="font-family: 'Inter', sans-serif; font-size: 1.5rem; font-weight: 600; letter-spacing: -0.03em; margin-bottom: 15px; color: #fff;">02. Velocity</h3>
                            <p style="color: rgba(255,255,255,0.6); line-height: 1.6; text-wrap: balance;">Optimizing every micro-interaction to respond under 16ms for elite players.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
'''

content = re.sub(r'<main id="bringer-main">.*?(?=<!-- Footer -->)', new_main, content, flags=re.DOTALL)

# Grab the premium footer from index.html
with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    index_html = f.read()
    
match = re.search(r'<!-- Premium 10/10 Footer -->.*?</main>', index_html, flags=re.DOTALL)
if match:
    premium_footer = match.group(0).replace('</main>', '')
    content = re.sub(r'<!-- Footer -->.*?</footer>', premium_footer, content, flags=re.DOTALL)

with open('portfolio-post03.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Case study 10/10 deployed!")
