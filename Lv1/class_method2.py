class Human():
    '''인간'''
    def __init__(self):
        '''초기화 함수'''
        
    def __str__(self):
        '''문자열화 함수'''

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