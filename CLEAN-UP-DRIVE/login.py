from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import pymysql
from tkinter import messagebox


def info_page():
    
    #function for view information table
    
    def view_records():
        cho_window.withdraw()

        #function for fethcing all records
        
        def populate_treeview():
            treeview.delete(*treeview.get_children())

            # Connect to the database
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="cleanupdrive"
            )
            cursor = conn.cursor()

            # Retrieve data from the cleanupinfo table
            cursor.execute(
                "SELECT id, first_name, last_name, state, organization, email, clean_up_event FROM cleanupinfo"
            )
            data = cursor.fetchall()

            # Populate the treeview with the retrieved data
            for entry in data:
                # Swap the ID value with the First Name value
                values = (
                    entry[0],
                    entry[1],
                    entry[2],
                    entry[3],
                    entry[4],
                    entry[5],
                    entry[6],
                )

                # Background change for each row
                if entry[0] % 2 == 0:
                    treeview.insert("", "end", values=values, tags=("evenrow",))
                else:
                    treeview.insert("", "end", values=values, tags=("oddrow",))

            # Close the cursor and connection
            cursor.close()
            conn.close()

        #function for delete button
        def delete_selected():
            # Connect to the database
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="cleanupdrive"
            )
            cursor = conn.cursor()

            # Get the ID of the selected record from the treeview widget
            selected_id = treeview.item(treeview.selection()[0])["values"][0]

            # Show a confirmation message box
            confirm = messagebox.askyesno(
                "Confirmation", "Are you sure you want to delete this record?"
            )

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


        #function for view button
        def view_selected():
            # Connect to the database
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="cleanupdrive"
            )
            cursor = conn.cursor()

            # Retrieve all records from the cleanupinfo table
            cursor.execute(
                "SELECT * FROM cleanupinfo WHERE id = %s",
                (treeview.item(treeview.selection()[0])["values"][0]),
            )

            records = cursor.fetchall()

            # Create a new window to display the records
            selected_window = Toplevel(check_window, background="#9DC4E5")
            selected_window.title("Selected Records")

            information_frame = LabelFrame(
                selected_window,
                text="Information",
                font=("Helvetica", 12, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
                padx=10,
                pady=10,
            )
            information_frame.grid(row=0, column=0, padx=50, pady=20, sticky=W)

            id_label = Label(
                information_frame,
                text="ID Number:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            id_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)

            id_value = Label(
                information_frame,
                text=records[0][0],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            id_value.grid(row=0, column=1, padx=5, pady=10, sticky=W)

            first_name_label = Label(
                information_frame,
                text="First Name:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            first_name_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)

            first_name_value = Label(
                information_frame,
                text=records[0][1],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            first_name_value.grid(row=0, column=3, padx=5, pady=10, sticky=W)

            last_name_label = Label(
                information_frame,
                text="Last Name:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            last_name_label.grid(row=0, column=4, padx=5, pady=10, sticky=W)

            last_name_value = Label(
                information_frame,
                text=records[0][2],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            last_name_value.grid(row=0, column=5, padx=5, pady=10, sticky=W)

            state_label = Label(
                information_frame,
                text="State:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            state_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)

            state_value = Label(
                information_frame,
                text=records[0][3],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            state_value.grid(row=1, column=1, padx=5, pady=10, sticky=W)

            postal_code_label = Label(
                information_frame,
                text="Postal Code:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            postal_code_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)

            postal_code_value = Label(
                information_frame,
                text=records[0][4],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            postal_code_value.grid(row=1, column=3, padx=5, pady=10, sticky=W)

            phone_number_label = Label(
                information_frame,
                text="Phone Number:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            phone_number_label.grid(row=1, column=4, padx=5, pady=10, sticky=W)

            phone_number_value = Label(
                information_frame,
                text=records[0][5],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            phone_number_value.grid(row=1, column=5, padx=5, pady=10, sticky=W)

            organization_label = Label(
                information_frame,
                text="Organization:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            organization_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)

            organization_value = Label(
                information_frame,
                text=records[0][6],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            organization_value.grid(row=2, column=1, padx=5, pady=10, sticky=W)

            email_label = Label(
                information_frame,
                text="Email:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            email_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)

            email_value = Label(
                information_frame,
                text=records[0][7],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            email_value.grid(row=2, column=3, padx=5, pady=10, sticky=W, columnspan=2)

            cleanupevent_label = Label(
                information_frame,
                text="Clean Up Event:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            cleanupevent_label.grid(row=3, column=0, padx=5, pady=10, sticky=W)

            cleanupevent_value = Label(
                information_frame,
                text=records[0][8],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            cleanupevent_value.grid(row=3, column=1, padx=5, pady=10, sticky=W)

            years_label = Label(
                information_frame,
                text="Years:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            years_label.grid(row=3, column=2, padx=5, pady=10, sticky=W)

            years_value = Label(
                information_frame,
                text=records[0][9],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )

            years_value.grid(row=3, column=3, padx=5, pady=10, sticky=W)

            activity_location_label = Label(
                information_frame,
                text="Activity Location:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )

            activity_location_label.grid(row=3, column=4, padx=5, pady=10, sticky=W)

            activity_location_value = Label(
                information_frame,
                text=records[0][10],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )

            activity_location_value.grid(row=3, column=5, padx=5, pady=10, sticky=W)

            activity_type_label = Label(
                information_frame,
                text="Activity Type:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            activity_type_label.grid(row=4, column=0, padx=5, pady=10, sticky=W)

            activity_type_value = Label(
                information_frame,
                text=records[0][11],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            activity_type_value.grid(row=4, column=1, padx=5, pady=10, sticky=W)

            environmental_type_label = Label(
                information_frame,
                text="Environmental Type:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            environmental_type_label.grid(row=4, column=2, padx=5, pady=10, sticky=W)

            environmental_type_value = Label(
                information_frame,
                text=records[0][12],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            environmental_type_value.grid(row=4, column=3, padx=5, pady=10, sticky=W)

            sdg_label = Label(
                information_frame,
                text="SDG:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
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
                13: records[0][20],
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
                13: "Climate Action",
            }

            row_counter = 5

            for sdg, value in sdg_values.items():
                if value == "1":
                    sdg_label = Label(
                        information_frame,
                        text="SDG {}: ".format(sdg) + sdg_titles[sdg],
                        font=("Helvetica", 11),
                        background="#9DC4E5",
                        fg="#FFFFFF",
                    )
                    sdg_label.grid(
                        row=row_counter, column=1, padx=10, pady=10, sticky=W
                    )
                    row_counter += 1
            
            
            cursor.close()
            conn.close()

        #function for update window
        def update_selected():

            #function for submit button in update window
            def submit_update():
                # Connect to the database
                conn = pymysql.connect(
                    host="localhost", user="root", password="", database="cleanupdrive"
                )
                cursor = conn.cursor()

                # Update the record in the database
                cursor.execute(
    "UPDATE cleanupinfo SET first_name = %s, last_name = %s, state = %s, postal_code = %s, phone_number = %s, organization = %s, email = %s, clean_up_event = %s, years = %s, activity_location = %s, activity_type = %s, environmental_type = %s WHERE id = %s",
                    (
                        fname.get(),
                        lname.get(),
                        state.get(),
                        postal_code.get(),
                        phone_number.get(),
                        organization.get(),
                        email.get(),
                        clean_up_event.get(),   
                        years.get(),
                        activity_location.get(),
                        activity_type.get(),
                        environmental_type.get(),
                        treeview.item(treeview.selection()[0])["values"][0],
                    ),
                )

                # Commit the changes to the database
                conn.commit()

                # Close the cursor and connection
                cursor.close()
                conn.close()

                # Destroy the update window
                update_selected_window.destroy()

                # Refresh the treeview
                populate_treeview()

            # Connect to the database
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="cleanupdrive"
            )
            cursor = conn.cursor()

            # Retrieve all records from the cleanupinfo table
            cursor.execute(
                "SELECT * FROM cleanupinfo WHERE id = %s",
                (treeview.item(treeview.selection()[0])["values"][0]),
            )

            records = cursor.fetchall()

            fname = StringVar()
            lname = StringVar()
            state = StringVar()
            postal_code = StringVar()
            phone_number = StringVar()
            organization = StringVar()
            email = StringVar()
            clean_up_event = StringVar()
            years = StringVar()
            activity_location = StringVar()
            activity_type = StringVar()
            environmental_type = StringVar()

            # Create a new window to display the records
            update_selected_window = Toplevel(check_window, background="#9DC4E5")
            update_selected_window.title("Selected Records")

            information_frame = LabelFrame(
                update_selected_window,
                text="Information",
                font=("Helvetica", 12, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
                padx=10,
                pady=10,
            )
            information_frame.grid(row=0, column=0, padx=50, pady=20, sticky=W)

            id_label = Label(
                information_frame,
                text="ID Number:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            id_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)

            id_value = Label(
                information_frame,
                text=records[0][0],
                font=("Helvetica", 11),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            id_value.grid(row=0, column=1, padx=5, pady=10, sticky=W)

            first_name_label = Label(
                information_frame,
                text="First Name:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            first_name_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)

            first_name_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=fname,
            )
            first_name_value.insert(0, records[0][1])  # Set the default value
            first_name_value.grid(row=0, column=3, padx=5, pady=10, sticky="w")

            last_name_label = Label(
                information_frame,
                text="Last Name:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            last_name_label.grid(row=0, column=4, padx=5, pady=10, sticky=W)

            last_name_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=lname,
            )
            last_name_value.insert(0, records[0][2])  # Set the default value
            last_name_value.grid(row=0, column=5, padx=5, pady=10, sticky="w")

            state_label = Label(
                information_frame,
                text="State:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            state_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)

            state_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=state,
            )
            state_value.insert(0, records[0][3])  # Set the default value
            state_value.grid(row=1, column=1, padx=5, pady=10, sticky=W)

            postal_code_label = Label(
                information_frame,
                text="Postal Code:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            postal_code_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)

            postal_code_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=postal_code,
            )
            postal_code_value.insert(0, records[0][4])  # Set the default value
            postal_code_value.grid(row=1, column=3, padx=5, pady=10, sticky=W)

            phone_number_label = Label(
                information_frame,
                text="Phone Number:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            phone_number_label.grid(row=1, column=4, padx=5, pady=10, sticky=W)

            phone_number_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=phone_number,
            )
            phone_number_value.insert(0, records[0][5])  # Set the default value
            phone_number_value.grid(row=1, column=5, padx=5, pady=10, sticky=W)

            organization_label = Label(
                information_frame,
                text="Organization:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            organization_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)

            organization_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=organization,
            )
            organization_value.insert(0, records[0][6])  # Set the default value
            organization_value.grid(row=2, column=1, padx=5, pady=10, sticky=W)

            email_label = Label(
                information_frame,
                text="Email:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            email_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)

            email_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=email,
            )
            email_value.insert(0, records[0][7])  # Set the default value
            email_value.grid(row=2, column=3, padx=5, pady=10, sticky=W, columnspan=2)

            cleanupevent_label = Label(
                information_frame,
                text="Clean Up Event:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            cleanupevent_label.grid(row=3, column=0, padx=5, pady=10, sticky=W)

            cleanupevent_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=clean_up_event,
            )
            cleanupevent_value.insert(0, records[0][8])  # Set the default value
            cleanupevent_value.grid(row=3, column=1, padx=5, pady=10, sticky=W)

            years_label = Label(
                information_frame,
                text="Years:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            years_label.grid(row=3, column=2, padx=5, pady=10, sticky=W)

            years_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=years,
            )
            years_value.insert(0, records[0][9])  # Set the default value
            years_value.grid(row=3, column=3, padx=5, pady=10, sticky=W)

            activity_location_label = Label(
                information_frame,
                text="Activity Location:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            activity_location_label.grid(row=3, column=4, padx=5, pady=10, sticky=W)

            activity_location_value = Entry(
                information_frame,
                font=("Helvetica", 11),
                bg="white",
                textvariable=activity_location,
            )
            activity_location_value.insert(0, records[0][10])  # Set the default value
            activity_location_value.grid(row=3, column=5, padx=5, pady=10, sticky=W)

            activity_type_label = Label(
                information_frame,
                text="Activity Type:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            activity_type_label.grid(row=4, column=0, padx=5, pady=10, sticky=W)

            activity_choices = [
                "Rubbish Clean Up",
                "Habitat Restoration",
                "Tree Planting",
                "Education",
                "Awareness Raising",
                "Other",
            ]

            activity_type_value = ttk.Combobox(
                information_frame,
                values=activity_choices,
                font=("Helvetica", 11),
                width=25,
                textvariable=activity_type,
            )
            activity_type_value.current(
                activity_choices.index(records[0][11])
            )  # Set the default value
            activity_type_value.grid(row=4, column=1, padx=5, pady=10, sticky=W)

            environmental_type_label = Label(
                information_frame,
                text="Environmental Type:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            environmental_type_label.grid(row=4, column=2, padx=5, pady=10, sticky=W)

            environmental_choices = [
                "Urban Built",
                "Park",
                "Tree Planting",
                "Forest/Reinforest",
                "Waterway/River",
                "Wetland/Mangrove",
                "Other",
            ]
            environmental_type_value = ttk.Combobox(
                information_frame,
                values=environmental_choices,
                font=("Helvetica", 11),
                width=25,
                textvariable=environmental_type,
            )
            environmental_type_value.current(
                environmental_choices.index(records[0][12])
            )  
            environmental_type_value.grid(row=4, column=3, padx=5, pady=10, sticky=W)
            
            updateSubmit = Button(
                information_frame,
                text="Update",
                font=("Helvetica", 11),
                width=10,
                command=submit_update,
            )
            updateSubmit.grid(row=4, column=4, padx=5, pady=10, sticky=W)
            
            
            sdg_label = Label(
                information_frame,
                text="SDG:",
                font=("Helvetica", 11, "bold"),
                background="#9DC4E5",
                fg="#FFFFFF",
            )
            sdg_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
            
            
            sdg_values = {
                4: records[0][13],
                11: records[0][14],
                14: records[0][15],
                6: records[0][16],
                12: records[0][17],
                15: records[0][18],
                7: records[0][19],
                13: records[0][20],
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
                13: "Climate Action",
            }


            cursor.close()
            conn.close()
            
            
            update_selected_window.mainloop()

        #function for search
        
        def search_records(search_phrase):

            treeview.delete(*treeview.get_children())

            # Connect to the database
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="cleanupdrive"
            )
            cursor = conn.cursor()

            # Construct the SQL query with the search phrase
            query = (
                "SELECT id, first_name, last_name, state, organization, email, clean_up_event FROM cleanupinfo WHERE "
                "id LIKE %s OR "
                "LOWER(first_name) LIKE %s OR "
                "LOWER(last_name) LIKE %s OR "
                "LOWER(state) LIKE %s OR "
                "LOWER(organization) LIKE %s OR "
                "LOWER(email) LIKE %s OR "
                "LOWER(clean_up_event) LIKE %s"
            )

            # Add wildcard characters to perform partial matching
            search_value = f"%{search_phrase.lower()}%"

            # Execute the query with the search values
            cursor.execute(
                query,
                (
                    search_value,
                    search_value,
                    search_value,
                    search_value,
                    search_value,
                    search_value,
                    search_value,
                ),
            )
            data = cursor.fetchall()

            # Populate the treeview with the retrieved data
            for entry in data:
                # Swap the ID value with the First Name value
                values = (
                    entry[0],
                    entry[1],
                    entry[2],
                    entry[3],
                    entry[4],
                    entry[5],
                    entry[6],
                )

                # Background change for each row
                if entry[0] % 2 == 0:
                    treeview.insert("", "end", values=values, tags=("evenrow",))
                else:
                    treeview.insert("", "end", values=values, tags=("oddrow",))

            cursor.close()
            conn.close()

        #Function Reset Searhch
        def reset_search():
            search_entry.delete(0, END)
            populate_treeview()

        #Function for returning
        def return_page():
            check_window.destroy()
            cho_window.deiconify()

        check_window = Toplevel(cho_window)
        r1_v = tk.StringVar()
        r1_v.set("")
        check_window.title("Clean Up Information")
        check_window.iconbitmap(
            r"pics/ocean.ico"
        )
        check_window.geometry("1100x620")
        check_window.config(bg="#9DC4E5")

        returnButton = Button(
            check_window,
            text="Return",
            font=("Helvetica", 12, "bold"),
            bg="#9DC4E5",
            fg="#FFFFFF",
            activeforeground="#8EE5EE",
            activebackground="#F0F8FF",
            cursor="hand2",
            bd=0,
            command=return_page,
        )
        returnButton.place(x=980, y=20)
        cleanup_frame = LabelFrame(
            check_window,
            text="Clean Up Information",
            font=("Helvetica", 12, "bold"),
            bg="#9DC4E5",
            fg="#FFFFFF",
            padx=10,
            pady=10,
        )
        cleanup_frame.place(x=50, y=50, width=1000, height=500)

        menu_frame = Frame(cleanup_frame, bg="#9DC4E5")
        menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_label = Label(
            menu_frame,
            text="Search by:",
            font=("Helvetica", 12, "bold"),
            bg="#9DC4E5",
            fg="#FFFFFF",
        )
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_entry = Entry(menu_frame, font=("Helvetica", 12), width=20)
        search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        search_button = Button(
            menu_frame,
            text="Search",
            font=("Helvetica", 12, "bold"),
            bg="#4b89bd",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            width=10,
            command=lambda: search_records(search_entry.get()),
        )
        search_button.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        reset_button = Button(
            menu_frame,
            text="Reset",
            font=("Helvetica", 12, "bold"),
            bg="#4b89bd",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            width=10,
            command=reset_search,
        )
        reset_button.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        view_button = Button(
            menu_frame,
            text="View",
            font=("Helvetica", 12, "bold"),
            bg="#4b89bd",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            width=10,
            command=view_selected,
        )
        view_button.grid(row=0, column=4, padx=10, pady=10, sticky=W)

        edit_button = Button(
            menu_frame,
            text="Edit",
            font=("Helvetica", 12, "bold"),
            bg="#4b89bd",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            width=10,
            command=update_selected,
        )
        edit_button.grid(row=0, column=5, padx=10, pady=10, sticky=W)

        delete_button = Button(
            menu_frame,
            text="Delete",
            font=("Helvetica", 12, "bold"),
            bg="#4b89bd",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            width=10,
            command=delete_selected,
        )
        delete_button.grid(row=0, column=6, padx=10, pady=10, sticky=W)

        treeview = ttk.Treeview(
            cleanup_frame,
            columns=("#0", "#1", "#2", "#3", "#4", "#5", "#6"),
            show="headings",
            height=18,
        )

        treeview.tag_configure("oddrow", background="white")
        treeview.tag_configure("evenrow", background="lightblue")

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
        scrollbar = ttk.Scrollbar(
            cleanup_frame, orient="vertical", command=treeview.yview
        )
        scrollbar.configure(command=treeview.yview)

        # Grid layout
        treeview.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        # Call function to populate the treeview
        populate_treeview()

        check_window.mainloop()

    def logout_user():
        login_window.destroy()
        import main

    login_window.withdraw()
    
    #Information Page

    cho_window = Toplevel(login_window)
    r1_v = StringVar()
    r1_v.set("")
    cho_window.title("Clean Up Information")
    cho_window.iconbitmap(
        r"pics/ocean.ico"
    )
    cho_window.geometry("850x720")
    cho_window.config(bg="gray90")

    background = ImageTk.PhotoImage(
        file="pics/infopage.png"
    )

    bgLabel = Label(cho_window, image=background)
    bgLabel.grid(row=0, column=0)

    viewRecordsButton = Button(
        cho_window,
        text="View Records",
        font=("Helvetica", 12, "bold"),
        bg="#9DC4E5",
        fg="#FFFFFF",
        activeforeground="#8EE5EE",
        activebackground="#F0F8FF",
        cursor="hand2",
        bd=0,
        command=view_records,
    )
    viewRecordsButton.place(x=600, y=20)

    logoutButton = Button(
        cho_window,
        text="Logout",
        font=("Helvetica", 12, "bold"),
        bg="#9DC4E5",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        activebackground="#F0F8FF",
        activeforeground="#8EE5EE",
        command=logout_user,
    )
    logoutButton.place(x=745, y=20)

    def check_page():
        # Connect to the database
        conn = pymysql.connect(
            host="localhost", user="root", password="", database="cleanupdrive"
        )
        cursor = conn.cursor()

        # Check if the table already exists
        cursor.execute("SHOW TABLES LIKE 'cleanupinfo'")
        table_exists = cursor.fetchone()

        if table_exists is None:
            # Create the table if it doesn't exist
            cursor.execute(
                """CREATE TABLE cleanupinfo (
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
                                )"""
            )

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

        cursor.execute(
            """INSERT INTO cleanupinfo (first_name, last_name, state, postal_code, phone_number, organization, email, clean_up_event, years, activity_location, activity_type, environmental_type, sdg1, sdg2, sdg3, sdg4, sdg5, sdg6, sdg7, sdg8)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                first_name,
                last_name,
                state,
                postal_code,
                phone_number,
                organization,
                email,
                clean_up_event,
                years,
                activity_location,
                activity_type,
                environmental_type,
                sdg1,
                sdg2,
                sdg3,
                sdg4,
                sdg5,
                sdg6,
                sdg7,
                sdg8,
            ),
        )

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        view_records()

    fnameLabel = Label(
        cho_window, text="FirstName:", font=("Helvetica", 10), bg="#9DC4E5", fg="black"
    )
    fnameLabel.place(x=300, y=130)
    fnameEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="#FFFFFF"
    )
    fnameEntry.place(x=300, y=150, width=200)

    lnameLabel = Label(
        cho_window, text="LastName:", font=("Helvetica", 10), bg="#9DC4E5", fg="black"
    )
    lnameLabel.place(x=550, y=130)
    lnameEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="#FFFFFF"
    )
    lnameEntry.place(x=550, y=150, width=200)

    stateLabel = Label(
        cho_window,
        text="State/Province:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    stateLabel.place(x=300, y=180)
    stateEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="#FFFFFF"
    )
    stateEntry.place(x=300, y=200, width=200)

    postLabel = Label(
        cho_window,
        text="Postal Code/ Zip Code:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    postLabel.place(x=550, y=180)
    postalEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="#FFFFFF"
    )
    postalEntry.place(x=550, y=200, width=200)

    phoLabel = Label(
        cho_window,
        text="Phone Number:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    phoLabel.place(x=300, y=230)
    phoEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="#FFFFFF"
    )
    phoEntry.place(x=300, y=250, width=200)

    orgLabel = Label(
        cho_window,
        text="Group/Organisation:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    orgLabel.place(x=550, y=230)
    orgEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="#FFFFFF"
    )
    orgEntry.place(x=550, y=250, width=200)

    mainLabel = Label(
        cho_window,
        text="Main Contact Email:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    mainLabel.place(x=300, y=280)
    mainEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="#FFFFFF"
    )
    mainEntry.place(x=300, y=300, width=300)

    qusLabel = Label(
        cho_window,
        text="Have you organised a Clean Up event before?",
        font=("Helvetica", 9),
        bg="#9DC4E5",
        fg="black",
    )
    qusLabel.place(x=300, y=340)

    r1 = tk.Radiobutton(
        cho_window, text="Yes", variable=r1_v, value="Yes", fg="black", bg="#9DC4E5"
    )
    r1.place(x=300, y=365)
    r2 = tk.Radiobutton(
        cho_window, text="No", variable=r1_v, value="No", fg="black", bg="#9DC4E5"
    )
    r2.place(x=360, y=365)

    yerLabel = Label(
        cho_window,
        text="If yes, for how many years?",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    yerLabel.place(x=600, y=340)
    yerEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="gray90"
    )
    yerEntry.place(x=600, y=365, width=100)

    actlocLabel = Label(
        cho_window,
        text="Activity Location:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    actlocLabel.place(x=90, y=405)
    actlocEntry = Entry(
        cho_window, width=30, font=("Helvetica", 10), fg="black", bg="gray90"
    )
    actlocEntry.place(x=90, y=430, width=200)

    acttyLabel = Label(
        cho_window,
        text="Activity Type:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    acttyLabel.place(x=350, y=405)
    cho = [
        "Rubbish Clean Up",
        "Habitat Restoration",
        "Tree Planting",
        "Education",
        "Awareness Raising",
        "Other",
    ]
    cb1 = ttk.Combobox(cho_window, values=cho, width=25)
    cb1.place(x=350, y=430)

    enviLabel = Label(
        cho_window,
        text="Environmental Type:",
        font=("Helvetica", 10),
        fg="black",
        bg="#9DC4E5",
    )
    enviLabel.place(x=580, y=405)
    cho1 = [
        "Urbnan Built ",
        "Park",
        "Tree Planting",
        "Forest/Reinforest",
        "Waterway/River",
        "Wetland/Mangrove",
        "Other",
    ]
    cb2 = ttk.Combobox(cho_window, values=cho1, width=25)
    cb2.place(x=580, y=430)

    qus1Label = Label(
        cho_window,
        text="Which of the following UN Sustainable Development Goals (SDGs)* does this activity help achieve? (Select all that apply):",
        font=("Helvetica", 10),
        bg="#9DC4E5",
        fg="black",
    )
    qus1Label.place(x=50, y=475)

    var1 = StringVar()
    che = Checkbutton(
        cho_window,
        text="SDG 4 - Quality Education",
        variable=var1,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che.deselect()
    che.place(x=50, y=505)

    var2 = StringVar()
    che1 = Checkbutton(
        cho_window,
        text="SDG 11 - Sustainable Cities and Communities",
        variable=var2,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che1.deselect()
    che1.place(x=50, y=535)

    var3 = StringVar()
    che2 = Checkbutton(
        cho_window,
        text="SDG 14 - Life Below Water",
        variable=var3,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che2.deselect()
    che2.place(x=50, y=560)

    var4 = StringVar()
    che3 = Checkbutton(
        cho_window,
        text="SDG 6 - Clean Water and Sanitation",
        variable=var4,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che3.deselect()
    che3.place(x=215, y=505)

    var5 = StringVar()
    che4 = Checkbutton(
        cho_window,
        text="SDG 12 - Responsible Consumption and Production",
        variable=var5,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che4.deselect()
    che4.place(x=340, y=535)

    var6 = StringVar()
    che5 = Checkbutton(
        cho_window,
        text="SDG 15 - Life and Land",
        variable=var6,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che5.deselect()
    che5.place(x=230, y=560)

    var7 = StringVar()
    che5 = Checkbutton(
        cho_window,
        text="SDG 7 - Affordable and Clean Energy",
        variable=var7,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che5.deselect()
    che5.place(x=440, y=505)

    var8 = StringVar()
    che6 = Checkbutton(
        cho_window,
        text="SDG 13 - Climate Action",
        variable=var8,
        font=("Helvetica", 9),
        bg="#9DC4E5",
    )
    che6.deselect()
    che6.place(x=655, y=535)

    submitButton = Button(
        cho_window,
        text="Submit",
        font=("Helvetica", 12, "bold"),
        bd=0,
        bg="#1668D9",
        fg="white",
        activebackground="#159FEE",
        activeforeground="white",
        width=10,
        command=check_page,
    )
    submitButton.place(x=690, y=620)

    cho_window.mainloop()


def login_user():

    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            conn = pymysql.connect(
                host="localhost", user="root", password="", database="cleanupdrive"
            )
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
            row = cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                messagebox.showinfo(
                    "Welcome", "Login is successful"
                )  # Define the INSERT query
                info_page()
            cursor.close()
            conn.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error connecting to database: {str(e)}")


def menu_page():
    login_window.destroy()
    import main


def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.config(file="pics/closeeye.png")
    passwordEntry.config(show="*")
    eyeButton.config(command=show)


def show():
    openeye.config(file="pics/openeye.png")
    passwordEntry.config(show="")
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)


def pass_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)


def forgot_pass():
    def change_password():
        if (
            user_entry.get() == ""
            or newpass_entry.get() == ""
            or confirmpass_entry.get() == ""
        ):
            messagebox.showerror("Error", "All Fields Are Required", parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror(
                "Error", "Password and Confirm Password are not matching", parent=window
            )
        else:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="cleanupdrive"
            )
            mycursor = con.cursor()
            query = "select * from users where username=%s"
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Incorrect Username", parent=window)
            else:
                query = "update users set password=%s where username=%s"
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo(
                    "Success",
                    "Password is reset, please login with new password",
                    parent=window,
                )
                window.destroy()

    window = Toplevel()
    window.title("Change Password")

    bgPic = ImageTk.PhotoImage(file="uvob.png")
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading_label = Label(
        window,
        text="RESET PASSWORD",
        font=("Helvetica", 15, "bold"),
        bg="#DEE6F0",
        fg="black",
    )
    heading_label.place(x=610, y=90)

    userLabel = Label(
        window,
        text="Username",
        font=("Helvetica", 10, "bold"),
        bg="#DEE6F0",
        fg="black",
    )
    userLabel.place(x=570, y=160)

    user_entry = Entry(
        window, width=25, fg="black", font=("Helvetica", 10, "bold"), bg="#DEE6F0", bd=0
    )
    user_entry.place(x=570, y=187)

    Frame(window, width=250, height=2, bg="azure4").place(x=570, y=206)

    newpassLabel = Label(
        window,
        text="New Password",
        font=("Helvetica", 10, "bold"),
        bg="#DEE6F0",
        fg="black",
    )
    newpassLabel.place(x=570, y=225)

    newpass_entry = Entry(
        window, width=25, fg="black", font=("Helvetica", 10, "bold"), bd=0, bg="#DEE6F0"
    )
    newpass_entry.place(x=570, y=250)

    Frame(window, width=250, height=2, bg="azure4").place(x=570, y=270)

    confirmpassLabel = Label(
        window,
        text="Confirm Password",
        font=("Helvetica", 10, "bold"),
        bg="#DEE6F0",
        fg="black",
    )
    confirmpassLabel.place(x=570, y=290)

    confirmpass_entry = Entry(
        window, width=25, fg="black", font=("Helvetica", 10, "bold"), bd=0, bg="#DEE6F0"
    )
    confirmpass_entry.place(x=570, y=315)

    Frame(window, width=250, height=2, bg="azure4").place(x=570, y=340)

    submitButton = Button(
        window,
        text="Submit",
        bd=0,
        bg="#1668D9",
        fg="white",
        font=("Helvetica", 16, "bold"),
        width=15,
        cursor="hand2",
        activebackground="#159FEE",
        activeforeground="white",
        command=change_password,
    )
    submitButton.place(x=595, y=380)

    window.mainloop()

#Login Page

login_window = Tk()
login_window.resizable(False, False)
login_window.title("Login Page")
login_window.iconbitmap(
    r"pics/ocean.ico"
)
bgImage = ImageTk.PhotoImage(
    file="pics/signinpage.png"
)

bgLabel = Label(login_window, image=bgImage)
bgLabel.grid(row=0, column=0)
heading = Label(
    login_window,
    text="SIGN IN",
    font=("Helvetica", 15, "bold"),
    bg="#DEE6F0",
    fg="black",
)
heading.place(x=645, y=90)

usernameLabel = Label(
    login_window, text="Username", font=("Open Sans", 10), fg="black", bg="#DEE6F0"
)
usernameLabel.place(x=570, y=160)
usernameEntry = Entry(
    login_window, width=25, font=("Open Sans", 10), bd=0, fg="black", bg="#DEE6F0"
)
usernameEntry.place(x=570, y=180)


usernameEntry.bind("<FocusIn>, user_enter")

frame1 = Frame(login_window, width=240, height=2, bg="black")
frame1.place(x=570, y=200)

passwordLabel = Label(
    login_window, text="Password", font=("Open Sans", 10), fg="black", bg="#DEE6F0"
)
passwordLabel.place(x=570, y=220)
passwordEntry = Entry(
    login_window, width=25, font=("Open Sans", 10), bd=0, fg="black", bg="#DEE6F0"
)
passwordEntry.place(x=570, y=245)

passwordEntry.bind("<FocusIn>, pass_enter")

frame2 = Frame(login_window, width=240, height=2, bg="black")
frame2.place(x=570, y=265)

openeye = PhotoImage(
    file="pics/openeye.png"
)
eyeButton = Button(
    login_window,
    image=openeye,
    bd=0,
    bg="#DEE6F0",
    activebackground="#DEE6F0",
    cursor="hand2",
    command=show,
)
eyeButton.place(x=785, y=243)

forgetButton = Button(
    login_window,
    text="Forgot Password?",
    font=("Helvetica", 9, "bold"),
    bd=0,
    fg="#159FEE",
    bg="#DEE6F0",
    cursor="hand2",
    command=forgot_pass,
)
forgetButton.place(x=700, y=275)

loginButton = Button(
    login_window,
    text="Login",
    font=("Helvetica", 14, "bold"),
    width=16,
    fg="#FFFFFF",
    bg="#1668D9",
    activeforeground="white",
    activebackground="#159FEE",
    cursor="hand2",
    bd=0,
    command=login_user,
)
loginButton.place(x=590, y=320)

orLabel = Label(
    login_window,
    text="---------------OR---------------",
    font=("Helvetica", 9),
    fg="#000000",
    bg="#DEE6F0",
)
orLabel.place(x=620, y=360)

signupLabel = Label(
    login_window,
    text="Dont have an account?",
    font=("Helvetica", 9),
    fg="black",
    bg="#DEE6F0",
)
signupLabel.place(x=585, y=400)

newaccountButton = Button(
    login_window,
    text="Create new one",
    font=("Helvetica", 8, "bold underline"),
    bg="#DEE6F0",
    fg="blue",
    activeforeground="white",
    activebackground="white",
    cursor="hand2",
    bd=0,
    command=signup_page,
)
newaccountButton.place(x=715, y=400)

menuPhoto = PhotoImage(
    file=r"pics/menu3.png"
)
menuButton = Button(
    login_window, image=menuPhoto, bd=0, bg="#FFFFFF", command=menu_page
)
menuButton.place(x=31, y=20)


login_window.mainloop()
