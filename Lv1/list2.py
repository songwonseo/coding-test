list1 = [1, 2]

list1.append(3)         # append를 이용 list1 = [1, 2, 3]

list2 = list1+[4]       # 뒤에 새로운 리스트 더하기 list2 = [1, 2, 3, 4]

list3 = list1 + list2   # list끼리 더하기 list3 = [1, 2, 3, 1, 2, 3, 4]

# 12라는 값이 리스트에 들어있는지 확인하는 코드
n = 12
if n in list1:    # list1에 12가 있으면 print문이 실행됩니다.
    print('{}가 리스트에 있다.'.format(n))
    
del list1[10]       # 리스트의 10번째 값을 지웁니다.
list1.remove(40)    # 리스트에 40이라는 값이 있는 경우 삭제합니다.
                    # 여러개의 값이 있는 경우 가장 앞에 있는 하나만 지워집니다.