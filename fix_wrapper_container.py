# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Replace the wrapper start
old_wrapper_start = '''<div class="page-content-wrapper" style="position: relative; z-index: 10; background: #000000; margin-left: calc(50% - 50vw); width: 100vw; padding: 8vh calc(50vw - 50%) 0; border-top-left-radius: 50px; border-top-right-radius: 50px; box-shadow: 0 -30px 100px rgba(0,0,0,0.9); border-top: 1px solid rgba(255,255,255,0.06); transform: translate3d(0,0,0);">'''

new_wrapper_start = '''<div class="page-content-wrapper" style="position: relative; z-index: 10; background: #000000; margin-left: calc(50% - 50vw); width: 100vw; padding-top: 8vh; padding-bottom: 8vh; border-top-left-radius: 50px; border-top-right-radius: 50px; box-shadow: 0 -30px 100px rgba(0,0,0,0.9); border-top: 1px solid rgba(255,255,255,0.06); transform: translate3d(0,0,0);">
                <div class="stg-container">'''

content = content.replace(old_wrapper_start, new_wrapper_start)

# Replace the wrapper end
old_wrapper_end = '''            </div><!-- .page-content-wrapper -->
        </div><!-- .stg-container -->'''

new_wrapper_end = '''                </div><!-- .inner-stg-container -->
            </div><!-- .page-content-wrapper -->
        </div><!-- .outer-stg-container -->'''

content = content.replace(old_wrapper_end, new_wrapper_end)

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Fixed wrapper container!")
