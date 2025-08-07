# coding-test# 1) 문제 풀이(예: programmers/level1/두_수의 합.py)

파일 안에 문제 설명/링크, 코드, 주석까지 간단하게 정리해두기

Ex)
#두 수의 합(프로그래머스, 레벨1)

#https://school.programmers.co.kr/learn/courses/30/lessons/123456

    def solution(a,b):
        return a+b

# 2) git add, git commit, git push하기

    git add .

    git commit -m "커밋 메시지(ex.프로그래머스 Lv1 - 두 수의 합 문제 풀이 추가)"

    git push origin main


Add .은 전체 파일을 스테이징, commit은 변경사항을 저장, push는 github에 업로드

### 3) git 초기화, 확인

터미널에서 해당 폴더로 이동

    cd ~/coding-test

git 초기화:

    git init

변경사항 확인: 

    git status

git에 업로드(초기):

    git branch -M main (처음에만)
    git push -u origin main

### 4) push 에러

    git pull --rebase origin main
    git push -u origin main

