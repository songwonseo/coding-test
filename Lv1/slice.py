"""
slicing
리스트나 문자열에서 값을 여러개 가져오는 기능

text = "hello world"
text = text[ 1:5 ]

list = [ 0, 1, 2, 3, 4, 5 ]
list = list[ 1:3 ]

slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 준다.

시작과 끝부분을 얻어 오는 방법
list[ 2: ] : 2번째부터 끝까지 반환
list[ : 2 ] : 처음부터 2번째 까지 반환
list[ : ] : 처음부터 끝까지 전부 반환
"""

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

# red_colors가 ["빨", "주", "노"]의 값을 가지도록 rainbow를 slice하세요.
red_colors = rainbow[0:3]

#blue_colors가 ["파", "남", "보"]의 값을 가지도록 rainbow를 slice하세요.
blue_colors = rainbow[4:7]

print("red_colors의 값 : {}".format(red_colors))
print("blue_colors의 값 : {}".format(blue_colors))

# slice_solution
def substring(text, start, end):
    return text[start:end]


my_text = "Hello world"
between_2_5 = substring(my_text, 2, 5)
print(between_2_5)