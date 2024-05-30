# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
""" # 줄바꿈 4 줄을 포함해서 모두 잘 찍힘
print(sentence3)

# 슬라이싱이란, 필요한 정보만을 잘라서 가져오는 것을 뜻함
jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 컴퓨터가 정보를 들고올떈 0자리 부터 시작 # 1
print("연 : " + jumin[0:2]) # [a,b]일 경우 a부터 b미만의 자리의 정보를 가져오는 것.
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전의 자리까지 정보를 들고 옴
print("뒤 7자리 : " + jumin[7:]) # 7자리 수부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amizing"
print(python.lower()) # 지정 sentence를 전부 소문자로 바꿈, upper의 경우 대문자
print(python.upper()) 
print(python[0].isupper()) # 지정 sentence의 특정 문자가 대문자인지 확인하는 함수
print(python[0].islower()) # 그럼 이건? False.
print(len(python)) # ()안 문장의 글자수 파악. 띄어쓰기 포함
print(python.replace("Python", "Java")) # 문장 안의 특정 단어를 다른 단어로 바꾸는 함수

index = python.index("n")
print(index) # 문장의 특정 단어가 든 위치 알려줌
index = python.index("n", index + 1) 
print(index) # 다음위치 찾는 법

# 특정 단어의 위치 찾는 두 가지 방법
print(python.find("Java")) # 오류날 경우 '-1' 출력 후 진행
# -> print(python.index("Java")) # 오류날 경우 그대로 프로그램 종료
print("hi")
print(python.count("n"))

# 문자열포멧
print("a" + "b")
print("a" ,"b")
# 방법 1
print("나는 %d살입니다." % 20) # 정수 %d
print("Apple은 %c로 시작해요." % "A") # 문자 한 개
print("나는 %s를 좋아해요." % "사과") # 문자열 %s 이건 모든 경우에 사용 가능
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))
# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
# 방법 3
print("나는 {age}살이고 {color}색을 좋아해요.".format(color = "빨간", age = 20))
# 방법 4 (3.6 버전 이상에서만 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이고 {color}색을 좋아해요.")

# 탈출문자
# 줄바꿈 = \n
print("백문이 불여일견 \n백견이 불여일타")
# \" \' : 문장 내에서 따옴표 가능
print("저는 '원지윤'입니다.")
print('저는 "원지윤"입니다.')
print("저는 \"원지윤\"입니다.")
# \\ : 문장 내에서 \
print("C:\\Users\\원지윤\\Desktop\\PythonWorkSpace>")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 (한글자만 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")
