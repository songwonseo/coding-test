"""
try:
    # 에러가 발생할 가능성이 있는 코드
except Exception: # 에러 종류
    #에러가 발생 했을 경우 처리할 코드
"""
text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요.'.format(text))
    
# list와 index를 받아들여서 인덱스에 해당하는 값을 출력하고, 
# 그 값을 index에서 지워주는 함수 만들기
def safe_pop_print(list, index): 
    try:
        print(list.pop(index)) # index에 해당하는 값을 지우면서 리턴
    except IndexError:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)

# if문 활용
def safe_pop_print(list, index):
    if index<len(list):
        print(list.pop(index))
    else:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)

# 예외처리 대신 if else를 사용할 수 있지만
# 이런 경우엔 try를 써야함
# try:
#     import your_module
# except ImportError:
#     print("모듈이 없습니다.")

# try except solution
try:
    a = 3/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
        

    
