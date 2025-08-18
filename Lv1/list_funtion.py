"""
List의 기능

list.index( value ) : 값을 이용하여 위치를 찾는 기능
list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
list.insert( index, value ) : 원하는 위치에 값을 추가
list.sort( ) : 값을 순서대로 정렬
list.reverse( ) : 값을 역순으로 정렬
"""

# list_solution

def safe_index(my_list, value):
    if value in my_list: # value in my_list >> my_list 안에 value가 있는지 확인
        return my_list.index(value)

    else:
        return None

print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))

# list_solution2

list1 = [1, 2, 3, 4]

# 아래줄에서 list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀어 보세요.
list1.insert(0,8)

print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))
# 아래줄에서 list1을 작은 수부터 큰 수로 정렬해 보세요
list1.sort()

print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))
# 아래줄에서 list1을 거꾸로 만들어 보세요
list1.reverse()

print("list1을 거꾸로 정렬한 결과 : {}".format(list1))