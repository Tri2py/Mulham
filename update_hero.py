# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_hero = '''    <!-- Avant-Garde Asymmetrical Hero Section -->
    <section class="bringer-hero-section" style="position: relative; width: 100vw; min-height: 120vh; display: flex; align-items: center; justify-content: center; overflow: hidden; margin-left: calc(50% - 50vw); margin-top: -120px; margin-bottom: 10vh; padding-top: 120px; background: #000;">

        <!-- Deep Ambient Glows -->
        <div style="position: absolute; top: 10%; left: -10%; width: 50vw; height: 50vw; background: radial-gradient(circle, rgba(140,45,246,0.3) 0%, transparent 70%); filter: blur(80px); opacity: 0.6; mix-blend-mode: screen; pointer-events: none;"></div>
        <div style="position: absolute; bottom: 0%; right: -10%; width: 60vw; height: 60vw; background: radial-gradient(circle, rgba(140,45,246,0.2) 0%, transparent 70%); filter: blur(100px); opacity: 0.5; mix-blend-mode: screen; pointer-events: none;"></div>
        
        <!-- Subtle Grain Overlay -->
        <div style="position: absolute; inset: 0; background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.85%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E'); opacity: 0.05; pointer-events: none; mix-blend-mode: overlay; z-index: 2;"></div>

        <!-- Floating Gallery Cards (Abstract Imagery) -->
        <!-- Card 1: Top Right -->
        <div style="position: absolute; top: 15%; right: 10%; width: 22vw; height: 32vw; max-width: 320px; max-height: 450px; z-index: 4; border-radius: 12px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.8); animation: float1 14s ease-in-out infinite;">
            <div class="bringer-parallax-media" style="width: 100%; height: 100%;">
                <img src="img/home/services_abstract_violet.jpg" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.9;" alt="Creative">
                <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%); mix-blend-mode: overlay;"></div>
            </div>
        </div>
        
        <!-- Card 2: Bottom Left -->
        <div style="position: absolute; bottom: 10%; left: 8%; width: 28vw; height: 20vw; max-width: 450px; max-height: 300px; z-index: 10; border-radius: 12px; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.8); animation: float2 18s ease-in-out infinite reverse;">
            <div class="bringer-parallax-media" style="width: 100%; height: 100%;">
                <img src="img/home/services_digital_fluid.jpg" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.85;" alt="Digital">
                <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(140,45,246,0.3) 0%, rgba(0,0,0,0) 100%);"></div>
            </div>
        </div>

        <!-- Massive Asymmetrical Typography -->
        <div style="position: relative; z-index: 5; width: 100%; max-width: 1600px; padding: 0 5vw; pointer-events: none;">
            
            <!-- Top text -->
            <div style="display: flex; justify-content: flex-start; margin-bottom: -5vw;" data-appear="fade-right">
                <h1 style="font-family: 'Inter', sans-serif; font-size: clamp(5rem, 15vw, 18rem); font-weight: 800; line-height: 0.85; letter-spacing: -0.05em; color: #fff; margin: 0; text-transform: uppercase;">
                    Unleash
                </h1>
            </div>
            
            <!-- Middle italic text -->
            <div style="display: flex; justify-content: center; margin-bottom: -4vw;" data-appear="fade-up" data-delay="200">
                <span style="font-family: 'Playfair Display', serif; font-size: clamp(2rem, 5vw, 6.5rem); font-weight: 400; font-style: italic; color: rgba(255,255,255,0.7); position: relative; z-index: 6;">
                    the absolute limits of
                </span>
            </div>
            
            <!-- Bottom text -->
            <div style="display: flex; justify-content: flex-end;" data-appear="fade-left" data-delay="400">
                <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(5rem, 16vw, 19rem); font-weight: 500; line-height: 0.85; letter-spacing: -0.02em; margin: 0; background: linear-gradient(135deg, #ffffff 0%, #8C2DF6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    Creativity.
                </h1>
            </div>
        </div>

        <!-- Interactive Scroll Badge -->
        <div data-appear="zoom-in" data-delay="800" style="position: absolute; bottom: 6vh; left: 50%; transform: translateX(-50%); z-index: 20; width: 150px; height: 150px; display: flex; align-items: center; justify-content: center; cursor: pointer; border-radius: 50%; mix-blend-mode: difference;" onclick="window.scrollBy({top: window.innerHeight * 0.9, behavior: 'smooth'})">
            <div style="position: absolute; inset: 0; animation: spin-slow 12s linear infinite; pointer-events: none;">
                <svg viewBox="0 0 100 100" width="100%" height="100%">
                    <defs><path id="circlePath2" d="M 50, 50 m -35, 0 a 35,35 0 1,1 70,0 a 35,35 0 1,1 -70,0" /></defs>
                    <text style="font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.22em; fill: #fff;">
                        <textPath href="#circlePath2" startOffset="0%">SCROLL TO EXPLORE &#8226; SCROLL TO EXPLORE &#8226; </textPath>
                    </text>
                </svg>
            </div>
            <div style="width: 8px; height: 8px; background: #fff; border-radius: 50%;"></div>
        </div>

        <style>
            @keyframes spin-slow {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            @keyframes float1 {
                0%, 100% { transform: translateY(0) rotate(-3deg); }
                50% { transform: translateY(-50px) rotate(2deg); }
            }
            @keyframes float2 {
                0%, 100% { transform: translateY(0) rotate(3deg); }
                50% { transform: translateY(-40px) rotate(-2deg); }
            }
        </style>
    </section>'''

# Regex to replace everything from <!-- Massive Creative Hero Section --> down to </section> before Selected Works
pattern = re.compile(r'<!-- Massive Creative Hero Section -->.*?</section>', re.DOTALL)
new_content = pattern.sub(new_hero, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Hero Updated!")
