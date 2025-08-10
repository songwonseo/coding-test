import random
list = ["빨","주","노","초","파","남","보"]
random_element = random.choice(list)

print(random_element)

"""random.choice(seq)
Return a random element from the non-empty sequence seq. 
If seq is empty, raises IndexError.
비어 있지 않은 시퀀스 seq 에서 임의의 요소를 반환합니다.
seq 가 비어 있으면 에러를 발생시킵니다
"""


random_number = random.randint(2, 5)
print(random_number)
# random_number가 2보다 크거나 같고, 5보다 작거나 같은 임의의 정수를 가지도록 만들기
"""
random.randint(a, b)
a 이상 b 이하 범위에서 정수를 무작위로 하나 골라주는 함수
"""

list = ["빨","주","노","초","파","남","보"]
random.shuffle(list)
print(list)
"""
random.shuffle(x[ ])
리스트(x) 안의 원소 순서를 무작위로 섞어버리는 함수입니다.
리턴값은 없고, 원본 리스트를 직접 변경합니다 (in-place).
기본 랜덤 소스를 쓰지만, 두 번째 인자로 다른 난수 생성 함수를 줄 수도 있습니다.
"""