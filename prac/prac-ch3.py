#연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)
#간단한 사칙연산, 제곱, 몫, 나머지 계산
print(2**3) #제곱
print(5%3) #나머지 구하기=2
print(10%3) 
print(5//3) #몫 구하기  =1
print(10//3)
#크기 비교 이때 '=='의 경우 앞과 뒤과 완전히 동일한 경우를 말함 
print(10>3)
print(4>=7)
print(10<3)
print(5<=5)
print(3==3)
print(4==2)
print(3+4==7)
print(1 != 3) #앞 뒤가 같지 않다는 의미 그러므로 이 값은 True가 될 것
print(not(1 != 3)) # not은 앞의 내용과 반대되는 항목이므로 False가 출력될것
print((3>0) and (3<5)) #True 출력, 두가지 조건 모두 충족해야 함
print((3>0) & (3<5)) #and 와 동일한 조건 설정
print((3>0) or (3>5)) #True 출력, 두가지 조건 중 하나만 충족해도 됨.
print((3>0) | (3>5)) #or과 동일
print(5>4>3) #True 출력
print(5>4>3) #False 출력 조건 불충족

#간단한 수식
print(2+3*4)
print((2+3)*4)
number= 2+3*4
print(number) #14
number = number+2
print(number)
number += 2 #number + 2를 줄여 부르는 말. '='이 핵심임
print(number) #아마 예상대로라면 18이 출력되어야 함.
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5 #1
print(number)

#파이썬에서 제공하는 몇가지 숫자 처리 함수
print(abs(-5)) # 절댓값
print(pow(4,2)) # , 앞에 위치한 값을 뒤에 위치한 값만큼 곱하는 함수 = 4*4 = 16
print(max(5, 12)) #5, 12 두 숫자 중 가장 큰 수를 출력
print(min(5, 12)) # max 함수와 반대 가장 작은 수를 출력하는 함수
print(round(3.14)) # 반올림 함수 = 3
print(round(4.99))

from math import * # 아직 나오지는 않았으나 math 라이브러리에 포함된 모든 수를 전부 곱하라는 의미
print(floor(4.99)) # 바닥이라는 뜻. 즉 내림
print(ceil(3.14)) # 천장이라는 뜻, 즉 올림
print(sqrt(16)) # 제곱근. 16은 4의 제곱이므로 = 4

#랜덤함수-난수 무작위로 뽑아주는 함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성 [0,1)
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0.0 ~ 10.0 미만의 임의의 정수 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 정수 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 정수 생성 

#randrange(a,b) = [a,b) 정수 랜덤
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 정수 생성
#randint(a,b) = [a,b] 정수 랜덤
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 정수 생성