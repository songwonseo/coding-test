# 리스트와 반복문
seasons = ['봄','여름','가을','겨울']

for season in seasons:
    print(season)
    
# 딕셔너리와 반복문
ages = {'Tod': 35, 'Jane':23, 'Paul':62}

# 경우에 따라 가져올 값을 정할 수 있다.
for key in ages.keys(): # keys()는 생략가능
    print(key)

for value in ages.values():
    print(value)
    
for key in ages.keys():
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))
    
# key와 value 둘다 가져올 수 있다.
for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, value))
    
# 딕셔너리는 값의 순서를 지키지 않는다.

# ex)
days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

# 키 출력
for key in days_in_month.keys():
    print(key)
    
# 값 출력
for value in days_in_month.values():
    print(value)
    
# 둘 다 출력
for key, value in days_in_month.items():
    print(key, value)

