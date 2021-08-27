# 숫자자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ")
print("ㅋ"*9)    # 숫자만큼 반복되어 출력

# boolean 자료형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)     # 뒤에 있는 것의 반대 출력
print(not False)
print(not (5 > 10))

# 변수
# 애완동물 소개
animal = "강아지"
name = "호두"
age = 4
hobby = "산책"
is_aduit = age >=3

print("우리집 " + animal + "의 이름은 " + name + "이예요")
hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")     # , 사용 시 자동으로 띄어쓰기
print(name + "는 어른일까요? " + str(is_aduit))



# Quiz)변수를 이용하여 다음 문장 출력
#
# 변수명
# : station
# 변수값
# : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장
# : XX 행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)     # 2의 3제곱
print(5%3)
print(10%3)
print(5//3)     # 몫 구하기
print(10//3)

print(10 > 3)
print(4 >= 7)
print(10 < 3)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not 1 != 3)

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

# 간단한 수식
print(2 + 3 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4
print(number)

number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)

# 숫자 처리 함수
print(abs(-5))          # 절댓값
print(pow(4, 2))        # 4의 2승
print(max(5, 12))       # 최댓값
print(min(5, 12))       # 최솟값
print(round((3.14)))    # 반올림
print(round(4.99))

from math import *
print((floor(4.99)))    # 내림
print(ceil(3.14))       #올림
print(sqrt(16))         #제곱근

# 랜덤함수
from random import *
print(random())         # 0.0 이상 - 1.0 미만의 임의의 값 생성
print(random() * 10)    # 0.0 이상 - 10.0 미만의 임의의 값 생성
print(int(random() * 10))   #정수 값으로 출력, 0 이상 - 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)   # 1 이상 - 10 이상의 임의의 값 생성

# 로또 만들기
print(int(random() * 45) + 1)   #1 - 45 이하의 임의의 값 생성
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46))     # 1부터 46미만의 임의의 값 생성
print(randint(1, 45))       # 1부터 45이하의 임의의 값 생성

# Quiz 당신의 최근에 코딩 스터디 모임을 새로 만들었다
# 월 4회 스터디를 하는데 3번은 온라인 1번은 오프라인으로 하기로 했다
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성
#
# 조건1 : 랜덤으로 날짜를 뽑아야함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수 28 이내로 정함
# 조건3 : 매월 1 - 3일은 스터디 준비를 해야므로 제외
#
# 출력문 예제
# : 오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.

from random import *
# print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + "일로 선정되었습니다.")
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])   # index는 0부터 시작
print("년 : " + jumin[0:2])  # 끝나는 수는 +1로 작성 -> 0, 1번째 값 출력
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])    # 처음 숫자 생략 -> 처음부터 가져와라
print("뒤 7자리 : " + jumin[7:])   # 마지막 숫자 생략 -> 마지막까지 가져와라

print("뒤 7자리(뒤에서부터) : " + jumin[-7:])   # 뒤에서부터 계산하여 가져오기(맨 뒤 = -1)

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())   # 모든 문자 소문자로 변환
print(python.upper())   # 모든 문자 대문자로 변환
print(python[0].isupper())   # python[0] 문자가 대문자인가 판별
print(len(python))  # 문자열의 길이 구하기
print(python.replace("Python", "Java"))     # 바꾸고 싶은 문자를 찾아서 변경

index = python.index("n")   # python 안에 n 글자 위치 구하기
print(index)
index = python.index("n", index + 1)    # python 안에 두 번째 n 글자 위치 구하기
print(index)

print(python.find("n"))     # python 안에 n 글자 위치 구하기

# print(python.index("Java"))     # 원하는 값이 없을 경우 오류발생 + 프로그램 종료
print(python.find("Java"))      # 원하는 값이 없을 경우 -1 출력

print(python.count("n"))    # python 안에 n이 들어간 횟수 구하기

# 문자열 포맷
print("a" + "b")
print("a", "b")

    # 1.
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "Python")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란","보라"))

    # 2.
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","보라"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란","보라"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","보라"))

    # 3.
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="보라"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="보라", age=20))

    # 4.  v3.6이상부터 가능
age = 20
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("백문이 불여일견\n백견이 불여일타")     # \n : 줄바꿈

print("저는 '나도코딩' 입니다.")   # '...' : 작은 따옴표 사용
print('저는 "나도코딩" 입니다.')   # "..." : 큰 따옴표 사용

print("저는 \'나도코딩\' 입니다.")   # \'...\' : 작은 따옴표 사용
print("저는 \"나도코딩\" 입니다.")   # \"...\" : 큰 따옴표 사용
print("F:\\2021미림\\Python")     # \\ : \ 사용
print("Red Apple\rPine")    # \r : 맨 앞으로 이동
print("Redd\bApple")     # \b : 마지막 글자 지우기
print("Red\tApple")     #\t : 탭

# Quiz 사이트별로 비밀번호를 만들어 주는 프로그램
# ex) http://naver.com
# 규칙1 : http://부분 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + '!' 로 구성
# => nav51!

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]     # my_str[0:5]

pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(url, pw))

# 리스트
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))  # 위치 출력

subway.append("하하")     # 리스트 마지막에 추가
print(subway)

subway.insert(1, "정형돈")     # 리스트 원하는 위치 추가
print(subway)

print(subway.pop())     # 뒤에 있는 사람부터 삭제
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)

print(subway.count("유재석"))  # 리스트 속 동일한 값 개수 출력

num_list = [5, 2, 4, 3, 1]
num_list.sort()     # 리스트 정렬
print(num_list)

num_list.reverse()  # 리스트 값 뒤집기
print(num_list)

num_list.clear()    # 리스트 값 삭제
print(num_list)

mix_list = ["유재석", 20, True]    #다양한 자료형을 함께 사용O
print(mix_list)

num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)   # 리스트 합치기
print(num_list)

# 사전
cabinet = {3:"유재석", 100:"김태호"}     # 3안에 유재석이 들어있음
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#print(cabinet[5])   # 오류 발생 시 프로그램 종료
print(cabinet.get(5))   # 오류 발생 시 'None' 값 출력 후 프로그램 계속 실행
print(cabinet.get(5, "사용가능"))   # 5안에 '사용가능' 값이 추가

print(3 in cabinet)     # True, cabinet 안에 값이 있는지 확인 가능
print(5 in cabinet)     # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet)

cabinet["A-3"] = "정형돈"     # 새로운 값 변경
cabinet["C-20"] = "하하"  # 새로운 값 추가
print(cabinet)

del cabinet["A-3"]  # 값 삭제
print(cabinet)

print(cabinet.keys())   # Key 값만 출력
print(cabinet.values())   # Values 값만 출력
print(cabinet.items())   # Key, Values 값 출력

cabinet.clear() # 모든 값 삭제
print(cabinet)

# 튜플 : 내용 변경, 출력 불가능 but 속도가 빠름
menu =("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")  추가 시 오류 발생 -> 추가 불가능

name = "김족국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")  # 서로 다른 변수에 한 번에 값 선언 가능
print(name, age, hobby)

# 세트(집합 : 중복&순서X)
my_set = {1, 2, 3, 3, 3}    # 중복 사용X
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)    # 교집합(java와 python을 다 할 수 있는 개발자)
print(java.intersection(python))

print(java | python)    # 합집합(java나 python을 할 수 있는 개발자)
print(java.union(python))

print(java - python)    # 차집합(java는 할 수 있지만 python은 못하는 개발자)
print(java.difference(python))

python.add("김태호")   # python 집합에 추가
print(python)

java.remove("김태호")  # java 집합에서 삭제
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)   # 타입 변경, 집합 -> list
print(menu, type(menu))
menu = tuple(menu)   # 타입 변경, list -> tuple
print(menu, type(menu))
menu = set(menu)   # 타입 변경, tuple -> 집합
print(menu, type(menu))

# Quiz 학교에서 Python 코딩 대회를 주최한다
# 참석률을 높이기 위해 댓글 이벤트를 진행하기 하였다
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다
# 추첨 프로그램
# 
# 조건1 : 댓글 20명이 작성, 아이디 1 - 20이라고 가정
# 조건2 : 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용
# ex)
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --축하합니다--
# 
# 활용예제)
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)  리스트 값을 무작위로 변경
# print(lst)
# print(sample(lst, 1))     리스트에서 1개를 무작위로 주첨

# -------------------------------------------------------------------------------------------------

from random import *
id_list = range(1, 21)
id_list = list(id_list)

shuffle(id_list)
winners = sample(id_list, 4)

print("--당첨자 발표--")
print("치킨당첨자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")

# if
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기새요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")

# for
for waiting_no in range(1, 6):
    print("대기번호 :  {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠그루트"]
for custmer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(custmer))

# while
customer ="토르"
index=5;
while index >=1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# while True:
#     print("{0}, 커피가 준비되었습니다.".format(customer))      # 무한루프

customer = "토르"
person = "unkown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요")

# continue와 break
absent = [2, 5]     # 결석
no_book = [7]       # 책이 없음
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지, {0}은 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한 줄 for문
# 출석 번호 1, 2, 3, 4... -> 101, 102, 103, 104...로 변경
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man" , "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man" , "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# Quiz 당신은 Cocoa 서비스를 이용하는 택시 기사이다
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램 작성
#
# 조건1 : 승객별 운행 소요 시간은 5-50분 사이의 난수
# 조건2 : 당신은 소요 시간 5-15분 사이의 승객만 매칭
#
# ex)
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2분
from random import *
cnt = 0     #탑승 승객 수
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15 :    # 매칭 성공
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:       #매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))

# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

# 전달값과 반환값
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
    # print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
    #       .format(name, age, main_lang))  두 줄 출력문 사용방법 \로 구분

profile("유재석", 20, "파이썬")
profile("김태호", 20, "자바")
# 같은 학교 같은 학년 같은 반 같은 수업을 듣는다면

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬",age = 20)
profile(main_lang = "자바",age = 25, name = "김태호")
# 순서가 변경되어도 키워드값으로 올바르게 출력

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")    # 밑에 있는 내용을 이어서 출력
#     print(lang1, lang2, lang3, lang4, lang5)
#
# profile("유재석", 20, "Python", "Java", "C", "C++", "c#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language):  # 서로 다른 개수 출력 시 가변인자 사용
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")    # 밑에 있는 내용을 이어서 출력
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "c#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# 지역변수와 전역변수
gun = 10

def checkpoint(soldiers):
    global gun     # gun을 전역변수로 변환하여 사용
    gun = gun - soldiers    # gun은 함수 안에서 사용된 지역변수이므로 함수 밖에서 사용X
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[합수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# Quiz 표준체중을 구하는 프로그램 작성
# * 표준체중 : 개인의 키에 적당한 체중
#
# 성별에 따른 공식
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21
#
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         함수명 : std_weight
#         전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
#
# ex)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
def str_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(str_weight(height / 100, gender), 2)     # round를 사용하여 소수자리 변경
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# --------------------------------------------------------------------------------------------------------------------

# 클래스
# name 유닛의 이름 |  hp 유닛의 체력 |  damage 유닛의 공격력
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marien1 = Unit("마린", 40, 5)
marien2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# init : python에서 사용하는 생성자, 클래스로 만들어지는 객체 생성 시 자동으로 호출
# init에 정의된 갯수와 인스턴스 객체의 개수가 동일해야함

# 멤버변수 : class 안에서 정의된 변수
wraith1 = Unit("레이스", 80, 5)
print(f"유닛이름 : {wraith1.name}, 공격력 : {wraith1.damage}")
# 멤버변수를 외부에서 사용가능

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True
# 외부에서 변수를 추가로 할당가능, but wraith1에는 clocking이 없음

if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")

# 메서드
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

firebat1 = AttackUnit("파이어벳",50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

# 상속
class Unit:     # 일반 유닛
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):   # 공격 유닛
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   # name과 hp를 상속
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

firebat1 = AttackUnit("파이어벳",50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

# 다중상속
class Unit:     # 일반 유닛
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):   # 공격 유닛
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)   # name과 hp를 상속
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

class Flyable:  # 날 수 있는 유닛
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{self.name} : {location} 방향으로 날아갑니다, [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):   # 공중 공격 유닛, 다중 상속 시 ,로 구분
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 연산자 오버로딩
class Unit:     # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

class AttackUnit(Unit):   # 공격 유닛
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # name과 hp를 상속
        self.damage = damage

    def attack(self, location):
        print("{self.name} : {self.damage} 방향으로 적군을 공격 합니다. [공격력 {2}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.".format(self.name, damage))
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.".format(self.name))

class Flyable:  # 날 수 있는 유닛
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다, [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):   # 공중 공격 유닛, 다중 상속 시 ,로 구분
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      # 지상유닛의 속도는 필요X 따라서 0으로 가져옴
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # move 함수를 새롭게 정의하여 오버로딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

# 패스
class Unit:     # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print(f"[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

class AttackUnit(Unit):   # 공격 유닛
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # name과 hp를 상속
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

class Flyable:  # 날 수 있는 유닛
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다, [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):   # 공중 공격 유닛, 다중 상속 시 ,로 구분
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      # 지상유닛의 속도는 필요X 따라서 0으로 가져옴
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # move 함수를 새롭게 정의하여 오버로딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BulldingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BulldingUnit("서플라이 디풋", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass    # 아무것도 하지 않고 넘어감

game_start()
game_over()

# super
class Unit:     # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

class AttackUnit(Unit):   # 공격 유닛
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # name과 hp를 상속
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

class Flyable:  # 날 수 있는 유닛
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{self.name} : {location} 방향으로 날아갑니다, [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):   # 공중 공격 유닛, 다중 상속 시 ,로 구분
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      # 지상유닛의 속도는 필요X 따라서 0으로 가져옴
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # move 함수를 새롭게 정의하여 오버로딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BulldingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        # Unit.__init__(self. name. hp, 0) 문장과 동일,
        # but super는 다중 상속 시 마지막에 상속 받는 유닛만 사용가능
        self.location = location

# 스타크래프트 전반전
class Unit:     # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

class AttackUnit(Unit):   # 공격 유닛
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # name과 hp를 상속
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

        if self.hp <= 0:
            print("{self.name} : 파괴되었습니다.")

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{self.name} : 시즈모드를 해재합니다.")
            self.damage /= 2
            self.seize_mode = False

class Flyable:  # 날 수 있는 유닛
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다, [속도 {2}]")

class FlyableAttackUnit(AttackUnit, Flyable):   # 공중 공격 유닛, 다중 상속 시 ,로 구분
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      # 지상유닛의 속도는 필요X 따라서 0으로 가져옴
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # move 함수를 새롭게 정의하여 오버로딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드를 해재합니다")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드로 전환합니다")
            self.clocked = True

# 스타크래프트 후반전
from random import *

class Unit:     # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 잃었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")

class AttackUnit(Unit):   # 공격 유닛
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)   # name과 hp를 상속
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드를 해재합니다.")
            self.damage /= 2
            self.seize_mode = False

class Flyable:  # 날 수 있는 유닛
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다, [속도 {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):   # 공중 공격 유닛, 다중 상속 시 ,로 구분
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      # 지상유닛의 속도는 필요X 따라서 0으로 가져옴
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # move 함수를 새롭게 정의하여 오버로딩
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드를 해재합니다")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드로 전환합니다")
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):     # 객체가 어떤 클래스의 인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.seize_mode
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()


'''
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
    # 매물 정보 표시
    def show_detail(self):
        pass
'''
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f"총 {len(houses)}대의 매물이 있습니다.")

for house in houses:
    house.show_detail()

# 모듈
import  theater_module
theater_module.price(3) #3명이서 영화보러 갔을 때 가격
theater_module.price_morning(4) #4명이서 조조 영화보러 갔을 때 가격
theater_module.price_soldien(5) #5명 군인이 영화보러 갔을 때 가격

import theater_module as mv
mv.price(3)
mv.price_morning(4 )
mv.price_soldien(5)

from theater_module import *
price(3)
price_morning(4)
price_soldien(5)

from theater_module import price, price_morning
price(5)
price_morning(6)

from theater_module import price_soldien as price
price(5)

# 패키지
import travel.thailand
# import travel.thailand.ThailandPackage
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamePackage()
trip_to.detail()

# __all__
from  travel import *
trip_to = vietnam.VietnamePackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 모듈 직접 실행
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 패키지, 모듈 위치
import  inspect
import random
print(inspect.getfile(random()))
print(inspect.getfile(thailand))