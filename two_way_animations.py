# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Strip the built-in one-way animation attributes to avoid conflicts
content = re.sub(r'data-appear="[^"]*"', '', content)
content = re.sub(r'data-stagger-appear="[^"]*"', '', content)
content = re.sub(r'data-unload="[^"]*"', '', content)
content = re.sub(r'data-delay="[^"]*"', '', content)
content = re.sub(r'data-stagger-delay="[^"]*"', '', content)

# 2. Inject the custom two-way CSS & JS
two_way_script = '''
    <!-- Two-Way Scroll Reveal Engine -->
    <style>
        .two-way-reveal {
            opacity: 0 !important;
            transform: translateY(50px) scale(0.98) !important;
            transition: opacity 0.7s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.7s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
            will-change: opacity, transform;
        }
        .two-way-reveal.is-visible {
            opacity: 1 !important;
            transform: translateY(0) scale(1) !important;
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Select elements we want to animate (everything outside the hero)
            const targets = document.querySelectorAll('section:not(#awwwards-hero) h2, section:not(#awwwards-hero) h5, section:not(#awwwards-hero) p, .bringer-block, .bringer-timeline-item, .cv-preview-section');
            
            // Add the base class
            targets.forEach(el => el.classList.add('two-way-reveal'));

            // Setup Intersection Observer
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                    } else {
                        // The magic line that makes it animate when scrolling UP too
                        entry.target.classList.remove('is-visible');
                    }
                });
            }, { 
                threshold: 0.15,
                rootMargin: "0px 0px -50px 0px"
            });

            targets.forEach(el => observer.observe(el));
        });
    </script>
</body>
'''

content = content.replace('</body>', two_way_script)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Two-way animations injected.")
