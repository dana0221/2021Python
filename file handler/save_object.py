import pickle

from person import Person

# 객체 생성
num9 = Person('송주연', '검정색')
num10 = Person('양가영', '보라색')

# 리스트 생성
friends = [num9, num10]

for i in friends:
    print(i)

# 저장
# 1. 객체 하나 저장
import pickle

with open('object.bin', 'wb') as f:
    pickle.dump(num10, f)

# 2. 객체 여러 개 저장
with open('object.bin', 'wb') as f:
    pickle.dump(friends, f)