# math
import math
print(math.ceil(3.5))       # 올림
print(math.floor(3.5))      # 내림
print(math.pow(2, 10))      # 제곱
print(math.sin(math.pi/2))

# random
import random
print(random.random())          # o.o <= r <= 1.0
print(random.randrange(1, 10))  # 1 <= r < 10
print(random.randint(1, 10))    # 1 <= r <= 10

list1 = ['굶음', '피자', '김치찜', '닭가슴살']
print(random.choice(list1))     # list1 중 하나
print(list1)
print(random.shuffle(list1))    # list1 섞기
print(list1)
print(random.sample(list1, 2))  # list1에서 랜덤으로 n개 뽑기

# datetime
import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.hour)
birthday = datetime.datetime(2004, 2, 21, 2, 21)
print(birthday)
print(now - birthday)

print('-'*10)

# 문제 1
phone = 59827
phone //= 100
print(phone * 100)

print('-'*10)

# 문제 2
grade = 56
print(round(grade, -1))

print('-'*10)

# 문제 3
rotto = random.sample(range(1, 46), 6)
print(rotto)

print('-'*10)

# 문제 4
numbers = random.sample(range(100, 1000), 1)
print(numbers)

print('-'*10)

# 문제 5
now = datetime.date.today()
birthday = datetime.date(2004, 2, 21)
print(now - birthday)

print('-'*10)

# 문제 6
christmas = datetime.date(2021, 12, 25)
print(christmas - now)

print('-'*10)

# 문제 7
next_birthay = datetime.date(2022, 2, 21)
print(next_birthay - now)

print('-'*10)

# 문제 8
seat = [[0 for col in range(5)] for row in range(5)]
student = random.sample(range(1, 20), 19)
student.remove(3)
seat = [student[i * 5:(i + 1) * 5] for i in range((len(student) + 5 - 1) // 5 )]
print(seat)