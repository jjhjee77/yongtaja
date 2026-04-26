# -*- coding: utf-8 -*-
"""yy-game (용용이) 타이틀 배경 영상을 main영상.mp4 로 교체."""
import base64
import re
import sys
from pathlib import Path

HTML_PATH  = Path(r"C:\Users\user\Desktop\yy-game\antigravity-korean.html")
VIDEO_PATH = Path(r"C:\Users\user\Desktop\photo-app\public\타자놀이\main영상.mp4")

print(f"Reading new video: {VIDEO_PATH}")
video_b64 = base64.b64encode(VIDEO_PATH.read_bytes()).decode("ascii")
print(f"  -> {len(video_b64):,} chars of base64")

print(f"Reading HTML: {HTML_PATH}")
html = HTML_PATH.read_text(encoding="utf-8")

pattern = re.compile(
    r'(<source\s+src=")data:video/mp4;base64,[A-Za-z0-9+/=]*(" type="video/mp4">)'
)
m = pattern.search(html)
if not m:
    print("ERROR: title video <source> not found")
    sys.exit(1)

new_src = f'{m.group(1)}data:video/mp4;base64,{video_b64}{m.group(2)}'
new_html = html[: m.start()] + new_src + html[m.end():]

HTML_PATH.write_text(new_html, encoding="utf-8")
print(f"Done. {len(html):,} -> {len(new_html):,} chars")
