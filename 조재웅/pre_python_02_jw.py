""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오

예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *
<출력>
150
"""
i = int(input("첫 번째 수를 입력하세요 : "))

j = int(input("두 번째 수를 입력하세요 : "))

op = input("어떤 연산을 하실 건가요? : ")

if i >= j:

    if op == '+':

        result = i + j

    elif op == '-':

        result = i - j

    elif op == '*':

        result = i * j

    elif op == '/':

        result = i / j

    elif op == '%':

        result = i % j

    else:

        print("입력하신 연산자는 지원하지 않습니다.")



else:

    if op == '+':

        result = j + i

    elif op == '-':

        result = j - i

    elif op == '*':

        result = j * i

    elif op == '/':

        result = j / i

    elif op == '%':

        result = j % i

    else:

        print("입력하신 연산자는 지원하지 않습니다.")

print(result)