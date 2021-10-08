import  pickle

# 객체 하나 불러오기
with open('object.bin', 'rb') as f:
    p1 = pickle.load(f)

print(p1)

# 객체 여러 개 불러오기
with open('object.bin', 'rb') as f:
    friends = pickle.load(f)

for person in friends:
    print(person)