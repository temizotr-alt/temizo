# -*- coding: utf-8 -*-
import json
import re
import sys

# Load translations.js
with open("js/translations.js", "r", encoding="utf-8") as f:
    content = f.read()

# Extract json
ar_match = re.search(r'ar:\s*(\{.*?\n  \}),', content, re.DOTALL)
tr_match = re.search(r'tr:\s*(\{.*?\n  \}),', content, re.DOTALL)
en_match = re.search(r'en:\s*(\{.*?\n  \})', content, re.DOTALL)

ar = json.loads(ar_match.group(1))
tr = json.loads(tr_match.group(1))
en = json.loads(en_match.group(1))

# Load index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find all data-i18n, data-i18n-ph, data-i18n-title, data-i18n-aria, data-i18n-alt, data-i18n-label, data-i18n-content
keys_in_html = set(re.findall(r'data-i18n(?:-[a-z]+)?="([^"]+)"', html))

print(f"Total unique keys referenced in index.html: {len(keys_in_html)}")

missing_in_ar = [k for k in keys_in_html if k not in ar]
missing_in_tr = [k for k in keys_in_html if k not in tr]
missing_in_en = [k for k in keys_in_html if k not in en]

if missing_in_ar:
    print(f"Missing in AR: {missing_in_ar}")
else:
    print("AR translations: 100% complete!")

if missing_in_tr:
    print(f"Missing in TR: {missing_in_tr}")
else:
    print("TR translations: 100% complete!")

if missing_in_en:
    print(f"Missing in EN: {missing_in_en}")
else:
    print("EN translations: 100% complete!")

# Check if any Arabic characters remain in TR or EN dictionary
arabic_regex = re.compile(r'[\u0600-\u06FF]')
tr_arabic = {k: v for k, v in tr.items() if arabic_regex.search(v)}
en_arabic = {k: v for k, v in en.items() if arabic_regex.search(v)}

if tr_arabic:
    print(f"Warning: Arabic found in TR keys: {list(tr_arabic.keys())}")
else:
    print("SUCCESS: 0 Arabic characters in entire Turkish dictionary!")

if en_arabic:
    print(f"Warning: Arabic found in EN keys: {list(en_arabic.keys())}")
else:
    print("SUCCESS: 0 Arabic characters in entire English dictionary!")
