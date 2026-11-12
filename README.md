# OSS GitHub Flow Practice

## 프로젝트 소개
OSS 기반 SW 프로그래밍 4주차 GitHub Flow 및 코드리뷰 협업 실습을 위한 Python 계산기 프로젝트입니다.

[[5주차] 비동기 협업 체계 구축 (Discussions/Wiki/ADR)](readme5.md)

[[6주차] 오픈소스 실습 및 Inner Source 계획](readme6.md)

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

## GitHub 협업 환경 구성 (선택 과제)

OSS 기반 SW 프로그래밍 4주차 실습의 선택 과제로 GitHub 협업 환경을 구성하고, 코드 관리 및 리뷰 규칙을 문서화하였습니다.

### 1. PR 템플릿 설정

- `.github/PULL_REQUEST_TEMPLATE.md` 파일 생성
- PR 생성 시 변경 사항, 작업 유형, 테스트 내용 등을 작성할 수 있도록 템플릿 구성
- PR 작성 형식을 표준화하여 변경 사항을 쉽게 파악할 수 있도록 개선

### 2. CODEOWNERS 설정

- `.github/CODEOWNERS` 파일 생성
- 프로젝트의 기본 코드 관리자를 지정
- Python 소스 코드 및 GitHub 설정 파일의 담당자를 명시

### 3. 팀 협업 가이드 작성

- `CONTRIBUTING.md` 파일을 통해 프로젝트 기여 규칙 문서화
- Feature 브랜치 명명 규칙 및 Conventional Commits 작성 기준 정리
- PR 생성, 코드 리뷰, 피드백 반영 및 Merge 절차 정의

### 4. 코드 리뷰 가이드 작성

- `REVIEW_GUIDE.md` 파일 생성
- `[MUST]`: 반드시 수정해야 하는 오류 및 필수 개선 사항
- `[SHOULD]`: 코드 가독성, 유지보수성 등을 높이기 위한 권장 사항
- 코드 리뷰 체크리스트와 리뷰 진행 절차 문서화

### 5. 브랜치 보호 규칙 설정

GitHub Rulesets 기능을 활용하여 `main` 브랜치 보호 규칙을 구성하였습니다.

| 설정 항목 | 적용 내용 |
|---|---|
| Ruleset Name | `main-branch-protection` |
| Enforcement status | Active |
| Target branch | `main` |
| Restrict deletions | 활성화 |
| Block force pushes | 활성화 |

이를 통해 기본 브랜치의 실수로 인한 삭제 및 강제 푸시를 방지하도록 설정하였습니다.

### 6. 실습 결과

이번 실습을 통해 다음과 같은 GitHub 협업 과정을 경험하였습니다.

- Feature 브랜치를 활용한 독립적인 기능 개발
- Conventional Commits 형식의 커밋 관리
- Pull Request 생성 및 Merge
- `[MUST]` / `[SHOULD]` 태그를 활용한 코드 리뷰
- 리뷰 피드백 반영을 통한 코드 개선
- PR 템플릿 및 CODEOWNERS 설정
- 협업 문서 작성 및 브랜치 보호 규칙 구성

GitHub Flow의
  
