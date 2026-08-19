# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Regex to match the old colorized line background block
bg_regex = re.compile(r'<div class="colorized-line-bg".*?</div>\s*<!-- Foreground Difference Text Overlay -->', re.DOTALL)

new_bg = '''<!-- Ambient Universe Background -->
        <div class="ambient-universe-bg" style="position: absolute; inset: 0; overflow: hidden; background: #000000; z-index: 1;">
            
            <!-- Subtle Tech Grid -->
            <div style="position: absolute; inset: 0; background-size: 100px 100px; background-image: linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px), linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px); z-index: 1;"></div>
            
            <!-- Ambient Drifting Orbs -->
            <div class="orb orb-1"></div>
            <div class="orb orb-2"></div>
            <div class="orb orb-3"></div>

            <!-- Floating Sparkles / Stars -->
            <div id="hero-particles" style="position: absolute; inset: 0; z-index: 2;"></div>

            <style>
                .orb {
                    position: absolute;
                    border-radius: 50%;
                    filter: blur(90px);
                    animation: drift ease-in-out infinite alternate;
                    pointer-events: none;
                }
                .orb-1 {
                    width: 45vw; height: 45vw;
                    background: rgba(140, 45, 246, 0.25);
                    top: -15%; left: -10%;
                    animation-duration: 20s;
                }
                .orb-2 {
                    width: 35vw; height: 35vw;
                    background: rgba(80, 20, 150, 0.35);
                    bottom: -15%; right: -10%;
                    animation-duration: 25s;
                    animation-delay: -7s;
                }
                .orb-3 {
                    width: 30vw; height: 30vw;
                    background: rgba(255, 255, 255, 0.04);
                    top: 30%; left: 35%;
                    animation-duration: 22s;
                    animation-delay: -12s;
                }

                @keyframes drift {
                    0% { transform: translate(0, 0) scale(1); }
                    100% { transform: translate(8vw, 6vh) scale(1.15); }
                }

                .hero-particle {
                    position: absolute;
                    border-radius: 50%;
                    opacity: 0;
                    animation: floatUp linear infinite;
                    pointer-events: none;
                }

                @keyframes floatUp {
                    0% { transform: translateY(110vh) scale(0.8); opacity: 0; }
                    10% { opacity: 0.8; }
                    80% { opacity: 0.8; }
                    100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
                }
            </style>
            <script>
                document.addEventListener('DOMContentLoaded', () => {
                    const container = document.getElementById('hero-particles');
                    if (!container) return;
                    const particleCount = 45;
                    for(let i=0; i<particleCount; i++) {
                        let p = document.createElement('div');
                        p.className = 'hero-particle';
                        let size = Math.random() * 2.5 + 0.5; // 0.5px to 3px
                        p.style.width = size + 'px';
                        p.style.height = size + 'px';
                        p.style.left = Math.random() * 100 + 'vw';
                        p.style.animationDuration = (Math.random() * 20 + 15) + 's'; // 15s to 35s
                        p.style.animationDelay = -(Math.random() * 35) + 's'; // start already on screen
                        
                        // Color variation
                        if (Math.random() > 0.85) {
                            p.style.background = '#8C2DF6';
                            p.style.boxShadow = '0 0 8px #8C2DF6';
                        } else {
                            p.style.background = '#ffffff';
                            p.style.boxShadow = '0 0 6px rgba(255,255,255,0.6)';
                        }
                        
                        container.appendChild(p);
                    }
                });
            </script>
        </div>

        <!-- Foreground Difference Text Overlay -->'''

if bg_regex.search(content):
    content = bg_regex.sub(new_bg, content, count=1)
    with open('index.html', 'w', encoding='windows-1252') as f:
        f.write(content)
    print("Successfully enhanced the hero background!")
else:
    print("Could not find the colorized-line-bg block.")

