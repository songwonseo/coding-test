class Human():
    '''인간'''
    
# person = Human()
# person.name = '철수'
# person.weight = 60.5

def create_human(name, weight): # 사람을 생성하는 함수
    person = Human() # 인자로 받은 name, weight로 새 Human 객체를 만들고
    person.name = name # 그 값을 객체의 속성으로 저장
    person.weight = weight
    return person # person 객체 반환

# p = create_human("철수", 60.5)하면,
# p.name == '철수', p.weight == 60.5인 Human 객체가 만들어져요.

Human.create = create_human # craete_human 함수를 Human 클래스의 속성으로 등록
                            # Human이 새로운 기능 create를 갖게 된 것(원래 클래스 안에 없던 함수를 붙인 것)
person = Human.create("철수", 60.5) # 이제 이렇게 쓸 수 있음 / Person = create_human("철수", 60.5)와 같음

def eat(person):
    person.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))
    
def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))
    
Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()