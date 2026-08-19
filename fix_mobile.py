# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='windows-1252', errors='ignore') as f:
    content = f.read()

# Replace the outdated mobile media query
old_media_query_regex = re.compile(r'/\*\s*Mobile Responsiveness\s*\*/.*?@media \(max-width: 768px\).*?}', re.DOTALL)

new_media_query = '''/* Mobile Responsiveness */
            @media (max-width: 768px) {
                /* Fix Massive Typography */
                .hero-blend-text h1:first-of-type { font-size: 24vw !important; }
                .hero-blend-text h1:last-of-type { font-size: 24vw !important; margin-top: 0 !important; }
                
                /* Fix Scroll Button */
                .hero-scroll-btn { width: 80px !important; height: 80px !important; font-size: 0.6rem !important; bottom: 2vh !important; right: 5vw !important; }
                
                /* Stack the Editorial Header perfectly */
                .hero-blend-text > div:first-child {
                    flex-direction: column !important;
                    align-items: flex-start !important;
                    gap: 15px !important;
                    border-bottom: none !important;
                }
                .hero-blend-text > div:first-child span {
                    text-align: left !important;
                    border-bottom: 1px solid rgba(255,255,255,0.2);
                    padding-bottom: 10px;
                    width: 100%;
                }

                /* Stack the Services Grid */
                .bringer-grid-2cols {
                    display: grid !important;
                    grid-template-columns: 1fr !important;
                    gap: 20px !important;
                }
                
                /* Adjust CV Editor Code */
                .editor-window pre {
                    font-size: 11px !important;
                    padding: 10px !important;
                }
            }'''

if old_media_query_regex.search(content):
    content = old_media_query_regex.sub(new_media_query, content, count=1)
else:
    # Inject it before the closing style tag of the hero
    content = content.replace('</style>', new_media_query + '\\n</style>', 1)

# Ensure bringer-tp-grid-2cols is removed or overridden so grid stacking works
content = content.replace('bringer-tp-grid-2cols', 'bringer-tp-grid-1col')

with open('index.html', 'w', encoding='windows-1252') as f:
    f.write(content)

print("Mobile optimizations applied to index.html!")
