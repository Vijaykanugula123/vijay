from tkinter import *

root = Tk()
root.geometry("200x200")

def open():
    top = Toplevel(root)

    menubar = Menu(top)
    team = Menu(menubar, tearoff=0)
    #team.add_command(label="CSK")
    #team.add_command(label="MI")
    #team.add_command(label="RCB")
    #team.add_command(label="SRH")

    csk_submenu = Menu(team, tearoff=0, bg='yellow')  # Set the background color to yellow
    #csk_submenu.add_command(label="Batsman")

    # Submenu for Batsman
    batsman_submenu = Menu(csk_submenu, tearoff=0,bg='yellow')
    batsman_submenu.add_command(label="Ruturaj")
    batsman_submenu.add_command(label="Dhoni", background='pink', command=lambda: blink_name(batsman_submenu,'Dhoni'))
    batsman_submenu.add_command(label="Conway")
    batsman_submenu.add_command(label="Rahane")
    batsman_submenu.add_command(label="Dube")

    csk_submenu.add_cascade(label="Batsman", menu=batsman_submenu)

    #csk_submenu.add_command(label="Bowler")
     # Submenu for Bowler in CSK
    csk_bowler_submenu = Menu(csk_submenu, tearoff=0,bg='yellow')
    csk_bowler_submenu.add_command(label="Shardul")
    csk_bowler_submenu.add_command(label="Theekshana")
    csk_bowler_submenu.add_command(label="Deepak",activebackground='pink',command=lambda: blink_name(csk_bowler_submenu,'Deepak'))
    csk_bowler_submenu.add_command(label="Mukesh")
    csk_bowler_submenu.add_command(label="Pathirana")

    csk_submenu.add_cascade(label="Bowler", menu=csk_bowler_submenu)

   # csk_submenu.add_command(label="Allrounder")
   # team.add_cascade(label="CSK", menu=csk_submenu, background='yellow')
    #csk_submenu.add_command(label="Allrounder")
    #team.add_cascade(label="CSK", menu=csk_submenu, background='yellow')
    # Submenu for All-Rounder in CSK
    csk_allrounder_submenu = Menu(csk_submenu, tearoff=0,bg='yellow')
    csk_allrounder_submenu.add_command(label="Moeen Ali")
    csk_allrounder_submenu.add_command(label="Jadeja", background='pink', command=lambda: blink_name(csk_allrounder_submenu,'Jadeja'))
    csk_allrounder_submenu.add_command(label="Mitchell")

    csk_submenu.add_cascade(label="All-Rounder", menu=csk_allrounder_submenu)

    team.add_cascade(label="CSK", menu=csk_submenu, background='yellow')

    # Submenu for MI
    mi_submenu = Menu(team, tearoff=0, bg='blue')  # Set the background color to blue
    #mi_submenu.add_command(label="Batsman")

    # Submenu for Batsman in MI
    mi_batsman_submenu = Menu(mi_submenu, tearoff=0,bg='blue')
    mi_batsman_submenu.add_command(label="Surya")
    mi_batsman_submenu.add_command(label="Tim David")
    mi_batsman_submenu.add_command(label="Rohith", background='pink', command=lambda: blink_name('Rohith'))
    mi_batsman_submenu.add_command(label="Tilak")
    mi_batsman_submenu.add_command(label="Ishan")
    mi_submenu.add_cascade(label="Batsman", menu=mi_batsman_submenu)

    #mi_submenu.add_command(label="Bowler")
    mi_bowler_submenu = Menu(mi_submenu, tearoff=0,bg='blue')
    mi_bowler_submenu.add_command(label="Karthikeya")
    mi_bowler_submenu.add_command(label="Chawla")
    mi_bowler_submenu.add_command(label="Madhwal")
    mi_bowler_submenu.add_command(label="Behrendoff")
    mi_bowler_submenu.add_command(label="Bumrah", background='pink',command=lambda:blink_name('Bumrah')) 
    mi_submenu.add_cascade(label="Bowler", menu=mi_bowler_submenu)
    
    #mi_submenu.add_command(label="Allrounder")
    # Submenu for All-Rounder in MI
    # Submenu for All-Rounder in MI
    mi_allrounder_submenu = Menu(mi_submenu, tearoff=0,bg='blue')
    mi_allrounder_submenu.add_command(label="Shepard")
    mi_allrounder_submenu.add_command(label="Hardik", background='pink', command=lambda: blink_name('Hardik'))
    mi_allrounder_submenu.add_command(label="Shams")

    mi_submenu.add_cascade(label="All-Rounder", menu=mi_allrounder_submenu)

    team.add_cascade(label="MI", menu=mi_submenu, background='blue')
    # Submenu for SRH
    srh_submenu = Menu(team, tearoff=0, bg='orange')  # Set the background color to orange
    #srh_submenu.add_command(label="Batsman")

    # Submenu for Batsman in SRH
    srh_batsman_submenu = Menu(srh_submenu, tearoff=0,bg='orange')
    srh_batsman_submenu.add_command(label="Mayank")
    srh_batsman_submenu.add_command(label="Abhishek")
    srh_batsman_submenu.add_command(label="Rahul", background='pink', command=lambda: blink_name('Rahul'))
    srh_batsman_submenu.add_command(label="Markram")
    srh_batsman_submenu.add_command(label="Head")

    srh_submenu.add_cascade(label="Batsman", menu=srh_batsman_submenu)

    #srh_submenu.add_command(label="Bowler")
    # Submenu for Bowler in SRH
    srh_bowler_submenu = Menu(srh_submenu, tearoff=0,bg='orange')
    srh_bowler_submenu.add_command(label="Nataraj")
    srh_bowler_submenu.add_command(label="Cummins")
    srh_bowler_submenu.add_command(label="Malik")
    srh_bowler_submenu.add_command(label="Bhuvi", background='pink',command=lambda:blink_name('Bhuvi'))
    srh_bowler_submenu.add_command(label="Markande")

    srh_submenu.add_cascade(label="Bowler", menu=srh_bowler_submenu)
    #srh_submenu.add_command(label="Allrounder")
    # Submenu for All-Rounder in SRH
    srh_allrounder_submenu = Menu(srh_submenu, tearoff=0,bg='orange')
    srh_allrounder_submenu.add_command(label="Jasen")
    srh_allrounder_submenu.add_command(label="Hasaranga", background='pink', command=lambda: blink_name('Hasaranga'))
    srh_allrounder_submenu.add_command(label="Samad")
    srh_submenu.add_cascade(label="All-Rounder", menu=srh_allrounder_submenu)

    team.add_cascade(label="SRH", menu=srh_submenu, background='orange')
    
    # Submenu for RCB
    rcb_submenu = Menu(team, tearoff=0, bg='red')  # Set the background color to red
    #rcb_submenu.add_command(label="Batsman")

    # Submenu for Batsman in RCB
    rcb_batsman_submenu = Menu(rcb_submenu, tearoff=0,bg='red')
    rcb_batsman_submenu.add_command(label="Patidar")
    rcb_batsman_submenu.add_command(label="Jacks")
    rcb_batsman_submenu.add_command(label="Virat", background='pink', command=lambda: blink_name('Faf Duplesis'))
    rcb_batsman_submenu.add_command(label="Faf duplesis")
    rcb_batsman_submenu.add_command(label="Rawat")

    rcb_submenu.add_cascade(label="Batsman", menu=rcb_batsman_submenu)
    # Submenu for Bowlers in RCB
    rcb_bowler_submenu = Menu(rcb_submenu, tearoff=0,bg='red')
    rcb_bowler_submenu.add_command(label="Topley")
    rcb_bowler_submenu.add_command(label="Akash")
    rcb_bowler_submenu.add_command(label="Vijay")
    rcb_bowler_submenu.add_command(label="Siraj", background='pink',command=lambda:blink_name('Siraj'))
    rcb_bowler_submenu.add_command(label="Himanshu")

    rcb_submenu.add_cascade(label="Bowler", menu=rcb_bowler_submenu)

    # Submenu for All-Rounders in RCB
    rcb_allrounder_submenu = Menu(rcb_submenu, tearoff=0,bg='red')
    rcb_allrounder_submenu.add_command(label="Lomror")
    rcb_allrounder_submenu.add_command(label="Maxwell", background='pink', command=lambda: blink_name('Maxwell'))
    rcb_allrounder_submenu.add_command(label="Karn Sharma")

    rcb_submenu.add_cascade(label="All-Rounder", menu=rcb_allrounder_submenu)

    team.add_cascade(label="RCB", menu=rcb_submenu, background='red')

    #rcb_submenu.add_command(label="Bowler")
    #rcb_submenu.add_command(label="Allrounder")
    #team.add_cascade(label="RCB", menu=rcb_submenu, background='red')

    menubar.add_cascade(label="team", menu=team)    

    top.config(menu=menubar)  
    top.mainloop()

def blink_name(name, batsman_submenu):
    current_color = 'pink'
    blink_colors = ['green', 'blue', 'orange', 'yellow']

    def update_color():
        nonlocal current_color
        current_color = blink_colors.pop(0)
        submenu.entryconfigure(name, background=current_color)
        top.after(500, update_color)
        blink_colors.append(current_color)

    top = Toplevel(root)
    submenu.entryconfigure(name, background=current_color)
    update_color()

btn = Button(root, text="IPL", bd=10, padx=50, pady=25, bg='violet', font=('Arial bold', 20), command=open)  
btn.place(relx=0.5, rely=0.5, anchor=CENTER) 
root.configure(bg='light blue')
root.mainloop()