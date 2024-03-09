from tkinter import * 
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import pymysql
from tkinter import messagebox


def signup_page():
    cho_window.destroy()
    import signup

def login_page():
    cho_window.destroy()
    import signin
def ab_page():
    cho_window.destroy()
    import About

cho_window=tk.Tk()
r1_v=tk.StringVar()
r1_v.set(None)
cho_window.title('Clean Up Information')
cho_window.iconbitmap(r'C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/ocean.ico')
cho_window.geometry('850x720')
cho_window.config(bg='gray90')



background=ImageTk.PhotoImage(file='C:/Users/ASUS/OneDrive/Desktop/VS-Programming/CLEAN-UP-DRIVE/pics/infopage.png')

bgLabel=Label(cho_window,image=background)
bgLabel.grid(row=0,column=0)

signupButton=Button(cho_window,text='Sign Up',font=('Helvetica', 12, 'bold'), bg='#9DC4E5', fg='#FFFFFF',activeforeground='#8EE5EE',activebackground='#F0F8FF', cursor='hand2', bd=0,command=signup_page)
signupButton.place(x=640,y=20)

loginButton=Button(cho_window,text='Login',font=('Helvetica',12, 'bold'),bg='#9DC4E5',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=login_page)
loginButton.place(x=745,y=20)

abButton=Button(cho_window,text='About',font=('Helvetica',12, 'bold'),bg='#9DC4E5',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=ab_page)
abButton.place(x=550,y=20)

def check_page():
    # Connect to the database
    conn = pymysql.connect(host='localhost', user='root', password='', database='cleanupdrive')
    cursor = conn.cursor()

    # Check if the table already exists
    cursor.execute("SHOW TABLES LIKE 'cleanupinfo'")
    table_exists = cursor.fetchone()

    if table_exists is None:
        # Create the table if it doesn't exist
        cursor.execute('''CREATE TABLE cleanupinfo (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            first_name VARCHAR(255),
                            last_name VARCHAR(255),
                            state VARCHAR(255),
                            postal_code VARCHAR(255),
                            phone_number VARCHAR(255),
                            organization VARCHAR(255),
                            email VARCHAR(255),
                            clean_up_event VARCHAR(255),
                            years VARCHAR(255),
                            activity_location VARCHAR(255),
                            activity_type VARCHAR(255),
                            environmental_type VARCHAR(255),
                            sdg1 VARCHAR(255),
                            sdg2 VARCHAR(255),
                            sdg3 VARCHAR(255),
                            sdg4 VARCHAR(255),
                            sdg5 VARCHAR(255),
                            sdg6 VARCHAR(255),
                            sdg7 VARCHAR(255),
                            sdg8 VARCHAR(255)
                            )''')

    # Insert the data into the table
    first_name = fnameEntry.get()
    last_name = lnameEntry.get()
    state = stateEntry.get()
    postal_code = postalEntry.get()
    phone_number = phoEntry.get()
    organization = orgEntry.get()
    email = mainEntry.get()
    clean_up_event = r1_v.get()
    years = yerEntry.get()
    activity_location = actlocEntry.get()
    activity_type = cb1.get()
    environmental_type = cb2.get()
    sdg1 = var1.get()
    sdg2 = var2.get()
    sdg3 = var3.get()
    sdg4 = var4.get()
    sdg5 = var5.get()
    sdg6 = var6.get()
    sdg7 = var7.get()
    sdg8 = var8.get()

    cursor.execute('''INSERT INTO cleanupinfo (first_name, last_name, state, postal_code, phone_number, organization, email, clean_up_event, years, activity_location, activity_type, environmental_type, sdg1, sdg2, sdg3, sdg4, sdg5, sdg6, sdg7, sdg8)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                   (first_name, last_name, state, postal_code, phone_number, organization, email, clean_up_event, years, activity_location, activity_type, environmental_type, sdg1, sdg2, sdg3, sdg4, sdg5, sdg6, sdg7, sdg8))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    cho_window.destroy()
    import check

fnameLabel=Label(cho_window,text='FirstName:',font=('Helvetica', 10),bg='#9DC4E5',fg='black')
fnameLabel.place(x=300,y=130)
fnameEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='#FFFFFF')
fnameEntry.place(x=300,y=150,width=200)

lnameLabel=Label(cho_window,text='LastName:',font=('Helvetica', 10),bg='#9DC4E5',fg='black')
lnameLabel.place(x=550,y=130)
lnameEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='#FFFFFF')
lnameEntry.place(x=550,y=150,width=200)

stateLabel=Label(cho_window, text='State/Province:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
stateLabel.place(x=300,y=180)
stateEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='#FFFFFF')
stateEntry.place(x=300,y=200,width=200)

postLabel=Label(cho_window, text='Postal Code/ Zip Code:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
postLabel.place(x=550,y=180)
postalEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='#FFFFFF')
postalEntry.place(x=550,y=200,width=200)

phoLabel=Label(cho_window, text='Phone Number:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
phoLabel.place(x=300,y=230)
phoEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='#FFFFFF')
phoEntry.place(x=300,y=250,width=200)

orgLabel=Label(cho_window, text='Group/Organisation:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
orgLabel.place(x=550,y=230)
orgEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='#FFFFFF')
orgEntry.place(x=550,y=250,width=200)

mainLabel=Label(cho_window, text='Main Contact Email:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
mainLabel.place(x=300,y=280)
mainEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='#FFFFFF')
mainEntry.place(x=300,y=300,width=300)

qusLabel=Label(cho_window,text='Have you organised a Clean Up event before?',font=('Helvetica', 9),bg='#9DC4E5',fg='black')
qusLabel.place(x=300,y=340)

r1=tk.Radiobutton(cho_window,text='Yes',variable=r1_v,value='Yes',fg='black',bg='#9DC4E5')
r1.place(x=300,y=365)
r2=tk.Radiobutton(cho_window,text='No',variable=r1_v,value='No',fg='black',bg='#9DC4E5')
r2.place(x=360,y=365)

yerLabel=Label(cho_window, text='If yes, for how many years?',font=('Helvetica',10),fg='black',bg='#9DC4E5')
yerLabel.place(x=600,y=340)
yerEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='gray90')
yerEntry.place(x=600,y=365,width=100)

actlocLabel=Label(cho_window, text='Activity Location:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
actlocLabel.place(x=90,y=405)
actlocEntry=Entry(cho_window,width=30,font=('Helvetica',10),fg='black',bg='gray90')
actlocEntry.place(x=90,y=430,width=200)

acttyLabel=Label(cho_window, text='Activity Type:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
acttyLabel.place(x=350,y=405)
cho=['Rubbish Clean Up', 'Habitat Restoration', 'Tree Planting', 'Education', 'Awareness Raising', 'Other']
cb1=ttk.Combobox(cho_window,values=cho,width=25)
cb1.place(x=350,y=430)

enviLabel=Label(cho_window, text='Environmental Type:',font=('Helvetica',10),fg='black',bg='#9DC4E5')
enviLabel.place(x=580,y=405)
cho1=['Urbnan Built ', 'Park', 'Tree Planting', 'Forest/Reinforest', 'Waterway/River', 'Wetland/Mangrove', 'Other']
cb2=ttk.Combobox(cho_window,values=cho1,width=25)
cb2.place(x=580,y=430)


qus1Label=Label(cho_window,text='Which of the following UN Sustainable Development Goals (SDGs)* does this activity help achieve? (Select all that apply):',font=('Helvetica', 10),bg='#9DC4E5',fg='black')
qus1Label.place(x=50,y=475)


var1=StringVar()
che=Checkbutton(cho_window,text='SDG 4 - Quality Education',variable=var1,font=('Helvetica',9),bg='#9DC4E5')
che.deselect()
che.place(x=50,y=505)

var2=StringVar()
che1=Checkbutton(cho_window,text='SDG 11 - Sustainable Cities and Communities',variable=var2,font=('Helvetica',9),bg='#9DC4E5')
che1.deselect()
che1.place(x=50,y=535)

var3=StringVar()
che2=Checkbutton(cho_window,text='SDG 14 - Life Below Water',variable=var3,font=('Helvetica',9),bg='#9DC4E5')
che2.deselect()
che2.place(x=50,y=560)

var4=StringVar()
che3=Checkbutton(cho_window,text='SDG 6 - Clean Water and Sanitation',variable=var4,font=('Helvetica',9),bg='#9DC4E5')
che3.deselect()
che3.place(x=215,y=505)

var5=StringVar()
che4=Checkbutton(cho_window,text='SDG 12 - Responsible Consumption and Production',variable=var5,font=('Helvetica',9),bg='#9DC4E5')
che4.deselect()
che4.place(x=340,y=535)

var6=StringVar()
che5=Checkbutton(cho_window,text='SDG 15 - Life and Land',variable=var6,font=('Helvetica',9),bg='#9DC4E5')
che5.deselect()
che5.place(x=230,y=560)

var7=StringVar()
che5=Checkbutton(cho_window,text='SDG 7 - Affordable and Clean Energy',variable=var7,font=('Helvetica',9),bg='#9DC4E5')
che5.deselect()
che5.place(x=440,y=505)

var8=StringVar()
che6=Checkbutton(cho_window,text='SDG 13 - Climate Action',variable=var8,font=('Helvetica',9),bg='#9DC4E5')
che6.deselect()
che6.place(x=655,y=535)

submitButton=Button(cho_window,text='Submit',font=('Helvetica',12,'bold'),bd=0,bg='#1668D9',fg='white',activebackground='#159FEE',activeforeground='white',width=10,command=check_page)
submitButton.place(x=690,y=620)

cho_window.mainloop()
