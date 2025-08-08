patterns = ['가위','바위','보']
for pattern in patterns:
    print(pattern)
    
for i in range(5): # 필요한 만큼의 숫자를 만들어내는 유용한 기능
    print(i)
    
# range 괄호에 len을 넣으면 리스트의 길이만큼 반복할 수 있습니다. 
names = ['철수', '영희', '바둑이', '귀도', '비단뱀']

for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i + 1, name))
    
    
 # enumerate , 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
names = ['철수', '영희', '영수']
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))