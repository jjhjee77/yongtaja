# -*- coding: utf-8 -*-
"""
yy-game (용용이) 플레이어 스프라이트시트를 주인공.png 로 교체.
주인공.json 에 정의된 프레임 좌표를 SPRITE_FRAMES 에 적용.
"""
import base64, json, re
from pathlib import Path

HTML       = Path(r"C:\Users\user\Desktop\yy-game\antigravity-korean.html")
SPRITE_PNG = Path(r"C:\Users\user\Desktop\photo-app\public\타자놀이\주인공.png")
SPRITE_JSON= Path(r"C:\Users\user\Desktop\photo-app\public\타자놀이\주인공.json")

# 1. 스프라이트 PNG → base64
b64 = base64.b64encode(SPRITE_PNG.read_bytes()).decode("ascii")
print(f"sprite sheet base64: {len(b64):,} chars")

# 2. 프레임 좌표 (JSON 파일에서 읽음)
frames = json.loads(SPRITE_JSON.read_text(encoding="utf-8"))
print(f"frames: {frames}")
# JSON 형식: [{name, x, y, width, height}, ...]
F = []
for f in frames[:2]:  # 최대 2 프레임 사용
    F.append({"x": f["x"], "y": f["y"], "w": f["width"], "h": f["height"]})

# 3. HTML 읽기
html = HTML.read_text(encoding="utf-8")

# 4. SPRITE_SHEET 의 base64 src 교체
pattern_sheet = re.compile(
    r"(const SPRITE_SHEET = \(\(\) => \{\s*const img = new Image\(\);\s*img\.src = ')[^']+(';\s*return img;\s*\}\)\(\);)",
    re.DOTALL,
)
m = pattern_sheet.search(html)
if not m:
    raise SystemExit("SPRITE_SHEET 찾기 실패")

new_src = f"data:image/png;base64,{b64}"
new_block = m.group(1) + new_src + m.group(2)
html = html[:m.start()] + new_block + html[m.end():]

# 5. SPRITE_FRAMES 교체
frame_pattern = re.compile(r"const SPRITE_FRAMES = \[[^\]]+\];", re.DOTALL)
new_frames_js = (
    "const SPRITE_FRAMES = [\n"
    f"  {{x:{F[0]['x']}, y:{F[0]['y']}, w:{F[0]['w']}, h:{F[0]['h']}}},\n"
    f"  {{x:{F[1]['x']}, y:{F[1]['y']}, w:{F[1]['w']}, h:{F[1]['h']}}}\n"
    "];"
)
m2 = frame_pattern.search(html)
if not m2:
    raise SystemExit("SPRITE_FRAMES 찾기 실패")
html = html[:m2.start()] + new_frames_js + html[m2.end():]

HTML.write_text(html, encoding="utf-8")
print(f"HTML 업데이트 완료. 새 파일 크기: {len(html):,} chars")
