"""
딕셔너리 수정하기
추가
dict['three'] = 3

수정
dict['one'] = 11

삭제
del(dict['one'])
dict.pop('two') >>지우는 값 반환해줌
"""

dict = {'one':1, 'two':2}
dict['three'] = 3
dict['one'] = 11
del(dict['one'])

print(dict)