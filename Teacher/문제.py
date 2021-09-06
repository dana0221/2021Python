# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
import math

bill = 62421
print(bill // 100 * 100)
print(bill - bill % 100)
print(math.floor(bill / 100) * 100)
print(int(bill / 100) * 100)

print('-' * 10)

# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
score = 93

print(round(score / 10) * 10)
print(round(score, -1))

print('-' * 10)

# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
import random

print(random.sample(range(1, 46), 6))

print('-' * 10)

# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
list_r = random.sample(range(1, 9 + 1), 3)
print("".join(str(n) for n in list_r))
print("".join(map(str, list_r)))

print('-' * 10)

# 5. 내가 태어난 날로부터 며칠이 지났는지?
import datetime

now = datetime.datetime.now()
birthday = datetime.datetime(2004, 2, 21, 2, 21)

print(now - birthday)

print('-' * 10)

# 6. 올해 크리스마스까지 며칠이 남았는지?
now = datetime.datetime.now()
christmas = datetime.datetime(2021, 12, 25)

print(christmas - now)

print('-' * 10)

# 7. 내 생일이 며칠 남았는지?
now = datetime.datetime.now()
next_birthday = datetime.datetime(2021, 2, 21)

if next_birthday < now:
    next_birthday = next_birthday.replace(year=2022)

next_birthday = datetime.datetime(2022, 2, 21)

print(next_birthday - now)

print('-' * 10)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
last_num = int(input('마지막 번호를 입력하세요'))
list_num = list(range(1, last_num + 1))
print(list_num)

while True:
    del_num = input('제거할 번호를 입력하세요[enter:종료]')

    if del_num == '':
        break

    list_num.remove(int(del_num))
    print(list_num)

random.shuffle(list_num)

print('자리\t학번')

for i, number in enumerate(list_num):
    print(f'{i + 1}\t{number}')