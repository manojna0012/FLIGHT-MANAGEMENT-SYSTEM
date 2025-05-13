from tkinter import *
from PIL import ImageTk
from tkinter import font
from PIL import Image,ImageTk
#GUIpart
admin=Tk()
admin.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='admin.png')
bgLabel=Label(admin,image=bg,border=0,bg='light blue')
bgLabel.place(x=-70,y=-80)
def back():
    admin.destroy()
    import home
def move_up(event):
    add.place(x=236, y=382)

def move_down(event):
    add.place(x=236, y=385)
    
def move_up1(event):
    update.place(x=459, y=382)

def move_down1(event):
    update.place(x=459, y=385)
    
def move_up2(event):
    delete.place(x=683, y=383)

def move_down2(event):
    delete.place(x=683, y=385)
    
def move_up3(event):
    see.place(x=923, y=383)

def move_down3(event):
    see.place(x=923, y=385)
def add():
    admin.destroy()
    import addfl

def see1():
    admin.destroy()
    import seedata
def updata():
    admin.destroy()
    import updatefl
def det():
    admin.destroy()
    import delflight
    
add=Button(admin,text='Add Flight',font=('Microsoft YaHei UI Light',11,'bold'),height=3,cursor='hand2',width=13,bd=0,fg='black',bg='#00245D',activebackground='#00245D',command=add)
add.place(x=236,y=385)
add.bind('<Enter>', move_up)
add.bind('<Leave>', move_down)

update=Button(admin,text='Update Flight',font=('Microsoft YaHei UI Light',11,'bold'),height=3,cursor='hand2',width=13,bd=0,fg='black',bg='#7BB4E3',activebackground='#7BB4E3',command=updata)
update.place(x=459,y=385)
update.bind('<Enter>', move_up1)
update.bind('<Leave>', move_down1)

delete=Button(admin,text='Delete Flight',font=('Microsoft YaHei UI Light',11,'bold'),height=3,cursor='hand2',width=13,bd=0,fg='black',bg='#8FB9C9',activebackground='#8FB9C9',command=det)
delete.place(x=683,y=385)
delete.bind('<Enter>', move_up2)
delete.bind('<Leave>', move_down2)

see=Button(admin,text='See Bookings',font=('Microsoft YaHei UI Light',11,'bold'),height=3,cursor='hand2',width=13,bd=0,fg='black',bg='#4B6FED',activebackground='#4B6FED',command=see1)
see.place(x=923,y=385)
see.bind('<Enter>', move_up3)
see.bind('<Leave>', move_down3)

q2=Button(admin,text='Back',font=('Microsoft YaHei UI Light',12,'bold'),cursor='hand2',width=10,bd=0,fg='black',bg='#C4DDF6',activebackground='#C4DDF6',command=back)
q2.place(x=30,y=35)

admin.mainloop()