# -*- coding: utf-8 -*-
import subprocess
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
arabic_regex = re.compile(r'[\u0600-\u06FF]')

def test_language(lang):
    url = f"http://localhost:8080/?lang={lang}"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=2000",
        "--dump-dom",
        url
    ]
    
    print(f"\n==========================================")
    print(f"Testing language: {lang.upper()} ({url})")
    print(f"==========================================")
    
    res = subprocess.run(cmd, capture_output=True)
    dom_text = res.stdout.decode('utf-8', errors='ignore')
    
    # We strip out comments and scripts so we test actual rendered DOM text & attributes
    clean_dom = re.sub(r'<!--.*?-->', '', dom_text, flags=re.DOTALL)
    clean_dom = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', clean_dom, flags=re.DOTALL)
    
    # Also find all text inside tags
    text_snippets = re.findall(r'>([^<]+)<', clean_dom)
    arabic_snippets = [t.strip() for t in text_snippets if arabic_regex.search(t) and t.strip()]
    
    # Check attributes (like alt, title, aria-label, placeholder)
    attrs = re.findall(r'(?:title|placeholder|alt|aria-label)="([^"]*)"', clean_dom)
    arabic_attrs = [a for a in attrs if arabic_regex.search(a)]
    
    # Check total Arabic characters in DOM (excluding <style> or script)
    total_arabic_chars = len(arabic_regex.findall(clean_dom))
    
    print(f"Total Arabic characters found in rendered DOM for {lang.upper()}: {total_arabic_chars}")
    
    lines_with_arabic = []
    for line_no, line in enumerate(clean_dom.splitlines(), 1):
        if arabic_regex.search(line):
            lines_with_arabic.append(f"Line {line_no}: {line.strip()}")
            
    if lines_with_arabic:
        print(f"Lines containing Arabic ({len(lines_with_arabic)}):")
        for l in lines_with_arabic:
            print(" ", l)
            
    if total_arabic_chars == 0:
        print(f"PASS: 100% Zero Arabic characters found in {lang.upper()} page!")
    else:
        print(f"FAIL: {total_arabic_chars} Arabic characters still present in {lang.upper()} page.")
        
    return total_arabic_chars

tr_fails = test_language('tr')
en_fails = test_language('en')

sys.exit(tr_fails + en_fails)
