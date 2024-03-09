from tkinter import *
from PIL import ImageTk

def signup_page():
    front_window.destroy()
    import signup

def login_page():
    front_window.destroy()
    import login
    
def ab_page():
    front_window.destroy()
    import About



front_window=Tk()
front_window.resizable(0,0)
front_window.title('Clean Up Drive')
front_window.iconbitmap(r'pics/ocean.ico')

bgImage = ImageTk.PhotoImage(file='pics/frontpage.png')
bgLabel = Label(front_window,image=bgImage)
bgLabel.grid(row=0,column=0)

signupButton = Button(front_window,text='Sign Up',font=('Helvetica', 12, 'bold'), bg='#CEE7EE', fg='#FFFFFF',activeforeground='#8EE5EE',activebackground='#F0F8FF', cursor='hand2', bd=0,command=signup_page)
signupButton.place(x=710,y=20)

loginButton = Button(front_window,text='Login',font=('Helvetica',12, 'bold'),bg='#CEE7EE',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=login_page)
loginButton.place(x=805,y=20)

abButton = Button(front_window,text='About',font=('Helvetica',12, 'bold'),bg='#CEE7EE',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=ab_page)
abButton.place(x=625,y=20)

front_window.mainloop()