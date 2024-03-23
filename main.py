from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

window = Tk()
window.title("Login System Of Student Management System By Jegan")
window.geometry("1280x848+0+0")
window.resizable(False,False)

#functions

def clear_field():
    user_entry.delete(0,'end')
    password_entry.delete(0,'end')

def login():
    if user_entry.get()=='' and password_entry.get()=='':
        messagebox.showerror("Error","Fields cannot be empty!")
    elif user_entry.get()=='Jegan' and password_entry.get()=='1234':
        messagebox.showinfo("Success","welcome user")
        window.destroy()
        import sms
    else:
        clear_field()
        messagebox.showerror("Error","please enter your correct credentials")



# bg image
background_image =ImageTk.PhotoImage(file="tkinter/background_image .jpg")
bg_label = Label(window,image=background_image)
bg_label.place(x=0,y=0)

# login frame
frame =Frame(window,bg="white")
frame.place(x=400,y=150)

# logo
logo =PhotoImage(file="tkinter/login_logo.png")
logo_label =Label(frame,image=logo,bg="white")
logo_label.grid(row=0,column=0,columnspan=2,pady=10)

# username logo
username_logo = PhotoImage(file="C:/Users/ORGIN/Desktop/Turtle/tkinter/username_logo.png")
user_label =Label(frame,image=username_logo,text="Username",bg="white",compound="left",font=("time new roman",15,'bold'))
user_label.grid(row=1,column=0,pady=10,padx=20)
user_entry =Entry(frame,bd=2,width=30)
user_entry.grid(row =1,column=1,pady=10,padx=20)

# password logo
password_logo =PhotoImage(file="tkinter/password_logo.png")
password_label=Label(frame,image=password_logo,text="Password",bg="white",compound=LEFT,font=("time new roman",15,'bold'))
password_label.grid(row=2,column=0,pady=10,padx=20)
password_entry =Entry(frame,bd=2,width=30)
password_entry.grid(row=2,column=1,pady=10,padx=20)

# login button
login_button =Button(frame,text="Login",bg="cornflowerblue",fg="white",activebackground="skyblue",activeforeground="white",font=("time new roman",10,'bold'),width=10,cursor='hand2',command=login)
login_button.grid(row=3,column=1,pady=10,padx=20)
window.mainloop()