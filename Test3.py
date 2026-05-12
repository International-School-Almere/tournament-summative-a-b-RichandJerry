from tkinter import *

root = Tk()
root.geometry("300x200")

def show():
    label.config(text=f"Selected: {listbox.get(ACTIVE)}")

# Listbox  
listbox = Listbox(root)
for item in ["Python", "Java", "C++", "JavaScript", "Swift"]:
    listbox.insert(END, item)
listbox.pack()

# Button & Label  
Button(root, text="Show Selection", command=show).pack()
label = Label(root, text=" ")
label.pack()

root.mainloop()