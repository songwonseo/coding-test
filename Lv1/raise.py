# 사용자가 직접 에러를 발생시키는 기능
# raise Exception 에러 종류
# 많이 사용하면 코드를 읽기 어려워진다.

def rsp(mine,yours):
    allowed = ['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
    # 가위바위보 승패를 판단하는 코드
    
try:
    rsp('가위','바')
except ValueError:
    print('잘못된 값을 넣은 것 같습니다.')
    
# 반복문이 중첩되어 있을 때도 한 번의 일을 종료시키는 방법
school = {'1반':[172,185,198,177,165,199], '2반':[165,177,167,181,190]}
try:
    for class_number, students in school.items():
        for student in students:
            if student>190:
                print(class_number, '에 190을 넘는 학생이 있습니다.')
                raise StopIteration
except StopIteration:
    print('정상종료')
    
# 풀이 있으면 문구점의 이름과 가격을 출력
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

for shop, products in shops.items(): # 예) 첫 반복 때 shop = "송일문방구", products = {"가위": 500, "크레파스": 3000}
    for product, price in products.items(): # 예) "가위" → 500, "크레파스" → 3000
        if product =='풀': # 상품 이름이 '풀'인 경우만 찾음
            print("{}: {}원".format(shop, price))
            
# 풀을 파는 가게를 발견하면 for문 전체를 즉시종료
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration # StopIteration은 “더 이상 반복하지 마라”라는 의미의 예외
except StopIteration:
    print("즉시종료")
            