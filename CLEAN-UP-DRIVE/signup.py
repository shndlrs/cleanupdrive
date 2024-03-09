from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)
 
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()==''or passwordEntry.get()=='' or confirmEntry.get()=='' :
        messagebox.showerror('Error', 'All Feilds Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root', password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
        try:
            query='create database cleanupdrive'
            mycursor.execute(query)
            query='use cleanupdrive'
            mycursor.execute(query)
            query='create table users(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        
        except:
            mycursor.execute('use cleanupdrive')

        query='select * from users where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Enter', 'Username Already exists')
        query='insert into users(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Registration is Successful')
        clear()
        signup_window.destroy()
        import login
def menu_page():
    signup_window.destroy()
    import main

def login_page():
    signup_window.destroy()
    import login

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(0,0)
signup_window.iconbitmap(r'pics/ocean.ico')
background=ImageTk.PhotoImage(file='pics/signuppage.png')

bgLabel=Label(signup_window,image=background)
bgLabel.grid(row=0,column=0)

heading=Label(signup_window,text='SIGN UP', font=('Helvetica',15,'bold'),bg='#DEE6F0',fg='black')
heading.place(x=640,y=90)

emailLabel=Label(signup_window,text='Email',font=('Helvetica', 10, 'bold'),bg='#DEE6F0',fg='black')
emailLabel.place(x=575,y=125)

emailEntry=Entry(signup_window,width=30,font=('Helvetica',10),fg='black',bg='#DCE5EF')
emailEntry.place(x=575,y=155,width=230)

usernameLabel=Label(signup_window,text='Username',font=('Helvetica',10,'bold'),bg='#DEE6F0',fg='black')
usernameLabel.place(x=575,y=175)

usernameEntry=Entry(signup_window,width=30,font=('Helvetica',10),fg='black',bg='#DCE5EF')
usernameEntry.place(x=575,y=200,width=230)

passwordLabel=Label(signup_window,text='Password',font=('Helvetica',10,'bold'),bg='#DEE6F0',fg='black')
passwordLabel.place(x=575,y=225)

passwordEntry=Entry(signup_window,width=30,font=('Helvetica',10),fg='black',bg='#DCE5EF')
passwordEntry.place(x=575,y=250,width=230)

confirmLabel=Label(signup_window,text='Confirm Password', font=('Helvetica',10,'bold'),bg='#DEE6F0',fg='black')
confirmLabel.place(x=575,y=275)

confirmEntry=Entry(signup_window,width=30,font=('Helvetica',10),fg='black',bg='#DCE5EF', show='*')
confirmEntry.place(x=575,y=300,width=230)

check=IntVar()
termsandconditions=Checkbutton(signup_window,text='I agree to the Terms & Conditions',font=('Helvetica',9,'bold'),fg='black',bg='#DEE6F0',activebackground='white',activeforeground='blue',cursor='hand2',variable=check)
termsandconditions.place(x=575,y=325)

signupButton=Button(signup_window,text='Sign Up',font=('Helvetica',12,'bold'),bd=0,bg='#1668D9',fg='white',activebackground='#159FEE',activeforeground='white',width=17,command=connect_database)
signupButton.place(x=605,y=370)

alreadyaccount=Label(signup_window,text="Don't have an account?", font=('Helvetica',10,'bold'),bg='#DEE6F0',fg='black')
alreadyaccount.place(x=580,y=420)

loginButton=Button(signup_window,text='Sign In',font=('Helvetica',9,'bold underline'),bg='#DEE6F0',fg='blue',bd=0, cursor='hand2', activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=740,y=420)

menuPhoto=PhotoImage(file=r'pics/menu3.png')
menuButton=Button(signup_window,image=menuPhoto,bd=0, bg='#FFFFFF',command=menu_page)
menuButton.place(x=31, y=20)

signup_window.mainloop()
