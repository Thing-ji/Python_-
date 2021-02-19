##
# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money): # 입금
    print("입금이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money
balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))



##
# 기본값
def profile(name, age, main_lang): # \ : 줄바꿈
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
    .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 기본값 추가하기: 같은 학교 같은 반 같은 과목일 때
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
    .format(name, age, main_lang))

profile("유재석")
profile("김태호")


##
# 키워드
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = '유재석', main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = 25, name = '김태호')


##
# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") # end = " " 은 print문에서 줄바꿈을 하지 않고 그 대로 이어준다.
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "kotlin", "Swift", "", "", "")

def profile(name, age, *language): # 다른 값을 넣어주고 싶을 때 가변인자 사용.
    print("이름 : {0}\t나이: : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C", 'C++', "C#")
profile("김태호", 25, "kotlin", "Swift")


##
# 지역변수와 전역변수
# 지역변수: 함수 내에서만 쓸 수 있는 것
# 전역변수: 모든 공간에서 쓸 수 있는 것

gun = 10

# 방법1
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

# 방법2
def checkpoint2(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint2(gun, 3)
print("남은 총 : {0}".format(gun))


##
# 표준입출력                                   # end 는 print가 끝나고 다음 출력할 때 기호
print("Python", "Java", sep = ",", end = "?") # sep 은 다음꺼 출력할 때 기호
print("무엇이 더 재밌을까요?")

import sys
print('Python', 'Java', file = sys.stdout) # 이 줄은 표준처리로 한다.
print('Python', 'Java', file = sys.stderr) # 이 줄은 에러를 확인해서 처리한다.

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":") # ljust는 왼쪽으로 숫자의 공간을 가지고 정렬, rjust는 오른쪽으로 숫자의 공간을 가지고 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3)) # zfill : 3자리의 공간에서 채워지지 않은 부분은 0으로 채운다.

answer = input("아무 값이나 입력하세요 : ") # input은 숫자도 str로 처리한다.
print("입력하신 값은 " + answer + "입니다.") 


##
# 다양한 출력포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000))
print("{0:+,}".format(-1000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(10000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))


##
# 파일입출력
score_file = open("score.txt", "w", encoding = "utf8") # 파일을 읽어서 "w": 작성하겠다.
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file) # 자동 줄바꿈됨
score_file.close() # 꼭 닫아주기!

score_file = open("score.txt", "a", encoding = 'utf8') # "a": 파일을 이어서 쓰겠다.
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # "a"는 자동 줄바꿈이 안됨
score_file.close()

score_file = open("score.txt", "r", encoding = 'utf8') # 파일 내용 전체 "r": 읽어오기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding = 'utf8')
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding = 'utf8')
print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line: # 만약 line이 없으면 if 실행
        break
    print(line, end = "")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # list 형태로 각 줄의 파일 내용을 저장
for line in lines:
    print(line, end = "")
score_file.close()


##
# pickle
import pickle
profile_file = open("profile.pickle", 'wb') # pickle은 "wb", w와 b를 같이 써야함
profile = {"이름": "박명수", "나이" : 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()


##
# with
import pickle

with open("profile.pickle", "rb") as profile_file: # 파일을 열어서 profile_file 변수에 넣는다.
    print(pickle.load(profile_file)) # with 은 자동으로 닫아주기 때문에 close()를 굳이 안써줘도 됨

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding = 'utf8') as study_file:
    print(study_file.read())


##
# 클래스 : 붕어빵 틀

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음.
name = "마린"
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

class Unit:
    def __init__(self, name, hp, damage): # self를 제외한 나머지 인자를 받아주어야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


##
# __init__ : 객체를 뜻한다.
# marine1, marine2, tank는 객체(__init__)이고, Unit을 인스턴스 한다고 말한다.


##
# 멤버변수 : 여기서는 name, hp, damage 를 뜻함.
class Unit:
    def __init__(self, name, hp, damage): # self를 제외한 나머지 인자를 받아주어야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))  # 여기서 .name, .damage를 사용하여 쓸 수 있음

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # clocking은 클래스 내애 없지만 외부로 쓸 수 있음.

if wraith2.clocking == True: # clocking은 클래스 내애 없지만 외부로 쓸 수 있음, but wraith1은 선언을 하지 않았기에 사용 불가!
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

wraith1.bagging = 90
print("레이스 배깅은 {0} 입니다.".format(wraith1.bagging))


##
# 메소드
class Unit:
    def __init__(self, name, hp, damage): # self를 제외한 나머지 인자를 받아주어야함
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
# 여기서 주의! 메소드에서 함수 attack은 location을 적어줄 때 self를 적지 않는다.
# 그 이유는! 외부에서 값을 받을 것이기 때문이다. 클래스 내에서 받을 것이 아니다.
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebet1 = AttackUnit("파이어뱃", 50, 16)
firebet1.attack("5시")

# 25 대미지의 공격을 2번 받는다고 가정
firebet1.damaged(25)
firebet1.damaged(25)
