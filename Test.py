from tkinter import *  

root = Tk()  
root.geometry("600x400")  

def show():  
    lbl.config(text=opt.get())  

# Dropdown options  
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  

# Selected option variable  
opt = StringVar(value="")  

# Dropdown menu  
OptionMenu(root, opt, *days).pack()  

# Button to update label  
Button(root, text="Click Me", command=show).pack()  

lbl = Label(root, text=" ")  
lbl.pack()  

root.mainloop()  