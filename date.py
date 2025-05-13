from PIL import ImageTk
from tkinter import font
import datetime
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
from tkinter import *
from tkinter import messagebox
import mysql.connector

import tkinter as tk
from tkinter import ttk
def Search():
    try:
        myconn=mysql.connector.connect(host="localhost",user="root",passwd="Manojna@123",database="mnm")
        if myconn.is_connected():
            print("connection succssful")
        mycur=myconn.cursor()
        itno=date1.get()
        #print(itno)
        query="select * from flint where date='{}'".format(itno)
        mycur.execute(query)
        rss=mycur.fetchall()
        print(rss)
        if len(rss)!=0:
            rs=list(rss)
            #print(rs)
            for i in range(len(rs)):
                Flno=rs[i][0]
                airlinename=rs[i][1]
                arriving=rs[i][2]
                departure=rs[i][3]
                airport=rs[i][4]
                boardingtiming=rs[i][5]
                date=rs[i][6]
                priceadult=rs[i][7]
                pricechild=rs[i][8]
            #rs = mycur.fetchall()
            root = tk.Tk() 
            root.geometry("1920x1800")
            root.title("Airline details")
            root['background'] = 'LightBlue'
            tk.Label(root, text ="AIRLINES SEARCH",font = ("Times New Roman Bold", 20)).pack()
            frame = Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9), height = 300, show = "headings")
            tree.pack(side = 'right')
            tree.heading(1, text = "Flight no")
            tree.heading(2, text = "Airline name")
            tree.heading(3, text = "Arriving")
            tree.heading(4, text = "Departure")
            tree.heading(5, text = "Airport")
            tree.heading(6, text = "Boarding Time")
            tree.heading(7, text = "Date")
            tree.heading(8, text = "Price per adult")
            tree.heading(9, text = "Price per child")
            
            tree.column(1, width = 130)
            tree.column(2, width = 130)
            tree.column(3, width = 130)
            tree.column(4, width = 160)
            tree.column(5, width = 200)
            tree.column(6, width = 130)
            tree.column(7, width = 130)
            tree.column(8, width = 100)
            tree.column(9, width = 130)
            #scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            #scroll.pack(side = 'right', fill = 'y')
            #scroll1 = ttk.Scrollbar(frame, orient="horizontal", command=tree.yview)
            #scroll1.pack(side = 'bottom', fill = 'x')
            for val in rs:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4], val[5], val[6],val[7],val[8]))

        #n=len(rs)
        
        else:
            messagebox.showinfo("Airline info","NO SUCH AIRLINE FOUND")
        #else:
            #messagebox.showinfo("ITEM INFO"," Item FOUND ")
                    
                            
                
    except Exception as e:
        print(e)
#GUIpart
date=Tk()
date.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='date.png')

bgLabel=Label(date,image=bg,border=0,bg='light blue')
bgLabel.place(x=-160,y=-130)
def example():
    def print_sel():
        date1.delete(0,END)
        date1.insert(0,cal.selection_get().strftime('%d-%m-%Y'))
        top.destroy()
    top = Toplevel(date)
    cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2023, month=11, day=18)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
        
        
def mm(event):
    if date1.get()=='DD-MM-YYYY':
        date1.delete(0,END)
def calender():
   cal= Calendar(date, selectmode="day",year= 2023, month=3, day=3)
   cal.pack(pady=10)
   cal.place(x=340,y=365)
   
cal1=PhotoImage(file='calender.png')
calb=Button(date,image=cal1,bd=0,bg='white',activebackground='white',cursor='hand2',command=example)
calb.place(x=340,y=326)

date1=Entry(date,font=('Microsoft YaHei UI Light',15,'bold'),width=40,bd=0,fg='grey',bg='white')
date1.place(x=395,y=339)
date1.insert(0,'DD-MM-YYYY')
date1.bind('<FocusIn>',mm)

entry=Button(date,text='Search',font=('Microsoft YaHei UI Light',15,'bold'),width=15,bd=0,cursor='hand2',fg='#C4DDF6',bg='#00245D',activebackground='#00245D',command=Search)
entry.place(x=548,y=460)

date.mainloop()
