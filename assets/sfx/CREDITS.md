# 효과음 출처 (모두 CC0 — 퍼블릭 도메인)

| 팩 | 저자 | 라이선스 | 받은 곳 |
|---|---|---|---|
| The Essential Retro Video Game Sound Effects Collection [512 sounds] | Juhani Junkala | CC0 1.0 | https://opengameart.org/content/512-sound-effects-8-bit-style |
| Music Jingles | Kenney (kenney.nl) | CC0 1.0 | https://kenney.nl/assets/music-jingles |

CC0라 표기 의무는 없지만 감사의 뜻으로 적어 둡니다.

## 원본 → 게임 파일

| 게임 파일 | 용도 | 원본 (팩) |
|---|---|---|
| key.m4a | 타자 한 글자 | sfx_menu_move4.wav (Juhani) |
| fire.m4a | 단어 완성 → 미사일 발사 | sfx_wpn_laser8.wav (Juhani) |
| hit.m4a | 미사일 명중(적 생존) | sfx_damage_hit6.wav (Juhani) |
| kill.m4a | 적 처치 | sfx_exp_shortest_soft8.wav (Juhani) |
| miss.m4a | 오타 | sfx_sounds_error10.wav (Juhani) |
| combo.m4a | 콤보 달성 | sfx_sounds_pause4_in.wav (Juhani) |
| levelup.m4a | 레벨업 | jingles_NES03.ogg (Kenney) |
| pick.m4a | 카드 선택 | sfx_sounds_button6.wav (Juhani) |
| boss.m4a | 보스 등장 | sfx_alarm_loop7.wav ×2회 반복 (Juhani) |
| bossdown.m4a | 보스 격파 | sfx_exp_medium7.wav + sfx_sounds_fanfare1.wav 겹침 (Juhani) |
| zap.m4a | 연쇄 번개 | sfx_sounds_high2.wav (Juhani) |
| beam.m4a | 레이저 빔 | sfx_wpn_laser1.wav (Juhani) |
| orbit.m4a | 회전 별 부딪힘 | sfx_sounds_Blip3.wav (Juhani) |
| petal.m4a | 유도 꽃잎 명중 | sfx_coin_single2.wav (Juhani) |
| damage.m4a | 보호막 잃음 | sfx_sounds_damage3.wav (Juhani) |
| gameover.m4a | 게임 오버 | jingles_NES11.ogg (Kenney) |
| cert.m4a | 인증서 획득 | jingles_NES12.ogg (Kenney) |
| click.m4a | UI 버튼 | sfx_sounds_button12.wav (Juhani) |
| wave.m4a | 새 웨이브 알림 | jingles_NES09.ogg (Kenney) |

가공: 모노 44.1kHz, 앞뒤 무음 제거, 로우패스로 고음 완화, 페이드, 피크 정규화, AAC 64kbps.
재생성: `/usr/bin/python3 scripts/build_sfx.py` (팩은 art/sfx_src/ 에 자동 다운로드)

## 뱀서류 게임에서 가져온 효과음 (2026-09-29 교체)
- 출처: **Mocas-12/no-survivor-game** (GitHub, Godot 뱀서류 슈팅) — `assets/sounds/*.wav`
- 라이선스: MIT (© Mocas-12) — 저장소 README: "Code & generated art/audio: MIT License", 소리는 tools/gen_sounds.py 로 합성된 것
- 대응: shoot→fire · hit→hit · explode→kill · levelup→levelup · boss_die→bossdown · warning→boss · gameover→gameover · pickup→combo · transform→beam
- 이전 Juhani Junkala 버전은 art/sfx_juhani_prev/ 에 보관(되돌리기용)

## 배경음악
- assets/bgm/battle.m4a — Juhani Junkala, Retro Game Music Pack / Chiptune Adventures (CC0, opengameart.org) — 환경몬고 trainer.m4a 를 모노 56kbps 로 재인코딩
