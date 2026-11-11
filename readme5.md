# OSS 5주차: 비동기 협업 체계 구축

## 1. 실습 개요

OSS 기반 SW 프로그래밍 5주차 과제로 GitHub Wiki, ADR, Discussions를 활용한 비동기 협업 환경을 구축하였습니다.

프로젝트의 사용 방법과 개발 규칙을 문서화하고, 기술적 의사결정 및 협업 자동화 방안을 정리하였습니다.

## 2. GitHub Wiki 구축

프로젝트 사용 및 개발에 필요한 Wiki 문서 3개를 작성하고 상호 링크를 연결하였습니다.

| 문서 | 주요 내용 |
|---|---|
| Getting Started | 프로젝트 설치, 실행 및 테스트 방법 |
| Development Guide | Feature 브랜치, Conventional Commits, PR 및 코드 리뷰 규칙 |
| Troubleshooting | Python 실행 오류, 테스트 실패, GitHub 협업 문제 해결 |

### Wiki 바로가기

- [Wiki Home](https://github.com/Kezluno2621/oss-github-flow-practice/wiki)
- [Getting Started](https://github.com/Kezluno2621/oss-github-flow-practice/wiki/Getting-Started)
- [Development Guide](https://github.com/Kezluno2621/oss-github-flow-practice/wiki/Development-Guide)
- [Troubleshooting](https://github.com/Kezluno2621/oss-github-flow-practice/wiki/Troubleshooting)

각 문서에 관련 문서 링크를 추가하여 Wiki 페이지 간 이동이 가능하도록 구성하였습니다.

## 3. ADR (기술결정기록) 작성

기술적 의사결정 과정과 선택 근거를 기록하기 위해 ADR 문서 구조를 구성하였습니다.

### 작성 파일

- `docs/adr/0000-template.md`
- `docs/adr/0001-use-unittest.md`

### 주요 기술 결정

Python 계산기 프로젝트의 단위 테스트 도구로 unittest를 선택한 이유를 기록하였습니다.

- Python 표준 라이브러리 활용
- 외부 패키지 의존성 최소화
- 간단한 테스트 환경 구성
- pytest와의 장단점 비교

[ADR 문서 확인](https://github.com/Kezluno2621/oss-github-flow-practice/tree/main/docs/adr)

## 4. 비동기 협업 자동화 워크플로우 설계

`docs/workflows/WORKFLOW_DESIGN.md`에 다음 세 가지 자동화 워크플로우의 설계 초안을 작성하였습니다.

### Issue 자동 응답
- 새로운 Issue 생성 시 접수 안내 댓글 작성
- 문제 재현 방법과 추가 정보 요청

### SLA 추적
- Issue 생성 후 24시간 이내 최초 응답 목표 설정
- 응답 시간 및 기준 초과 여부 추적 방안 설계

### 주간 요약
- 매주 GitHub 협업 활동을 요약하는 방식 설계
- Issue 및 PR 생성, 종료, Merge 현황 집계

본 워크플로우는 설계 초안으로, 실제 자동화 기능은 구현하지 않았습니다.

[워크플로우 설계 문서](https://github.com/Kezluno2621/oss-github-flow-practice/blob/main/docs/workflows/WORKFLOW_DESIGN.md)

## 5. GitHub Discussions 구성

GitHub Discussions를 활성화하여 비동기 토론 환경을 구축하였습니다.

### 카테고리 설계
- RFC - Proposals: 기능 및 기술 개선 제안
- General: 일반적인 프로젝트 논의
- Q&A: 개발 및 사용 관련 질문
- Ideas: 새로운 아이디어 공유

### RFC 토론 실습

RFC-001: 계산기 곱셈 기능 추가 제안

기존 계산기 프로젝트에 곱셈 기능을 추가하는 방안을 제안하고 검토하였습니다.

주요 논의 내용:
- 곱셈 기능 추가의 필요성
- 입력 자료형 및 예외 상황 고려
- 단위 테스트 작성 범위
- 기능 추가에 따른 기대 효과

제안, 자체 검토 의견, 결정 및 후속 작업을 기록하여 RFC 기반 비동기 의사결정 과정을 실습하였습니다.

[GitHub Discussions 바로가기](https://github.com/Kezluno2621/oss-github-flow-practice/discussions)

## 6. 실습 결과

이번 5주차 과제를 통해 다음 활동을 수행하였습니다.

- GitHub Wiki 문서 3개 작성 및 상호 링크 연결
- ADR 템플릿 및 기술 결정 사례 작성
- 자동 응답, SLA 추적, 주간 요약 워크플로우 초안 설계
- GitHub Discussions 활성화 및 카테고리 설계
- RFC 형식의 기능 개선 제안 및 토론 실습

이를 통해 GitHub를 활용한 비동기 협업 문서화와 기술적 의사결정 관리 방법을 학습하였습니다.
