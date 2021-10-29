class TictactoGameEngine:
    def __init__(self):
        self.borad = list['.' * 9]  # ['.', '.', '.', '.', '.', '.', '.', '.', '.',]

    def show_borad(self):
        print(self.borad)

    def set(self, row, col):
        pass

    def set_winner(self):
        # 입력 값 : self.borad 값을 가져옴
        # 출력 값 :
        # 이기는 법 : 가로3, 세로3, 대각선3
        # 끝나는 경우 : 무승부(승자가 없는 상태로 놓을 자리가 없음), 승자 결정(승자가 있음)
        # 대각선과 끝나는 경우 코딩
        pass

    def change_turn(self):
        pass


if __name__ == '__main__':
    game_engine = TictactoGameEngine()
    game_engine.show_borad()
    game_engine.set(2, 2)
    game_engine.show_borad()
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_borad()
    game_engine.borad = ['.', '.', '.', 'X', 'X', 'X', '.', '.', '.',]
    game_engine.set_winner()
    game_engine.change_turn()
    print(game_engine.turn)