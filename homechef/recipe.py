class Recipe:
    def __init__(self, name):
        # 이름
        self.name = name
        # 인원 수
        self.people = 1
        # 재료, 재료 개수(양)
        self.ingredient = {}    # 딕셔너리로 지정(key(중복 불가, 수정 가능), value 형태로 값을 저장, index로 접근하는 리스트와 다르게 key로 접근한다.)
        # 내용(설명)
        self.contents = ''
        # 영상 링크
        self.video = ''         # 문자열로 지정

    def set_recipe(self):
        self.set_people()
        self.set_contents()
        self.set_ingredient()
        self.set_video()

    def set_people(self):
        people = input('몇 인분인가요?:')

        self.people = '1' if people == '' else people

    def set_ingredient(self):
        while True:
            ingredient = input('재료를 입력하세요 : 예시_"돼지고기 130"\n재료입력이 끝나면 Enter키를 누르세요')

            if ingredient == '':
                break;

            ingredient_name, ingredient_gram = ingredient.split()   # 공백을 기준으로 나눔
            # ingredient.split('나누는 기준 입력')     문자열을 나눠줌

            self.ingredient[ingredient_name] = ingredient_gram
            # self.ingredient[key 값] = value 값  딕셔너리 추가
            # {'감자':'200', '당근':'100'}

    def set_contents(self):
        contents = input('레시피 내용을 입력하세요:')

        # if contents == '':
        #     self.contents = '1'
        # else:
        #     contents
        self.contents = '입력된 정보가 없습니다.' if contents == '' else contents

    def set_video(self):
        video = input('레시피 영상 링크를 입력하세요:')
        self.video = video

        self.video = '입력된 정보가 없습니다' if video == '' else video

    def __str__(self):
        return f'레시피이름:{self.name}\n양:{self.people}인분\n정보:{self.contents}\n재료:{self.ingredient}\n영상링크:{self.video}'

# 카레 = Recipe('카레')
# 카레.set_recipe()
# print(카레)
