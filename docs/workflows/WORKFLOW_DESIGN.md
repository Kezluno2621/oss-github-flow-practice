# 비동기 협업 자동화 워크플로우 설계

## 1. 개요

OSS 기반 SW 프로그래밍 5주차 실습의 일환으로 GitHub 기반 비동기 협업 자동화 워크플로우를 설계합니다.

다음 세 가지 워크플로우를 대상으로 합니다.

- Issue 자동 응답
- SLA 응답 시간 추적
- 주간 협업 활동 요약

본 문서는 구현 전 설계 초안이며, 실제 자동화 기능은 아직 적용하지 않았습니다.

## 2. Issue 자동 응답 워크플로우

### 목적
새로운 Issue가 생성되었을 때 접수 안내 댓글을 자동으로 작성하여 요청자가 처리 절차를 알 수 있도록 합니다.

### 실행 조건
- GitHub Issue가 새로 생성되었을 때
- GitHub Actions 이벤트: issues.opened

### 처리 절차
1. 새로운 Issue 생성 감지
2. Issue 제목과 작성자 확인
3. 접수 안내 댓글 자동 작성
4. 담당자의 추후 확인 대기

### 자동 응답 예시
안녕하세요. Issue가 정상적으로 접수되었습니다.

문제 상황, 재현 방법, 예상 결과를 작성해 주세요.
담당자가 내용을 확인한 후 답변하겠습니다.

이 댓글은 자동으로 작성된 접수 안내이며, 담당자가 직접 검토했다는 의미는 아닙니다.

## 3. SLA 추적 워크플로우

### 목적
Issue에 대한 최초 응답 시간을 추적하여 협업 요청이 장기간 방치되지 않도록 합니다.

### SLA 기준 (실습용)
- 최초 응답 목표: Issue 생성 후 24시간 이내
- 추적 대상: 새로 생성된 Issue
- 자동 응답 댓글은 최초 담당자 응답으로 계산하지 않음

### 처리 절차
1. Issue 생성 시각 기록
2. 담당자의 최초 응답 시각 확인
3. 두 시각의 차이 계산
4. 24시간 초과 여부 판단
5. 미응답 또는 기준 초과 Issue를 보고 대상으로 분류

### 예시
- Issue 생성: 월요일 10:00
- 담당자 최초 응답: 월요일 15:00
- 응답 소요 시간: 5시간
- SLA 결과: 준수

## 4. 주간 요약 워크플로우

### 목적
한 주 동안의 GitHub 협업 활동을 정리하여 프로젝트 진행 상황을 공유합니다.

### 실행 조건
- 매주 일요일 21:00 (한국 시간 기준)
- GitHub Actions의 schedule 이벤트 활용 예정

### 요약 항목
- 신규 Issue 수
- 종료된 Issue 수
- 생성된 PR 수
- Merge된 PR 수
- SLA 기준 초과 Issue 수
- 주요 개발 및 문서 변경 사항

### 출력 예시
주간 OSS 협업 요약

기간: 월요일 ~ 일요일

- 신규 Issue: 2건
- 종료된 Issue: 1건
- 생성된 PR: 3건
- Merge된 PR: 2건
- SLA 기준 초과: 0건

위 수치는 워크플로우 출력 형식을 보여주기 위한 예시입니다.

## 5. 향후 구현 계획

### 자동 응답
GitHub Actions와 GitHub API를 이용해 Issue 생성 시 접수 댓글을 작성합니다.

### SLA 추적
Issue 생성 시간과 담당자 응답 시간을 비교하고, 기준 초과 여부를 기록합니다.

### 주간 요약
예약 실행을 통해 Issue 및 PR 활동 내역을 수집하고 요약 문서를 생성합니다.

## 6. 기대 효과

- 반복적인 안내 업무 감소
- 협업 요청에 대한 응답 지연 확인
- GitHub 활동 기록의 체계적 관리
- 비동기 협업의 투명성 향상

## 7. 참고 자료

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Getting Started Wiki](https://github.com/Kezluno2621/oss-github-flow-practice/wiki/Getting-Started)
- [Development Guide Wiki](https://github.com/Kezluno2621/oss-github-flow-practice/wiki/Development-Guide)
  
