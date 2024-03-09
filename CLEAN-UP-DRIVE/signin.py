from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import pymysql

# Establish a connection to the database
conn = pymysql.connect(host='localhost', user='root', password='', database='cleanupdrive')
cursor = conn.cursor()

# Define the CREATE TABLE query
create_table_query = '''
CREATE TABLE IF NOT EXISTS login_state (
    id INT,
    username VARCHAR(255),
    state VARCHAR(255),
    FOREIGN KEY (id) REFERENCES users(id)
)
'''

try:
    # Execute the CREATE TABLE query
    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'login_state' created successfully.")
except pymysql.Error as e:
    print(f"Error creating table: {str(e)}")

# Close the cursor and connection
cursor.close()
conn.close()

def login_user():

    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='cleanupdrive')
            cursor = conn.cursor()

            query = 'SELECT * FROM users WHERE username = %s AND password = %s'
            cursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
            row = cursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Invalid username or password')
            else:
                messagebox.showinfo('Welcome', 'Login is successful')# Define the INSERT query
    
            # Close the cursor and connection
            cursor.close()
            conn.close()
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error connecting to database: {str(e)}')

def menu_page():
    login_window.destroy()
    import front

def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='pics/closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='pics/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def forgot_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=window)
        else:
            con=pymysql.connect(host='localhost', user='root', password='',database='cleanupdrive')
            mycursor=con.cursor()
            query='select * from users where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query='update users set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                window.destroy()


        
    window = Toplevel()
    window.title('Change Password')

    bgPic=ImageTk.PhotoImage(file='uvob.png')
    bgLabel= Label(window, image=bgPic)
    bgLabel.grid()

    heading_label=Label(window,text='RESET PASSWORD',font=('Helvetica', 15, 'bold'),bg='#DEE6F0',fg='black')
    heading_label.place(x=610,y=90)

    userLabel= Label(window,text='Username',font=('Helvetica', 10, 'bold'),bg='#DEE6F0', fg='black')
    userLabel.place(x=570,y=160)

    user_entry = Entry(window, width=25,fg='black', font=('Helvetica', 10, 'bold'), bg='#DEE6F0', bd=0)
    user_entry.place(x=570,y=187)

    Frame(window, width=250, height=2, bg='azure4').place(x=570, y=206)

    newpassLabel= Label(window,text='New Password',font=('Helvetica', 10, 'bold'),bg='#DEE6F0', fg='black')
    newpassLabel.place(x=570,y=225)

    newpass_entry = Entry(window, width=25,fg='black', font=('Helvetica', 10, 'bold'), bd=0, bg='#DEE6F0')
    newpass_entry.place(x=570,y=250)

    Frame(window, width=250, height=2, bg='azure4').place(x=570, y=270)

    confirmpassLabel= Label(window,text='Confirm Password',font=('Helvetica', 10, 'bold'),bg='#DEE6F0', fg='black')
    confirmpassLabel.place(x=570,y=290)

    confirmpass_entry = Entry(window, width=25,fg='black', font=('Helvetica', 10, 'bold'), bd=0, bg='#DEE6F0')
    confirmpass_entry.place(x=570,y=315)

    Frame(window, width=250, height=2, bg='azure4').place(x=570, y=340)

    submitButton= Button(window, text ='Submit', bd=0, bg='#1668D9', fg='white', font=('Helvetica', 16, 'bold'), width=15, cursor='hand2', activebackground='#159FEE', activeforeground='white', command=change_password)
    submitButton.place(x=595, y=380)

    window.mainloop()

login_window=Tk()
login_window.resizable(0,0)
login_window.title('Login Page')
login_window.iconbitmap(r'C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/ocean.ico')
bgImage=ImageTk.PhotoImage(file='C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/signinpage.png')

bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)
heading=Label(login_window,text='SIGN IN',font=('Helvetica', 15, 'bold'),bg='#DEE6F0',fg='black')
heading.place(x=645,y=90)

usernameLabel=Label(login_window, text='Username',font=('Open Sans',10),fg='black',bg='#DEE6F0')
usernameLabel.place(x=570,y=160)
usernameEntry=Entry(login_window,width=25,font=('Open Sans',10),bd=0,fg='black',bg='#DEE6F0')
usernameEntry.place(x=570,y=180)


usernameEntry.bind('<FocusIn>, user_enter')

frame1=Frame(login_window,width=240,height=2,bg='black')
frame1.place(x=570,y=200)

passwordLabel=Label(login_window,text='Password',font=('Open Sans',10),fg='black',bg='#DEE6F0')
passwordLabel.place(x=570,y=220)
passwordEntry=Entry(login_window,width=25,font=('Open Sans',10),bd=0,fg='black',bg='#DEE6F0')
passwordEntry.place(x=570,y=245)

passwordEntry.bind('<FocusIn>, pass_enter')

frame2=Frame(login_window,width=240,height=2,bg='black')
frame2.place(x=570,y=265)

openeye=PhotoImage(file='C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='#DEE6F0',activebackground='#DEE6F0',cursor='hand2',command=show)
eyeButton.place(x=785,y=243)

forgetButton=Button(login_window,text='Forgot Password?',font=('Helvetica',9, 'bold'),bd=0,fg='#159FEE',bg='#DEE6F0',cursor='hand2',command=forgot_pass)
forgetButton.place(x=700,y=275)

loginButton=Button(login_window,text='Login', font=('Helvetica', 14, 'bold'),width=16,fg='#FFFFFF',bg='#1668D9',activeforeground='white',activebackground='#159FEE', cursor='hand2',bd=0,command=login_user)
loginButton.place(x=590,y=320)

orLabel=Label(login_window,text='---------------OR---------------', font=('Helvetica',9),fg='#000000',bg='#DEE6F0')
orLabel.place(x=620,y=360)

signupLabel=Label(login_window,text='Dont have an account?',font=('Helvetica',9),fg='black',bg='#DEE6F0')
signupLabel.place(x=585,y=400)

newaccountButton=Button(login_window,text='Create new one',font=('Helvetica', 8, 'bold underline'),bg='#DEE6F0',fg='blue',activeforeground='white',activebackground='white', cursor='hand2', bd=0,command=signup_page)
newaccountButton.place(x=715,y=400)

menuPhoto=PhotoImage(file=r'C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/menu3.png')
menuButton=Button(login_window,image=menuPhoto,bd=0, bg='#FFFFFF',command=menu_page)
menuButton.place(x=31, y=20)



login_window.mainloop()
