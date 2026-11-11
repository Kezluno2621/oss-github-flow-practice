# ADR-0001: Python 단위 테스트 도구로 unittest 사용

- 상태: Accepted
- 작성일: 2026-11-11

## 1. 배경 (Context)

OSS GitHub Flow Practice 프로젝트는 Python으로 구현한 간단한 계산기 프로젝트입니다.

계산기의 덧셈, 뺄셈, 나눗셈 기능이 정상적으로 동작하는지 확인하고, 코드 변경 후에도 기존 기능이 유지되는지 검증할 필요가 있습니다.

이를 위해 Python 단위 테스트 도구를 선정하였습니다.

## 2. 결정 (Decision)

Python 표준 라이브러리인 unittest를 단위 테스트 도구로 사용하기로 결정하였습니다.

별도의 외부 패키지를 설치하지 않고 테스트를 작성하고 실행할 수 있도록 구성합니다.

테스트 실행 명령어:

    python -m unittest discover

## 3. 고려한 대안 (Alternatives)

### unittest
- Python 표준 라이브러리에 포함
- 별도의 설치 과정이 필요하지 않음
- 테스트 클래스를 활용한 구조화된 테스트 작성 가능

### pytest
- 간결한 테스트 코드 작성 가능
- 다양한 플러그인 제공
- 별도의 패키지 설치 필요

## 4. 결정 이유 (Rationale)

unittest를 선택한 이유는 다음과 같습니다.

1. Python에 기본적으로 포함되어 있어 설치가 간단합니다.
2. 소규모 계산기 프로젝트에 필요한 테스트 기능을 제공합니다.
3. GitHub Flow 실습에서 테스트 코드 작성 및 리뷰에 집중할 수 있습니다.
4. 외부 의존성을 최소화할 수 있습니다.

## 5. 결과 및 영향 (Consequences)

### 장점
- 별도의 테스트 패키지 설치 불필요
- 간단한 명령어로 테스트 실행 가능
- 기존 계산기 기능에 대한 회귀 테스트 작성 가능
- 프로젝트 환경 구성이 단순함

### 단점
- 일부 테스트에서 pytest보다 코드가 길어질 수 있음
- 다양한 추가 테스트 기능을 사용하려면 별도 구현이 필요할 수 있음

## 6. 관련 자료 (References)

- [Python unittest 공식 문서](https://docs.python.org/3/library/unittest.html)
- [Getting Started Wiki](../../wiki/Getting-Started)
- [Development Guide Wiki](../../wiki/Development-Guide)
