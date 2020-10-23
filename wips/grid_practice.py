#!/usr/bin/env python3

from tkinter import *

root=Tk()
#standard format from box.py
root.title("Grid Practice")
root.configure(bg="#4e4f50")
root.minsize(1200, 450)
#instead of the .minsize, we can do geometry but geometry is very fixed
#root.geometry("1350x450")

#column header text
# num_header=Label(root, text="RULE No.")
# iof_header=Label(root, text="INPUT/OUTPUT/FORWARD")
# src_ip=Label(root, text="SOURCE IP")
# src_port=Label(root, text="SOURCE PORT")
# dest_ip=Label(root, text="DESTINATION IP")
# dest_port=Label(root, text="DESTINATION PORT")
# proto=Label(root, text="PROTOCOL")
# accdr=Label(root, text="ACCEPT/DROP")


#1st row of entry
# num_entry=Entry(root)
# iof_entry=Entry(root)
# src_ip_entry=Entry(root)
# src_port_entry=Entry(root)
# dest_ip_entry=Entry(root)
# dest_port_entry=Entry(root)
# proto_entry=Entry(root)
# accdr_entry=Entry(root)



# .grid and placing by row and column
# num_header.grid(row=0, column=0)
# iof_header.grid(row=0, column=1)
# src_ip.grid(row=0, column=2)
# src_port.grid(row=0, column=3)
# dest_ip.grid(row=0, column=4)
# dest_port.grid(row=0, column=5)
# proto.grid(row=0, column=6)
# accdr.grid(row=0, column=7)
# num_entry.grid(row=1, column=0)
# iof_entry.grid(row=1, column=1)
# src_ip_entry.grid(row=1, column=2)
# src_port_entry.grid(row=1, column=3)
# dest_ip_entry.grid(row=1, column=4)
# dest_port_entry.grid(row=1, column=5)
# proto_entry.grid(row=1, column=6)
# accdr_entry.grid(row=1, column=7)

##GEOMETRY MANAGERS - pack, grid, and place - can use only one per window
#pack - easiest (top,bottom, left, right)
#grid - more detail - can take more than one column/row
#place - even more control - for super complex programs

##COMMAND BUTTONS
#2 - command that goes into button should go first
# def press_button():
#     #print("Button has been clicked!")
#     #3 - introducing .config - make a change 
#     button1.config(text="Oh no, I've been clicked!", fg="red") #text on the button changes, in red font - you can put in padding too
#     #button1.grid(side=TOP) #you can also call the button within the def.
# #1 - making button
# button1=Button(root, text="Click Me!", command= press_button)
# button1.grid()

##FRAMES - INVISIBLE RECTANGLES
# frame1=Frame(root)
# frame2=Frame(root)

# label1=Label(frame1, text="I am in frame1") #don't need to say root, you can say which frame
# label1.pack()
# button1=Button(frame1,text="I am in frame1 too!")
# button1.pack()

# label2=Label(frame2, text="I am in frame2")
# label2.pack()
# button2=Button(frame2,text="I am in frame2 too!")
# button2.pack()

# frame1.pack()
# frame2.pack(side=BOTTOM)


##GETTING USER INPUT
# def name_submit():
#     print('Your name is: {}'.format(e1.get())) #the {} is a placeholder - will tell what to put in there using .format - we are getting whatever is in e1

# label1=Label(root, text="What's your name?")
# label1.pack()
# e1=Entry(root)
# e1.pack()
# button1=Button(root, text="Submit", command=name_submit)
# button1.pack()

##ADDING ICON TO TITLE
#drawing your own icon - http://www.rw-designer.com/online_icon_maker.php
#iconbitmap
#.ico 


root.mainloop()