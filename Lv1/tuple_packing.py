# packing: 하나의 변수에 여러개의 값을 넣는 것
# unpacking: 패킹된 변수에서 여러개의 값을 꺼내오는 것
c = (3,4)
d, e = c # c의 값을 언패킹하여 d, e에 값을 넣었다
f = d, e # 변수 d와 e를 f에 패킹

# 튜플의 활용
# 두 변수의 값을 바꿀 때 임시변수가 필요 없다.
# 함수의 리턴 값으로 여러 값을 전달할 수 있다.

x = 5
y = 10
temp = x
x = y
y = temp
print(x,y)
x, y = y, x
print(x,y)

def tuple_func():
    return 1,2
q,w = tuple_func()
print(q,w)