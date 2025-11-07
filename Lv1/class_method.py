# 클래스 내부에 메서드를 정의해서 Human 객체(사람)를 만들고,
# 그 사람이 행동하는 과정을 보여주는 예제

# 함수 vs 메서드
# | 구분        | 함수(Function)  | 메서드(Method)                |
# | --------- | ------------- | -------------------------- |
# | 정의 위치     | 클래스 밖         | 클래스 안                      |
# | 호출 방식     | `함수이름()`      | `객체이름.메서드이름()`             |
# | 첫 번째 매개변수 | 자유롭게 지정       | `self` (자기 자신 객체를 가리킴) |
# | 예시        | `print("안녕")` | `person.eat()`             |


class Human():
    '''인간'''

    def create(name, weight): # 사람을 생성하는 함수
        person = Human() # 인자로 받은 name, weight로 새 Human 객체를 만들고
        person.name = name # 그 값을 객체의 속성으로 저장
        person.weight = weight
        return person # person 객체 반환

    def eat(self): # 자기 자신 객체(person이 호출하면 self == person)
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
        
    def walk(person):
        person.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))
        
    def speak(self, message):
        print(message)


person = Human.create("철수", 60.5) 

person.speak("안녕하세요.")




# solution
# class Car():
#     '''자동차'''


# def run(car):
#     print("{}가 달립니다.".format(car.name))

# taxi = Car()
# taxi.name = "택시"
# taxi.run()

# 클래스 밖에 정의 되어 있는 run 함수를 클래스 안으로 가져오기 vvvv

class Car():
    '''자동차'''
    def run(self): # 자동차가 달리는 행동을 정의한 메서드
        print("{}가 달립니다.".format(self.name)) # 객체마다 독립적으로 작동하기 위해 객체 자신을 가리키는 self사용

taxi = Car()
taxi.name = "택시" # 객체에 이름 속성 추가
taxi.run()
