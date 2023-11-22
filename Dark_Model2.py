import customtkinter as ck
from tkinter import *
from tkinter import messagebox as msg
import sqlite3
import os
from PIL import Image


log = ck.CTk()
log.resizable(False, False)
log.config(background='#18191c')
file_path = os.path.dirname(os.path.relpath(__file__))

def Sign_in():
  logup_frame.pack_forget()
  log.geometry('370x180+700+450')
  log.title('Sign In')
  login_frame.pack(padx=5, pady=4)

def Sign_up():
  login_frame.pack_forget()
  log.geometry('370x360+700+350')
  log.title('Sign up')
  logup_frame.pack(padx=5, pady=5)

def check():
  if not User_entry.get() and not Password_entry.get():
    Sign_up()
  else:
    msg.showinfo('Success', 'Welcome to your account.')

login_frame = ck.CTkFrame(log, width=360, height=170, bg_color='#18191c', fg_color='#202225')
logup_frame = ck.CTkFrame(log, width=360, height=350, bg_color='#18191c', fg_color='#202225')

user_img = ck.CTkImage(Image.open(file_path + 'Icons/profile.png'), size=(30, 30))
user_img = ck.CTkLabel(login_frame, image = user_img, bg_color='#202225', text='').place(x=7, y=20)

pass_img = ck.CTkImage(Image.open(file_path + 'Icons/password.png'), size=(30,30))
pass_img = ck.CTkLabel(login_frame, image = pass_img, bg_color='#202225', text='').place(x=7, y=70)


User_entry = ck.CTkEntry(login_frame, placeholder_text='Username', font=('Ariel', 15, 'bold'), width=305, height=40, bg_color='#202225', fg_color='#202225')
User_entry.place(x=48, y=15)

Password_entry = ck.CTkEntry(login_frame, placeholder_text='Password', font=('Ariel', 15, 'bold'), show='⏣', width=305, height=40, bg_color='#202225', fg_color='#202225')
Password_entry.place(x=48, y=65)

login_button = ck.CTkButton(login_frame, text='Login', font=('Ariel', 15, 'bold'), width=348, height=40, bg_color='#202225', fg_color='royalblue', command=check).place(x=5, y=120)


# ---------------------------------------- Sign up window.
New_User_entry = ck.CTkEntry(logup_frame, placeholder_text='Username', font=('Ariel', 15, 'bold'), width=350, height=40, bg_color='#202225', fg_color='#202225')
New_User_entry.place(x=5, y=15)

New_full_entry = ck.CTkEntry(logup_frame, placeholder_text='Full-name', font=('Ariel', 15, 'bold'), width=350, height=40, bg_color='#202225', fg_color='#202225')
New_full_entry.place(x=5, y=65)

email_entry = ck.CTkEntry(logup_frame, placeholder_text='E-mail', font=('Ariel', 15, 'bold'), width=350, height=40, bg_color='#202225', fg_color='#202225')
email_entry.place(x=5, y=115)

New_pass_entry = ck.CTkEntry(logup_frame, placeholder_text='Password', font=('Ariel', 15, 'bold'), show='⏣', width=350, height=40, bg_color='#202225', fg_color='#202225')
New_pass_entry.place(x=5, y=165)

New_conf_entry = ck.CTkEntry(logup_frame, placeholder_text='Confirm Password', font=('Ariel', 15, 'bold'), show='⏣', width=350, height=40, bg_color='#202225', fg_color='#202225')
New_conf_entry.place(x=5, y=215)

logup_button = ck.CTkButton(logup_frame, text='Sign up', font=('Ariel', 15, 'bold'), width=350, height=40, bg_color='#202225', fg_color='royalblue').place(x=5, y=270)

logup_button = ck.CTkButton(logup_frame, text="I now have an account", font=('Ariel', 15, 'underline'), bg_color='#202225', fg_color='#202225', hover_color='#202225', command=Sign_in).place(x=100, y=320)

Sign_in()
log.mainloop()