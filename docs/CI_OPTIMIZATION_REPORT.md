# GitHub Actions 워크플로우 최적화 비교 리포트

## 1. 실습 목적

OSS 기반 SW 프로그래밍 8주차 과제로 GitHub Actions의 재사용, Matrix 확장, 캐싱 및 조건부 실행 기능을 적용하고 실행 성능을 분석하였다.

## 2. 적용한 최적화 기법

- Composite Action으로 공통 Lint/Test 단계 재사용
- Reusable Workflow로 테스트 Job 중복 제거
- Ubuntu, Windows, macOS × Python 3.11, 3.12, 3.13의 9개 조합 테스트
- pip 패키지 다운로드 캐싱 적용
- 변경 파일 감지 및 브랜치/PR 조건부 실행
- 조건부 모의 배포 파이프라인 구성

## 3. 캐싱 전후 실행 시간 비교

| 구분 | 실행 시간 | 결과 |
|---|---|---|
| 캐싱 OFF (#2) | 50초 | 성공 |
| 캐싱 ON 최초 (#3) | 50초 | 성공 |
| 캐싱 ON 재실행 (#4) | 53초 | 성공 |

### 실행 시간 개선률

(50 - 53) / 50 × 100 = **-6%**

캐싱 적용 후 전체 실행 시간이 3초 증가하였다.

### Ubuntu / Python 3.12 Job 비교

| 구분 | Job 실행 시간 |
|---|---|
| 캐싱 OFF | 9초 |
| 캐싱 ON 최초 | 14초 |
| 캐싱 ON 재실행 | 9초 |

해당 Job의 캐싱 전후 실행 시간은 동일하였다.

## 4. 결과 분석

캐싱 기능은 정상적으로 실행되었지만 전체 워크플로우의 실행 시간 감소는 관찰되지 않았다.

가능한 원인은 다음과 같다.

- 패키지 설치 대상이 Ruff 하나로 비교적 작음
- 캐시 조회 및 복원 과정에서 추가 작업 발생
- Matrix 테스트의 병렬 실행 및 Runner 실행 환경에 따른 변동
- 네트워크 상태에 따라 패키지 설치 시간이 달라질 수 있음

전체 워크플로우 실행 시간은 캐싱 성능만으로 결정되지 않는다.

캐시 적중 여부는 개별 실행 로그에서 추가 확인이 필요하다.

## 5. 최적화 전후 구조 비교

| 항목 | 7주차 기존 CI/CD | 8주차 최적화 CI/CD |
|---|---|---|
| Matrix | 4개 조합 | 9개 조합 |
| Reusable Workflow | 없음 | 적용 |
| Composite Action | 없음 | 적용 |
| 캐싱 | 없음 | 적용 |
| 변경 파일 감지 | 없음 | 적용 |
| 조건부 배포 | PR 제외 | 브랜치 및 변경 파일 조건 적용 |

## 6. 결론

GitHub Actions 워크플로우에 재사용 구조, Matrix 확장, 캐싱 및 조건부 실행을 적용하였다.

캐싱 실험에서는 실행 시간 단축이 확인되지 않았으나, 공통 테스트 로직을 재사용하고 코드 변경 여부에 따라 실행을 제어하는 구조를 구축하였다.

향후 반복 측정 및 패키지 의존성 변화에 따른 캐싱 효과를 추가 분석할 수 있다.

## 7. 실행 기록

- [캐싱 OFF 실행 #2](https://github.com/Kezluno2621/oss-github-flow-practice/actions/runs/43578278254)
- [캐싱 ON 최초 실행 #3](https://github.com/Kezluno2621/oss-github-flow-practice/actions/runs/43578392247)
- [캐싱 ON 재실행 #4](https://github.com/Kezluno2621/oss-github-flow-practice/actions/runs/43578531047)
- [최적화 워크플로우](https://github.com/Kezluno2621/oss-github-flow-practice/blob/main/.github/workflows/optimized-ci.yml)
