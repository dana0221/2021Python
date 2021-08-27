# recipe 파일에서 Recipe를 가져옴
from recipe import Recipe

class Recipebook:
    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

    # 레시피 검색하기
    def search_recipe(self):
        # 찾은 레시피
        searched_recipe = []

        # 검색하고 싶은 레시피 입력
        name = input('원하는 레시피를 입력하세요:')

        # 리스트에 검색한 레시피와 동일한 이름이 있는지 탐색
        for recipe in self.recipe_list:
            # 레시피 존재 여부 체크
                # 사용자가 원하는 레시피 출력
            if name == recipe.name:
                print(recipe)
                searched_recipe.append(recipe)

        # 검색한 레시피가 없다면 없다는 것을 알려줌
        if len(searched_recipe) == 0:
            # 레시피를 추가할지 물어봄
            answer = int(input('검색한 레시피가 존재하지 않습니다. 추가하시겠습니까(1:yes|0:no)'))

            # 레시피를 추가할지 체크
            # 레시피 추가하기
            if answer == 1:
                self.add_recipe()
            else:
                return

    # 레시피 추가하기
    def add_recipe(self):
        # 추가할 레시피 이름 입력
        name = input('레시피 이름을 입력하세요:')

        # 리스트에서 레시피와 동일한 이름이 있는지 탐색
        for recipe in self.recipe_list:
        # 레시피 중복 체크
            # 중복된다면
            if name == recipe.name:
                # 중복된다는 것을 알려줌
                print('이미 존재하는 레시피입니다')
                return

        # 중복되지 않으면 추가
        # 레시피 생성
        new_recipe = Recipe(name)
        new_recipe.set_recipe()

        # 리스트에 추가
        self.recipe_list.append(new_recipe)

    # 재료로 레시피 검색하기
    def search_ingredient(self):
        # 빈 set을 생성 -> 중복 재료를 제거해서 담아줌
        all_ingredient = set()

        # 레시피 북 중 레시피에 있는 재료를 Set에 넣어줌
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredient:
                all_ingredient.add(ingredient)      # set에 재료를 하나씩 추가 -> key 추가(중복X)

        # 모든 재료를 보여줌
        for index, ingredient in enumerate(all_ingredient):
            print(f'{index + 1}. {ingredient}')

        # 검색하고 싶은 재료 입력
        search_num = int(input('사용할 재료의 번호를 입력하세요:'))
        serach_ingredient = list(all_ingredient)[search_num - 1]

        # 레시피 리스트 중 재료 탐색
        for recipe in self.recipe_list:
            # 입력한 재료가 있다면
            if serach_ingredient in recipe.ingredient:
                # 레시피를 보여줌
                print(recipe)

    def init_recipe(self):
        recipe1 = Recipe('떡볶이')
        recipe1.people = 2
        recipe1.contents = '재료를 넣고 끓이세요'
        recipe1.video = 'youtube.com'
        recipe1.ingredient = {'떡':'200', '고추장':'100', '어묵':'100', '양파':'100'}
        self.recipe_list.append(recipe1)

        recipe2 = Recipe('카레')
        recipe2.people = 1
        recipe2.contents = '재료를 넣고 끓이세요'
        recipe2.video = 'youtube.com'
        recipe2.ingredient = {'감자':'200', '당근':'100', '카레가루':'80', '돼지고기':'120'}
        self.recipe_list.append(recipe2)

        recipe3 = Recipe('파스타')
        recipe3.people = 2
        recipe3.contents = '재료를 넣고 볶아주세요'
        recipe3.video = 'youtube.com'
        recipe3.ingredient = {'파스타면':'100', '베이컨':'80', '버섯':'100', '양파':'100', '소스':'120'}
        self.recipe_list.append(recipe3)



    # 모든 레시피 보여주기
    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1}. {recipe}')


    def __str__(self):
        pass

