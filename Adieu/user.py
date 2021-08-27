class User:
    def __init__(self, us):  # 원래 등록된 user들 가져오기
        self.name = ''
        self.pw = ''
        self.age = ''
        self.gender = 'w'
        self.number = ''

        self.us = us
        #올린 게시물
        self.up_list = []
        #신청한 게시물
        self.pick_list = []

    def set_all(self):
        # user 객체 보내기 :이름 입력받기
        self.set_name(self.us)
        # 비밀번호 설정
        self.set_pw()
        # 나이
        self.set_age()
        # 성별
        self.set_gender()
        # 전화번호
        self.set_number()

        # 올린 게시물
        self.up_list = []
        # 신청한 게시물
        self.pick_list = []

    # 이름 입력
    def set_name(self, users):  # 매개변수로 이름
        # 중복 체크
        stop = False
        while stop == False:
        # 중복되는 이름이 없으면 나옴
            stop = True
            name = input('이름 : ')

            # 있는지 찾기
            for u in users:
                if name == u.name:
                    print('다시 입력하세요')
                    stop = False
                    break

        self.name = name

    # 나이 입력
    def set_age(self):
        while True:
            age = input('생일 ex(20040810) : ')
            if age.isdigit() == True:
                self.age = age
                break
            else:
                print('잘못 입력했습니다. 다시 입력하세요')


    # 비밀번호 입력
    def set_pw(self):
        self.pw = input('비밀번호 : ')

    # 성별 입력 
    def set_gender(self):
        while True:
            gender = input('성별 w/m : ')
            if gender == 'w' or gender == 'm':
                self.gender = gender
                break
            else:
                print('잘못 입력했습니다. 다시 입력하세요')

    # 전화번호 입력
    def set_number(self):
        while True:
            number = input('전화번호 (숫자만) : ')

            if number.isdigit() == True:
                self.number = number
                break
            else:
                print('잘못 입력했습니다. 다시 입력하세요')

    # 신청한 동물들 보기
    def show_picklist(self):
        for i, pick in enumerate(self.pick_list):
            print(f'{i + 1}. {pick.name} : {pick.kind}')

    # 올린 게시물 보기
    def show_uplist(self):
        for i, up in enumerate(self.up_list()):
            # 올린 동물들 이름과 종류만
            print(f'{i + 1}. {up.name}-{up.kind}')

            # 올렸던 동물들에 신청한 사람들 확인
            print(f'신청한 사람 >> {up.applys}')

    # 사용자 정보 확인
    def __str__(self):
        # 사용자 정보로 수정
        return f' 이름 : {self.name}\n성별 : {self.gender}\n전화번호 : {self.number}'