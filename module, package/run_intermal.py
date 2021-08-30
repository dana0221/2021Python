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