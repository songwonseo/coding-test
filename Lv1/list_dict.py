# 리스트와 딕셔너리의 비교

### 공통점 ###

# 생성
list = [1,2,3]
dict = {'one':1, 'two':2}
print(list,dict)

# 호출
print(list[0])
print(dict['one'])

# 삭제
del(list[0])
del(dict['one'])
print(list,dict)

# 개수 확인
print(len(list))
print(len(dict))

# 값 확인
print(2 in list)
print('two' in dict.keys())

# 전부 삭제
print(list.clear())
print(dict.clear())

### 차이점 ###

# 순서
# list: 삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다
# dictionary: key로 값을 가져오기 때문에 삭제 여부와 상관없다.

# 결합
# list1 + list2
# dict1.update(dict2)
