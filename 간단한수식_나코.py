print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 5  # 1
print(number)

##
# 숫자처리함수
print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99))

from math import *
print(floor(4.99)) # 내림. 4 
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4

##
# 랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ i0.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 0 ~ 10 미만의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# 퀴즈#2
from random import *
date = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월' + str(date) + '일로 선정되었습니다.')

##
# 슬라이싱
jumin = '990120-1234567'

print('성별 : ' + jumin[7])
print('연 : ' + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])

print('생년월일 : ' + jumin[:6]) # 처음부터 6 직전까지
print('뒤 7자리 : ' + jumin[7:]) # 7 부터 끝까지
print('뒤 7자리 (뒤에부터) : ' + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

##
# 문자열 처리 함수
python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'Java'))

index = python.index('n')
print(index) # 'n'이 위치한 index 출력
index = python.index('n', index + 1) # 그 다음꺼 출력
print(index)

print(python.find('Python'))
print(python.find('java')) # 없으면 -1 출력
print(python.index('Python')) # 얘는 없으면 오류 출력
print(python.count('n')) # n이 몇번 등장하는지

##
# 문자열 포맷
# 방법1
print('나는 %d살입니다.' % 20) # d는 정수, % 뒤에 올 숫자
print('나는 %s을 좋아해요.' % '파이썬') # s는 문자열
print('Apple은 %c로 시작해요.' % 'A') # c는 문자 1개
print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))
# 방법2
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간'))
# 방법3
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color = '빨간'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(color = '빨간', age = 20))
# 방법4(버전 3.6 이상~)
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')

##
# 탈출 문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# \" \' : 문장 내에서 따옴표
# 저는 "홍길동" 입니다.
print("저는 '홍길동'입니다.") 
print('저는 "홍길동"입니다.')
print("저는 \"홍길동\"입니다.")
print("저는 \'홍길동\'입니다.")
# \\ : 문장 내에서 \
print("C:\\Users\\rlaek\\Desktop\\git_start")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")

# 퀴즈#3
url = "http://naver.com"
url = "http://daum.com"
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0~5 직전까지 (0, 1, 2, 3, 4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

##
# 리스트
subway = [10, 20, 30]
print(subway)
subway = ['유재석', '조세호', '박명수']
print(subway)
# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append('하하')
print(subway)
# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼낸다.
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
# 순서 뒤집기 가능
num_list.reverse()
print(num_list)
# 모두 지우기
num_list.clear()
print(num_list)
# 다양한 자료형 함께 사용
mix_list = ['조세호', 20, True]
print(mix_list)
# 리스트 확장
num_list = [5, 2, 4, 3, 1]
mix_list = ['조세호', 20, True]
num_list.extend(mix_list)
print(num_list)

##
# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석 출력
print(cabinet[100]) # 김태호 출력
print(cabinet.get(3)) # 키가 3인 값 출력
# but
print(cabinet[5]) # 없는 값을 집어넣으면 에러를 바로 출력
print('hi')

print(cabinet.get(5)) # get은 없는 값이면 None을 출력한 후 그래도 진행함
print(cabinet.get(5, "사용 가능")) # "사용 가능"을 출력시킴
print('hi')

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3": "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)

##
# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 튜플은 추가, 삭제가 안된다.

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, '코딩')
print(name, age, hobby)

##
# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))
# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))
# python 할 줄 아는 사람이 늘어났다.
python.add("김태호")
print(python)
# java 를 잊었어요
java.remove("김태호")
print(java)

##
# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} # set
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))

#퀴즈5
# random과 sample
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst) # 리스트 안에 있는 숫자를 무작위로 바꾼다.
print(lst)
print(sample(lst, 1))
# 방법1
comment = list(range(1, 20+1))
from random import *
shuffle(comment)
print(comment)
first = sample(comment, 1)
secon = sample(comment, 3)
print(secon)
print("-- 당첨자 발표 --\n" + '치킨 당첨자 : ', first, '\n' + '커피 당첨자 : ' , secon, '\n-- 축하합니다 --')
# 방법2
winners = sample(comment, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨지 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

##
# if
weather = input("오늘 날씨는 어떤가요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

##
#for
for waiting_no in range(5): # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no)) 

starbucks = ['아이언맨', '토르', '아이엠 그루트']
for customer in starbucks:
    print('{0}, 커피가 준비되었습니다.'.format(customer))

##
#while
customer = '토르'
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")
        
customer = "아이언맨"
index = 1
while True: # 무한 루프, 강제종료 ctrl + c
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1
    if index == 10:
        break

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
    if person == customer:
        print("맛있게 드세요~")
    else:
        print("토르가 아닙니다.")

##
# continue와 break
absent = [2, 5] # 결석
for student in range(1, 11): # 1부터 10까지
    if student in absent:
        continue # 조건에 만족하면 넘어감
    print("{0}, 책을 읽어봐".format(student))
    
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

##
# 한 줄 for
# 출석번호 앞에 100 붙이기
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ['iron man', 'thor', 'i am groot']
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ['iron man', 'thor', 'i am groot']
students = [i.upper() for i in students]
print(students)

