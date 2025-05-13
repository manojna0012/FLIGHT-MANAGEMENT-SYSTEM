from PIL import ImageTk
from tkinter import font
import datetime
from PIL import Image,ImageTk
#from tkcalendar import Calendar
from tkinter import *
from tkinter import messagebox
import mysql.connector
#GUIpart
byfl=Tk()
byfl.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='byfl.png')

bgLabel=Label(byfl,image=bg,border=0,bg='light blue')
bgLabel.place(x=-130,y=-70)
def focus_next_box(event, widget_list):
    widget_list[(widget_list.index(event.widget) + 1) % len(widget_list)].focus_set()
def booking():
    no=noflyers.get()
    pay=int(no)*1000
    if custid.get()==''or Boardingdate.get()=='':
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
        query2='create table flbooking (custid varchar(100) ,flid varchar(100), noflyers int(5),flname varchar(100), departurecity varchar(100),Boardingdate varchar(100),Arrivingdate varchar(100),Arrivalcity varchar(100))'
        #mycur.execute(query2)
        q2='insert into flbooking(Flid,custid,flname,noflyers,Departurecity,Boardingdate,Arrivalcity,Arrivingdate) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        mycur.execute(q2,(flid.get(),custid.get(),flname.get(),noflyers.get(),Departurecity.get(),Boardingdate.get(),Arrivalcity.get(),Arrivingdate.get()))
        con.commit()
        con.close()
        messagebox.showinfo('The amount of your payment',pay)
        
        byfl.destroy()
        import payment
    
def q22():
    byfl.destroy()
    import user
custid=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
custid.place(x=700,y=195)

flid=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
flid.place(x=700,y=240)

noflyers=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
noflyers.place(x=700,y=290)

flname=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
flname.place(x=700,y=340)

Departurecity=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
Departurecity.place(x=700,y=390)

Boardingdate=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
Boardingdate.place(x=700,y=445)

Arrivingdate=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
Arrivingdate.place(x=700,y=500)

Arrivalcity=Entry(byfl,text='',font=('Microsoft YaHei UI Light',10,'bold'),width=40,bd=0,fg='black',bg='#FCF8F1')
Arrivalcity.place(x=700,y=560)

entry_list = [custid, flid, noflyers,flname,Departurecity,Boardingdate,Arrivingdate,Arrivalcity]
for entry in entry_list:
    entry.bind('<Return>', lambda event, entry_list=entry_list: focus_next_box(event, entry_list))


next1=Button(byfl,text='Next',width=5,font=('Lora',14,'bold'),fg='white',bg='#233F54',bd=0,cursor='hand2',activebackground='#233F54',command=booking)
next1.place(x=550,y=636)
q1=Button(byfl,text='Back',width=9,font=('Lora',14,'bold'),fg='white',bg='#37678A',bd=0,cursor='hand2',activebackground='#37678A',command=q22)
q1.place(x=55,y=33)
byfl.mainloop()