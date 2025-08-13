list = [1,2,3,5,7,2,5,237,55]
for val in list:
    if val % 3 == 0:
        print(val) # 3과 237이 나오는데 하나만 나오게 하고 싶으면
        break #break 사용해서 3만 출력되고 종료
    
print("#######")

"""
for i in range(10):
    if i%2 !=0:
        print(i)
        print(i)
        print(i)
        print(i)
"""

for i in range(10):
    if i % 2 == 0:
        continue # 제외 하는 경우를 첫번째 처리해줌으로써 핵심이 되는 블록이 너무 깊이 들어가지 않도록해줌
                # 반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능     
    print(i)
    print(i)
    print(i)
    print(i)