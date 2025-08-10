import math
# 수학과 관련된 기능
print("파이의 값은 {}입니다.".format(math.pi))

import random
# 무작위와 관련된 기능

import urllib.request
#인터넷의 내용을 가져오는 기능


# random.choice()  # 후보로 받은 리스트 중 하나를 무작위로 골라주는 함수

def get_web(url):
    """URL을 넣으면 페이지 내용을 올려주는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹 페이지 주소?')
content = get_web(url)
print(content)