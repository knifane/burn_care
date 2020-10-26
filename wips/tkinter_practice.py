#!/usr/bin/env python3

from tkinter import *

root=Tk()
#standard format from box.py
root.title("Tkinter Practice")
root.configure(bg="#4e4f50")
root.minsize(1200, 450)

##MENUS - referring to the menu along the top of a window ; already built in thing

my_menu = Menu(root)
root.config(menu = my_menu)



root.mainloop()

##CREATING CLASSES OOP - instructor had this already typed out - class is basically like a template we can create objects with 
# class OneButton: #class name typically start with capital letter
#     def __init__(self,master): #initialize function to start, must always have self parameter first, and whatever premises we want after that, we refer to as master
#         frame = Frame(master) #a frame is created whenver we use this class
#         frame.pack()

#         self.printButton = Button(frame, text="Click me!", command=self.printMessage)
#         self.printButton.pack(side=LEFT)

#     def printMessage(self):
#         print("Congratulations, you CLASSY person.")

# button = OneButton(root) #we're feeding into this class: create a frame and button if pressed, print message ; master is the root



##LEFT RIGHT CLICK COUNTER
# left_counter=0
# right_counter=0

# def left_click(e):
#     global left_counter
#     left_counter+=1
#     left_label.config(text="Left clicks: {}".format(left_counter))

# def right_click(e):
#     global right_counter
#     right_counter+=1
#     right_label.config(text="Right_clicks: {}".format(right_counter))


# left_label=Label(root, text="Left clicks: {}".format(left_counter))
# right_label=Label(root, text="Right_clicks: {}".format(right_counter))

# left_button=Button(root, text="I'm left") 
# right_button=Button(root, text="I'm right")

# left_button.bind("<Button-1>", left_click)#button only works if you left click on it 
# right_button.bind("<Button-3>", right_click)# button only works if you right click on it



# left_button.pack()
# left_label.pack()
# right_button.pack()
# right_label.pack()



##LEFT AND RIGHT CLICK - isn't there a way to create multiple functions for just ONE BUTTON?
# def left_click(e):
#     print("You have left clicked!")

# def right_click(e):
#     print("You have right clicked!")


# left_button=Button(root, text="I'm left") 
# right_button=Button(root, text="I'm right")

# left_button.bind("<Button-1>", left_click)#button only works if you left click on it 
# right_button.bind("<Button-3>", right_click)# button only works if you right click on it

# left_button.pack()
# right_button.pack()


##CREATING A CLICK COUNTER
# counter=0 #start at 0 bc obviously the button hasn't been clicked

# def click_counter():
#     global counter #getting the counter variable into the function
#     counter+=1 #add 1 to the counter @event
#     button_counter.config(text=counter) #change within the label, text of the new counter

# button1=Button(root, text="Click Me", command=click_counter)
# button_counter=Label(root, text=counter)

# button1.pack()
# button_counter.pack()



##COMMON EVENT LABELS 

# def foo(e):
#     print("Working just fine!")


#root.bind("<Double-Button-1>", foo) #everytime you double click left button
#root.bind("<Return>", foo) # everytime the Enter key is pressed
#root.bind("a", foo) #everytime the "a" key is pressed, trigger foo
#root.bind("<Leave>", foo) #everytime the mouse leaves the window, trigger foo
#root.bind("<Enter>", foo) #everytime the mouse enters the window, trigger foo


##BINDING FUNCTIONS
#binding command is only when someone left clicks on a button
#bind does same but can be used for different widgets, in a root, frame, or a button, or a field - more powerful and versatile
#on event that key is pressed while in a frame
# def key_pressed(e):
#     print("I see you typing!")

# root.bind("<Key>", key_pressed)

# #left click on a button
# def button_clicked(e):
#     print("Great click!")

# button1 = Button(root, text="Click Me!")
# button1.bind("<Button-1>", button_clicked)
# button1.pack()


## MAKING CHECKBOXES
# check = Checkbutton(root)
# check2 = Checkbutton(root)
# check.grid(row=0, column=3,columnspan=2)
# check2.grid(row=0,column=5)


##ADDING ICON TO TITLE
#drawing your own icon - http://www.rw-designer.com/online_icon_maker.php
#iconbitmap
#.ico 


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

