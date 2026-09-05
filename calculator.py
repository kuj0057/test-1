def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return num1 / num2
    else:
        raise ValueError("지원하지 않는 연산자입니다. (+, -, *, / 만 가능)")


def main():
    print("=== 간단한 계산기 ===")
    print("종료하려면 'q'를 입력하세요.\n")

    while True:
        num1_input = input("첫 번째 숫자: ")
        if num1_input.lower() == "q":
            break

        op = input("연산자 (+, -, *, /): ")
        if op.lower() == "q":
            break

        num2_input = input("두 번째 숫자: ")
        if num2_input.lower() == "q":
            break

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
            result = calculate(num1, op, num2)
            print(f"결과: {num1} {op} {num2} = {result}\n")
        except ValueError as e:
            print(f"오류: {e}\n")


if __name__ == "__main__":
    main()
