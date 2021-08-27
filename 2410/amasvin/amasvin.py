class Drink:
    _CUPS = ("레귤러", "점보")       # 기본값 = 레귤러
    _ICES = ("0%", "50%", "100%", "150%")   # 100%
    _SUGARS = ("0%", "50%", "100%", "150%")     # 100%

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0    # 레귤러
        self.ice = 2    # 100%
        self.sugar = 2  # 100%

    def set_cup(self):
        # 컵 종류 보여주기
        for index, cup in enumerate(Drink._CUPS):
                print(f"{index + 1} {cup}")

        # 컵 선택 후 self에 넣기
        cup = input("컵 사이즈를 선택하세요:")

        if cup == "":   # 입력값이 없다면 기본값으로 지정
            self.cup = 0
        else:
            self.cup = int(cup) - 1

        # 컵 사이즈에 따른 가격 변동(점보는 +500)
        if self.cup == 1:
            self.price += 500

    def set_ice(self):
        # 얼음량 종류 보여주기
        for index, ice in enumerate(Drink._ICES):
                print(f"{index + 1} {ice}")

        # 얼음 선택 후 self에 넣기
        ice = input("얼음량을 선택하세요")
        
        if ice == "":
            self.ice = 2
        else:
            self.ice = int(ice) - 1

    def set_sugar(self):
        # 당도 종류 보여주기
        for index, sugar in enumerate(Drink._SUGARS):
                print(f"{index + 1} {sugar}")

        # 당도 선택 후 self에 넣기
        sugar = input("당도를 선택하세요")
        
        if sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(sugar) - 1

        # self.sugar = 2 if sugar == "" else self.sugar = int(sugar) - 1

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f"이름:{self.name}\t가격:{self.price}원\t컵사이즈:{Drink._CUPS[self.cup]}\t얼음량:{Drink._ICES[self.ice]}\t당도:{Drink._SUGARS[self.sugar]}"

class Coffee(Drink):
    # Drink의 내용을 상속 받아 그대로 사용
    pass

class Bubbletea(Drink):
    _PEARLS = ("타피오카", "화이트", "알로에", "코코넛")
    def __init__(self, name, price):
        # 부모 초기화
        super().__init__(name, price)
        self.pearl = 0

    def set_pearl(self):
        # 펄 종류 보여주기
        for index, pearl in enumerate(Bubbletea._PEARLS):
            print(f"{index + 1} {pearl}")

        # 펄 선택 후 self에 넣기
        pearl = input("펄을 선택하세요")

        if pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(pearl) - 1

    def order(self):
        # Drink.order(self)
        super().order()
        self.set_pearl()

    def __str__(self):
        result = super().__str__()
        return result + f"\t펄:{Bubbletea._PEARLS[self.pearl]}"

class Oreder:
    def __init__(self):
        self.menu = []
        self.init_menu()
        self.order_menu = []

    def init_menu(self):
        # 매장에 있는 음료수
        cof1 = Coffee("아메리카노", 2000)
        bub1 = Bubbletea("오레오 쉐이크", 3900)
        bub2 = Bubbletea("애플망고스무디", 3700)

        self.menu.append(cof1)
        self.menu.append(bub1)
        self.menu.append(bub2)

    def show_menu(self):
        # 메뉴 보여주기
        for index, drink in enumerate(self.menu):
            print(f"{index + 1} {drink.name}\t{drink.price}원")

    def order_drink(self):
        # 반복
        while True:
            # 메뉴 보여주기
            self.show_menu()

            # 메뉴 선택
            drink = input("메뉴를 선택하세요")
            drink = int(drink) -1

            # 옵션 선택
            new_drink = self.menu[drink]
            new_drink.order()

            # self.order_menu에 추가
            self.order_menu.append(new_drink)

            # 추가 주문
            is_add = input("더 주문하시겠습니까?(n:종료)")

            if is_add == "n":
                break

        # 내가 고른 메뉴보여주기
        print(self)

    def sum_price(self):
        sum_value = 0
        # 주문한 메뉴 가격 합계
        for drink_price in self.order_menu:
            sum_value += drink_price.price

        return sum_value
    
    def __str__(self):
        # 주문내역 보여주기
        res = "-" * 20 + "주문내역" + "-" * 20 + "\n"

        # 주문한 음료 목록 보여주기
        for drink in self.order_menu:
            res += str(drink) + "\n"

        # 총 가격 보여주기
        res += f"총금액:{self.sum_price()}원"

        return res

# drink = Drink("애플망고스무디", 3700)
# drink.order()
# print(drink)
#
# coffee = Coffee("카페모카", 2500)
# coffee.order()
# print(coffee)

# bubble = Bubbletea("타로버블티", 3900)
# bubble.order()
# print(bubble)

order = Oreder()
order.order_drink()