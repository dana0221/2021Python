from tkinter import *
from adieu_main import adieuMain

class StartAdieu():
     def __init__(self):
        # GUI 설정
        root = Tk()
        root.title('Adieu')
        root.geometry('745x580')
        root.configure(bg="#FFC978")
        self.root = root

        # 프레임 설정
        self.mainFrame = Frame(self.root, bg='#FFC978')
        self.mainFrame.pack(expand=True)

        # logo 설정
        loog_img = PhotoImage(file='')

        # 위젯 추가하기
        btn_login = Button(root, padx=84, pady=10, fg='#B96F00', bg='#F0AD48', text='로그인')
        btn_login.pack()
        btn_new_login = Button(root, padx=78, pady=10, fg='#B96F00', bg='#F0AD48',  text='회원가입')
        btn_new_login.pack()
        root.mainloop()