from tkinter import *
from PIL import ImageTk


def signup_page():
    ab_window.destroy()
    import signup

def login_page():
    ab_window.destroy()
    import login
    
def ab_page():
    ab_window.destroy()
    import About

ab_window=Tk()
ab_window.title('About')
ab_window.iconbitmap(r'C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/ocean.ico')
ab_window.geometry('850x720')
background=ImageTk.PhotoImage(file='C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/aboutpage.png')

bgLabel=Label(ab_window,image=background)
bgLabel.grid(row=0,column=0)

signupButton=Button(ab_window,text='Sign Up',font=('Helvetica', 12, 'bold'), bg='#AEDCF4', fg='#FFFFFF',activeforeground='#8EE5EE',activebackground='#F0F8FF', cursor='hand2', bd=0,command=signup_page)
signupButton.place(x=640,y=20)

loginButton=Button(ab_window,text='Login',font=('Helvetica',12, 'bold'),bg='#AEDCF4',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=login_page)
loginButton.place(x=745,y=20)

abButton=Button(ab_window,text='About',font=('Helvetica',12, 'bold'),bg='#AEDCF4',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=ab_page)
abButton.place(x=550,y=20)

ab_window.mainloop()