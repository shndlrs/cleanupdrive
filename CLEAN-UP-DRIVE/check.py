from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
import pathlib
import pymysql
def signup_page():
    cho_window.destroy()
    import signup

def logout_page():
    cho_window.destroy()
    import signin
def ab_page():
    cho_window.destroy()
    import About
        
def populate_treeview():
    treeview.delete(*treeview.get_children())

    # Connect to the database
    conn = pymysql.connect(host='localhost', user='root', password='', database='cleanupdrive')
    cursor = conn.cursor()

    # Retrieve data from the cleanupinfo table
    cursor.execute("SELECT id, first_name, last_name, state, organization, email, clean_up_event FROM cleanupinfo")
    data = cursor.fetchall()

    # Populate the treeview with the retrieved data
    for entry in data:
        # Swap the ID value with the First Name value
        values = (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
        
        # Background change for each row
        if entry[0] % 2 == 0:
            treeview.insert('', 'end', values=values, tags=('evenrow',))
        else:
            treeview.insert('', 'end', values=values, tags=('oddrow',))

    # Close the cursor and connection
    cursor.close()
    conn.close()

def delete_selected():
    # Connect to the database
    conn = pymysql.connect(host='localhost', user='root', password='', database='cleanupdrive')
    cursor = conn.cursor()

    # Get the ID of the selected record from the treeview widget
    selected_id = treeview.item(treeview.selection())['values'][0]

    # Show a confirmation message box
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")

    if confirm:
        # Delete the selected record from the cleanupinfo table
        cursor.execute("DELETE FROM cleanupinfo WHERE id = %s", (selected_id,))
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully.")
    else:
        messagebox.showinfo("Cancelled", "Deletion cancelled.")

    populate_treeview()
    # Close the database connection
    cursor.close()
    conn.close()


def view_selected():
    # Connect to the database
    conn = pymysql.connect(host='localhost', user='root', password='', database='cleanupdrive')
    cursor = conn.cursor()

    # Retrieve all records from the cleanupinfo table
    cursor.execute("SELECT * FROM cleanupinfo WHERE id = %s", (treeview.item(treeview.selection())['values'][0]))
    records = cursor.fetchall()

    # Create a new window to display the records
    selected_window = Toplevel(cho_window)
    selected_window.title("Selected Records")

    id_label = Label(selected_window, text="ID Number:", font=('Helvetica', 11, 'bold'))
    id_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    
    id_value = Label(selected_window, text=records[0][0], font=('Helvetica', 11))
    id_value.grid(row=0, column=1, padx=10, pady=10, sticky=W)
    
    first_name_label = Label(selected_window, text="First Name:", font=('Helvetica', 11, 'bold'))
    first_name_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)
    
    first_name_value = Label(selected_window, text=records[0][1], font=('Helvetica', 11))
    first_name_value.grid(row=0, column=3, padx=10, pady=10, sticky=W)
    
    last_name_label = Label(selected_window, text="Last Name:", font=('Helvetica', 11, 'bold'))
    last_name_label.grid(row=0, column=4, padx=10, pady=10, sticky=W)
    
    last_name_value = Label(selected_window, text=records[0][2], font=('Helvetica', 11))
    last_name_value.grid(row=0, column=5, padx=10, pady=10, sticky=W)
    
    state_label = Label(selected_window, text="State:", font=('Helvetica', 11, 'bold'))
    state_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    
    state_value = Label(selected_window, text=records[0][3], font=('Helvetica', 11))
    state_value.grid(row=1, column=1, padx=10, pady=10, sticky=W)
    
    postal_code_label = Label(selected_window, text="Postal Code:", font=('Helvetica', 11, 'bold'))
    postal_code_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)
    
    postal_code_value = Label(selected_window, text=records[0][4], font=('Helvetica', 11))
    postal_code_value.grid(row=1, column=3, padx=10, pady=10, sticky=W)
    
    phone_number_label = Label(selected_window, text="Phone Number:", font=('Helvetica', 11, 'bold'))
    phone_number_label.grid(row=1, column=4, padx=10, pady=10, sticky=W)
    
    phone_number_value = Label(selected_window, text=records[0][5], font=('Helvetica', 11))
    phone_number_value.grid(row=1, column=5, padx=10, pady=10, sticky=W)
    
    organization_label = Label(selected_window, text="Organization:", font=('Helvetica', 11, 'bold'))
    organization_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    
    organization_value = Label(selected_window, text=records[0][6], font=('Helvetica', 11))
    organization_value.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    
    email_label = Label(selected_window, text="Email:", font=('Helvetica', 11, 'bold'))
    email_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
    
    email_value = Label(selected_window, text=records[0][7], font=('Helvetica', 11))
    email_value.grid(row=2, column=3, padx=10, pady=10, sticky=W, columnspan=2)
    
    cleanupevent_label = Label(selected_window, text="Clean Up Event:", font=('Helvetica', 11, 'bold'))
    cleanupevent_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    
    cleanupevent_value = Label(selected_window, text=records[0][8], font=('Helvetica', 11))
    cleanupevent_value.grid(row=3, column=1, padx=10, pady=10, sticky=W)
    
    years_label = Label(selected_window, text="Years:", font=('Helvetica', 11, 'bold'))
    years_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)
    
    years_value = Label(selected_window, text=records[0][9], font=('Helvetica', 11))
    
    years_value.grid(row=3, column=3, padx=10, pady=10, sticky=W)
    
    activity_location_label = Label(selected_window, text="Activity Location:", font=('Helvetica', 11, 'bold'))
    
    activity_location_label.grid(row=3, column=4, padx=10, pady=10, sticky=W)
    
    activity_location_value = Label(selected_window, text=records[0][10], font=('Helvetica', 11))
    
    activity_location_value.grid(row=3, column=5, padx=10, pady=10, sticky=W)
    
    activity_type_label = Label(selected_window, text="Activity Type:", font=('Helvetica', 11, 'bold'))
    activity_type_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    
    activity_type_value = Label(selected_window, text=records[0][11], font=('Helvetica', 11))
    activity_type_value.grid(row=4, column=1, padx=10, pady=10, sticky=W)
    
    environmental_type_label = Label(selected_window, text="Environmental Type:", font=('Helvetica', 11, 'bold'))
    environmental_type_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)
    
    environmental_type_value = Label(selected_window, text=records[0][12], font=('Helvetica', 11))
    environmental_type_value.grid(row=4, column=3, padx=10, pady=10, sticky=W)
    
    sdg_label = Label(selected_window, text="SDG:", font=('Helvetica', 11, 'bold'))
    sdg_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    
    # Define the SDG values and corresponding column indices
    sdg_values = {
        4: records[0][13],
        11: records[0][14],
        14: records[0][15],
        6: records[0][16],
        12: records[0][17],
        15: records[0][18],
        7: records[0][19],
        13: records[0][20]
    }

    # Define the SDG titles
    sdg_titles = {
        4: "Quality Education",
        11: "Sustainable Cities and Communities",
        14: "Life Below Water",
        6: "Clean Water and Sanitation",
        12: "Responsible Consumption and Production",
        15: "Life and Land",
        7: "Affordable and Clean Energy",
        13: "Climate Action"
    }

    row_counter = 5  

    for sdg, value in sdg_values.items():
        if value == '1':
            sdg_label = Label(selected_window, text="SDG {}: ".format(sdg) + sdg_titles[sdg], font=('Helvetica', 11))
            sdg_label.grid(row=row_counter, column=1, padx=10, pady=10, sticky=W)
            row_counter += 1

            
        
        
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

def search_records(search_phrase):
    
    treeview.delete(*treeview.get_children())
    
    # Connect to the database
    conn = pymysql.connect(host='localhost', user='root', password='', database='cleanupdrive')
    cursor = conn.cursor()

    # Construct the SQL query with the search phrase
    query = "SELECT id, first_name, last_name, state, organization, email, clean_up_event FROM cleanupinfo WHERE " \
        "id LIKE %s OR " \
        "LOWER(first_name) LIKE %s OR " \
        "LOWER(last_name) LIKE %s OR " \
        "LOWER(state) LIKE %s OR " \
        "LOWER(organization) LIKE %s OR " \
        "LOWER(email) LIKE %s OR " \
        "LOWER(clean_up_event) LIKE %s"

    # Add wildcard characters to perform partial matching
    search_value = f"%{search_phrase.lower()}%"

    # Execute the query with the search values
    cursor.execute(query, (search_value, search_value, search_value, search_value, search_value, search_value, search_value))
    data = cursor.fetchall()

    # Populate the treeview with the retrieved data
    for entry in data:
        # Swap the ID value with the First Name value
        values = (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
        
        # Background change for each row
        if entry[0] % 2 == 0:
            treeview.insert('', 'end', values=values, tags=('evenrow',))
        else:
            treeview.insert('', 'end', values=values, tags=('oddrow',))
            
    cursor.close()
    conn.close()

def reset_search():
    search_entry.delete(0, END)
    populate_treeview()
    


cho_window=tk.Tk()
r1_v=tk.StringVar()
r1_v.set(None)
cho_window.title('Clean Up Information')
cho_window.iconbitmap(r'C:/Users/Justmyr Gutierrez\Downloads/IT222-CleanUp-Drive-Registration-IS-main/clean_up_drive/ocean.ico')
cho_window.geometry('1100x620')
cho_window.config(bg='#9DC4E5')

returnButton=Button(cho_window,text='Return',font=('Helvetica', 12, 'bold'), bg='#9DC4E5', fg='#FFFFFF',activeforeground='#8EE5EE',activebackground='#F0F8FF', cursor='hand2', bd=0,command=signup_page)
returnButton.place(x=890,y=20)

logoutButton=Button(cho_window,text='Logout',font=('Helvetica',12, 'bold'),bg='#9DC4E5',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=logout_page)
logoutButton.place(x=980,y=20)

abButton=Button(cho_window,text='About',font=('Helvetica',12, 'bold'),bg='#9DC4E5',fg='#FFFFFF',bd=0, cursor='hand2', activebackground='#F0F8FF',activeforeground='#8EE5EE',command=ab_page)
abButton.place(x=800,y=20)

cleanup_frame = LabelFrame(cho_window, text="Clean Up Information", font=('Helvetica', 12, 'bold'), bg='#9DC4E5', fg='#FFFFFF', padx=10, pady=10)
cleanup_frame.place(x=50, y=50, width=1000, height=500)

menu_frame = Frame(cleanup_frame, bg='#9DC4E5')
menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W)

search_label = Label(menu_frame, text="Search by:", font=('Helvetica', 12, 'bold'), bg='#9DC4E5', fg='#FFFFFF')
search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

search_entry = Entry(menu_frame, font=('Helvetica', 12), width=20)
search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

search_button = Button(menu_frame, text="Search", font=('Helvetica', 12, 'bold'), bg='#4b89bd', fg='#FFFFFF', bd=0, cursor='hand2', width=10, command=lambda: search_records(search_entry.get()))
search_button.grid(row=0, column=2, padx=10, pady=10, sticky=W)

reset_button = Button(menu_frame, text="Reset", font=('Helvetica', 12, 'bold'), bg='#4b89bd', fg='#FFFFFF', bd=0, cursor='hand2', width=10, command=reset_search)
reset_button.grid(row=0, column=3, padx=10, pady=10, sticky=W)  


view_button = Button(menu_frame, text="View", font=('Helvetica', 12, 'bold'), bg='#4b89bd', fg='#FFFFFF', bd=0, cursor='hand2', width=10, command=view_selected)
view_button.grid(row=0, column=4, padx=10, pady=10, sticky=W)

edit_button = Button(menu_frame, text="Edit", font=('Helvetica', 12, 'bold'), bg='#4b89bd', fg='#FFFFFF', bd=0, cursor='hand2', width=10)
edit_button.grid(row=0, column=5, padx=10, pady=10, sticky=W)

delete_button = Button(menu_frame, text="Delete", font=('Helvetica', 12, 'bold'), bg='#4b89bd', fg='#FFFFFF', bd=0, cursor='hand2', width=10, command=delete_selected)
delete_button.grid(row=0, column=6, padx=10, pady=10, sticky=W)

treeview = ttk.Treeview(cleanup_frame, columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6"), show="headings", height=18)

treeview.tag_configure('oddrow', background="white")
treeview.tag_configure('evenrow', background="lightblue")

treeview.heading("#1", text="ID")
treeview.heading("#2", text="First Name")
treeview.heading("#3", text="Last Name")
treeview.heading("#4", text="State")
treeview.heading("#5", text="Organization")
treeview.heading("#6", text="Email")
treeview.heading("#7", text="Clean Up Event")

treeview.column("#1", width=50, anchor=CENTER)
treeview.column("#2", width=50, anchor=CENTER)
treeview.column("#3", width=50, anchor=CENTER)
treeview.column("#4", width=50, anchor=CENTER)
treeview.column("#5", width=50, anchor=CENTER)
treeview.column("#6", width=120, anchor=CENTER)
treeview.column("#7", width=50, anchor=CENTER)




# Add a scrollbar
scrollbar = ttk.Scrollbar(cleanup_frame, orient="vertical", command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)

# Grid layout
treeview.grid(row=1, column=0, sticky="nsew")
scrollbar.grid(row=1, column=1, sticky="ns")

# Call function to populate the treeview
populate_treeview()

cho_window.mainloop()
