# #Quiz1) 변수를 이용하여 다음 문장을 출력하시오
# 변수명: station
# 변수값: "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장: xx 행 열차가 들어오고 있습니다.

station="사당"
print (station,"행 열차가 들어오고 있습니다.")
station="신도림"
print (station,"행 열차가 들어오고 있습니다.")
station="인천공항"
print (station,"행 열차가 들어오고 있습니다.")

# Quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번을 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

from random import *

date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# # 퀴즈 3
# Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                 (nav)               (5)             (1)         (!)
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
print(url[7:10]+str(len(url[7:-4]))+str(url.count("e"))+"!")

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{1}의 비밀번호는 {0} 입니다.".format(password, url))

