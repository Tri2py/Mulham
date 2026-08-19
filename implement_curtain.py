# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# 1. Make hero sticky
content = content.replace('id="awwwards-hero" style="position: relative;', 'id="awwwards-hero" style="position: sticky; top: 0; z-index: 1;')

# 2. Insert wrapper start after the hero's </section>
wrapper_start = '''</section>

            <!-- Premium Curtain Transition Wrapper -->
            <div class="page-content-wrapper" style="position: relative; z-index: 10; background: #000000; margin-left: calc(50% - 50vw); width: 100vw; padding: 8vh calc(50vw - 50%) 0; border-top-left-radius: 50px; border-top-right-radius: 50px; box-shadow: 0 -30px 100px rgba(0,0,0,0.9); border-top: 1px solid rgba(255,255,255,0.06); transform: translate3d(0,0,0);">
'''
# We find the closing tag of the hero section. 
# It's right before <!-- Section: Selected Works
content = content.replace('</section>\n            <!-- Section: Selected Works', wrapper_start + '\n            <!-- Section: Selected Works')

# 3. Insert wrapper end right before </div><!-- .stg-container -->
wrapper_end = '''            </div><!-- .page-content-wrapper -->
        </div><!-- .stg-container -->'''
content = content.replace('</div><!-- .stg-container -->', wrapper_end)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Curtain transition added!")
