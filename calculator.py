# Simple Calculator
# OSS GitHub Flow Practice


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def divide(a: int, b: int) -> float:
    return a / b


def main():
    print("Simple Calculator")
    print("Addition result:", add(10, 5))
    print("Subtraction result:", subtract(10, 5))
    print("Division result:", divide(10, 2))


if __name__ == "__main__":
    main()
