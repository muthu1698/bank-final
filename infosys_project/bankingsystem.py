from tkinter import *
from tkinter import messagebox
import sqlite3

def new_database():
    firstname_info = Firstname.get()
    lastname_info = Lastname.get()
    global mobile_info
    mobile_info = Mobile.get()
    address_info = Address.get()
    pincode_info = Pincode.get()
    email_info = Email.get()
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Bank ('
                'FirstName TEXT,'
                'LastName TEXT,'
                'Mobile TEXT, Address TEXT,'
                ' Pincode TEXT, Email TEXT, AccountNumber TEXT, Password TEXT, Balance INT)')
    connection.commit()
    cur.execute('INSERT INTO Bank (FirstName, LastName, Mobile, Address, Pincode, Email, AccountNumber, Balance) '
                'VALUES(?,?,?,?,?,?,?,?)',(firstname_info, lastname_info, mobile_info,
                                       address_info, pincode_info, email_info, mobile_info, 500))
    connection.commit()
    connection.close()
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    mobile_entry.delete(0, END)
    address_entry.delete(0, END)
    pincode_entry.delete(0, END)
    email_entry.delete(0, END)
    password_gen()

def password_gen():
    global screen4
    screen4 = Toplevel(screen3)
    screen4.title("Password")
    screen4.geometry("500x400")

    global password1
    global password2
    global password1_entry
    global password2_entry
    password1 = StringVar()
    password2 = StringVar()
    Label(screen4, text=" ").pack()
    Label(screen4, text=" ").pack()
    Label(screen4, text="Create your own passsword", fg='DarkBlue', font=("Arial", 7)).pack()
    Label(screen4, text=" ").pack()
    Label(screen4, text=" ").pack()
    Label(screen4, text="Password", fg='Maroon').pack()
    password1_entry = Entry(screen4, textvariable=password1, show="*")
    password1_entry.pack()
    Label(screen4, text="Confirm Password", fg='Maroon').pack()
    password2_entry = Entry(screen4, textvariable=password2, show="*")
    password2_entry.pack()
    Label(screen4, text=" ").pack()
    Button(screen4, text="Submit", width=10, height=1, bg='GreenYellow', fg='Darkblue', command=newacc_msg).pack()


def newacc_msg():
    pass_info = password1.get()
    pass2_info = password2.get()
    if pass_info == pass2_info:
        print(pass_info)
        connection = sqlite3.connect("data.db")
        cur = connection.cursor()
        cur.execute('UPDATE Bank SET Password = ? WHERE AccountNumber = ?', (pass_info, mobile_info))
        connection.commit()
        connection.close()
        messagebox.showinfo('','\nAccount Created Successfully\n')
    else:
        messagebox.showwarning('', "   \n   Incorrect Password     \n\n     ")
    password1_entry.delete(0, END)
    password2_entry.delete(0, END)


def user_acc():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x400")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text=" ").pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text="User Login", fg='DarkBlue', font=("Arial", 10)).pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text="Account number", fg='Maroon').pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password", fg='Maroon').pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text=" ").pack()
    Button(screen1, text="Submit", width=10, height=1, bg='GreenYellow', fg='Darkblue', command=verify).pack()


def admin_acc():
    global screen0
    screen0 = Toplevel(screen)
    screen0.title("Register")
    screen0.geometry("500x400")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen0, text=" ").pack()
    Label(screen0, text=" ").pack()
    Label(screen0, text="Admin Login", fg='DarkBlue', font=("Arial", 10)).pack()
    Label(screen0, text=" ").pack()
    Label(screen0, text=" ").pack()
    Label(screen0, text="Username", fg='Maroon').pack()
    username_entry = Entry(screen0, textvariable=username)
    username_entry.pack()
    Label(screen0, text="Password", fg='Maroon').pack()
    password_entry = Entry(screen0, textvariable=password)
    password_entry.pack()
    Label(screen0, text=" ").pack()
    Button(screen0, text="Submit", width=10, height=1, bg='GreenYellow', fg='Darkblue', command=admin_verify).pack()


def signup_form():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("SIGN UP")
    screen3.geometry("500x400")

    global Firstname
    global Lastname
    global Mobile
    global Address
    global Pincode
    global Email
    global firstname_entry
    global lastname_entry
    global mobile_entry
    global address_entry
    global pincode_entry
    global email_entry
    Firstname = StringVar()
    Lastname = StringVar()
    Mobile = StringVar()
    Address = StringVar()
    Pincode = StringVar()
    Email = StringVar()

    Label(screen3, text="Please enter the details below", fg='MediumVioletRed', font=("Book Antiqua", 11)).grid(row=0, columnspan=2, padx=85, pady=2)
    Label(screen3, text=" ").grid(row=1, padx=50, pady=4)
    fname = Label(screen3, text="FIRST NAME", fg='Indigo')
    fname.grid(row=2, column=0, padx=50, pady=6)
    firstname_entry = Entry(screen3, textvariable=Firstname, relief='groove', bg='Lavender', bd=3)
    firstname_entry.grid(row=2, column=1, padx=50, pady=6)
    lname = Label(screen3, text="LAST NAME", fg='Indigo')
    lname.grid(row=3, column=0, padx=50, pady=8)
    lastname_entry = Entry(screen3, textvariable=Lastname, relief='groove', bg='Lavender', bd=3)
    lastname_entry.grid(row=3, column=1, padx=50, pady=8)
    mobile = Label(screen3, text="ACCOUNT NUMBER", fg='Indigo')
    mobile.grid(row=4, column=0, padx=50, pady=10)
    mobile_entry = Entry(screen3, textvariable=Mobile, relief='groove', bg='Lavender', bd=3)
    mobile_entry.grid(row=4, column=1, padx=50, pady=10)
    address = Label(screen3, text="ADDRESS", fg='Indigo')
    address.grid(row=5, column=0, padx=50, pady=12)
    address_entry = Entry(screen3, textvariable=Address, relief='groove', bg='Lavender', bd=3)
    address_entry.grid(row=5, column=1, padx=50, pady=12)
    pincode = Label(screen3, text="PINCODE", fg='Indigo')
    pincode.grid(row=6, column=0, padx=50, pady=14)
    pincode_entry = Entry(screen3, textvariable=Pincode, relief='groove', bg='Lavender', bd=3)
    pincode_entry.grid(row=6, column=1, padx=50, pady=14)
    email = Label(screen3, text="EMAIL", fg='Indigo')
    email.grid(row=7, column=0, padx=50, pady=16)
    email_entry = Entry(screen3, textvariable=Email, relief='groove', bg='Lavender', bd=3)
    email_entry.grid(row=7, column=1, padx=50, pady=16)
    Button(screen3, text="Register", width=10, height=1,bg='snow', fg='Darkblue',
           command=new_database).grid(row=9,columnspan=2, padx=150, pady=18)

def verify():
    username_info = username.get()
    password_info = password.get()
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    ver = ('SELECT * FROM Bank WHERE AccountNumber = ? AND Password = ?')
    cur.execute(ver,(username_info, password_info))
    verified = cur.fetchall()
    connection.commit()
    if verified:
        register_user()
    else:
        messagebox.showerror('Error','\n Incorrect username or password')
    #username_entry.delete(0, END)
    password_entry.delete(0, END)

def admin_verify():
    username_info = username.get()
    password_info = password.get()
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    ver = ('SELECT * FROM Bank WHERE AccountNumber = ? AND Password = ?')
    cur.execute(ver,(username_info, password_info))
    verified = cur.fetchall()
    connection.commit()
    if verified:
        admin_user()
    else:
        messagebox.showerror('Error','\n Incorrect username or password')
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def admin_user():
    global screen20
    screen20 = Toplevel(screen0)
    screen20.geometry("500x400")
    screen20.title(" ")
    Label(screen20, text=" ").pack()
    Label(screen20, text=" ").pack()
    Button(screen20,text="Change Address", height="2", width="30", bg='Aqua', relief='raised', command=change_address).pack()
    Label(screen20,text=" ").pack()
    Button(screen20,text="Transfer Money", height="2", width="30", bg='GreenYellow', relief='raised', command=transfers).pack()
    Label(screen20,text=" ").pack()
    Button(screen20,text="Check Balance", height="2", width="30", bg='LightPink', relief='raised', command=balance).pack()
    Label(screen20,text=" ").pack()
    Button(screen20,text="Deposit/Withdraw", height="2", width="30", bg='Aqua', relief='raised', command=depowith).pack()
    Label(screen20,text=" ").pack()
    Button(screen20,text="View Closed Accounts", height="2", width="30", bg='GreenYellow', relief='raised', command=register).pack()
    Label(screen20,text=" ").pack()
    Button(screen20,text="Logout", height="2", width="30", bg='LightPink', relief='raised', command=screen20.destroy).pack()
    Label(screen20,text=" ").pack()


def register_user():
    global screen2
    screen2 = Toplevel(screen1)
    screen2.geometry("500x400")
    screen2.config(bg='gray')
    screen2.title("")
    Label(screen2, text=" ",bg="gray").pack()
    Label(screen2, text=" ",bg="gray").pack()
    Button(screen2,text="Change Address", height="2", width="30", bg='snow', relief='raised', command=change_address).pack()
    Label(screen2,text=" ", bg="gray").pack()
    Button(screen2,text="Transfer Money", height="2", width="30", bg='snow', relief='raised', command=transfers).pack()
    Label(screen2,text=" ", bg="gray").pack()
    Button(screen2,text="Check Balance", height="2", width="30", bg='snow', relief='raised', command=balance).pack()
    Label(screen2,text=" ",bg="gray").pack()
    Button(screen2,text="Deposit/Withdraw", height="2", width="30", bg='snow', relief='raised', command=depowith).pack()
    Label(screen2,text=" ",bg="gray").pack()
    Button(screen2,text="Close Account", height="2", width="30", bg='snow', relief='raised', command=closing).pack()
    Label(screen2,text=" ",bg="gray").pack()
    Button(screen2,text="Logout", height="2", width="30", bg='snow', relief='raised', command=screen2.destroy).pack()
    Label(screen2,text=" ",bg="gray").pack()

def change_address():
    global address
    global address_entry
    address = StringVar()
    global screen6
    screen6 = Toplevel(screen2)
    screen6.geometry("500x400")
    screen6.title(" ")
    screen6.config(bg='Lavender')
    Label(screen6, text=" ",bg="Lavender").pack()
    Label(screen6, text=" ",bg="Lavender").pack()
    Label(screen6, text="Change Address", fg='DarkBlue', font=("Arial", 10)).pack()
    Label(screen6, text=" ").pack()
    Label(screen6, text=" ").pack()
    Label(screen6, text="Enter your new address", fg='Maroon').pack()
    address_entry = Entry(screen6, textvariable=address)
    address_entry.pack()
    Label(screen6, text=" ").pack()
    Button(screen6, text="Submit", width=10, height=1, bg='GreenYellow', fg='Darkblue', command=address_changer).pack()

def address_changer():
    global address_info
    acc_no = username.get()
    address_info = address.get()
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    cur.execute('UPDATE Bank SET Address = ? WHERE AccountNumber = ?', (address_info, acc_no))
    connection.commit()
    messagebox.showinfo('','\n Address changed\n')
    address_entry.delete(0, END)

def transfers():
    global screen7
    screen7 = Toplevel(screen2)
    screen7.geometry("500x400")
    screen7.title(" ")
    global acc1
    global acc2
    global money
    acc1 = StringVar()
    acc2 = StringVar()
    money = StringVar()
    global acc1_entry
    global acc2_entry
    global money_entry
    Label(screen7, text="Please enter the details below",
          fg='MediumVioletRed', font=("Arial", 11)).grid(row=0, columnspan=2,padx=85,pady=2)
    Label(screen7, text=" ").grid(row=1, padx=50, pady=4)
    acc1name = Label(screen7, text="Your account number", fg='Indigo')
    acc1name.grid(row=2, column=0, padx=50, pady=6)
    acc1_entry = Entry(screen7, textvariable=acc1, relief='groove', bg='Lavender', bd=3)
    acc1_entry.grid(row=2, column=1, padx=50, pady=6)
    acc2name = Label(screen7, text="Transfer to(Acc No.)", fg='Indigo')
    acc2name.grid(row=3, column=0, padx=50, pady=8)
    acc2_entry = Entry(screen7, textvariable=acc2, relief='groove', bg='Lavender', bd=3)
    acc2_entry.grid(row=3, column=1, padx=50, pady=8)
    amount = Label(screen7, text="Amount", fg='Indigo')
    amount.grid(row=4, column=0, padx=50, pady=10)
    money_entry = Entry(screen7, textvariable=money, relief='groove', bg='Lavender', bd=3)
    money_entry.grid(row=4, column=1, padx=50, pady=10)
    Button(screen7, text="Proceed", width=10, height=1, bg='Cyan', fg='Darkblue',
           command=transfer_process).grid(row=5, columnspan=2, padx=150, pady=18)
def transfer_process():
    from_acc = acc1.get()
    to_acc = acc2.get()
    transfer_amount = int(money.get())
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    cur.execute('SELECT Balance FROM Bank WHERE AccountNumber = ?', (from_acc,))
    user1bal = cur.fetchone()
    cur.execute('SELECT Balance FROM Bank WHERE AccountNumber = ?', (to_acc,))
    user2bal = cur.fetchone()
    user1_bal = user1bal[0]-transfer_amount
    user2_bal = user2bal[0]+transfer_amount
    if (user1_bal > 0):
        print('hi')
        cur.execute('UPDATE Bank SET Balance = ? WHERE AccountNumber = ?', (user1_bal, from_acc))
        cur.execute('UPDATE Bank SET Balance = ? WHERE AccountNumber = ?', (user2_bal, to_acc))
        connection.commit()
        messagebox.showinfo('','\n Transaction Successfull \n')
        acc1_entry.delete(0, END)
        acc2_entry.delete(0, END)
        money_entry.delete(0, END)

    else:
        messagebox.showwarning('', "    Account Balance low    \n\n      Cannot Proceed Transaction    ")
        acc1_entry.delete(0, END)
        acc2_entry.delete(0, END)
        money_entry.delete(0, END)


def balance():
    global screen8
    screen8 = Toplevel(screen2)
    screen8.geometry("500x400")
    screen8.title(" ")
    global ur_acc
    ur_acc = StringVar()
    global ur_acc_entry
    Label(screen8, text="Enter your Account Number",
          fg='DarkMagenta', font=("Arial", 13), height="2", width="30").grid(row=0, columnspan=2, padx=85, pady=2)
    Label(screen8, text=" ").grid(row=1, padx=50, pady=4)
    accname = Label(screen8, text="Your account number", font=("Arial", 10), fg='Indigo')
    accname.grid(row=2, column=0, padx=50, pady=6)
    ur_acc_entry = Entry(screen8, textvariable=ur_acc, relief='groove', bg='Lavender', bd=3,)
    ur_acc_entry.grid(row=2, column=1, padx=50, pady=6)
    Button(screen8, text="Submit", width=10, height=1, bg='LawnGreen', relief='groove', fg='Black',
           command=show_balance).grid(row=5, columnspan=2, padx=150, pady=18)

def show_balance():
    acc = ur_acc.get()
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    cur.execute('SELECT Balance FROM Bank WHERE AccountNumber = ?', (acc,))
    user1bal = cur.fetchone()
    user1_bal = user1bal[0]
    if(user1_bal):
        global screen9
        screen9 = Toplevel(screen8)
        screen9.geometry("350x250")
        screen8.title(" ")
        Label(screen9, text=" ").grid(row=0, padx=50, pady=4)
        Label(screen9, text=" ").grid(row=1, padx=50, pady=4)
        Label(screen9, text=" ").grid(row=2, padx=50, pady=4)
        Label(screen9, text="Your Account Balance is:", fg='DarkMagenta', font=("Arial", 13), height="2",
              width="30").grid(row=3, columnspan=2, padx=30, pady=2)
        Label(screen9, text=user1_bal, fg='DarkMagenta', font=("Arial", 13), height="2",
              width="30").grid(row=4, columnspan=2, padx=60, pady=2)
        Label(screen9, text=" ").grid(row=5, padx=50, pady=4)
    else:
        messagebox.showerror('','\nWrong Details.\n')
    ur_acc_entry.delete(0, END)

def depowith():
    global screen10
    screen10 = Toplevel(screen2)
    screen10.geometry("500x400")
    screen10.title(" ")
    Label(screen10, text=" ").pack()
    Label(screen10, text=" ").pack()
    Label(screen10, text=" ").pack()
    Button(screen10, text="Deposit", height="2", width="30", bg='Aqua', relief='raised',
           command=deposit).pack()
    Label(screen10, text=" ").pack()
    Label(screen10, text=" ").pack()
    Button(screen10, text="Withdraw", height="2", width="30", bg='GreenYellow', relief='raised',
           command=withdraw).pack()
    Label(screen10, text=" ").pack()

def deposit():
    global screen11
    screen11 = Toplevel(screen10)
    screen11.geometry("500x400")
    screen11.title(" ")
    global deprs
    global money2
    deprs = StringVar()
    money2 = StringVar()
    global deprs_entry
    global money2_entry
    Label(screen11, text="Enter your Account Number",
          fg='Green', font=("Arial", 13), height="2", width="30").grid(row=0, columnspan=2, padx=85, pady=2)
    Label(screen11, text=" ").grid(row=1, padx=50, pady=4)
    accname = Label(screen11, text="Your account number", font=("Arial", 10), fg='Green')
    accname.grid(row=2, column=0, padx=50, pady=6)
    deprs_entry = Entry(screen11, textvariable=deprs, relief='groove', bg='LightGreen', bd=3, )
    deprs_entry.grid(row=2, column=1, padx=50, pady=6)
    acc1name = Label(screen11, text="Amount to be deposited", font=("Arial", 10), fg='Green')
    acc1name.grid(row=3, column=0, padx=50, pady=6)
    money2_entry = Entry(screen11, textvariable=money2, relief='groove', bg='LightGreen', bd=3, )
    money2_entry.grid(row=3, column=1, padx=50, pady=6)
    Button(screen11, text="Submit", width=10, height=1, bg='MediumTurquoise', relief='groove', fg='Black',
           command=deposit_process).grid(row=5, columnspan=2, padx=150, pady=18)

def withdraw():
    global screen12
    screen12 = Toplevel(screen10)
    screen12.geometry("500x400")
    screen12.title(" ")
    global wirs
    global money1
    wirs = StringVar()
    money1 = StringVar()
    global wirs_entry
    global money1_entry
    Label(screen12, text="Enter your Account Number",
          fg='Green', font=("Times New Roman", 13), height="2", width="30").grid(row=0, columnspan=2, padx=85, pady=2)
    Label(screen12, text=" ").grid(row=1, padx=50, pady=4)
    accname = Label(screen12, text="Your account number", font=("Times New Roman", 10), fg='Green')
    accname.grid(row=2, column=0, padx=50, pady=6)
    wirs_entry = Entry(screen12, textvariable=wirs, relief='groove', bg='LightGreen', bd=3, )
    wirs_entry.grid(row=2, column=1, padx=50, pady=6)
    acc1name = Label(screen12, text="Amount to be withdrawn", font=("Times New Roman", 10), fg='Green')
    acc1name.grid(row=3, column=0, padx=50, pady=6)
    money1_entry = Entry(screen12, textvariable=money1, relief='groove', bg='LightGreen', bd=3, )
    money1_entry.grid(row=3, column=1, padx=50, pady=6)
    Button(screen12, text="Submit", width=10, height=1, bg='MediumTurquoise', relief='groove', fg='Black',
           command=withdraw_process).grid(row=5, columnspan=2, padx=150, pady=18)

def deposit_process():
    from_acc = deprs.get()

    transfer_amount = int(money2.get())
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    cur.execute('SELECT Balance FROM Bank WHERE AccountNumber = ?', (from_acc,))
    user1bal = cur.fetchone()
    if (user1bal):
        user1_bal = user1bal[0] + transfer_amount
        print('hi')
        cur.execute('UPDATE Bank SET Balance = ? WHERE AccountNumber = ?', (user1_bal, from_acc))
        connection.commit()
        messagebox.showinfo('','\n Amount Successfully Deposited \n')
    else:
        messagebox.showwarning('', "  \n Wrong Entry \n ")
    deprs_entry.delete(0, END)
    money2_entry.delete(0, END)

def withdraw_process():
    from_acc = wirs.get()

    transfer_amount = int(money1.get())
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    cur.execute('SELECT Balance FROM Bank WHERE AccountNumber = ?', (from_acc,))
    user2bal = cur.fetchone()
    user2_bal = user2bal[0] - transfer_amount
    if (user2_bal>0):

        print('hi')
        cur.execute('UPDATE Bank SET Balance = ? WHERE AccountNumber = ?', (user2_bal, from_acc))
        connection.commit()
        messagebox.showinfo('', '\n Amount Successfully Withdrawn \n')
    else:
        messagebox.showwarning('', "  \n Wrong Entry \n ")
    wirs_entry.delete(0, END)
    money1_entry.delete(0, END)

def closing():
    acc = username.get()
    connection = sqlite3.connect("data.db")
    cur = connection.cursor()
    cur.execute('SELECT * FROM Bank WHERE AccountNumber = ?', (acc,))
    res = cur.fetchall()
    connection.commit()
    if(res):
        cur.execute('DELETE FROM Bank WHERE AccountNumber = ?', (acc,))
        connection.commit()
        connection.close()
        messagebox.showinfo('','\nAccount Deleted\n')
    else:
        messagebox.showwarning('',"\nAccount doesn't exist\n")

def register():
    messagebox.showerror('',"  \n Sorrry ! \n Couldn't retrieve data\n    ")
    return

def main():
    global screen
    screen = Tk()
    screen.geometry("500x400")
    C = Canvas(screen, bg='red', height=250, width=500)
    filename = PhotoImage(file = "C:\\Users\\Muthu\\Downloads\\infosys_project\\image\\red.png")
    background_screen = Label(screen, image=filename)
    background_screen.place(x=0, y=0, relwidth=1, relheight=1)
    screen.title("WELCOME")
    Label(text="",bg="lavender blush").pack()
    Label(text="",bg="lavender blush").pack()
    Label(text="",bg="lavender blush").pack()
    Label(text="WELCOME", fg="black", font=("Century", 15)).pack()
    Label(text="",bg='lavender blush').pack()
    Button(text="New Account", height="2", width="30", bg='peach puff', relief='raised', command=signup_form).pack()
    Label(text="",bg='misty rose').pack()
    Button(text="User Login", height="2", width="30", bg='peach puff', relief='raised', command=user_acc).pack()
    Label(text="", bg='misty rose').pack()
    C.pack()
    screen.mainloop()


main()

