"""
클래스 만들기

클래스 선언
class Human( ):
    '''사람'''
    
인스턴스 생성
person1 = Human( )
person2 = Human( )

클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있다.
"""

class Human():
    '''사람'''
person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

# print(person1.language)
# print(person2.language)

person1.name = '서울시민'
person2.name = '인도인'

def speak(person):  # 클래스 밖의 함수, person(단순한 변수 이름)이라는 매개변수를 받음
    # 함수를 호출할 때 객체를 인자로 전달하면, 이 변수(person)이 그 객체를 가리키게 됨
    # 객체를 받아서 그 객체의 name과 language 속성을 이용
    # speak(person1)라고 하면, person은 함수 안에서 person1과 같은 객체를 가리키게 됨
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))

# speak(person1)
# speak(person2)

Human.speak = speak # 클래스 안의 함수

# person1.speak()
# person2.speak()

person1.speak()
speak(person2)
    