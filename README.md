> 📚 **학습 아카이브** — 이 저장소는 학습 과정에서 만든 기록을 보관하는 아카이브입니다.
> 코드는 학습 당시 작성된 그대로 두며, 별도 업데이트 예정이 없습니다.
> 📚 **Learning Archive** — This repo preserves my learning journey. Code is kept as-is.

---
# Mission Computer Log Parser

파이썬 PBL 과제 문서입니다.  
로그 파일을 파싱하고, 리스트 및 딕셔너리로 변환 후 JSON 파일로 저장하는 과제를 수행합니다.

---

## ✅ 수행 과제

- `mission_computer_main.log` 파일을 읽어 들여 출력한다.
- 콤마(`,`)를 기준으로 날짜 및 시간과 로그 내용을 분류하여 **Python의 리스트(List) 객체**로 전환한다.  
  > (여기서 말하는 리스트는 배열이 아니라 파이썬에서 제공하는 `list` 타입의 객체를 의미한다.)
- 전환된 리스트 객체를 화면에 출력한다.
- 리스트 객체를 **시간의 역순**으로 정렬(`sort`)한다.
- 리스트 객체를 **사전(Dict) 객체**로 전환한다.
- 사전 객체로 전환된 내용을 `mission_computer_main.json` 파일로 저장한다.  
  - 저장 시 파일 포맷은 **JSON (JavaScript Object Notation)** 이어야 한다.

---

## ✅ 로그 파일 예시

`mission_computer_main.log`


---

## ✅ 실행 흐름

1. 로그 파일 읽기
2. 콤마로 분리 → 리스트로 변환
3. 리스트 출력
4. 시간 역순 정렬
5. 리스트 → 딕셔너리 변환
6. JSON 파일 저장

---

## ✅ 사용 기술

- Python 3.x
- 파일 입출력
- 리스트(List) 자료형
- 사전(Dict) 자료형
- JSON 파일 처리

---

## ✅ JSON 파일 설명

- JSON은 **Key-Value 쌍**으로 이루어진 데이터 포맷입니다.
- 파이썬의 `dict`와 1:1로 대응되며, 데이터 교환 및 저장 시 많이 사용됩니다.

---

## ✅ 실행 방법

아래 명령어로 실행할 수 있습니다.

```bash
python main.py
