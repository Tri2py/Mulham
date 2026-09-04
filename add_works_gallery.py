"""Add Works Gallery section to home.html, replacing the removed Selected Works comment."""

import os

FILE = os.path.join(os.path.dirname(__file__), 'home.html')

with open(FILE, 'r', encoding='cp1252') as f:
    content = f.read()

TARGET = '<!-- Section: Selected Works temporarily removed per user request -->'

REPLACEMENT = '''<!-- Section: Works Gallery -->
            <section id="works-gallery" style="margin-top: 2vh; margin-bottom: 12vh; position: relative;">
                <!-- Section Title -->
                <div class="stg-row bringer-section-title" style="margin-bottom: 48px;">
                    <div class="stg-col-8">
                        <h2 style="font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 24px;">
                            Selected <span style="font-style: italic; color: var(--bringer-s-text);">Works</span>
                        </h2>
                        <p class="bringer-large-text" style="color: rgba(255,255,255,0.7); font-weight: 400; text-wrap: balance; line-height: 1.6;">A curated collection of projects across web development, branding, and digital design.</p>
                    </div>
                </div>

                <!-- Filter Tabs -->
                <div style="display: flex; gap: 12px; margin-bottom: 40px; flex-wrap: wrap;">
                    <button class="works-filter-btn active" data-filter="all" style="background: rgba(140, 45, 246, 0.2); border: 1px solid rgba(140, 45, 246, 0.4); color: #fff; padding: 10px 24px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 500; cursor: pointer; transition: all 0.3s ease;">All</button>
                    <button class="works-filter-btn" data-filter="web" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.6); padding: 10px 24px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 500; cursor: pointer; transition: all 0.3s ease;">Web</button>
                    <button class="works-filter-btn" data-filter="branding" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.6); padding: 10px 24px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 500; cursor: pointer; transition: all 0.3s ease;">Branding</button>
                    <button class="works-filter-btn" data-filter="design" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); color: rgba(255,255,255,0.6); padding: 10px 24px; border-radius: 100px; font-family: 'Inter', sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 500; cursor: pointer; transition: all 0.3s ease;">Design</button>
                </div>

                <!-- Works Masonry Grid -->
                <div class="works-gallery-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">

                    <!-- Work Item 1 - tall -->
                    <div class="works-item" data-category="web" style="grid-row: span 2; position: relative; border-radius: 20px; overflow: hidden; cursor: pointer;">
                        <img src="img/home/hero_creative_1.jpg" alt="Web Development Project" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 32px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Web Development</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 500; color: #fff; margin: 0 0 8px 0;">Corporate Platform</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">Full-stack web application with modern UI/UX</p>
                        </div>
                    </div>

                    <!-- Work Item 2 -->
                    <div class="works-item" data-category="branding" style="position: relative; border-radius: 20px; overflow: hidden; cursor: pointer; aspect-ratio: 4/3;">
                        <img src="img/home/services_branding.jpg" alt="Branding Project" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Branding</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 500; color: #fff; margin: 0 0 6px 0;">Brand Identity System</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">Complete visual identity and brand guidelines</p>
                        </div>
                    </div>

                    <!-- Work Item 3 -->
                    <div class="works-item" data-category="design" style="position: relative; border-radius: 20px; overflow: hidden; cursor: pointer; aspect-ratio: 4/3;">
                        <img src="img/home/hero_creative_3.jpg" alt="Creative Design" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Design</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 500; color: #fff; margin: 0 0 6px 0;">Creative Direction</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">Art direction and visual storytelling</p>
                        </div>
                    </div>

                    <!-- Work Item 4 -->
                    <div class="works-item" data-category="web" style="position: relative; border-radius: 20px; overflow: hidden; cursor: pointer; aspect-ratio: 16/10;">
                        <img src="img/home/services_web.jpg" alt="Web Engineering" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Web Development</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 500; color: #fff; margin: 0 0 6px 0;">Interactive Web App</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">High-performance responsive web application</p>
                        </div>
                    </div>

                    <!-- Work Item 5 -->
                    <div class="works-item" data-category="design" style="position: relative; border-radius: 20px; overflow: hidden; cursor: pointer; aspect-ratio: 16/10;">
                        <img src="img/home/hero_creative_4.jpg" alt="Digital Design" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Design</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 500; color: #fff; margin: 0 0 6px 0;">Digital Experience</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">Immersive digital design and interaction</p>
                        </div>
                    </div>

                    <!-- Work Item 6 - tall -->
                    <div class="works-item" data-category="branding" style="grid-row: span 2; position: relative; border-radius: 20px; overflow: hidden; cursor: pointer;">
                        <img src="img/home/hero_creative_2.jpg" alt="Branding Work" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 32px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Branding</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 500; color: #fff; margin: 0 0 8px 0;">Visual Identity</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">Brand strategy and identity design</p>
                        </div>
                    </div>

                    <!-- Work Item 7 -->
                    <div class="works-item" data-category="web" style="position: relative; border-radius: 20px; overflow: hidden; cursor: pointer; aspect-ratio: 4/3;">
                        <img src="img/home/services_marketing.jpg" alt="Marketing Platform" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Web Development</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 500; color: #fff; margin: 0 0 6px 0;">Marketing Platform</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">Data-driven digital marketing solution</p>
                        </div>
                    </div>

                    <!-- Work Item 8 -->
                    <div class="works-item" data-category="design" style="position: relative; border-radius: 20px; overflow: hidden; cursor: pointer; aspect-ratio: 4/3;">
                        <img src="img/home/services_digital_fluid.jpg" alt="Digital Fluid Design" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);" loading="lazy">
                        <div class="works-item-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0) 50%); display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; opacity: 0; transition: opacity 0.4s ease;">
                            <span style="color: #8C2DF6; font-size: 11px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 600; margin-bottom: 8px;">Design</span>
                            <h4 style="font-family: 'Playfair Display', serif; font-size: 1.3rem; font-weight: 500; color: #fff; margin: 0 0 6px 0;">Fluid Aesthetics</h4>
                            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; line-height: 1.5; margin: 0;">Abstract visual design and creative exploration</p>
                        </div>
                    </div>

                </div><!-- .works-gallery-grid -->

                <!-- View All CTA -->
                <div style="text-align: center; margin-top: 56px;">
                    <a href="/portfolio" style="display: inline-flex; align-items: center; gap: 12px; padding: 16px 40px; border: 1px solid rgba(140, 45, 246, 0.4); border-radius: 100px; color: #fff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 500; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); background: rgba(140, 45, 246, 0.08);">
                        View All Works
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </a>
                </div>

                <!-- Works Gallery Styles & Interactions -->
                <style>
                    /* Hover effects */
                    .works-item:hover img {
                        transform: scale(1.05);
                    }
                    .works-item:hover .works-item-overlay {
                        opacity: 1 !important;
                    }

                    /* Filter button states */
                    .works-filter-btn:hover {
                        background: rgba(140, 45, 246, 0.15) !important;
                        border-color: rgba(140, 45, 246, 0.3) !important;
                        color: #fff !important;
                    }
                    .works-filter-btn.active {
                        background: rgba(140, 45, 246, 0.2) !important;
                        border-color: rgba(140, 45, 246, 0.4) !important;
                        color: #fff !important;
                    }

                    /* View All CTA hover */
                    section#works-gallery a[href="/portfolio"]:hover {
                        background: rgba(140, 45, 246, 0.2) !important;
                        border-color: rgba(140, 45, 246, 0.6) !important;
                        transform: translateY(-2px);
                        box-shadow: 0 8px 30px rgba(140, 45, 246, 0.2);
                    }

                    /* Filtered-out items */
                    .works-item.hidden {
                        display: none;
                    }

                    /* Responsive: 2 columns on tablet */
                    @media (max-width: 1024px) {
                        .works-gallery-grid {
                            grid-template-columns: repeat(2, 1fr) !important;
                        }
                    }
                    /* Responsive: 1 column on mobile */
                    @media (max-width: 600px) {
                        .works-gallery-grid {
                            grid-template-columns: 1fr !important;
                            gap: 16px !important;
                        }
                        .works-item[style*="grid-row: span 2"] {
                            grid-row: span 1 !important;
                            aspect-ratio: 4/3;
                        }
                    }
                </style>
                <script>
                    document.addEventListener('DOMContentLoaded', function() {
                        var filterBtns = document.querySelectorAll('.works-filter-btn');
                        var items = document.querySelectorAll('.works-item');

                        filterBtns.forEach(function(btn) {
                            btn.addEventListener('click', function() {
                                filterBtns.forEach(function(b) { b.classList.remove('active'); });
                                btn.classList.add('active');

                                var filter = btn.getAttribute('data-filter');

                                items.forEach(function(item) {
                                    if (filter === 'all' || item.getAttribute('data-category') === filter) {
                                        item.classList.remove('hidden');
                                    } else {
                                        item.classList.add('hidden');
                                    }
                                });
                            });
                        });
                    });
                </script>
            </section>'''

if TARGET not in content:
    print('ERROR: Target comment not found in home.html')
    exit(1)

new_content = content.replace(TARGET, REPLACEMENT, 1)

with open(FILE, 'w', encoding='cp1252', errors='xmlcharrefreplace') as f:
    f.write(new_content)

print('SUCCESS: Works Gallery section added to home.html')
print(f'File size: {len(content)} -> {len(new_content)} bytes')
