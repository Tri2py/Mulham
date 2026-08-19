# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Remove the broken script
import re
content = re.sub(r'<!-- Advanced Scroll Animations Injection -->.*</body>', '</body>', content, flags=re.DOTALL)

# Inject the clean script
clean_script = '''
    <!-- Advanced Scroll Animations Injection -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // 1. Create a Premium Scroll Progress Bar
            const progressBar = document.createElement('div');
            progressBar.style.position = 'fixed';
            progressBar.style.top = '0';
            progressBar.style.left = '0';
            progressBar.style.height = '4px';
            progressBar.style.width = '0%';
            progressBar.style.background = 'linear-gradient(90deg, #8C2DF6, #e0c8ff)';
            progressBar.style.zIndex = '999999';
            progressBar.style.boxShadow = '0 0 15px rgba(140, 45, 246, 0.8)';
            progressBar.style.transition = 'width 0.1s ease-out';
            document.body.appendChild(progressBar);

            // 2. Select elements for continuous parallax & scroll animations
            const parallaxBlocks = document.querySelectorAll('.bringer-masked-media, .bringer-parallax-media');
            const skewBlocks = document.querySelectorAll('h2, .bringer-block');
            
            let lastScrollY = window.scrollY;
            let ticking = false;
            let scrollTimeout;

            const updateScroll = function() {
                const currentScrollY = window.scrollY;
                const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                
                // Update Progress Bar
                if (docHeight > 0) {
                    const scrollPercent = (currentScrollY / docHeight) * 100;
                    progressBar.style.width = scrollPercent + '%';
                }

                // Calculate Scroll Velocity
                const velocity = currentScrollY - lastScrollY;
                const skew = Math.max(-2.5, Math.min(2.5, velocity * 0.015)); // Extremely smooth subtle skew

                // Apply Parallax to background images
                parallaxBlocks.forEach(function(block) {
                    const rect = block.getBoundingClientRect();
                    if (rect.top < window.innerHeight && rect.bottom > 0) {
                        const offset = (rect.top - window.innerHeight / 2) * 0.15;
                        if (block.hasAttribute('data-bg-src')) {
                            block.style.backgroundPositionY = "calc(50% + " + offset + "px)";
                        }
                    }
                });

                // Apply Velocity Skew to text and cards
                skewBlocks.forEach(function(block) {
                    const rect = block.getBoundingClientRect();
                    if (rect.top < window.innerHeight && rect.bottom > 0) {
                        block.style.transform = "skewY(" + skew + "deg)";
                        block.style.transition = 'transform 0.2s cubic-bezier(0.165, 0.84, 0.44, 1)';
                    }
                });

                lastScrollY = currentScrollY;
                ticking = false;
                
                // Reset skew when scrolling stops
                clearTimeout(scrollTimeout);
                scrollTimeout = setTimeout(function() {
                    skewBlocks.forEach(function(b) {
                        b.style.transform = 'skewY(0deg)';
                    });
                }, 50);
            };

            window.addEventListener('scroll', function() {
                if (!ticking) {
                    window.requestAnimationFrame(updateScroll);
                    ticking = true;
                }
            });
            
            updateScroll();
        });
    </script>
</body>
'''

content = content.replace('</body>', clean_script)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Clean scroll script injected.")
