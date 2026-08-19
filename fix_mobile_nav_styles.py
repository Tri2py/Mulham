# -*- coding: utf-8 -*-

missing_css = '''
        /* Hide the misaligned JS active menu indicator */
        .bringer-active-menu-ind {
            display: none !important;
        }

        /* Mobile Header Overrides */
        @media (max-width: 768px) {
            #bringer-header {
                min-width: 0;
                width: calc(100% - 40px) !important;
                padding: 0 20px !important;
            }
            .bringer-header-inner { display: none !important; }
            .bringer-mobile-header-inner {
                display: flex !important;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                padding: 12px 0;
            }
        }
    </style>
'''

files_to_fix = ['contacts.html', 'portfolio.html']

for filename in files_to_fix:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    # We replace the closing </style> tag in the <head> with our missing CSS
    # Make sure we don't duplicate it if we run it twice
    if ".bringer-mobile-header-inner {" not in content:
        content = content.replace('</style>\n</head>', missing_css + '\n</head>')
        
        with open(filename, 'w', encoding='windows-1252') as f:
            f.write(content)
        print(f"Fixed mobile nav styles in {filename}")
    else:
        print(f"{filename} already has mobile nav styles.")

