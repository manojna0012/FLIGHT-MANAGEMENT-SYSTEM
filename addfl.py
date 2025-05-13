from tkinter import *
from PIL import ImageTk
from tkinter import font
from PIL import Image,ImageTk
#GUIpart
addfl=Tk()
addfl.geometry('1960x1080')
bg=ImageTk.PhotoImage(file='add.png')
bgLabel=Label(addfl,image=bg,border=0,bg='light blue')
bgLabel.place(x=-120,y=-100)

def back():
    addfl.destroy()
    import admin
def trip():
    addfl.destroy()
    import tripdet
def add():
    addfl.destroy()
    import addflight
addtt=Button(addfl,text='Add''\n''Trip details',font=('Microsoft YaHei UI Light',17,'bold'),cursor='hand2',width=10,bd=0,fg='black',bg='#BDE6FA',activebackground='#BDE6FA',command=trip)
addtt.place(x=345,y=360)

addfld=Button(addfl,text='Add''\n''flight details',font=('Microsoft YaHei UI Light',17,'bold'),cursor='hand2',width=11,bd=0,fg='black',bg='#BDE6FA',activebackground='#BDE6FA',command=add)
addfld.place(x=886,y=360)

back=Button(addfl,text='Back',font=('Microsoft YaHei UI Light',15,'bold'),cursor='hand2',width=6,bd=0,fg='white',bg='#272C26',activebackground='#272C26',command=back)
back.place(x=55,y=20)



addfl.mainloop()