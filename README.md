# 용용 타자 오름길 (Yong Typing)

한글 타자 학습 웹 게임. Firebase Hosting + Realtime Database로 운영.

## 🌐 라이브 사이트
[https://yongtaja.web.app](https://yongtaja.web.app)

## 🎮 주요 기능
- **4단계 인증 도전 시스템**: 초보자(40K) / 중급자(100K) / 고수(1M) / 달인(10M)
- **15단계 점진 학습**: 받침 없는 1글자부터 6글자까지
- **무한 도전 + 전체 순위 TOP 20** (Firebase 실시간 DB)
- **인증서 발급 + 이미지 저장** (PNG 다운로드)
- **풀 모드 키보드 단축키** (F11 / Ctrl+Shift+1~4 미리보기)

## 📁 파일 구조
| 파일 | 역할 |
|------|------|
| `antigravity-korean.html` | 게임 본체 (16MB, base64 임베드) |
| `cert-preview.html` | 인증서 4종 미리보기 (관리자용) |
| `firebase.json` | Firebase Hosting 설정 |
| `.firebaserc` | Firebase 프로젝트 매핑 |
| `database.rules.json` | Realtime DB 보안 규칙 (다른 폴더에서 관리) |
| `replace_title_video.py` | 타이틀 배경 영상 교체 스크립트 |
| `replace_player_sprite.py` | 플레이어 캐릭터 스프라이트 교체 스크립트 |

## 🚀 배포 방법
```bash
firebase deploy --only hosting:yongtaja
```

## 🛠 자료 교체 스크립트
새 영상/캐릭터로 갈아끼울 때:
```bash
python replace_title_video.py     # 타이틀 영상
python replace_player_sprite.py   # 플레이어 캐릭터
```

## 📊 데이터베이스
- 랭킹 path: `/yong-ranks` (풍풍이 사이트의 `/pung-ranks`와 분리됨)
- 프로젝트: `adys2026-8da59`

---

🐉 **용용이 캐릭터** + 🎬 **간판 영상** + 🥇 **YY TYPING 메달**
