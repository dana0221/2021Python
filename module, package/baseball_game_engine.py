import random

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


# 무한반복
while True:
    # 숫자 물어보기
    guess = input('세 자리 숫자를 입력하세요')

    # 숫자인지 판정
    guess_int = int(guess)



    # strike, ball 판정
    strike, ball = check(guess, answer)

    # 출력
    print(f'{guess} | strike : {strike}, ball : {ball}')

    # 정답 == 입력숫자
    if answer == guess:
        print('정답입니다.')
        break;