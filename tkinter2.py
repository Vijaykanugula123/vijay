from tkinter import *

top = Tk()

def open():
    # CSK
    mb1=  Menubutton(canvas, text="CSK",bg='yellow')
    mb1.menu  =  Menu(mb1,tearoff=0,bg='yellow')
    mb1["menu"]  =  mb1.menu

    helpmenu = Menu(mb1.menu,tearoff=0,bg='yellow')
    nested_menu1 = Menu(helpmenu,tearoff=0,bg='yellow')
    nested_menu1.add_command(label='dhoni')
    nested_menu1.add_command(label='ruturaj',background='pink')
    nested_menu1.add_command(label='dube')
    nested_menu1.add_command(label='rahane')

    nested_menu2 = Menu(helpmenu,tearoff=0,bg='yellow')
    nested_menu2.add_command(label='deepak')
    nested_menu2.add_command(label='mukesh',background='pink')
    nested_menu2.add_command(label='shardul')

    nested_menu3=Menu(helpmenu,tearoff=0,bg='yellow')
    nested_menu3.add_command(label='jadeja')
    nested_menu3.add_command(label='mitchel',background='pink')
    nested_menu3.add_command(label='bravo')

    helpmenu.add_cascade(label='batsman', menu=nested_menu1)
    helpmenu.add_cascade(label='bowler', menu=nested_menu2)
    helpmenu.add_cascade(label='allrounder',menu=nested_menu3)

    mb1.menu.add_cascade(label="players", menu=helpmenu)
    mb1.place(x=750,y=300)
    canvas.create_line(600,100,750,300,width=2,fill='black',arrow='last')
    
    # MI
    mb2=  Menubutton(canvas, text="MI",bg='blue')
    mb2.menu  =  Menu(mb2,tearoff=0,bg='blue')
    mb2["menu"]  =  mb2.menu

    helpmenu = Menu(mb2.menu,tearoff=0,bg='blue')
    nested_menu1 = Menu(helpmenu,tearoff=0,bg='blue')
    nested_menu1.add_command(label='rohith')
    nested_menu1.add_command(label='ishan',background='pink')
    nested_menu1.add_command(label='surya')
    nested_menu1.add_command(label='tilak')

    nested_menu2 = Menu(helpmenu,tearoff=0,bg='blue')
    nested_menu2.add_command(label='jasprit')
    nested_menu2.add_command(label='gerald',background='pink')
    nested_menu2.add_command(label='wadhera')

    nested_menu3=Menu(helpmenu,tearoff=0,bg='blue')
    nested_menu3.add_command(label='hardik')
    nested_menu3.add_command(label='tim david',background='pink')
    nested_menu3.add_command(label='piyush')

    helpmenu.add_cascade(label='batsman', menu=nested_menu1)
    helpmenu.add_cascade(label='bowler', menu=nested_menu2)
    helpmenu.add_cascade(label='allrounder',menu=nested_menu3)

    mb2.menu.add_cascade(label="players", menu=helpmenu)
    mb2.place(x=650,y=300)
    canvas.create_line(600,100,650,300,width=2,fill='black',arrow='last')

    # RCB
    mb3=  Menubutton(canvas, text="RCB",bg='red')
    mb3.menu  =  Menu(mb3,tearoff=0,bg='red')
    mb3["menu"]  =  mb3.menu

    helpmenu = Menu(mb3.menu,tearoff=0,bg='red')
    nested_menu1 = Menu(helpmenu,tearoff=0,bg='red')
    nested_menu1.add_command(label='virat')
    nested_menu1.add_command(label='duplesis',background='pink')
    nested_menu1.add_command(label='rajat')
    nested_menu1.add_command(label='lomror')

    nested_menu2 = Menu(helpmenu,tearoff=0,bg='red')
    nested_menu2.add_command(label='siraj')
    nested_menu2.add_command(label='topley',background='pink')
    nested_menu2.add_command(label='vyshak')

    nested_menu3=Menu(helpmenu,tearoff=0,bg='red')
    nested_menu3.add_command(label='maxwell')
    nested_menu3.add_command(label='karn',background='pink')
    nested_menu3.add_command(label='green')

    helpmenu.add_cascade(label='batsman', menu=nested_menu1)
    helpmenu.add_cascade(label='bowler', menu=nested_menu2)
    helpmenu.add_cascade(label='allrounder',menu=nested_menu3)

    mb3.menu.add_cascade(label="players", menu=helpmenu)
    mb3.place(x=550,y=300)
    canvas.create_line(600,100,550,300,width=2,fill='black',arrow='last')

    # SRH
    mb4=  Menubutton(canvas, text="SRH",bg='orange')
    mb4.menu  =  Menu(mb4,tearoff=0,bg='orange')
    mb4["menu"]  =  mb4.menu

    helpmenu = Menu(mb4.menu,tearoff=0,bg='orange')
    nested_menu1 = Menu(helpmenu,tearoff=0,bg='orange')
    nested_menu1.add_command(label='samad')
    nested_menu1.add_command(label='mayank',background='pink')
    nested_menu1.add_command(label='head')
    nested_menu1.add_command(label='markram')

    nested_menu2 = Menu(helpmenu,tearoff=0,bg='orange')
    nested_menu2.add_command(label='bhuvi')
    nested_menu2.add_command(label='washi')
    nested_menu2.add_command(label='abhishek',background='pink')

    nested_menu3=Menu(helpmenu,tearoff=0,bg='orange')
    nested_menu3.add_command(label='philips')
    nested_menu3.add_command(label='cummins',background='pink')
    nested_menu3.add_command(label='sanvir')

    helpmenu.add_cascade(label='batsman', menu=nested_menu1)
    helpmenu.add_cascade(label='bowler', menu=nested_menu2)
    helpmenu.add_cascade(label='allrounder',menu=nested_menu3)

    mb4.menu.add_cascade(label="players", menu=helpmenu)
    mb4.place(x=450,y=300)
    canvas.create_line(600,100,450,300,width=2,fill='black',arrow='last')
    top.mainloop()
canvas=Canvas(top,width=1500,height=1000)
canvas.pack()
btn = Button(canvas, text="IPL", bd=10, padx=20, pady=20, bg='violet', font=('Arial bold', 20), command=open)  
btn.place(x=550,y=50)
top.configure(bg='light blue')
top.mainloop()