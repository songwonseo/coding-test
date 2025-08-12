"""
check_and_clear는 딕셔너리 타입의 box를 매개변수로 받는데요. 
만약 box에 "불량품"이라는 이름표가 있으면 box 전체를 빈 딕셔너리로 만들어 버리고, 
불량품이 없으면 box를 그대로 두는 함수입니다. 
다음 코드를 수정해서 check_and_clear 함수를 완성하세요.
"""

def check_and_clear(box): # box는 check_and_clear 함수의 매개변수 이름
    if "불량품" in box:   # 매개변수 box 안에 불량품이라는 키가 있는 경우
        print("불량품이 있으면 box를 clear합니다.")
        box.clear()       # 딕셔너리 비우기
    print(box)
    
box1 = {"불량품": 10} # 딕셔너리 변수 box1 생성
check_and_clear(box1) # box 매개변수에 box1을 전달  (box=box1)
print(box1)  # {} 출력

box2 = {"정상품": 10}
check_and_clear(box2)
print(box2)  # {"정상품": 10} 출력
