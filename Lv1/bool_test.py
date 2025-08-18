value = input('입력해 주세요>') or '아무것도 못받았어'
print('입력받은 값>',value)

# 인풋의 '입력해 주세요>'의 빈 값은 false
# 앞에 값이 false인 경우 or 연산에서 값은 무조건 뒷부분을 따름
# 뒷부분이 false인지 true인지에 따라 전체식의 값이 결정

# 인풋의 '입력해 주세요>'에 hi를 입력: true
# 앞에 값이 true인 경우 or 연산에서 뒷부분은 볼 것도 없이 앞에 값을 따름

"""
bool 값과 논리연산

숫자 0을 제외한 모든 수 - true
빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
아무 값도 없다는 의미인 None - false
빈문자열을 제외한 모든 문자열 - true
"""

# bool_solution
if []:
    print("[]은 True입니다.")

if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")

if {}:
    print("{}은 True입니다.")

if {'abc': 1}:
    print("{'abc':1}은 True입니다.")

if 0:
    print("0은/는 True입니다.")

if 1:
    print("1은 True입니다.")
    
# bool_solution2
a = 1 or 10    # 1의 bool 값은 True입니다.
b = 0 or 10    # 0의 bool 값은 False입니다.


print("a:{}, b:{}".format(a, b))