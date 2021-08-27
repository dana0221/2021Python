class Celebrity:
    # 연예인의 이름과 소속사
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_entertinment(self, entertainment):
        self.entertainment = entertainment

    def __str__(self):
        return f"이름:{self.name}\t소속사:{self.entertainment}"
        # <__main Celebrity object at 0x000...>

class Actor(Celebrity):
    def __init__(self, name):
        super().__init__(name)      # Celebriy 클래스 생성자 호출

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        # return f"이름:{self.name}\t소속사:{self.entertainment}\t드라마:{self.drama}"
        return super().__str__() + f"\t드라마:{self.drama}"

class Singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return super().__str__() + f"\t노래:{self.song}"

IU = Celebrity("아이유")
IU.set_entertinment("이담")
# IU.info()
# print(IU.name, IU.entertainment)
print(IU)       # __str__() 클래스 호출

방탄 = Celebrity("방탄소년단")
방탄.set_entertinment("빅히트")
print(방탄)

이광수 = Actor("이광수")
이광수.set_entertinment("킹콩")
이광수.set_drama("라이브")
print(이광수)

온유 = Singer("온유", "Don't call me")
온유.set_entertinment("SM")
print(온유)

키 = Singer("키", "View")
키.set_entertinment("SM")
print(키)



샤이니 = []
샤이니.append(온유)
샤이니.append(키)
print(샤이니)  # <__main__.Singer object at 0x0000...>
for 멤버 in 샤이니:   #i : 객체
    print(멤버)
# for i in range(len(샤이니)):
#     print(샤이니[i])