#!/usr/bin/env python3
# POC add rows
import tkinter as tk
class App:
    def new_row(self):
        new_entry = tk.Entry(root)
        self.num_rows += 1
        new_entry.grid(column=0, row=self.num_rows)
    def __init__(self): #the code that executes when an class is initiated
        self.num_rows = 1
        createRow_button = tk.Button(root, text='New Row', command=self.new_row) #self refers to the current instance of the class, used to access variables/functions within the class
        createRow_button.grid()
root = tk.Tk() #creates the Tk window thing
app = App() #initiates an instance of the App class called app
root.mainloop()