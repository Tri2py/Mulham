import glob
import re

# Official Vercel Web Analytics Snippet for static HTML sites
VERCEL_ANALYTICS_TAG = """    <!-- Vercel Web Analytics -->
    <script>
        window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/insights/script.js"></script>"""

def inject_analytics(filepath):
    with open(filepath, 'r', encoding='cp1252', errors='replace') as fp:
        content = fp.read()

    # Avoid duplicate insertion
    if '/_vercel/insights/script.js' in content:
        print(f"Skipping {filepath} (already present)")
        return True

    # Insert right before </head>
    head_idx = content.find('</head>')
    if head_idx != -1:
        content = content[:head_idx] + VERCEL_ANALYTICS_TAG + "\n" + content[head_idx:]
        with open(filepath, 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
            fp.write(content)
        print(f"Injected into {filepath}")
        return True
    else:
        print(f"FAILED for {filepath}: </head> not found")
        return False

for f in sorted(glob.glob('*.html')):
    inject_analytics(f)

print("--- Vercel Analytics successfully injected into all pages ---")
