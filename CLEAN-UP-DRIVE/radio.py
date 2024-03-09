import tkinter as tk
my_w=tk.Tk()
my_w.geometry("300x150")
r1_v=tk.StringVar()
r1_v.set(None)

r1=tk.Radiobutton(my_w,text='Passed',variable=r1_v,value='Passed')
r1.grid(row=1,column=1, padx=30, pady=30)

my_w.mainloop()