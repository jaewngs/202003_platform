"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오.

예시
<입력>
print(Triangle(10,20))
<출력>
100
"""

def TriSize(a, b):
    return a * b * 0.5


i, j = input("삼각형의 높이와 가로 길이를 입력하세요 :").split()
i = int(i)
j = int(j)

result = TriSize(i, j)
print("삼각형의 넓이는 : ", result, "입니다.")