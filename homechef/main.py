from recipebook import Recipebook

def print_menu():
    print('1. 레시피 검색하기')
    print('2. 레시피 추가하기')
    print('3. 재료로 검색하기')
    print('4. 전체 레시피 보여주기')
    print('5. 종료하기')

    num = input('메뉴를 선택하세요:')

    return int(num)

def main():
    # 메서드를 사용할 객체 생성
    recipebook = Recipebook()

    while True:
        num = print_menu()

        if num == 1:
            # 레시피 검색하기
            recipebook.search_recipe()

        elif num == 2:
            # 레시피 추가하기
            recipebook.add_recipe()

        elif num == 3:
            # 재료로 레시피 검색하기
            recipebook.search_ingredient()

        elif num == 4:
            # 전체 레시피 보여주기
            recipebook.show_recipe()

        elif num == 5:
            # 종료하기
            break;

        # 레시피 수정
        # 레시피 여러 개 검색
        # 인원 수 변경 시 재료량 변경

        else:
            print('다시 입력하세요:')

# 파일은 다른 곳에서 재사용 시에 내가 원하지 않는 부분도 실행하는 것을 방지
if __name__ == '__main__':
    main()