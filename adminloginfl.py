from tkinter import *
from PIL import ImageTk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#Functionality part
def signup3():
    login.destroy()
    import signupadminfl
    
def onenter(event):
    if username.get()=='Username':
        username.delete(0,END)
def password(event):
    if code.get()=='Password':
        code.delete(0,END)
def hide():
    openeye.config(file='closeye2.png')
    code.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='open2.png')
    code.config(show='')
    eyebutton.config(command=hide)
def loginuser():
    if username.get()=='' or code.get()=='':
        messagebox.showerror('Error','All fields must be filled')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='Manojna@123')
            mycur=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try agin')
            return
        q1='use userdata'
        mycur.execute(q1)
        q5='select * from data where username=%s and password=%s'
        
        mycur.execute(q5,(username.get(),code.get()))
        
        row=mycur.fetchone()
        print(row)
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login succesful')
            login.destroy()
            import admin

            
            
#GUIpart
login=Tk()
login.geometry('1920x1080')
bg=ImageTk.PhotoImage(file='adminloginbg.png')
bgLabel=Label(login,image=bg,border=0,bg='light blue')
bgLabel.place(x=-160,y=-140)
#####################FONT######################
username=Entry(login,width=25,font=('Microsoft YaHei UI Light',13,'bold'),bd=0,fg='grey',bg='#BDE6FA')
username.place(x=770,y=286)
username.insert(0,'Username')
username.bind('<FocusIn>',onenter)

##################password##############################
code=Entry(login,width=25,font=('Microsoft YaHei UI Light',13,'bold'),bd=0,fg='grey' ,bg='#BDE6FA')
code.place(x=770,y=413)
code.insert(0,'Password')

code.bind('<FocusIn>',password)

#############################################EYEBUTTON#############################################################
openeye=PhotoImage(file='open2.png')
eyebutton=Button(login,image=openeye,bd=0,bg='#BDE6FA',activebackground='light blue',cursor='hand2',command=hide)
eyebutton.place(x=1072,y=413)
 ######################################LOGINBUTTON##########################
loginButton=Button(login,text='Login',width=15,font=('Lora',16,'bold'),fg='#89C7E1',bg='#2D0C8B',bd=0,cursor='heart',activebackground='#2D0C8B',command=loginuser)
loginButton.place(x=815,y=502)

#########################################ACCOUNT?####################################
signupb=Label(login,text="Dont have an account ?",font=('Microsoft YaHei UI Light',14,'bold'),fg='#89C7E1',bg='white',bd=0)
signupb.place(x=740,y=555)
######################################RIGESTER########################################333
signup=Button(login,text='Register',font=('Microsoft YaHei UI Light',13,'bold underline'),fg='#2D0C8B',bg='white',bd=0,cursor='hand2',activeforeground='white',activebackground='white',command=signup3)
signup.place(x=975,y=553)



login.mainloop()
