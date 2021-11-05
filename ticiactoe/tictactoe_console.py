from tictactoe_gameengine import TictactoeGameEngine

class TictactoeConsole:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        # show_board
        self.game_engine.show_board()

        # 무한반복
        while True:
            # input row, col
            row = int(input('행 : '))
            col = int(input('열 : '))

            # set row, col
            self.game_engine.set(row, col)

            # show_board
            self.game_engine.show_board()

            # set_winner
            winner = self.game_engine.set_winner()

            # 승자가 있거나 무승부일 경우 게임 끝, 결과 출력
            if winner == 'X' or winner == 'O':
                print(f'🎉{winner} 승리🎉')
                break;

            if winner == 'd':
                print('무승부🤔')
                break;

            # change_turn
            self.game_engine.change_turn()

if __name__ == '__main__':
    ttt_console = TictactoeConsole()
    ttt_console.play()

# show board
# input row, col
# set row, col
# show board
# set winner
# 승자가 있으면 끝내고 출력
# change_turn