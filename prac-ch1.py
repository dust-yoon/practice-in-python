#숫자자료형 #저장이 안되었을 경우 ctrl+s
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1+1)) #순서에 따라 계산 됨.

#문자열자료형
print('풍선')
print("나비")
print("ㅋ"*8)

#분리항 -> 참/거짓
print(5>10) #False 출력
print(5<10) #True 출력
print(True)
print(False)
print(not True) #not=무언가의 반대
print(not False)
print(not(5>10)) #True 출력됨. False의 반대가 되니까

#애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4 #str은 정수형을 문자형으로 바꾸어주는 역할을 함.
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby="공놀이"
print(name + "은/는 " + str(age) + "살이며, " + hobby + "을/를 아주 좋아해요")
print(name + "은/는 어른일까요? " + str(is_adult))
#변수만 수정함으로써 모든 내용을 변경할 수 있음. 변수는 이후에 변경 가능.
#+가 아니라 ,를 넣음으로써도 사용이 가능함
#'+' => 하나하나 모두 연결해 붙인다는 느낌, 문자열로 변환할 필요가 있음.
#',' => 자동으로 띄어쓰기가 들어가고 숫자 변수를 문자열로 바꾸지 않아도 됨

#주석
#해제하고자 하는 범위를 슬러쉬로 이동하여 긁은 뒤 "ctrl+/"
