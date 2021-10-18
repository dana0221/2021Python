import random
from custom_error import InvalidLengthError

# 정답 만들기
def make_answer():
    list_answer = random.sample (range(9 + 1), 3)
    return ''.join(map(str, list_answer))

# strike, ball 판정
def check(guess, answer):
    strike = 0
    ball = 0

    for i in range(3):
        for j in range(3):
            if answer[i] == guess[j] and i == j:
                strike += 1
            elif answer[i] == guess[j]:
                ball += 1

    return strike, ball

answer = make_answer()
print(answer)

def save_history(answer, cnt, name):
    with open('baseball_history.txt', 'a', encoding='utf-8') as f:  # 기존의 내용에서 추가
        f.write(f'{answer}:{cnt}:{name}\n')

def load_history():
    cnt_name = {}

    with open('baseball_history.txt', 'r', encoding='utf-8') as f:
        print('-----history-----')

        while True:
            # 한 줄 읽기
            line = f.readline()

            # 읽을 내용 없으면 끝내기
            if line == '':
                break

            # \n 지우기
            print(line.rstrip())    #answer:cnt:name
            line = line.rstrip()    # answer:cnt:name의 데이터
            data = line.split(':')
            cnt_name[data[1]] = data[2]     # {3: name}

        cnt_name = sorted(cnt_name.items())
        return cnt_name[:3]

cnt = 0

# 무한반복
while True:
    # 숫자 물어보기
    guess = input('세 자리 숫자를 입력하세요(t:history)')

    # t 입력 시 불러오기(top3)
    if guess == 't':
        top3 = load_history()
        print(top3)
        continue

    # 숫자인지 판정
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자만 입력하세요')
        continue

    if len(guess) != len(answer):
        # raise InvalidLengthError('정답의 길이와 다름니다.')
        print(f'정답의 길이와 다름니다. {len((answer))} 자리')
        continue

    # strike, ball 판정
    strike, ball = check(guess, answer)
    cnt += 1

    # 출력
    print(f'{guess} | strike : {strike}, ball : {ball}\ttry : {cnt}')

    # 정답 == 입력숫자
    if answer == guess:
        print('정답입니다.')

        # 저장하기(정답, 시도횟수, 이름)
        name = input('이름 : ')
        save_history(answer, cnt, name)

        # 게임기록 불러오기(top3)
        top3 = load_history()
        print(top3)

        break;