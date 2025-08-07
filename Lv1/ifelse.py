mine = '가위'
yours = '바위'
if mine == yours:
    print("비겼습니다.")
#이 아래줄에 else문을 추가해서 비기지 않은 경우에만 아래 print문이 실행되도록 만들어 보세요
else:
    print("비기지 않았습니다.")#else문이 추가되고 나면 이 줄은 들여쓰기 되어야 합니다.
    
###
gender = "남자"
#이 아래줄에 if문을 추가하세요
if gender == "남자":
    print("남자입니다.")
#이 아래줄에 elif문을 추가하세요
elif gender == "여자":
    print("여자입니다.")
#이 아래줄에 else문을 추가하세요
else:
    print("논바이너리입니다")
    
    
###
mine = "가위"
yours = "바위"

if mine == yours:
    print("비김")
else:
    if mine == "가위":
        if yours == "보":
            print("이겼다")
        else:
            print("졌다")
    elif mine == "바위":
        if yours == "가위":
            print("이겼다")
        else:
            print("졌다")
    elif mine == "보":
        if yours == "바위":
            print("이겼다")
        else:
            print("졌다")