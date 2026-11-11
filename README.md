# OSS GitHub Flow Practice

## 프로젝트 소개
OSS 기반 SW 프로그래밍 4주차 GitHub Flow 및 코드리뷰 협업 실습을 위한 Python 계산기 프로젝트입니다.

## 실습 목표
- Feature 브랜치를 활용한 기능 개발
- Conventional Commits 형식 적용
- Pull Request 생성 및 Merge
- [MUST] / [SHOULD] 태그를 활용한 코드 리뷰
- 리뷰 피드백 반영 및 코드 개선

## 구현 기능
- 덧셈: add(a, b)
- 뺄셈: subtract(a, b)
- 나눗셈: divide(a, b)
- 0으로 나누는 경우 예외 처리
- unittest 기반 단위 테스트 코드

## Pull Request 작업 내역

| PR | 작업 내용 | 커밋 유형 |
|---|---|---|
| #1 | 덧셈 기능 추가 및 테스트 | feat, refactor, test |
| #2 | 뺄셈 기능 추가 및 테스트 | feat, test |
| #3 | 나눗셈 기능 및 예외 처리 | feat, fix, test |

## 코드 리뷰 실습
각 PR에서 [MUST]와 [SHOULD] 태그를 사용하여 코드 리뷰를 작성하고, 피드백을 반영해 코드를 개선했습니다.

- [MUST]: 반드시 수정해야 하는 문제
- [SHOULD]: 개선을 권장하는 사항

## 협업 환경
- PR 템플릿: .github/PULL_REQUEST_TEMPLATE.md
- 브랜치 명명 규칙: feature/기능명
- 커밋 메시지: Conventional Commits 적용

## 테스트 실행 방법

```bash
python -m unittest discover
```

## 과제 정보
- 과목: OSS 기반 SW 프로그래밍
- 주차: 4주차
- 과제명: GitHub Flow 및 코드리뷰 협업 실습
  
