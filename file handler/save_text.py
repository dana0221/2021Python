f = open('text.txt', 'w', encoding='utf-8')

f.write('양가영')
f.write('보라색')
f.write('\n')
f.write('양가영')
f.write('검정색')

f.close()

# 위의 코드와 동일하지만 close()를 따로 작성하지 않아도 자동으로 닫아줌
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('양가영')
    f.write('보라색')
    f.write('\n')
    f.write('양가영')
    f.write('검정색')