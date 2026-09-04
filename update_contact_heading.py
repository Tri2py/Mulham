with open('contact.html', 'r', encoding='cp1252', errors='replace') as fp:
    txt = fp.read()

# Replace Send Message. with Initiate Contact.
old_h5 = '<h5>Send Message<span class="bringer-accent">.</span></h5>'
new_h5 = '<h5>Initiate Contact<span class="bringer-accent">.</span></h5>'

if old_h5 in txt:
    txt = txt.replace(old_h5, new_h5, 1)
    txt = txt.replace('<!-- Send Message -->', '<!-- Initiate Contact -->', 1)
    with open('contact.html', 'w', encoding='cp1252', errors='xmlcharrefreplace') as fp:
        fp.write(txt)
    print("SUCCESS: Replaced 'Send Message.' with 'Initiate Contact.' in contact.html")
else:
    print("ERROR: Old heading not found in contact.html")
