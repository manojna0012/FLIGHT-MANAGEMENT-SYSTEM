from tkinter import *
from PIL import ImageTk
from tkinter import font
from PIL import Image,ImageTk
from datetime import datetime
from tkinter import messagebox
import mysql.connector

cust=Tk()
cust.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='customerdetails.png')

bgLabel=Label(cust,image=bg,border=0,bg='light blue')
'''def user():
    cust.destroy()
    import user'''
def skip1():
    cust.destroy()
    import user
    
def clear():
    custid.delete(0,END)
    name.delete(0,END)
    age.delete(0,END)
    contact.delete(0,END)
    check.set(0)
    
def details():
    if custid.get()==''or name.get()=='' or age.get()==''or contact.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='Manojna@123')
            mycur=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue,Please Try Again')
            return
        q1='use mnm'
        mycur.execute(q1)
        query2='create table custdetails(custid int(5),name varchar(20),age int(2),contact varchar(40))'
        #mycur.execute(query2)
        q2='insert into custdetails(custid,name,age,contact) values(%s,%s,%s,%s)'
        mycur.execute(q2,(custid.get(),name.get(),age.get(),contact.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Sucess',' Welcome')
        clear()
        cust.destroy()
        import user
bgLabel.place(x=-120,y=-95)
next1=Button(cust,text='Next',width=15,font=('Lora',16,'bold'),fg='black',bg='#7BB4E3',bd=0,cursor='hand2',activebackground='#7BB4E3',command=details)
next1.place(x=600,y=590)

custid=Entry(cust,text='',border=0,width=22,font=(' Helvetica',16,'bold'),fg='#C4DDF6',bg='#00245D')
custid.place(x=630,y=235)

name=Entry(cust,text='',border=0,width=22,font=(' Helvetica',16,'bold'),fg='#C4DDF6',bg='#00245D')
name.place(x=630,y=320)

age=Entry(cust,text='',border=0,width=22,font=(' Helvetica',16,'bold'),fg='#C4DDF6',bg='#00245D')
age.place(x=630,y=410)
check=IntVar()

contact=Entry(cust,text='',border=0,width=22,font=(' Helvetica',16,'bold'),fg='#C4DDF6',bg='#00245D')
contact.place(x=630,y=490)
skip=Button(cust,text='Skip',border=0,width=8,cursor='hand2',font=(' Helvetica',14,'bold'),fg='black',bg='#E0EDFA',activebackground='#E0EDFA',command=skip1)
skip.place(x=1150,y=52)
cust.mainloop()
