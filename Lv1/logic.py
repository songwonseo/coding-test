a = 10
if a<0 and 2**a>1000 and a%5==2 and round(a)==a: 
    # and 연산은 전체가 true여야 실행되는데 처음부터 false이므로 뒤에는 볼 필요가 없음
    print("복잡한 식")
    # or 연산은 하나만 true이면 전체가 true임
    
def return_false():
    print("함수return_false")
    return False

def return_true():
    print("함수return_true")
    return True

print("테스트1")
a = return_false()
b = return_true()
if a and b:
    print(True)
else:
    print(False)
    
print("테스트2")
if return_false() and return_true():
    print(True)
else:
    print(False)
    
# 단락평가
# 논리연산에서 코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 보지 않고 값을 결정
# 복잡한 코드를 단순하게 하는 방식

dic = {"key2":"Value1"}
if "key1" in dic and dic["key1"] == "Value1":
    print("key1도 있고, 그 값은 Value1이네")
else:
    print("아니네.")
    
# dic = {"key2":"Value1"}
# if dic["key1"] == "Value1" and "key1" in dic:
#     print("key1도 있고, 그 값은 Value1이네.")
# else:
#     print("아니네.")
# 단락평가 에러 발생