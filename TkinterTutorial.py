from tkinter import *

root = Tk()

# Creating a Label Widget
L1 = Label(root, text="Hello world")
L2 = Label(root, text="My name is Benjamin Gonzalez")
L3 = Label(root, text="Side text")
# Shoving Label Widget onto the screen
#   myLabel.pack()

# Put widgets onto root using grid layout
# L1.grid(row=0, column=0)
# L2.grid(row=1, column=0)
# L3.grid(row = 0, column=2)

B1 = Button(root, text="Click here", padx=50, pady=50)

L1.pack()
L2.pack()
L3.pack()
B1.pack()

root.mainloop()