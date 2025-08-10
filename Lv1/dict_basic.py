#wintable: 각 가위바위보 패에 승리 조건을 담고 있는 딕셔너리
wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}
print(wintable['가위']) #가위가 이기는 패를 print

# 리스트
words = ['a','b','c']
print(words[0])

# 딕셔너리
"""
여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능
이름표를 이용하여 값을 꺼내 사용 (이름:값)
사용할 때는 리스트와 비슷한 방식
딕셔너리명 = {
    '이름표1':'값1',
    '이름표2':'값2'
}
"""

def rsp(mine,yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'
    
result = rsp('가위','바위')
print(result)

messages = {
    'win': '이겼다!',
    'draw': '비겼네.',
    'lose': '졌어...'
}

print(messages[result])


