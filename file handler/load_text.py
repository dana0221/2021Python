# 전체 한꺼번에 읽기
f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()

print(data)

with open('text.txt', 'r', encoding='utf-8') as f:
    data = f.read()

print('-'*15)

# 한 줄씩 읽기
f = open('text.txt', 'r', encoding='utf-8')

while True:
    line = f.readline()

    # 빈칸이면 끝내기
    if line =='':
        break;

    print(line.rstrip())

f.close()

print('-'*15)

# 전체 한 꺼번에 읽고, 줄 별로 리스트
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

for line in lines:
    print(line.rstrip())

print('_'*15)

# quiz
# 이름 : 양가영\t좋아하는 색 : 보라색
# 이름 : 양가영\t좋아하는 색 : 검정색

f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

for line in lines:
    print('이름 : ' + line.rstrip()[:3] + '\t좋아하는 색 : ' + line.rstrip()[-3:])