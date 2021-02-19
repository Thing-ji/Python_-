## Quiz5
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님이다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *
customers = list(range(1, 51))
sum = 0
for customer in customers:
    time = randint(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        sum += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
print("총 탑승 승객 : {} 분".format(sum))


# 해답
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))



## 
# 퀴즈 #6
# Quiz) 표준 체중응 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#       * 함수명 : std_weight
#       * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        generate = (height * 0.01) * (height * 0.01) * 22
        print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height, generate))
        return generate
    elif gender == "여자":
        generate = (height * 0.01) * (height * 0.01) * 21
        print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height, generate))
        return generate
gender = input("성별을 입력하세요.")
height = float(input("키(cm)를 입력하세요."))
generate = std_weight(height, gender)
print('출력값: {}'.format(generate))

# 해답
def std_weight(height, gender): # 키 m 단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


##
# 퀴즈 #7
# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.

for week in range(1, 4):
    with open(str(week) + "주차.txt", "w", encoding = "utf8") as file:
        print("- " + str(week) + "주차 주간보고 - ", file = file)
        print('부서 : ', file = file)
        print("이름 : ", file = file)
        print("업무 요약 : ", file = file)

def report(weeks):
    for week in range(1, weeks+1):
        with open(str(week) + "주차.txt", "w", encoding = "utf8") as file:
             print("- " + str(week) + "주차 주간보고 - ", file = file)
             print('부서 : ', file = file)
             print("이름 : ", file = file)
             print("업무 요약 : ", file = file)
report(4)

# 해답
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write("- {0} 주차 주간보고".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")

