# while문: 조건이 참인 경우 계속 실행하는 반복문
"""
selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')
    
print('선택된 값은: ',selected)
"""

# for 반복문으로 작성한 코드는 while 반복문으로 작성할 수 있다.


"""
selected = None
if selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')
    
print('선택된 값은: ',selected)
> 반복해서 물어보지 않고 딱 한 번만 실행함
"""

patterns = ['가위','보','보']
for i in range(len(patterns)):
    print(patterns[i])
    
patterns = ['가위','보','보']
length = len(patterns)
i = 0
while i < length:
    print(patterns[i])
    i = i + 1
    

# 상황에 맞는 반복문 만들기. for문으로 먼저 만들어보고 너무 복잡하면 while문 사용
