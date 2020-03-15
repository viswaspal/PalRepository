import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('SUBSCRIBTION RECORD TO A TEXT FILE')
#create Labels
name_label=ttk.Label(win,text='Enter your name:')
name_label.grid(row=0,column=0,sticky=tk.W)
age_label=ttk.Label(win,text="Enter your age")
age_label.grid(row=1,column=0,sticky=tk.W)
email_label=ttk.Label(win,text="Enter your email-id")
email_label.grid(row=2,column=0,sticky=tk.W)
gender_label=ttk.Label(win,text="Select your gender")
gender_label.grid(row=3,column=0,sticky=tk.W)
# create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=15,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()
age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=15,textvariable=age_var)
age_entrybox.grid(row=1,column=1)
email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=15,textvariable=email_var)
email_entrybox.grid(row=2,column=1)
#create button
def action():
    name=name_var.get()
    age=age_var.get()
    email=email_var.get()
    print(f'User name is: {name} and his/her age is:{age} and email is {email} ')
    check=checkbtn_var.get()
    user=usertype.get()
    gender=gender_var.get()
    if(check==0):
        subscribed="NO"
    else:
        subscribed="YES"
    print(gender,user,subscribed)
    with open('text1.txt','a') as f:
        f.write(f'{name},{age},{email},{user},{subscribed}\n')
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Red')
    age_label.configure(foreground="Red")
    email_label.configure(foreground="Red")
    submit_button.configure(foreground="Red")
    gender_label.configure(foreground="Red")
submit_button=ttk.Button(win,text='submit',command=action)
submit_button.grid(row=7,column=0)
#create combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=11,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.grid(row=3,column=1)
gender_combobox.current(0)
#create RAdiobutton
usertype=tk.StringVar()
radio_button1=ttk.Radiobutton(win,text='student',value='student',variable=usertype)
radio_button1.grid(row=5,column=0)
radio_button2=ttk.Radiobutton(win,text='teacher',value='teacher',variable=usertype)
radio_button2.grid(row=5,column=1)
#create Checkbutton
checkbtn_var=tk.IntVar()
check_button1=ttk.Checkbutton(win,text='check if you want to subscribe our newsletter',variable=checkbtn_var)
check_button1.grid(row=6,columnspan=3)
win.mainloop()
