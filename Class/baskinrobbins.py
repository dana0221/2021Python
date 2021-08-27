'''
class Icecream:
    # 이름 name | 설명 explanation
    def __init__(self, name):   # 생성자, 변수 초기화
        self.name = name

    def set_explanation(self, explanation):
        self.explanation = explanation

    def __str__(self):
        return f"이름:{self.name}"

민트초콜릿칩 = Icecream("민트초콜릿칩")
민트초콜릿칩.set_explanation("쿨한 그녀들의 선택! 상쾌한 민트향에 초코칩까지!")
print(민트초콜릿칩)
print(민트초콜릿칩.explanation)

요거트 = Icecream("31요거트")
민트초콜릿칩.set_explanation("유산균이 살아있는 오리지널 요거트 아이스크림")
print(요거트)
print(요거트.explanation)

민트초코봉봉 = Icecream("민트초코봉봉")
민트초콜릿칩.set_explanation("민트초코와 엄마는 외계인이 만났다!")
print(민트초코봉봉)
print(민트초코봉봉.explanation)
'''

class Order:
    # 클래스 변수
    # 상수로 선언한다는 표현(Python은 상수와 변수 구분이 없음)
    _CATEGOROIES = ("싱글레귤러", "더블레귤러", "파인트")
    _PRICES = (3200, 6200, 8200)

    def __init__(self):     # 카테고리를 입력 받아서 초기화
        # 종류 콘, 컵, 파인트 | 메뉴 | 주문한 메뉴
        self.set_cateries()
        self.menu = []
        self.init_menu()
        self.order_menu = []

    def set_cateries(self):
        for index, catefory in enumerate(Order._CATEGOROIES):
            print(index + 1, catefory)

        # 종류를 고른다(싱글레귤러, 더블레귤러, 파인트...)
        category_numder = input("종류를 골라주세요 : ")     # 문자열로 입력
        self.category = int(category_numder)    # 입력 후 정수로 저장
        print("-" * 20)

    # 메뉴 초기화
    def init_menu(self):
        # 아이스크립을 객체화해서 추가
        self.menu.append("민트초코봉봉")
        self.menu.append("엄마는외계인")
        self.menu.append("31요거트")

    # 초기화 완료

    def show_menu(self):    # 메뉴를 보여줌
        for index, icecream in enumerate(self.menu):
            print(f"{index + 1} {icecream}")

        print("-"*20)
    def order(self):

        # 아이스크림 보여주기(메뉴)
        self.show_menu()

        # 종류에 따라 반복
        for _ in range(self.category):  # 변수를 사용하지 않음
            # 메뉴선택
            icecream = input("아이스크림을 고르세요 : ")
            icecream = int(icecream)
            # 주문한 메뉴 추가
            self.order_menu.append(self.menu[icecream - 1])

        # 종류 출력
        print("-"*10 + "주문 내역" + "-"*10)
        print(Order._CATEGOROIES[self.category - 1])
        print(str(Order._PRICES[self.category - 1]), "원")

        # 주문한 메뉴 출력
        for icecream in self.order_menu:
            print(icecream)

order = Order()
order.order()
