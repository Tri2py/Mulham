# -*- coding: utf-8 -*-
import re

files_to_fix = ['contacts.html', 'portfolio.html']

for filename in files_to_fix:
    with open(filename, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    # Extract everything from <!DOCTYPE html> to </head>
    head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', content, re.DOTALL)
    if head_match:
        head_content = head_match.group(1)
        
        # Remove all <style>...</style> blocks from the head
        clean_head = re.sub(r'<style>.*?</style>', '', head_content, flags=re.DOTALL)
        
        # Replace the old head with the clean head
        content = content.replace(head_content, clean_head)
        
        with open(filename, 'w', encoding='windows-1252') as f:
            f.write(content)
        
        print(f"Stripped all style blocks from the head of {filename}")
    else:
        print(f"Could not find head in {filename}")

