"""
예외 이름을 모르는 경우 처리 방법
try:
    # 에러가 발생할 가능성이 있는 코드
except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다', ex) 
    # ex는 발생한 에러의 이름을 받아오는 변수
"""
try:
    list = []
    print(list[0]) # 에러가 발생했습니다. list index out of range

    text = 'abc'
    number = int(text) # 에러가 발생했습니다. invalid literal for int() with base 10: 'abc'
except Exception as ex:
    print('에러가 발생했습니다.',ex)
    
# except 뒤에 에러 종류를 적지 않아도 에러가 발생했다고 뜨지만,
# 둘 중 어느 곳에 어떤 에러가 발생했는지는 나오지 않기 때문에
# except Exception as ex: 를 사용하고 발생한 에러의 정보를 ex에 담아서 가져옴