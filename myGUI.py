from tkinter import *
from tkinter import ttk
import System
import Permissions

#Log-In Screen
def start():
    #Main window
    global root
    root = Tk()
    #root.Title("Authentication")
    #Setting variables
    global username #global variabels so it can be accessed by System
    global password
    username = StringVar()
    password = StringVar()
    #Frame for logging in
    entryFrame = ttk.Frame(root, relief = RIDGE)
    entryFrame.pack(padx = 20, pady = 20, ipadx = 20, ipady = 20)
    ttk.Label(entryFrame,
              text = "Welcome to my program! Please log-in!").pack(pady = 20)
    
    ttk.Label(entryFrame, text = "Username:").pack()
    
    username_entry = ttk.Entry(entryFrame, width = 24, textvariable = username)
    username_entry.pack()
    
    ttk.Label(entryFrame, text = "Password:").pack()
    
    password_entry = ttk.Entry(entryFrame, width = 24, textvariable = password)
    password_entry.pack()
    password_entry.config(show = "*")
    
    log_inButton = ttk.Button(entryFrame, text = "Log In")
    log_inButton.config(command = lambda: System.log_in(username.get(), password.get()))
    log_inButton.pack(pady = 10)
    
    #I have no idea why bind wants an arg but the button doesn't
    root.bind('<Return>', lambda x: System.log_in(username.get(), password.get()))

    #Frame for registering a new user
    registerFrame = ttk.Frame(root, relief = RIDGE)
    registerFrame.pack(padx = 20, pady = 20, ipadx = 20, ipady = 10)
    
    ttk.Label(registerFrame, text = "Not a user? Register here:").pack(pady = 10)

    registerButton = ttk.Button(registerFrame, text = "Register")
    registerButton.config(command = lambda: register_window())
    registerButton.pack(pady = 5)

    root.mainloop()

def register_window():
    global r_window
    r_window = Toplevel(root)
    #window.Title("Register")
    #Frame for logging in
    global r_frame
    register_frame = ttk.Frame(r_window, relief = RIDGE)
    register_frame.pack(padx = 10, pady = 10, ipadx = 5, ipady = 5)

    #Variables
    global n
    global p
    n = StringVar()
    p = StringVar()
    
    ttk.Label(register_frame, text = "Username:").pack()
    
    input_username = ttk.Entry(register_frame, width = 24, textvariable = n)
    input_username.pack()
    
    ttk.Label(register_frame, text = "Password:").pack()
    
    password_entry = ttk.Entry(register_frame, width = 24, textvariable = p)
    password_entry.pack()
    password_entry.config(show = "*")
    
    submit = ttk.Button(register_frame, text = "Submit")
    submit.config(command = lambda: register())
    submit.pack()

    global error
    error = ttk.Label(register_frame, text = "", foreground = "Red")
    error.pack(pady = 5)

def register():
    """Calls System.new_user() and modifies GUI to match results"""
    global n
    global p
    global register_window
    global register_frame
    success = System.new_user(n.get(), p.get())
    if success == True:
        #Change this later to redirect to mainGUI
        r_window.destroy()
    else:
        error.config(text = "Username Taken")

def addProfile_window():
    window = TopLevel(root)
    #Use grid manager.
    
    global name
    name = StringVar()
    name_label = ttk.Label(window, text = "Name:")
    name_input = ttk.Entry(window, textvariable = name)
    
    global role
    role = StringVar()
    role_label = ttk.Label(window, text = "Role:")
    role_input = ttk.Entry(window, textvariable = role)
    
    global talent
    talent = StringVar()
    talent_label = ttk.Label(window, text = "Talent:")
    talent_input = ttk.Entry(window, textvariable = talent)
    
    global month
    global day
    global year
    month = IntVar()
    day = IntVar()
    year = IntVar()
    dob_label = ttk.Label(window, text = "Date of Birth:")
    month_input = ttk.Combobox(window, textvariable = month)
    month_input.configure(values=range(1, 13))
    day_input = ttk.Combobox(window, textvariable = day)
    day_input.configure(values=range(1, 32))
    
    year_input = ttk.Spinbox(window, from_=1930, to=2020, textvariable = year)
    global faction
    global race
    global sex
    global height
    global weight
    global hclr
    global eclr
    global sclr
    global other
    global bio
    
    lname = StringVar()
    
    scrollbar = Scrollbar(window)
    scrollbar.pack(side = RIGHT, fill = Y)

def addProfile():
    pass


def mainScreen():
    pass
        

