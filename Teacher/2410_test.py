# 랜덤으로 번호 뽑기
import random
반4 = list(range(1, 20))     #1 - 19까지 list에 삽입
반4.remove(3)    # 3번을 삭제
print(반4)

print(random.choice(반4))

print()
print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

'''
주민등록번호 앞 6자리를 변수 id_number에 넣고,
출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
예시
id_number = 020316 일 때
출력 예시
02
0316
632
'''
id_number = "040221"
# print(id_number[:2])
# print(id_number[2:])
#
# print(id_number[0:2])
# print(id_number[2:6])
#
# print(id_number[-6:-4])
# print(id_number[-4:])
#
# print(id_number[:-4])
# print(id_number[-4:])

year = id_number[:2]
month_day = id_number[2:]

print(year)
print(month_day)

# print(int(id_number[:2]) * int(id_number[2:]))
print(int(year) * int(month_day))
print("곱한 결과 : " + str(int(year) * int(month_day)))     # str과 int를 같이 연결할 수 없음
print("곱한 결과 :", int(year) * int(month_day))     # +가 아닌 , 입력 시 자료형 상관 없음(자동 띄어쓰기)

print()
print()

'''
집 전화번호를 phone_number에 넣고,
지역번호\n맨 끝 네 자리 출력하기
예시
phone_number = 02-1234-5678 또는 032-9876-4321
출력 예시
02			또는		032
5678		또는		4321
'''
phone_number1 = "02-1234-5678"
# print(phone_number1[:-10])
print(phone_number1[:phone_number1.index("-")])
print(phone_number1[-4:])
print()
phone_number2 = "032-9876-4321"
# print(phone_number2[:-10])
print(phone_number1[:phone_number1.index("-")])
print(phone_number2[-4:])

print()
print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# String Format 연습_f-string
name = "양가영"    # 따옴표가 없을 경우 변수명으로 해석   ''와 ""는 상관이 없다(문자와 문자열 구분이 없다) but 작은 따옴표나 큰 따옴표가 사용될 경우는 구분해서 사용
age = 18
# %-formatting
print("안녕 나는 %s이야. 내 나이는 %d살이야" % (name, age))

# str.format()
print("안녕 나는 {}이야. 내 나이는 {}살이야" .format(name, age))

#f-string
print(f"안녕 나는 {name}이야. 내 나이는 {age}살이야")

print()
print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# 이름 10번 출력하기
print(name * 10)    # 문자열 + 문자열 | 문자열 * 정수형

print()
print()

# student_number에 학번을 넣고, 본인의 학급을 출력하기
studnet_number = "2410"
print(studnet_number[1])

# student_number에 학번을 넣고, 본인의 번호를 출력하기(10 이하 인 경우 0 없애기)
# print(studnet_number[-2:][1])   # 문자열 '03' 중의 [1]
print(int(studnet_number[-2:])) # 문자열 안에 있는 숫자를 int형으로 변형

# 휴대폰 번호를 입력할 때 - 가 있든 없든, - 없이 숫자만 출력하기
phone_number1 = "010-2540-5357"
phone_number2 = "010 7584 1367"
phone_number3 = "01073201685"

phone_number = phone_number1
result = phone_number.replace('-', '').replace(' ', '')  # 두 가지의 경우를 해결
print(result)

print()
print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Quiz 2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
student_number = '2100' 또는 student_number = '2000'
<출력 예시>
1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
'''
studnet_number = "2410"
studnet_class = int(studnet_number[1])
majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']

if 1 <= studnet_class <= 6:
    print(f"{studnet_class}반 {majors[studnet_class-1]}")
else:
    print("잘못 입력했습니다.")

print()
print()

'''
Quiz 2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
<함수 호출>
grade, major = get_major('2100')
print(major, grade) #뉴미디어소프트웨어과 2
'''
def get_major(student_number):
    majors = ['소프트웨어과', '소프트웨어과', '웹솔루션과', '웹솔루션과', '디자인과', '디자인과']
    grade = student_number[0]
    class_number = int(student_number[1])

    return grade, majors[class_number-1]

grade, major = get_major("2410")
print(major, grade)


print()
print()

'''
Quiz 2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
<함수 호출>
print(average(10, 20, 30)) #20.0
print(average(4, 23)) #13.5
'''
def average(*numbers):
    return sum(numbers)/len(numbers)
    # len(numbers)를 사용하여 numbers의 갯수를 구함, sum에 기본적으로 함수가 들어있음

print(average(10, 20, 30))
print(average(4, 23))

print()
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
    height /= 100;
    bmi = weight / height ** 2
    return round(bmi, 1)

bmi = get_bmi(176, 69)
print(bmi)

if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("보통")
elif bmi < 25:
    print("과체중")
else:
    print("비만")

print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

# 구구단 7단 출력
print(f"7 X 1 = {7*1}")
print(f"7 X 2 = {7*2}")
print(f"7 X 3 = {7*3}")
print()

for i in range(1, 9 + 1):   #
    print(f"7 X {i} = {7 * i}")
print()

for i in range(2, 10):
    for j in range(1, 10):
        if j % 2 == 0:
            continue
        print(f"{i} X {j} = {i * j}")
    print()

    if i == 7:
        break

print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

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
def n_sum(n):
    sum_value = 0
    n_str = str(n)

    if len(n_str) >= 10:
        return -1
    else:
        for i in range(0, len(n_str)):
            sum_value += i

    return sum_value

result = n_sum(10)
print(result)
result = n_sum(331)
print(result)
result = n_sum(408)
print(result)
result = n_sum(1000000000)
print(result)

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


print()

'''
Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
* 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음

result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝
'''


print()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

