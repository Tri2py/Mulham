import os

with open('home.html', 'r', encoding='cp1252', errors='replace') as f:
    content = f.read()

# ── 1. Find and replace the Works Gallery section ──
# Marker: <!-- Section: Works Gallery -->
# Ends at: </section> before <!-- Section: Services -->

works_start_marker = '<!-- Section: Works Gallery -->'
services_marker = '<!-- Section: Services -->'

ws_idx = content.find(works_start_marker)
sv_idx = content.find(services_marker)

if ws_idx == -1:
    print("ERROR: Could not find Works Gallery section")
    exit(1)
if sv_idx == -1:
    print("ERROR: Could not find Services section")
    exit(1)

# The works section ends right before the services marker
# We need to find the </section> + whitespace right before services_marker
# Actually let's just replace everything from works_start_marker to (and including) the old services </section>

# Find the end of old services section
cv_marker = '<!-- Section: CV Preview -->'
cv_idx = content.find(cv_marker)
if cv_idx == -1:
    print("ERROR: Could not find CV Preview section")
    exit(1)

# The old services </section> is right before CV preview
# Replace from works_start_marker to just before cv_marker
old_block = content[ws_idx:cv_idx]

NEW_BLOCK = """<!-- Section: Services (2 Images) -->
            <section id="services-preview" style="margin-top: 2vh; margin-bottom: 14vh; position: relative;">
                <!-- Section Title -->
                <div class="stg-row bringer-section-title" style="margin-bottom: 48px;">
                    <div class="stg-col-8">
                        <h2 style="font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 24px;">
                            Capabilities <span style="font-style: italic; color: var(--bringer-s-text);">&amp;</span> Services
                        </h2>
                        <p style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: 1rem; line-height: 1.7; max-width: 540px;">Strategic disciplines to elevate your digital presence.</p>
                    </div>
                </div>

                <!-- Two Service Cards -->
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 28px;">

                    <!-- Card 1: Web Development -->
                    <a href="/web-projects" style="text-decoration: none; position: relative; border-radius: 24px; overflow: hidden; aspect-ratio: 4/5; display: block; border: 1px solid rgba(140,45,246,0.15); box-shadow: inset 0 0 50px rgba(140,45,246,0.05); transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease;" class="svc-card">
                        <img src="img/home/services_web.jpg" alt="Web Development" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);">
                        <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0.3) 50%, rgba(6,2,10,0.1) 100%); z-index: 1;"></div>
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 36px; z-index: 2;">
                            <span style="display: inline-block; font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 12px;">01</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.6rem, 3vw, 2.4rem); font-weight: 400; color: #fff; margin: 0 0 12px 0; letter-spacing: -0.02em; line-height: 1.15;">Web<br>Development<span style="color: #8C2DF6;">.</span></h3>
                            <p style="color: rgba(255,255,255,0.55); font-size: 0.88rem; line-height: 1.6; margin: 0; max-width: 320px;">Modern, responsive websites built with the latest technologies for optimal performance.</p>
                        </div>
                    </a>

                    <!-- Card 2: Design -->
                    <a href="/portfolio" style="text-decoration: none; position: relative; border-radius: 24px; overflow: hidden; aspect-ratio: 4/5; display: block; border: 1px solid rgba(255,255,255,0.06); box-shadow: inset 0 0 40px rgba(255,255,255,0.02); transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease; transform: translateY(8%);" class="svc-card">
                        <img src="img/home/services_branding.jpg" alt="Design Services" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);">
                        <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0.3) 50%, rgba(6,2,10,0.1) 100%); z-index: 1;"></div>
                        <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 36px; z-index: 2;">
                            <span style="display: inline-block; font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 12px;">02</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.6rem, 3vw, 2.4rem); font-weight: 400; color: #fff; margin: 0 0 12px 0; letter-spacing: -0.02em; line-height: 1.15;">Creative<br>Design<span style="color: #8C2DF6;">.</span></h3>
                            <p style="color: rgba(255,255,255,0.55); font-size: 0.88rem; line-height: 1.6; margin: 0; max-width: 320px;">Branding, UI/UX design, and visual identity systems that make your business stand out.</p>
                        </div>
                    </a>

                </div>

                <!-- Service Card Styles -->
                <style>
                    .svc-card:hover {
                        transform: translateY(-6px) !important;
                        box-shadow: 0 20px 60px rgba(140, 45, 246, 0.15), inset 0 0 50px rgba(140,45,246,0.08) !important;
                        border-color: rgba(140, 45, 246, 0.3) !important;
                    }
                    .svc-card:hover img {
                        transform: scale(1.06);
                    }
                    @media (max-width: 768px) {
                        #services-preview > div:nth-child(3) {
                            grid-template-columns: 1fr !important;
                        }
                        .svc-card {
                            transform: none !important;
                        }
                    }
                </style>
            </section>

            <!-- Section: Selected Works -->
            <section id="works-gallery" style="margin-bottom: 12vh; position: relative;">
                <!-- Section Title -->
                <div class="stg-row bringer-section-title" style="margin-bottom: 48px;">
                    <div class="stg-col-8">
                        <h2 style="font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 24px;">
                            Selected <span style="font-style: italic; color: var(--bringer-s-text);">Works</span>
                        </h2>
                        <p style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: 1rem; line-height: 1.7; max-width: 540px;">A curated selection of projects across web, branding, and digital design.</p>
                    </div>
                </div>

                <!-- Works List (Text-only, no images) -->
                <div class="works-list" style="display: flex; flex-direction: column; border-top: 1px solid rgba(255,255,255,0.08);">

                    <!-- Work Item 1 -->
                    <a href="/web-projects" class="work-row" style="display: flex; align-items: center; justify-content: space-between; padding: 32px 0; border-bottom: 1px solid rgba(255,255,255,0.08); text-decoration: none; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); position: relative; cursor: pointer;">
                        <div style="display: flex; align-items: center; gap: 40px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 500; color: rgba(255,255,255,0.25); letter-spacing: 0.1em; min-width: 28px;">01</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 3.5vw, 2.8rem); font-weight: 400; color: #fff; margin: 0; letter-spacing: -0.02em; transition: color 0.3s ease;">E-Commerce Platform</h3>
                        </div>
                        <div style="display: flex; align-items: center; gap: 32px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: rgba(255,255,255,0.35); letter-spacing: 0.08em; text-transform: uppercase;">Web Development</span>
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transition: all 0.3s ease;"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                        </div>
                    </a>

                    <!-- Work Item 2 -->
                    <a href="/portfolio" class="work-row" style="display: flex; align-items: center; justify-content: space-between; padding: 32px 0; border-bottom: 1px solid rgba(255,255,255,0.08); text-decoration: none; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); position: relative; cursor: pointer;">
                        <div style="display: flex; align-items: center; gap: 40px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 500; color: rgba(255,255,255,0.25); letter-spacing: 0.1em; min-width: 28px;">02</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 3.5vw, 2.8rem); font-weight: 400; color: #fff; margin: 0; letter-spacing: -0.02em; transition: color 0.3s ease;">Brand Identity System</h3>
                        </div>
                        <div style="display: flex; align-items: center; gap: 32px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: rgba(255,255,255,0.35); letter-spacing: 0.08em; text-transform: uppercase;">Branding</span>
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transition: all 0.3s ease;"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                        </div>
                    </a>

                    <!-- Work Item 3 -->
                    <a href="/web-projects" class="work-row" style="display: flex; align-items: center; justify-content: space-between; padding: 32px 0; border-bottom: 1px solid rgba(255,255,255,0.08); text-decoration: none; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); position: relative; cursor: pointer;">
                        <div style="display: flex; align-items: center; gap: 40px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 500; color: rgba(255,255,255,0.25); letter-spacing: 0.1em; min-width: 28px;">03</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 3.5vw, 2.8rem); font-weight: 400; color: #fff; margin: 0; letter-spacing: -0.02em; transition: color 0.3s ease;">Portfolio Website</h3>
                        </div>
                        <div style="display: flex; align-items: center; gap: 32px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: rgba(255,255,255,0.35); letter-spacing: 0.08em; text-transform: uppercase;">Web Design</span>
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transition: all 0.3s ease;"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                        </div>
                    </a>

                    <!-- Work Item 4 -->
                    <a href="/portfolio" class="work-row" style="display: flex; align-items: center; justify-content: space-between; padding: 32px 0; border-bottom: 1px solid rgba(255,255,255,0.08); text-decoration: none; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); position: relative; cursor: pointer;">
                        <div style="display: flex; align-items: center; gap: 40px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 500; color: rgba(255,255,255,0.25); letter-spacing: 0.1em; min-width: 28px;">04</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 3.5vw, 2.8rem); font-weight: 400; color: #fff; margin: 0; letter-spacing: -0.02em; transition: color 0.3s ease;">Digital Campaign</h3>
                        </div>
                        <div style="display: flex; align-items: center; gap: 32px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: rgba(255,255,255,0.35); letter-spacing: 0.08em; text-transform: uppercase;">Marketing</span>
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transition: all 0.3s ease;"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                        </div>
                    </a>

                    <!-- Work Item 5 -->
                    <a href="/portfolio" class="work-row" style="display: flex; align-items: center; justify-content: space-between; padding: 32px 0; border-bottom: 1px solid rgba(255,255,255,0.08); text-decoration: none; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); position: relative; cursor: pointer;">
                        <div style="display: flex; align-items: center; gap: 40px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.7rem; font-weight: 500; color: rgba(255,255,255,0.25); letter-spacing: 0.1em; min-width: 28px;">05</span>
                            <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(1.5rem, 3.5vw, 2.8rem); font-weight: 400; color: #fff; margin: 0; letter-spacing: -0.02em; transition: color 0.3s ease;">UI/UX Redesign</h3>
                        </div>
                        <div style="display: flex; align-items: center; gap: 32px;">
                            <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; color: rgba(255,255,255,0.35); letter-spacing: 0.08em; text-transform: uppercase;">Design</span>
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transition: all 0.3s ease;"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                        </div>
                    </a>

                </div>

                <!-- View All CTA -->
                <div style="text-align: center; margin-top: 56px;">
                    <a href="/portfolio" style="display: inline-flex; align-items: center; gap: 12px; padding: 16px 40px; border: 1px solid rgba(140, 45, 246, 0.4); border-radius: 100px; color: #fff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 500; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); background: rgba(140, 45, 246, 0.08);" class="works-cta-btn">
                        View All Works
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </a>
                </div>

                <!-- Works List Hover Styles -->
                <style>
                    .work-row:hover {
                        padding-left: 16px !important;
                        background: rgba(140, 45, 246, 0.03);
                    }
                    .work-row:hover h3 {
                        color: #8C2DF6 !important;
                    }
                    .work-row:hover svg {
                        stroke: #8C2DF6 !important;
                        transform: translate(4px, -4px);
                    }
                    .work-row::after {
                        content: '';
                        position: absolute;
                        bottom: 0;
                        left: 0;
                        width: 0;
                        height: 1px;
                        background: linear-gradient(90deg, #8C2DF6, transparent);
                        transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
                    }
                    .work-row:hover::after {
                        width: 100%;
                    }
                    .works-cta-btn:hover {
                        background: rgba(140, 45, 246, 0.2) !important;
                        border-color: rgba(140, 45, 246, 0.6) !important;
                        transform: translateY(-2px);
                        box-shadow: 0 8px 30px rgba(140, 45, 246, 0.2);
                    }
                    @media (max-width: 768px) {
                        .work-row {
                            flex-direction: column !important;
                            align-items: flex-start !important;
                            gap: 12px !important;
                            padding: 24px 0 !important;
                        }
                        .work-row > div:last-child {
                            padding-left: 68px;
                        }
                    }
                </style>
            </section>

            """

content_new = content[:ws_idx] + NEW_BLOCK + content[cv_idx:]

with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as f:
    f.write(content_new)

# Verify
with open('home.html', 'r', encoding='cp1252', errors='replace') as f:
    verify = f.read()

has_services = '<!-- Section: Services (2 Images) -->' in verify
has_works = '<!-- Section: Selected Works -->' in verify
has_works_list = 'works-list' in verify
has_no_gallery_grid = 'works-gallery-grid' not in verify

print(f"Services section with 2 images: {'OK' if has_services else 'MISSING'}")
print(f"Works section (text-only): {'OK' if has_works else 'MISSING'}")
print(f"Works list (no images): {'OK' if has_works_list else 'MISSING'}")
print(f"Old gallery grid removed: {'OK' if has_no_gallery_grid else 'STILL PRESENT'}")
print(f"File size: {os.path.getsize('home.html')} bytes")
print("SUCCESS" if all([has_services, has_works, has_works_list, has_no_gallery_grid]) else "ISSUES FOUND")
