from tkinter import*
from tkinter import messagebox
import tkinter.font as font
from PIL import ImageTk,Image
import runpy
import sqlite3

project=Tk()
project.configure(bg="white")
project.attributes("-fullscreen",True)

screen_width = project.winfo_screenwidth()
screen_height= project.winfo_screenheight()

#creating title bar
a=Frame(project,width=screen_width,height=35,bg="#57a1f8").place(x=0,y=0)
title=Label(a, text="AccuResult",font=("Comic Sans MS",15,"bold"), bg="#57a1f8").place(x=36,y=0)
img=Image.open(r"assets/logo.png") #image logo
img=img.resize((30,30))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=0,bg="#57a1f8").place(x=5,y=3)
label1=LabelFrame(project,height=35,fg="blue",bg="#57a1f8").place(x=0,y=0)
buttonFont = font.Font(size=14)
buttonFont1 = font.Font(size=13)

#making maximize and minimize button manually
def min():
    project.iconify()
def on_enter(i):
    btn2['background']="red"
def on_leave(i):
    btn2['background']="#57a1f8"
def max():
    msg_box =messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?',icon='warning')
    if msg_box == 'yes':
        project.destroy()

btn2=Button(a,text="✕", command=max,width=4,bg="#57a1f8",border=0,font=buttonFont)
btn2.pack(anchor="ne")
btn2.bind('<Enter>',on_enter)
btn2.bind('<Leave>',on_leave)
btn=Button(a,text="-", command=min,width=4,bg="#57a1f8",border=0,font=buttonFont)
btn.place(x=screen_width-100,y=0)
def enter(i):
    btn['background']="red"
def leave(i):
    btn['background']="#57a1f8"
btn.bind('<Enter>',enter)
btn.bind('<Leave>',leave)

#back_button
def back():
    project.destroy()
    runpy.run_path(
        "base.py")
btn4=Button(project,text="<<",width=4,bg="#57a1f8",border=0,font=buttonFont,command=back)
btn4.place(x=screen_width-150,y=0)
def enter(i):
    btn4['background']="red"
def leave(i):
    btn4['background']="#57a1f8"
btn4.bind('<Enter>',enter)
btn4.bind('<Leave>',leave)


#Inserting picture

img = Image.open(r"assets/sideimg.png")
img = img.resize((700, 500))
img = ImageTk.PhotoImage(img)
Label(image=img, bg="white").place(x=600, y=180)

# Add a small description below the image
desc_label = Label(project,text="Inventory Management System\nFast, Secure, and Smart!",font=("Arial", 14, "italic"),fg="#333333",bg="#F9FBFC")
desc_label.place(x=800, y=690)

# Add a support contact
contact_label = Label(project,text="Need Help? Contact us at support@example.com",font=("Arial", 10),fg="blue",bg="#F9FBFC",cursor="hand2")
contact_label.place(x=800, y=740)



# Creating frame for login
frame2= Frame(project,width=420,height=470,bg="white")
frame2.place(x=70, y=200)

heading = Label(frame2, text='Log In', font=("Arial", 18, "bold"), fg="blue", bg="white")
heading.place(x=70, y=10)

# Google Sign-In Button
google_btn = Button(frame2,text="Sign In With Google",font=("Arial", 10, "bold"),fg="white",bg="#DB4437",border=0,activebackground="#B73A2F",cursor="hand2")
google_btn.place(x=70, y=70, width=350, height=35)

# Email Entry with Placeholder
def on_enter(e):
    if user.get() == "Enter email here...":
        user.delete(0, "end")
def on_leave(e):
    if user.get() == "":
        user.insert(0, "Enter email here...")

user = Entry(frame2, width=35, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 12))
user.place(x=70, y=125)
user.insert(0, "Enter email here...")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame2, width=350, height=2, bg="black").place(x=70, y=152)

# Password Entry with Placeholder
def on_enter_password(e):
    if code.get() == "Enter password here...":
        code.delete(0, "end")
        code.config(show="●")
def on_leave_password(e):
    if code.get() == "":
        code.config(show="")
        code.insert(0, "Enter password here...")

code = Entry(frame2, width=35, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 12))
code.place(x=70, y=200)
code.insert(0, "Enter password here...")
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)
Frame(frame2, width=350, height=2, bg="black").place(x=70, y=227)

# Remember Me & Forgot Password
Checkbutton(frame2, text="Remember me", bg="white", font=("Arial", 10)).place(x=70, y=250)
Label(frame2, text="Forgot Password?", fg="blue", bg="white", cursor="hand2", font=("Arial", 10)).place(x=280, y=250)

# Login Function
def signin():
    username = user.get()
    password = code.get()
    ayu = sqlite3.connect("signup.db")
    a = ayu.cursor()

    a.execute("SELECT * FROM sign WHERE email=? AND password=?", (username, password))
    sleep = a.fetchone()
    if sleep:
        ayu.commit()
        ayu.close()
        project.destroy()
        
    else:
        messagebox.showerror("Error", "Invalid information")

# Login Button
login_btn = Button(frame2, text="Log In", bg="black", fg="white", width=37, pady=7, border=0, font=("Arial", 12), command=signin)
login_btn.place(x=70, y=300)

# Signup Redirect
Label(frame2, text="Not Register yet?", fg="black", bg="white", font=("Arial", 10)).place(x=130, y=360)
signup_btn = Button(frame2, text="Contact Us!!", border=0, bg="white", cursor="hand2", fg="blue", font=("Arial", 10))
signup_btn.place(x=230, y=360)
project.mainloop()
