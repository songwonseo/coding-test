"""
인스턴스 이해

클래스
함수나 변수들을 모아 놓은 집합체

인스턴스
클래스에 의해 생성된 객체
인스턴스 각자 자신의 값을 가지고 있다.
"""

# instance_solution
list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
    print("당연히 list1과 list1은 같은 인스턴스입니다.")

if list1 == list2:
    print("list1과 list2의 값은 같습니다.")
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다.")
        
# instance_solution2
list1 = list(range(10))
list2 = [1, 2, 3]

if isinstance(list1, list) and isinstance(list2, list):
    print("list1과 list2는 둘 다 list클래스 입니다.")