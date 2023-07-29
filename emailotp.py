import random
import smtplib
from threading import Thread
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image


#Design
back= '#1f8384'
cl='#59ebcb'
df='#ff74d9'


window=Tk()
window.title("Alarm Clock")
window.geometry('450x200')
window.configure(bg=cl)


top=Frame(window,width=450,height=5,bg='#34495e')
top.grid(row=0,column=0)

bd=Frame(window,width=450,height=200,bg='#F6F3E4')
bd.grid(row=1,column=0)

#Import Icon and Labels
ala=Label(bd,text="Generate OTP",width=14,font=('Ivy 20 bold'),bg='#F6F3E4',fg='#F16F6E')
ala.place(x=110,y=10)

def send_otp(email):
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    email_address = 'yourmail@gmail.com'       #Type your Gmail account      
    email_password = 'yourpassword'            #Type your Gmail Password
    server.login(email_address, email_password)
    otp = ''.join([str(random.randint(0, 9)) for i in range(6)]) 
    message = f'Your OTP is {otp}'
    server.sendmail(email_address, email, message)
    server.quit()

    return otp
def verify_otp():
    email = input("Enter your email address: ")

    otp = send_otp(email)

    user_input = input("Enter the OTP sent to your email: ")
    if user_input == otp:
        print("OTP verified successfully!")
    else:
        print("Invalid OTP, please try again.")

rad1=Button(bd,font=('arial 10 bold'),text="Click To Generate",bg='#FFFFFF',command=verify_otp)
rad1.place(x=170,y=120)


window.mainloop()