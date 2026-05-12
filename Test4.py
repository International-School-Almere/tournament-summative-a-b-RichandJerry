from tkinter import *

root = Tk()
root.geometry("300x200")

def show():
    lbl.config(text=f"Selected: {opt.get()}")

# Selected option variable  
opt = StringVar(value="Python")

# Radio buttons  
for lang in ["Python", "Java", "C++", "JavaScript"]:
    Radiobutton(root, text=lang, variable=opt, value=lang).pack()

# Button & Label  
Button(root, text="Show Selection", command=show).pack()
lbl = Label(root, text=" ")
lbl.pack()


root.mainloop()