'''
Quiz 1-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력
예시
id_number = 020316 일 때

출력 예시
02
0316
732
'''
id_number = "040221"
print(id_number[:2])
print(id_number[2:])
print(int(id_number[0:2]) + int(id_number[2:6]))

print()

'''
Quiz 1-2. 집 전화번호를 phone_number에 넣고,
지역번호(줄바꿈)맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
예시
phone_number = 02-1234-5678 또는 032-9876-4321

출력 예시
02 또는 032
5678 또는 432
'''
phone_number1 = "02-1234-5678"
phone_number2 = "032-9876-4321"

print(phone_number1[:-10])
print(phone_number1[-4:])
print(phone_number2[0:-10])
print(phone_number2[-4:])

print()

# --------------------------------------------------------------------------------------------------------------------

'''
Quiz 2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
student_number = '2100' 또는 student_number = '2000'
<출력 예시>
1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
'''
student_number = "2410"
if student_number[1] == "1" or student_number[1] == "2":
    print("{0}반 뉴미디어소프트웨어과".format(student_number[1]))
elif student_number[1] == "3" or student_number[1] == "4":
    print("{0}반 뉴미디어웹솔루션과".format(student_number[1]))
elif student_number[1] == "5" or student_number[1] == "6":
    print("{0}반 뉴미디어디자인과".format(student_number[1]))
else:
    print("잘못 입력했습니다.")

print()

'''
Quiz 2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
<함수 호출>
grade, major = get_major('2100')
print(major, grade) #뉴미디어소프트웨어과 2
'''
def get_major(argument):
    grade = argument[0]
    if argument[1] == "1" or argument[1] == "2":
        major = "뉴미디어소프트웨어과"
    elif argument[1] == "3" or argument[1] == "4":
        major = "뉴미디어웹솔루션과"
    elif argument[1] == "5" or argument[1] == "6":
        major = "뉴미디어디자인과"
    print(major, grade)

get_major("2410")

print()

'''
Quiz 2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
<함수 호출>
print(average(10, 20, 30)) #20.0
print(average(4, 23)) #13.5
'''
def average(*number):
    sum_value = 0

    for i in number:
        sum_value += i

    avg = sum_value / len(number)
    return avg

print(average(10, 20, 30))
print(average(4, 23))

print()

'''
Quiz 2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
(소수 첫째자리까지 반올림)
* BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
18.5 미만: 저체중
18.5 이상 23 미만: 보통
23 이상 25 미만: 과체중
25 이상: 비만

<함수 호출>
bmi = get_bmi(176, 69)
print(bmi) #22.3
'''
def get_bmi(height, weight):
    height /= 100
    bmi = weight / (height * height)

    if bmi < 18.5:   # 저체중
        return round(bmi, 1)
    elif bmi < 23:   # 보통
        return round(bmi, 1)
    elif bmi < 25:   # 과체중
        return round(bmi, 1)
    elif bmi >= 25:  # 비만
        return round(bmi, 1)

bmi = get_bmi(176, 69)
print(bmi)

print()

# --------------------------------------------------------------------------------------------------------------------

'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1
'''
def n_sum(number_1):
    num_str = str(number_1)
    sum_value = 0

    if len(num_str) < 10:
        # index 방식
        # for i in range(len(num_str)):
        #     sum_value += int(num_str[i])
        for i in num_str:       #for i in '408':    i: '4' '0' '8'
            sum_value+= int(i)
        pass
    else:
        sum_value = -1

    return sum_value


# result = n_sum(10)
# print(result)
# result = n_sum(331)
# print(result)
# result = n_sum(408)
# print(result)
# result = n_sum(1000000000)
# print(result)

print()

'''
Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
* 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(61)
print(fare)        #1720
'''
def get_subway_fare(km):
    money = 720

    if km <= 10:
        return money

    if 10 < km <= 50:
        km -= 10

        if km % 5 != 0:
            money += 100

        km = (km // 5) * 100
        money += km
    else:
        money = 720 + ((50-10)//5)*100
        km -= 50

        if km % 8 != 0:
            money += 100

        km = (km // 8) * 100
        money += km
    return money

fare = get_subway_fare(5)
print(fare)

fare = get_subway_fare(26)
print(fare)

fare = get_subway_fare(61)
print(fare)

print()

'''
Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
* 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝
'''
def get_three_six_nine(number):
    cnt = 0
    str_num = str(number)

    for i in str_num:
        if int(i) % 3 == 0:
            cnt += 1
    # index 방식
    # for i in range(len(str_num)):
    #     if int(str_num[i]) % 3 == 0:
    #         cnt += 1

    if cnt == 0:
        return number
    else:
        return cnt * "짝"
        # string = ''
        # for i in range(cnt):
        #     string += '짝'

    # if number == 1 :
    #     return number

    # if number >= 10 :
    #     ten = number // 10
    #     one = number - ten * 10
    #     if ten % 3 == 0:
    #         cnt += 1
    #     if one % 3 == 0:
    #         cnt += 1
    # elif number % 3 == 0:
    #     return "짝"
    #
    # if cnt == 1:
    #     return "짝"
    # elif cnt == 2:
    #     return "짝짝"

result = get_three_six_nine(1)
print(result)
result = get_three_six_nine(3)
print(result)
result = get_three_six_nine(16)
print(result)
result = get_three_six_nine(36)
print(result)

print()

'''
Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
1. 함수의 이름을 정해준다.
2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
3. 리턴하는 것을 말해준다.
4. 출력 예시를 보여준다.
5. 내가 낸 문제의 답안을 제출한다.
-----------------------------------------------------------
Quiz3-4. 가위바위보게임
함수 이름은 game로 한다. 자신이 낼 것(me)을 입력하고 랜덤으로 들어간 컴퓨터(com)와 비교하여
승리와 패배, 무승부를 출력한다.

com = 1
result = game(1)
print(result)   #무승부
result = game(2)
print(result)   #패배
result = game(3)
print(result)   #승리
'''
import random
def game(me):
   list = range(1, 4)
   com = random.choice(list)

   print(f"me = {me}, com = {com}")

   if me == 1:
       if com == 1:
           return "무승부"
       elif com == 2:
           return "패배"
       elif com == 3:
           return "승리"
   elif me == 2:
       if com == 1:
           return "승리"
       elif com == 2:
           return "무승부"
       elif com == 3:
           return "패배"
   elif me == 3:
       if com == 1:
           return "패배"
       elif com == 2:
           return "승리"
       elif com == 3:
           return "무승부"
   else:
       return "입력 오류"

print("가위 : 1 | 바위 : 2 | 보 : 3")

result = game(1)
print(result)
result = game(2)
print(result)
result = game(3)
print(result)

print()

# --------------------------------------------------------------------------------------------------------------------

'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
--------------------------------------------
result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님
'''
def is_prime(num):
    cnt = 0

    for i in range(2, num):
        if num % i == 0:
            cnt += 1

    if cnt != 0:
        return "소수아님"
    else:
        return "소수"

result = is_prime(2)
print(result)
result = is_prime(3)
print(result)
result = is_prime(36)
print(result)

print()

'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
--------------------------------------------
result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황') 
print(result) # 요모야..! 
result = get_compliment('좋은 마음가짐이다!') 
print(result) # 으무!
'''
def get_compliment(answer):
    if answer.find("고구마") != -1:
        return "왓쇼이!"
    elif answer.find("맛있는") != -1:
        return "우마이!"
    elif answer.find("놀랄 만한") != -1:
        return "요모야..!"
    else:
        return "으무!"

result = get_compliment('고구마 된장국')
print(result)
result = get_compliment('맛있는 크레이프')
print(result)
result = get_compliment('놀랄 만한 상황')
print(result)
result = get_compliment('좋은 마음가짐이다!')
print(result)

# --------------------------------------------------------------------------------------------------------------------

'''
Quiz5-1. 모듈이란?
'''
# 필요한 것들끼리 부품처럼 파일로 모여 있는 것
# 함수 정의나 클래스, Python 문장을 담고 있는 것

'''
Quiz5-2. 패키지란?
'''
# 모듈들을 모아놓은 집합
# 하나의 디렉토리에 여러 모듈 파일을 가져다놓은 것

'''
Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
'''
import  theater_module as p학번
p학번.price(3)
p학번.price_morning(4)
p학번.price_soldien(5)

'''
Quiz5-4. __all__의 역할은?
'''
# 패키지의 공개범위를 설정해서 import를 원하는 것만 공개할 수 있도록 만들어줌

'''
Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
'''
# if __name__ == "__main__":
#     print("Thailand 모듈을 직접 실행")
#     print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
#     trip_to= ThailandPackage()
#     trip_to.detail()
# else:
#     print("Thailand 외부에서 모듈 호출")

'''
Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
------------------------------------------------------
import travel.vietnam
< 가 > 


from travel import vietnam
< 나 > 


from travel.vietnam import ThailandPackage

< 다 > 
'''
# # < 가 >
# trip_to = travel.vietnam.VietnamePackage()
#
# # < 나 >
# trip_to = vietnam.VietnamePackage()
#
# # < 다 >
# trip_to = ThailandPackage()
