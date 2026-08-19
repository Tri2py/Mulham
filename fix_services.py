# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Replace Services Cards
services_regex = re.compile(r'<!-- Service Web Development -->.*?(?=</div>\s*</section>)', re.DOTALL)

new_services = '''<!-- Service Web Development -->
                    <div class="bringer-masked-block">
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between bringer-masked-media" data-bg-src="img/home/services_web.jpg" style="position: relative; border: 1px solid rgba(255,255,255,0.05);">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.2)); z-index: 0;"></div>
                            <h5 style="position: relative; z-index: 1;">Service Web Development<span class="bringer-accent">.</span></h5>
                            <p style="position: relative; z-index: 1;">Modern, responsive websites built with the latest technologies for optimal performance.</p>
                        </div>
                    </div>

                    <!-- Service Designs -->
                    <div class="bringer-masked-block">
                        <div class="bringer-block stg-aspect-square stg-vertical-space-between bringer-masked-media" data-bg-src="img/home/services_branding.jpg" style="position: relative; border: 1px solid rgba(255,255,255,0.05);">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.2)); z-index: 0;"></div>
                            <h5 style="position: relative; z-index: 1;">Service Designs<span class="bringer-accent">.</span></h5>
                            <p style="position: relative; z-index: 1;">Creative branding, UI/UX design, and visual identity systems that make your business stand out.</p>
                        </div>
                    </div>'''

content = services_regex.sub(new_services, content, count=1)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Updated Services cards with background images!")
