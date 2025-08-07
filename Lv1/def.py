a = 5
b = 7

#이 아래줄에 a와 b를 더해서 result에 저장하는 함수add를 만들어 보세요.
def add():
    result = a + b #함수 내부의 코드가 되려면 이 줄은 들여쓰기 되어야 합니다.
    print(result) #함수 내부의 코드가 되려면 이 줄은 들여쓰기 되어야 합니다.
#이 아래에서 add함수를 사용해 보세요.
add()

###
def add(a,b):
    #함수 add에서 a와 b를 입력받아서 두 값을 더한 값을 result에 저장하고 출력하도록 만들어 보세요.
    result = a + b
    print( "{} + {} = {}".format(a,b,result) )#print문은 수정하지 마세요.

add(10,5)

###
#아래 영역에 코드를 작성해 보세요.
def add(a, b):
    result = a + b
    return result