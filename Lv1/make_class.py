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