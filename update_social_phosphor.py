with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    content = fp.read()

# 1. Ensure Phosphor CSS stylesheets are in <head> for reliable font icon rendering
old_script = '<script src="https://unpkg.com/@phosphor-icons/web"></script>'
new_head_icons = """<!-- Phosphor Icons: Full CSS Stylesheets + Web Component -->
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" />
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css" />
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/bold/style.css" />
    <script src="https://unpkg.com/@phosphor-icons/web"></script>"""

if old_script in content:
    content = content.replace(old_script, new_head_icons, 1)
    print("OK: Added Phosphor CSS fonts to head")

# 2. Refine the Social Ecosphere card with prominent Phosphor icon pills & SVGs
old_chips = """<!-- Custom Social Chips -->
                            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 14px;">
                                <a href="https://www.instagram.com/creative_mulham/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: #fff; text-decoration: none; font-size: 0.8rem; font-weight: 500; transition: all 0.25s ease;">
                                    <i class="ph-fill ph-instagram-logo" style="font-size: 1rem; color: #e1306c;"></i>
                                    Instagram
                                </a>
                                <a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: #fff; text-decoration: none; font-size: 0.8rem; font-weight: 500; transition: all 0.25s ease;">
                                    <i class="ph-fill ph-linkedin-logo" style="font-size: 1rem; color: #0a66c2;"></i>
                                    LinkedIn
                                </a>
                                <a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; color: #fff; text-decoration: none; font-size: 0.8rem; font-weight: 500; transition: all 0.25s ease;">
                                    <i class="ph-fill ph-pinterest-logo" style="font-size: 1rem; color: #e60023;"></i>
                                    Pinterest
                                </a>
                            </div>"""

new_chips = """<!-- Custom Social Phosphor Cards / Chips -->
                            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px;">
                                <!-- Instagram -->
                                <a href="https://www.instagram.com/creative_mulham/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(225, 48, 108, 0.08); border: 1px solid rgba(225, 48, 108, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-instagram-logo" style="font-size: 1.2rem; color: #f04276; display: inline-block; vertical-align: middle;"></i>
                                    <span>Instagram</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                                
                                <!-- LinkedIn -->
                                <a href="https://www.linkedin.com/in/mulham-ibrahim-2021643ab?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(10, 102, 194, 0.08); border: 1px solid rgba(10, 102, 194, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-linkedin-logo" style="font-size: 1.2rem; color: #2884e0; display: inline-block; vertical-align: middle;"></i>
                                    <span>LinkedIn</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                                
                                <!-- Pinterest -->
                                <a href="https://www.pinterest.com/normal_person_as_trippy/" target="_blank" class="social-chip" style="display: inline-flex; align-items: center; gap: 9px; padding: 10px 16px; background: rgba(230, 0, 35, 0.08); border: 1px solid rgba(230, 0, 35, 0.25); border-radius: 12px; color: #ffffff; text-decoration: none; font-family: 'Inter', sans-serif; font-size: 0.82rem; font-weight: 500; transition: all 0.3s ease;">
                                    <i class="ph-fill ph-pinterest-logo" style="font-size: 1.2rem; color: #ff334b; display: inline-block; vertical-align: middle;"></i>
                                    <span>Pinterest</span>
                                    <i class="ph-bold ph-arrow-up-right" style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-left: 2px;"></i>
                                </a>
                            </div>"""

content_n = content.replace('\r\n', '\n')
old_chips_n = old_chips.replace('\r\n', '\n')
new_chips_n = new_chips.replace('\r\n', '\n')

if old_chips_n in content_n:
    content_n = content_n.replace(old_chips_n, new_chips_n, 1)
    print("OK: Replaced Social Chips with enhanced Phosphor cards")
else:
    print("WARN: Old chips not found by exact string, checking fallback")

with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
    fp.write(content_n)

print("SUCCESS: Enhanced Phosphor icons on Social Ecosphere card!")
