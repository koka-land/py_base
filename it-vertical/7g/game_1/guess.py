from tkinter import *
from tkinter import ttk

game = Tk()

width, height = 600, 600
screen_width, screen_height = game.winfo_screenwidth(), game.winfo_screenheight()
x, y = (screen_width/2) - (width/2), (screen_height/2) - (height/2)

game.geometry('%dx%d+%d+%d' % (width, height, x, y))
game.title('Угадайка')

title_frame = Frame(game,
                    bg='#2D1016')
control_frame = Frame(game,
                      bg='#FDF1D8')
title_frame.pack(fill=BOTH,
                 ipadx=50,)
control_frame.pack(fill=BOTH,
                   ipady=10)

button_style = ttk.Style()
button_style.theme_use('alt')
button_style.configure("Button.TButton",
                       font=('PT Sans', 18),
                       background='#ECD5BB',
                       foreground='#FF8000',
                       borderwidth=2)
button_style.map('Button.TButton',
                 foreground=[('disabled', '#FF8000'),
                             ('pressed', '#ECD5BB'),
                             ('active', '#FDF1D8')],
                 background=[('disabled', '#123123'),
                             ('pressed', '!focus', '#ECD5BB'),
                             ('active', '#FF8000')],
                 highlightcolor=[('focus', '#2D1016'),
                                 ('!focus', '#2D1016')],
                 relief=[('pressed', 'flat'),
                         ('!pressed', 'flat')])

title_heading = Label(title_frame,
                      text='УГАДАЙКА',
                      bg='#2D1016',
                      fg="#FDF1D8",
                      font=('PT Sans', 60))
title_subheading = Label(title_frame,
                      text='Интелектуальная игра. Не для всех.',
                      bg='#2D1016',
                      fg="#FDF1D8",
                      font=('PT Sans', 18))
title_heading.pack(fill=BOTH,
                   pady=(150, 0))
title_subheading.pack(fill=BOTH,
                      pady=(0, 150))

button_ai = ttk.Button(control_frame,
                       text='Загадывает ИИ',
                       style='Button.TButton')
button_user = ttk.Button(control_frame,
                         text='Угадывает ИИ',
                         style='Button.TButton')
button_ai.pack(fill=BOTH,
               side=LEFT,
               padx=(25, 5),
               pady=5,
               expand=True)
button_user.pack(fill=BOTH,
                 side=LEFT,
                 padx=(5, 25),
                 pady=5,
                 expand=True)

game.mainloop()
