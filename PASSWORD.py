# -*- coding: utf-8 -*-
"""
Created on Tue Aug 2 19:20:34 2023

@author: User
"""



from tkinter import *
from tkinter import messagebox
import random

pd = Tk()
pd.geometry("450x250+400+250")
pd.title("Password Generator-M")
pd.configure(bg="#32405b")
pd.resizable(0, 0)
tl_label = Label(pd, text=" Create a safe password", font=('Ubuntu Mono',20),bg='#32405b')
tl_label.pack()
len_label = Label(pd, text="Enter length of password: ",bg='#32405b',font=("script mj bold ",10,"bold"))
len_label.place(x=20,y=60)
len_entry = Entry(pd, width=3)
len_entry.place(x=190,y=60)
rep_label = Label(pd, text="Repetition? 1: No repetition, 2: Otherwise: ",bg='#32405b',font=("script mj bold ",10,"bold"))
rep_label.place(x=20,y=90)
rep_entry = Entry(pd, width=3)
rep_entry.place(x=295,y=90)


def gen():
    try:
      l=int(len_entry .get())
      r=int(rep_entry.get())
      
      if l==0:
        messagebox.showerror(message="length selected is too short")  
        return
      else:
          pass
    except:
        messagebox.showerror(message="Please key in the required inputs")
        return
    if r==1:
        pas = random.sample(character,l)
    elif r==2:
        pas = random.choices(character,k=l)
    else:
       messagebox.showerror(message="Please enter a proper selection")

    pas=''.join(pas)
    pas_v = StringVar()

    pas="Created password:  " +str(pas)
    pas_v.set(pas)
    pas_label = Entry(pd,bg="GREY", textvariable= pas_v)
    pas_label.place(x=20, y=180, height=50, width=320)
    
  

####
character="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
####


pd_button = Button(pd, text="Generate Password",bg='olive',command=gen)
pd_button.place(x=20,y=140)
pd.mainloop()