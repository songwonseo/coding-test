# 한번 정해진 순서를 바꿀 수 없다.
# 튜플 선언
tuple1 = (1, 2, 3, 4)

tuple2 = 1, 2, 3, 4

mylist = [1,2,3,4]
tuple3 = tuple(mylist)

# 튜플은 값의 변경과 삭제가 불가능

print(tuple1, tuple2, tuple3)

# tuple1 solution
tuple1 = (11, 22, 33)
for i in range( len( tuple1) ): # i에는 순서대로 0 > 1 > 2가 들어감
    print( tuple1[i] ) # tuple1[0], tuple[1], tuple[2]
