import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Create a variable with a value of "1"
check_var = tk.StringVar(value="1")

# Create the Checkbutton widget
check_button = tk.Checkbutton(
    window,
    text="Check me!",
    variable=check_var
)

# Pack or grid the Checkbutton in the window
check_button.pack()

# Start the Tkinter event loop
window.mainloop()
