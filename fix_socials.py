# -*- coding: utf-8 -*-
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

override = '''
/* Fix Phosphor Icons in Social List */
.bringer-socials-list i.ph-fill, .bringer-socials-list i.ph {
    background-color: transparent !important;
    -webkit-mask: none !important;
    mask: none !important;
    font-size: 24px !important;
    color: var(--bringer-s-heading) !important;
    width: auto !important;
    height: auto !important;
    display: inline-flex !important;
    align-items: center;
    justify-content: center;
}
.bringer-socials-list a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
'''

if '/* Fix Phosphor Icons in Social List */' not in css:
    css += override
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Fixed social icons in style.css!")
else:
    print("Already fixed.")
