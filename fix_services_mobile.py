with open('home.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

old_services_section = """<!-- Section: Services (2 Images) -->
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
            </section>"""

new_services_section = """<!-- Section: Services (2 Images Preview - Responsive) -->
            <section id="services-preview" class="services-preview-section">
                <!-- Section Title -->
                <div class="stg-row bringer-section-title services-section-title">
                    <div class="stg-col-8">
                        <span style="display: inline-block; font-family: 'Inter', sans-serif; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.25em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 12px;">Capabilities</span>
                        <h2 style="font-family: 'Playfair Display', serif; font-size: clamp(2.4rem, 6vw, 4.5rem); font-weight: 400; letter-spacing: -0.02em; line-height: 1.1; margin-bottom: 18px;">
                            Capabilities <span style="font-style: italic; color: var(--bringer-s-text);">&amp;</span> Services
                        </h2>
                        <p style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: 1rem; line-height: 1.7; max-width: 540px; margin: 0;">Strategic disciplines to elevate your digital presence.</p>
                    </div>
                </div>

                <!-- Two Service Cards -->
                <div class="services-cards-grid">

                    <!-- Card 1: Web Development -->
                    <a href="/web-projects" class="svc-card svc-card--dev">
                        <img src="img/home/services_web.jpg" alt="Web Development" class="svc-card-img">
                        <div class="svc-card-overlay"></div>
                        <div class="svc-card-body">
                            <span class="svc-card-num">01</span>
                            <h3 class="svc-card-title">Web<br>Development<span style="color: #8C2DF6;">.</span></h3>
                            <p class="svc-card-desc">Modern, responsive websites built with the latest technologies for optimal performance.</p>
                        </div>
                    </a>

                    <!-- Card 2: Design -->
                    <a href="/portfolio" class="svc-card svc-card--design">
                        <img src="img/home/services_branding.jpg" alt="Design Services" class="svc-card-img">
                        <div class="svc-card-overlay"></div>
                        <div class="svc-card-body">
                            <span class="svc-card-num">02</span>
                            <h3 class="svc-card-title">Creative<br>Design<span style="color: #8C2DF6;">.</span></h3>
                            <p class="svc-card-desc">Branding, UI/UX design, and visual identity systems that make your business stand out.</p>
                        </div>
                    </a>

                </div>

                <!-- Responsive Service Card Styles -->
                <style>
                    .services-preview-section {
                        margin-top: 2vh;
                        margin-bottom: 14vh;
                        position: relative;
                    }
                    .services-section-title {
                        margin-bottom: 48px;
                    }
                    .services-cards-grid {
                        display: grid;
                        grid-template-columns: repeat(2, 1fr);
                        gap: 28px;
                    }
                    .svc-card {
                        text-decoration: none;
                        position: relative;
                        border-radius: 24px;
                        overflow: hidden;
                        aspect-ratio: 4/5;
                        display: block;
                        border: 1px solid rgba(140,45,246,0.15);
                        box-shadow: inset 0 0 50px rgba(140,45,246,0.05);
                        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease, border-color 0.4s ease;
                    }
                    .svc-card--design {
                        border-color: rgba(255,255,255,0.06);
                        box-shadow: inset 0 0 40px rgba(255,255,255,0.02);
                        transform: translateY(8%);
                    }
                    .svc-card-img {
                        position: absolute;
                        inset: 0;
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                        transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
                    }
                    .svc-card-overlay {
                        position: absolute;
                        inset: 0;
                        background: linear-gradient(to top, rgba(6,2,10,0.95) 0%, rgba(6,2,10,0.4) 50%, rgba(6,2,10,0.1) 100%);
                        z-index: 1;
                    }
                    .svc-card-body {
                        position: absolute;
                        bottom: 0;
                        left: 0;
                        right: 0;
                        padding: 36px;
                        z-index: 2;
                    }
                    .svc-card-num {
                        display: inline-block;
                        font-family: 'Inter', sans-serif;
                        font-size: 0.65rem;
                        font-weight: 600;
                        letter-spacing: 0.2em;
                        text-transform: uppercase;
                        color: #8C2DF6;
                        margin-bottom: 12px;
                    }
                    .svc-card-title {
                        font-family: 'Playfair Display', serif;
                        font-size: clamp(1.6rem, 3vw, 2.4rem);
                        font-weight: 400;
                        color: #fff;
                        margin: 0 0 12px 0;
                        letter-spacing: -0.02em;
                        line-height: 1.15;
                    }
                    .svc-card-desc {
                        color: rgba(255,255,255,0.6);
                        font-size: 0.88rem;
                        line-height: 1.6;
                        margin: 0;
                        max-width: 320px;
                    }

                    /* Desktop Hover */
                    .svc-card:hover {
                        transform: translateY(-6px) !important;
                        box-shadow: 0 20px 60px rgba(140, 45, 246, 0.18), inset 0 0 50px rgba(140,45,246,0.08) !important;
                        border-color: rgba(140, 45, 246, 0.4) !important;
                    }
                    .svc-card:hover .svc-card-img {
                        transform: scale(1.06);
                    }

                    /* Tablet & Mobile Breakpoints */
                    @media (max-width: 900px) {
                        .services-cards-grid {
                            grid-template-columns: 1fr !important;
                            gap: 24px !important;
                        }
                        .svc-card--design {
                            transform: none !important;
                        }
                        .svc-card {
                            aspect-ratio: 16/10 !important;
                            min-height: 300px !important;
                            border-radius: 20px !important;
                        }
                        .svc-card-body {
                            padding: 28px 24px !important;
                        }
                        .svc-card-title br {
                            display: none;
                        }
                        .svc-card-desc {
                            max-width: 100% !important;
                        }
                    }

                    @media (max-width: 600px) {
                        .services-preview-section {
                            margin-top: 1vh !important;
                            margin-bottom: 8vh !important;
                        }
                        .services-section-title {
                            margin-bottom: 28px !important;
                        }
                        .services-cards-grid {
                            gap: 18px !important;
                        }
                        .svc-card {
                            aspect-ratio: 4/3 !important;
                            min-height: 260px !important;
                            border-radius: 16px !important;
                        }
                        .svc-card-body {
                            padding: 22px 18px !important;
                        }
                        .svc-card-title {
                            font-size: 1.5rem !important;
                            margin-bottom: 8px !important;
                        }
                        .svc-card-desc {
                            font-size: 0.82rem !important;
                            line-height: 1.5 !important;
                        }
                    }
                </style>
            </section>"""

content_norm = content.replace('\r\n', '\n')
old_sec_norm = old_services_section.replace('\r\n', '\n')
new_sec_norm = new_services_section.replace('\r\n', '\n')

if old_sec_norm in content_norm:
    content_norm = content_norm.replace(old_sec_norm, new_sec_norm, 1)
    with open('home.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
        fp.write(content_norm)
    print("SUCCESS: Upgraded Services (2 Images Preview) section for responsive mobile view in home.html")
else:
    print("ERROR: old_services_section not found by exact match")
