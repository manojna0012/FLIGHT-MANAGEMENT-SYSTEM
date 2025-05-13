from tkinter import *
from PIL import ImageTk
from tkinter import font
from PIL import Image,ImageTk
#GUIpart
cancel=Tk()
cancel.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='cancell.png')
 
def backii():
    cancel.destroy()
    import user




from tkinter import *
from PIL import ImageTk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from tkinter import ttk
#GUIpart
def back():
    arn.destroy()
    import search
    
def Searchd():
        myconn=mysql.connector.connect(host="localhost",user="root",passwd="Manojna@123",database="mnm")
        if myconn.is_connected():
            print("connection succssful")
        mycur=myconn.cursor()
        itn=en.get()
        print(itn)
        query="select * from flbooking where custid={}".format(itn)
        mycur.execute(query)
        r=mycur.fetchall()
        #print(rss)
        if len(r)==0:
            messagebox.showinfo("AIRLINE INFO"," BOOK A FLIGHT TO CANCEL... ")
        else:
            Delete()
            

def Delete():
    try:
        myconn=mysql.connector.connect(host="localhost",user="root",passwd="Manojna@123",database="mnm")
        if myconn.is_connected():
            print("connection succssful")
        mycur=myconn.cursor()
        itno=en.get()
        print(itno)
        queryy="delete from flbooking where custid={}".format(itno)
        mycur.execute(queryy)
        myconn.commit()
        messagebox.showinfo("AIRLINE INFO"," YOUR FLIGHT IS CANCELED.YOU WILL NOT BE REFUNDED COMPLETELY. ")
                                          
    except Exception as e:
        print(e)
                  
    

    
bgLabel=Label(cancel,image=bg,border=0,bg='light blue')
bgLabel.place(x=-160,y=-130)

en=Entry(cancel,text='',font=('Microsoft YaHei UI Light',15,'bold'),width=40,bd=0,fg='black',bg='#7BA3B9')
en.place(x=390,y=375)

ok=Button(cancel,text='OK',bd=0,font=('Microsoft YaHei UI Light ',14,'bold'),width=10,fg='black',bg='#C4DDF6',activebackground='#C4DDF6',command=Searchd)
ok.place(x=420,y=472)

back6=Button(cancel,text='Back',bd=0,font=('Microsoft YaHei UI Light ',14,'bold'),width=10,fg='black',bg='#C4DDF6',activebackground='#C4DDF6',command=backii)
back6.place(x=730,y=472)







cancel.mainloop()