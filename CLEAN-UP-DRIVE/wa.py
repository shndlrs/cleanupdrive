from tkinter import *
import tkinter as tk

def info_page():
    window.destroy()
    import check


window = tk.Tk()
window.geometry("900x600")
window.config(bg='white')

bech_logo=PhotoImage(file='C:/Users/Justmyr Gutierrez\Downloads/IT222-CleanUp-Drive-Registration-IS-main/clean_up_drive/env.png')
bechLabel=Label(window,image=bech_logo,bg='white')
bechLabel.place(x=10,y=20)

nameLabel=Label(window,text='FullName',font=('Microsoft Yahei IU Light', 10, 'bold'),bg='white',fg='black')
nameLabel.place(x=50,y=350)

nameEntry=Entry(window,width=30,font=('Microsoft Yahei IU Light',10),fg='black',bg='azure3')
nameEntry.place(x=50,y=400,width=230)

submitButton=Button(window, text='Submit', font=('Times New Roman', 14, 'bold'),width=16,fg='white',bg='azure4',activeforeground='white',activebackground='black', cursor='hand2',bd=0,command=info_page)
submitButton.place(x=300,y=800)

SVBar = tk.Scrollbar(window)
SVBar.pack (side = tk.RIGHT,
			fill = "y")

window.mainloop()

conLabel=Label(cho_window,text='Contact',font=('Georgia', 10),bg='gray90',fg='black')
conLabel.place(x=50,y=100)

conEntry=Entry(cho_window,width=30,font=('Georgia',10),fg='black',bg='gray90')
conEntry.place(x=50,y=130,width=230)

locLabel=Label(cho_window,text='Address',font=('Georgia', 10),bg='gray90',fg='black')
locLabel.place(x=50,y=155)

locsLabel=Label(cho_window,text='Province',font=('Georgia', 8),bg='gray90',fg='black')
locsLabel.place(x=50,y=175)
locEntry=Entry(cho_window,width=30,font=('Georgia',10),fg='black',bg='gray90')
locEntry.place(x=50,y=195,width=80)

locs1Label=Label(cho_window,text='Municipality',font=('Georgia', 8),bg='gray90',fg='black')
locs1Label.place(x=150,y=175)
loc1Entry=Entry(cho_window,width=30,font=('Georgia',10),fg='black',bg='gray90')
loc1Entry.place(x=150,y=195,width=80)

locs2Label=Label(cho_window,text='Barangay',font=('Georgia', 8),bg='gray90',fg='black')
locs2Label.place(x=250,y=175)
loc2Entry=Entry(cho_window,width=30,font=('Georgia',10),fg='black',bg='gray90')
loc2Entry.place(x=250,y=195,width=80)

datetimeLabel=Label(cho_window,text='Date/Time',font=('Georgia', 10),bg='gray90',fg='black')
datetimeLabel.place(x=50,y=225)

dateLabel=Label(cho_window,text='Date',font=('Georgia', 8),bg='gray90',fg='black')
dateLabel.place(x=50,y=245)
dateEntry=Entry(cho_window,width=30,font=('Georgia',10),fg='black',bg='gray90')
dateEntry.place(x=50,y=265,width=80)


timeLabel=Label(cho_window,text='Time',font=('Georgia', 8),bg='gray90',fg='black')
timeLabel.place(x=150,y=245)
timeEntry=Entry(cho_window,width=30,font=('Georgia',10),fg='black',bg='gray90')
timeEntry.place(x=150,y=265,width=80)
