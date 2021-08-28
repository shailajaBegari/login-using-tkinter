from tkinter import*
import tkinter.messagebox as mb
window=Tk()
def log():
    username=entry_username.get()
    password=entry_password.get()
    if (username=="shailaja" and password=="1234"):
        mb.showinfo("login","loginsuccfully")
    else:
        mb.showinfo("login","failed")
label_username=Label(window,text="username",font=("times",15))
label_password=Label(window,text="password",font=("times",15))
entry_username=Entry()
entry_password=Entry()
label_username.grid(row=0,sticky=E)
label_password.grid(row=1,sticky=E)
entry_username.grid(row=0,column=1)
entry_password.grid(row=1,column=1)

button=Button(window,text="login",command=log)
button.grid(columnspan=2)