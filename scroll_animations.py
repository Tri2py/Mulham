# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

scroll_script = '''
    <!-- Advanced Scroll Animations Injection -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // 1. Create a Premium Scroll Progress Bar
            const progressBar = document.createElement('div');
            progressBar.style.position = 'fixed';
            progressBar.style.top = '0';
            progressBar.style.left = '0';
            progressBar.style.height = '3px';
            progressBar.style.width = '0%';
            progressBar.style.background = 'linear-gradient(90deg, #8C2DF6, #e0c8ff)';
            progressBar.style.zIndex = '999999';
            progressBar.style.boxShadow = '0 0 10px #8C2DF6';
            progressBar.style.transition = 'width 0.1s ease-out';
            document.body.appendChild(progressBar);

            // 2. Select elements for continuous parallax & scroll animations
            const parallaxBlocks = document.querySelectorAll('.bringer-masked-media, .bringer-parallax-media, .cv-preview-section');
            const skewBlocks = document.querySelectorAll('h2, .bringer-block');
            
            let lastScrollY = window.scrollY;
            let ticking = false;

            const updateScroll = () => {
                const currentScrollY = window.scrollY;
                const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                
                // Update Progress Bar
                if (docHeight > 0) {
                    const scrollPercent = (currentScrollY / docHeight) * 100;
                    progressBar.style.width = scrollPercent + '%';
                }

                // Calculate Scroll Velocity
                const velocity = currentScrollY - lastScrollY;
                const skew = Math.max(-3, Math.min(3, velocity * 0.02)); // Subtle skew

                // Apply Parallax and Skew
                parallaxBlocks.forEach(block => {
                    const rect = block.getBoundingClientRect();
                    // Check if in viewport
                    if (rect.top < window.innerHeight && rect.bottom > 0) {
                        const offset = (rect.top - window.innerHeight / 2) * 0.1;
                        
                        // If it's a background element, shift the background
                        if (block.hasAttribute('data-bg-src')) {
                            block.style.backgroundPositionY = \calc(50% + \px)\;
                        }
                    }
                });

                skewBlocks.forEach(block => {
                    const rect = block.getBoundingClientRect();
                    if (rect.top < window.innerHeight && rect.bottom > 0) {
                        // Apply subtle velocity skew to texts and cards
                        block.style.transform = \skewY(\deg)\;
                        block.style.transition = 'transform 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)';
                    }
                });

                lastScrollY = currentScrollY;
                ticking = false;
                
                // Return skew to 0 after scrolling stops
                setTimeout(() => {
                    if (window.scrollY === lastScrollY) {
                        skewBlocks.forEach(b => b.style.transform = 'skewY(0deg)');
                    }
                }, 100);
            };

            window.addEventListener('scroll', () => {
                if (!ticking) {
                    window.requestAnimationFrame(updateScroll);
                    ticking = true;
                }
            });
            
            // Initial call
            updateScroll();
        });
    </script>
</body>
'''

# Inject right before </body>
content = content.replace('</body>', scroll_script)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Scroll animations injected.")
