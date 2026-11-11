# Contributing Guide

## 1. 프로젝트 소개
이 저장소는 OSS 기반 SW 프로그래밍 4주차
GitHub Flow 및 코드리뷰 협업 실습용 프로젝트입니다.

## 2. 브랜치 전략
기본 브랜치는 main입니다.

새 기능은 Feature 브랜치에서 개발합니다.

브랜치 이름 예시:
- feature/addition
- feature/subtraction
- feature/division

## 3. Conventional Commits
커밋 메시지는 다음 규칙을 따릅니다.

- feat: 새로운 기능 추가
- fix: 버그 수정
- docs: 문서 수정
- test: 테스트 추가
- refactor: 코드 개선

예시:
feat: add addition function

## 4. Pull Request
1. main에서 Feature 브랜치를 생성합니다.
2. 기능을 개발하고 커밋합니다.
3. PR 템플릿에 맞춰 설명을 작성합니다.
4. 코드 리뷰를 수행합니다.
5. 피드백을 반영한 후 Merge합니다.

## 5. 코드 리뷰 규칙
- [MUST]: 반드시 수정해야 하는 문제
- [SHOULD]: 개선을 권장하는 사항

자세한 내용은 REVIEW_GUIDE.md를 참고합니다.

## 6. 테스트
변경 사항에 대한 단위 테스트를 작성합니다.

테스트 명령어:
python -m unittest discover
