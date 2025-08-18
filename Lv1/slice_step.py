"""
step
slice한 값의 범위에서 step 값을 주어 그 값만큼 건너뛰어 가져오는 기능
list[ 시작값:끝값:step ]

step은 음수도 가능
list[15:5:-1]
"""

# step_solution

list1 = list(range(20))

# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice하세요
new_list = list1[5:15:3]

print(new_list)

# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list1[17:4:-4]

print(reverse_list)