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
def Search():
    try:
        myconn=mysql.connector.connect(host="localhost",user="root",passwd="Manojna@123",database="mnm")
        if myconn.is_connected():
            print("connection succssful")
        mycur=myconn.cursor()
        itno=an.get()
        print(itno)
        query="select * from flint where airlinename='{}'".format(itno)
        mycur.execute(query)
        rss=mycur.fetchall()
        #print(rss)
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
        
       
arn=Tk()
arn.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='ang.png')

bgLabel=Label(arn,image=bg,border=0,bg='light blue')
bgLabel.place(x=-160,y=-130)

an=tk.Entry(arn,text='',font=('Microsoft YaHei UI Light',15,'bold'),width=40,bd=0,fg='black',bg='white')
an.place(x=360,y=398)
#x=an.get()
#print(x)
entry=tk.Button(arn,text='Search',font=('Microsoft YaHei UI Light',15,'bold'),width=15,bd=0,cursor='hand2',fg='#C4DDF6',bg='#00245D',activebackground='#00245D',command=Search)
entry.place(x=550,y=480)

back=tk.Button(arn,text='Back',font=('Microsoft YaHei UI Light',10,'bold'),height=0,cursor='hand2',width=13,bd=0,fg='white',bg='black',activebackground='black',command=back)
back.place(x=350,y=570)
arn.mainloop()
