# -*- coding: utf-8 -*-
import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = r"C:\Users\Hp\.gemini\antigravity\brain\13efcc79-f855-421d-a9b1-8498f1e46b91"

shots = [
    {
        "url": "http://localhost:8080/?lang=tr",
        "file": os.path.join(out_dir, "preview-turkish-desktop.png"),
        "size": "1440,1050"
    },
    {
        "url": "http://localhost:8080/?lang=en",
        "file": os.path.join(out_dir, "preview-english-desktop.png"),
        "size": "1440,1050"
    },
    {
        "url": "http://localhost:8080/?lang=tr",
        "file": os.path.join(out_dir, "preview-turkish-mobile.png"),
        "size": "390,844"
    },
    {
        "url": "http://localhost:8080/?lang=en",
        "file": os.path.join(out_dir, "preview-english-mobile.png"),
        "size": "390,844"
    },
    {
        "url": "http://localhost:8080/#calculator?lang=tr",
        "file": os.path.join(out_dir, "preview-turkish-calc.png"),
        "size": "1440,1050"
    },
    {
        "url": "http://localhost:8080/#calculator?lang=en",
        "file": os.path.join(out_dir, "preview-english-calc.png"),
        "size": "1440,1050"
    }
]

for s in shots:
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={s['size']}",
        f"--screenshot={s['file']}",
        "--virtual-time-budget=2000",
        s["url"]
    ]
    subprocess.run(cmd)
    print(f"Captured: {s['file']}")
