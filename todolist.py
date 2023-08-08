# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:24:31 2023

@author: User
"""



from tkinter import *
from tkinter import messagebox

m=Tk()
m.geometry('1280x638+-10+0')
m.configure(bg='grey')
m.title("my todo")
m.resizable(0,0)
tl_entry=Entry(borderwidth=2,width=40,font=("Arial",20),bg='grey',relief=SOLID)
tl_entry.place(x=10,y=80)
Al=Label(m,text="ALL TASKS",font=(" monotype corsiva",30,"italic bold"),width=16,bg='grey')
Al.place(x=150,y=20)


task_list=[]

def todo():
    
    ad = tl_entry.get()
    
    if ad:
        
        listbox.insert(END,ad)
        tl_entry.delete(0,END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task!")

        
        
        
def edit():
    selected_index = listbox.curselection()
    if selected_index:
        selected_task = listbox.get(selected_index)
        e = Toplevel(m)
        e.geometry('400x300+780+190')
        e.configure(bg='azure4')
        e.title(" EDIT WINDOW")
        e.resizable(False,False)
        def save_change():
            ad= edit_entry.get()
            if ad:
                listbox.delete(selected_index)
                listbox.insert(selected_index,ad)
                e.destroy()
                messagebox.showinfo('CONGO!',"TASK UPDATED SUCCESSFULLY :)")
            else:
                messagebox.showwarning("Empty Task", "Please enter a task!")

        edit_label = Label(e, text="Edit Task:", font=("Arial", 12, "bold"),bg='azure4')
        edit_label.pack(pady=10)
        edit_entry = Entry(e, font=("Arial", 12),bg='ivory4')
        edit_entry.pack()
        edit_entry.insert(END, selected_task)
        save_button = Button(e, text="Save Changes", font=("Arial", 12, "bold"),bg='peachpuff4', command=save_change)
        save_button.pack(pady=10)
        
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to edit!")
        
  
        
   
        
def cmp():
    selected_index = listbox.curselection()
    if selected_index:
        selected_task = listbox.get(selected_index)
        sel=selected_task+" ✓"
        listbox.delete(selected_index)
        listbox.insert(selected_index,sel)

    else:
        messagebox.showwarning("No Task Selected", "Please select a task to Mark Complete!")

    
    
def dlt():
    selected_index = listbox.curselection()
    if selected_index:
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")
        if confirm:
            listbox.delete(selected_index)
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete!")
        
#add button    
A=Button(m,text="ADD",font=("script mj bold",18,"italic bold"),bg="grey",borderwidth=7,relief=RAISED,command=todo)
A.place(x=650,y=70)


#add frame
add=Frame(m,borderwidth=10,relief=GROOVE,bg="snow3")
add.place(x=10,y=135,width=700,height=368)



#scrollbar
sbr=Scrollbar(add,orient=VERTICAL)
sbr.pack(side=RIGHT,fill=Y)



#listbox
listbox=Listbox(add,font=('arial',25),width=600,height=300,bg='#32405b')
listbox.pack(side=LEFT,fill=BOTH,padx=1,pady=1)


listbox.config(yscrollcommand=sbr.set)
sbr.config(command=listbox.yview)



#delete button
D=Button(m,text=" DELETE ✖",font=("script mj bold ",18,"bold"),bg="red",borderwidth=5,relief=RAISED,command=dlt)
D.place(x=500,y=550)


#edit button
E=Button(m,text=" EDIT 🖋 ",font=("script mj bold ",18,"italic bold"),bg="deepskyblue4",borderwidth=5,relief=RAISED,command=edit)
E.place(x=310,y=550)


#completed button
C=Button(m,text=" COMPLETED ✓",font=("script mj bold ",18,"italic bold"),bg="green",borderwidth=5,relief=RAISED,command=cmp)
C.place(x=30,y=550)


mainloop()
