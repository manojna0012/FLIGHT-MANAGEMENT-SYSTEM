from tkinter import *
from PIL import ImageTk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from tkinter import ttk

def Display():
    try:
        myconn=mysql.connector.connect(host="localhost",user="root",passwd="Manojna@123",database="mnm")
        if myconn.is_connected():
            print("connection succssful")
        mycur=myconn.cursor()
        query="select * from interflight"
        mycur.execute(query)
        rss=mycur.fetchall()
        #print(rss)
        if len(rss)!=0:
            rs=list(rss)
            #print(rs)
            for i in range(len(rs)):
                Flno=rs[i][0]
                fltype=rs[i][1]
                airlinename=rs[i][2]
                noofseats=rs[i][3]
                noofflights=rs[i][4]
                
            #rs = mycur.fetchall()
            root = tk.Tk() 
            root.geometry("1920x1800")
            root.title("Airline details")
            root['background'] = 'LightBlue'
            tk.Label(root, text ="AIRLINES DISPLAY",font = ("Times New Roman Bold", 20)).pack()
            frame = Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 300, show = "headings")
            tree.pack(side = 'right')
            tree.heading(1, text = "Flight no")
            tree.heading(2, text = "Flight type")
            tree.heading(3, text = "Airline name")
            tree.heading(4, text = "No.of Seats")
            tree.heading(5, text = "No.of flights")
            
            tree.column(1, width = 130)
            tree.column(2, width = 130)
            tree.column(3, width = 130)
            tree.column(4, width = 160)
            tree.column(5, width = 200)

            
            #scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            #scroll.pack(side = 'right', fill = 'y')
            #scroll1 = ttk.Scrollbar(frame, orient="horizontal", command=tree.yview)
            #scroll1.pack(side = 'bottom', fill = 'x')
            for val in rs:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))

        #n=len(rs)
        
        else:
            messagebox.showinfo("Airline Info","Airline not added ")
        #else:
            #messagebox.showinfo("ITEM INFO"," Item FOUND ")
                    
                            
                
    except Exception as e:
        print(e)

def idetails():
    if flno.get()==''or fltype2.get()=='' or arn1.get()==''or arn.get()==''or arn2.get()=='' :
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
        query2='create table interflight(Flno int(20) primary key,Fltype varchar(200),Airlinename varchar(100),Seats int(5),Flweek int(5))'
        #mycur.execute(query2)
        q2='insert into interflight(Flno,Fltype,Airlinename,Seats,Flweek) values(%s,%s,%s,%s,%s)'
        mycur.execute(q2,(flno.get(),fltype2.get(),arn1.get(),arn.get(),arn2.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Airline','Trip details added succesfully')
        Display()






def q3():
    addflad.destroy()
    import addfl
    

addflad=Tk()
addflad.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='addfl.png')

bgLabel=Label(addflad,image=bg,border=0,bg='light blue')
bgLabel.place(x=-160,y=-120)

flno=tk.Entry(addflad,text='',font=('play',12,'bold'),width=15,bd=0,fg='#00245D',bg='#E0EDFA')
flno.place(x=320,y=114)

fltype2=tk.Entry(addflad,text='',font=('play',12,'bold'),width=20,bd=0,fg='#00245D',bg='#E0EDFA')
fltype2.place(x=280,y=186)

arn1=tk.Entry(addflad,text='',font=('play',12,'bold'),width=20,bd=0,fg='#00245D',bg='#E0EDFA')
arn1.place(x=310,y=256)

arn=tk.Entry(addflad,text='',font=('play',12,'bold'),width=20,bd=0,fg='#00245D',bg='#E0EDFA')
arn.place(x=285,y=325)

arn2=tk.Entry(addflad,text='',font=('play',12,'bold'),width=20,bd=0,fg='#00245D',bg='#E0EDFA')
arn2.place(x=390,y=390)

addtt=Button(addflad,text='Add',font=('Microsoft YaHei UI Light',13,'bold'),cursor='hand2',width=14,bd=0,fg='black',bg='#37678A',activebackground='#37678A',command=idetails)
addtt.place(x=405,y=495)

q1=Button(addflad,text='Back',font=('Microsoft YaHei UI Light',13,'bold'),cursor='hand2',width=14,bd=0,fg='black',bg='#37678A',activebackground='#37678A',command=q3)
q1.place(x=143,y=495)

addflad.mainloop()