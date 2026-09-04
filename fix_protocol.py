with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# Locate the strip
start_marker = '<!-- Client Expectations / Working With Me Strip -->'
end_marker = '</section>\n\n        </div><!-- .stg-container -->'

idx_start = content.find(start_marker)
if idx_start == -1:
    idx_start = content.find('Collaboration Protocol')
    idx_start = content.rfind('<!--', 0, idx_start)

idx_end = content.find('</section>', idx_start)

UPGRADED_PROTOCOL = """<!-- Client Collaboration Protocol: High-End Bento Grid -->
                <div class="collaboration-protocol-wrap" style="margin-top: 10vh; margin-bottom: 8vh; position: relative;">
                    <!-- Section Header -->
                    <div style="text-align: center; margin-bottom: 40px;">
                        <span style="display: inline-block; font-family: 'Inter', sans-serif; font-size: 0.68rem; font-weight: 600; letter-spacing: 0.28em; text-transform: uppercase; color: #8C2DF6; margin-bottom: 12px;">Collaboration Protocol</span>
                        <h3 style="font-family: 'Playfair Display', serif; font-size: clamp(2rem, 4.5vw, 3.2rem); font-weight: 400; color: #ffffff; letter-spacing: -0.02em; margin: 0 0 14px 0;">
                            What to expect when reaching out<span style="color: #8C2DF6;">.</span>
                        </h3>
                        <p style="color: rgba(255,255,255,0.5); font-family: 'Inter', sans-serif; font-size: 0.95rem; max-width: 560px; margin: 0 auto; line-height: 1.6;">
                            A refined studio workflow engineered for transparency, rapid momentum, and zero friction.
                        </p>
                    </div>

                    <!-- 4-Pillar Architectural Bento Grid -->
                    <div class="protocol-cards-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
                        
                        <!-- Card 01 -->
                        <div class="protocol-card" style="background: rgba(14, 8, 20, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(140, 45, 246, 0.16); border-radius: 20px; padding: 32px 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px;">
                                    <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(140, 45, 246, 0.12); border: 1px solid rgba(140, 45, 246, 0.25); display: flex; align-items: center; justify-content: center;">
                                        <i class="ph-fill ph-lightning" style="font-size: 1.3rem; color: #b066ff;"></i>
                                    </div>
                                    <span style="font-family: 'Inter', monospace, sans-serif; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; color: rgba(255,255,255,0.3);">01</span>
                                </div>
                                <h4 style="font-family: 'Playfair Display', serif; font-size: 1.25rem; font-weight: 500; color: #ffffff; margin: 0 0 10px 0; letter-spacing: -0.01em;">Rapid Scoping</h4>
                                <p style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: 0.86rem; line-height: 1.6; margin: 0;">Inquiries receive an initial review and scoping framework within 24 business hours.</p>
                            </div>
                            <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; gap: 8px;">
                                <i class="ph-bold ph-clock" style="font-size: 0.85rem; color: #8C2DF6;"></i>
                                <span style="font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4);">Sub-24h Response</span>
                            </div>
                        </div>

                        <!-- Card 02 -->
                        <div class="protocol-card" style="background: rgba(14, 8, 20, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(140, 45, 246, 0.16); border-radius: 20px; padding: 32px 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px;">
                                    <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(140, 45, 246, 0.12); border: 1px solid rgba(140, 45, 246, 0.25); display: flex; align-items: center; justify-content: center;">
                                        <i class="ph-fill ph-user-focus" style="font-size: 1.3rem; color: #b066ff;"></i>
                                    </div>
                                    <span style="font-family: 'Inter', monospace, sans-serif; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; color: rgba(255,255,255,0.3);">02</span>
                                </div>
                                <h4 style="font-family: 'Playfair Display', serif; font-size: 1.25rem; font-weight: 500; color: #ffffff; margin: 0 0 10px 0; letter-spacing: -0.01em;">Direct Access</h4>
                                <p style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: 0.86rem; line-height: 1.6; margin: 0;">Work directly with Mulham throughout ideation and execution &mdash; no middle layers or agency fluff.</p>
                            </div>
                            <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; gap: 8px;">
                                <i class="ph-bold ph-shield-check" style="font-size: 0.85rem; color: #8C2DF6;"></i>
                                <span style="font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4);">Principal Lead</span>
                            </div>
                        </div>

                        <!-- Card 03 -->
                        <div class="protocol-card" style="background: rgba(14, 8, 20, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(140, 45, 246, 0.16); border-radius: 20px; padding: 32px 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px;">
                                    <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(140, 45, 246, 0.12); border: 1px solid rgba(140, 45, 246, 0.25); display: flex; align-items: center; justify-content: center;">
                                        <i class="ph-fill ph-sketch-logo" style="font-size: 1.3rem; color: #b066ff;"></i>
                                    </div>
                                    <span style="font-family: 'Inter', monospace, sans-serif; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; color: rgba(255,255,255,0.3);">03</span>
                                </div>
                                <h4 style="font-family: 'Playfair Display', serif; font-size: 1.25rem; font-weight: 500; color: #ffffff; margin: 0 0 10px 0; letter-spacing: -0.01em;">Tailored Systems</h4>
                                <p style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: 0.86rem; line-height: 1.6; margin: 0;">Bespoke aesthetics and high-performance engineering tailored to distinct brand identity.</p>
                            </div>
                            <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; gap: 8px;">
                                <i class="ph-bold ph-diamond" style="font-size: 0.85rem; color: #8C2DF6;"></i>
                                <span style="font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4);">Zero Templates</span>
                            </div>
                        </div>

                        <!-- Card 04 -->
                        <div class="protocol-card" style="background: rgba(140, 8, 20, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(140, 45, 246, 0.16); border-radius: 20px; padding: 32px 24px; display: flex; flex-direction: column; justify-content: space-between; position: relative; overflow: hidden; transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);">
                            <div>
                                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px;">
                                    <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(140, 45, 246, 0.12); border: 1px solid rgba(140, 45, 246, 0.25); display: flex; align-items: center; justify-content: center;">
                                        <i class="ph-fill ph-globe-hemisphere-east" style="font-size: 1.3rem; color: #b066ff;"></i>
                                    </div>
                                    <span style="font-family: 'Inter', monospace, sans-serif; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; color: rgba(255,255,255,0.3);">04</span>
                                </div>
                                <h4 style="font-family: 'Playfair Display', serif; font-size: 1.25rem; font-weight: 500; color: #ffffff; margin: 0 0 10px 0; letter-spacing: -0.01em;">Global Cadence</h4>
                                <p style="color: rgba(255,255,255,0.55); font-family: 'Inter', sans-serif; font-size: 0.86rem; line-height: 1.6; margin: 0;">Seamless async-first communication loops optimized for international clients and partners.</p>
                            </div>
                            <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; gap: 8px;">
                                <i class="ph-bold ph-globe-stand" style="font-size: 0.85rem; color: #8C2DF6;"></i>
                                <span style="font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4);">Worldwide Sync</span>
                            </div>
                        </div>

                    </div>
                </div>"""

# Replace in content
content = content[:idx_start] + UPGRADED_PROTOCOL + "\n            " + content[idx_end:]

# Update the media query and hover css in <head>
extra_css_marker = '</style>\n</head>'
protocol_css = """
        .protocol-card {
            background: rgba(14, 8, 20, 0.6) !important;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 0 25px rgba(140, 45, 246, 0.03);
        }
        .protocol-card:hover {
            transform: translateY(-5px);
            border-color: rgba(140, 45, 246, 0.45) !important;
            box-shadow: 0 25px 60px rgba(140, 45, 246, 0.12), inset 0 0 35px rgba(140, 45, 246, 0.08) !important;
        }
        @media (max-width: 1024px) {
            .protocol-cards-grid {
                grid-template-columns: repeat(2, 1fr) !important;
            }
        }
        @media (max-width: 640px) {
            .protocol-cards-grid {
                grid-template-columns: 1fr !important;
            }
        }
    </style>
</head>"""

if extra_css_marker in content:
    content = content.replace(extra_css_marker, protocol_css, 1)

with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content)

print("SUCCESS: Transformed Collaboration Protocol into high-end architectural Bento grid with Phosphor icons!")
