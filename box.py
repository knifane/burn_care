#!/usr/bin/env python3
# POC : create a GUI that will auto-populate with the current IPtables rules
# maybe after pressing a button

#importing tkinter
from tkinter import *
#importing subprocess: allows you to spawn new processes, connect to input/output/ error pipes
#and obtain their return codes
import subprocess

#creating a window - create a variable - Tk = tkinter
root = Tk()

#creating window title
root.title("Burn Care")

#window color and size
root.configure(bg="#4e4f50")
root.minsize(1200, 450)


#1-adding label - text or image - to main root window
subtitle_label = Label(root, text = "CURRENT IPTABLE RULES", font="bold", fg="white", bg="#4e4f50")

#3 - command for the button click
def button():
    #.config makes a change to something - in this case, have the print show up in GUI, not command line
    #print("ipmebruh is a made-up command, duh.") - this just prints in command line
    ipmebruh_button.config(text="Refresh") #-> this just replaces button text
    #creating subprocess variable to run command and print output in GUI
    process = subprocess.Popen(["sudo iptables -L"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    output,stderr_ouput = process.communicate()
    #print ('>', output)
    #result['text']= output.decode('utf-8') -> unncessary
    #trying to print in main window once button cmd is called
    content_label = Label(root, text=output) #everytime button is hit, line will repeat
    #result.pack() -> unnecessary
    content_label.pack()

#2-putting in a button, styling it, and fitting it with a command (just the name to call it)
ipmebruh_button = Button(root, text ="ipmebruh", fg="white", bg="#4e4f50", command=button)


#1-"calling" the label - default is center top
subtitle_label.pack()

#2-calling the button - placing at bottom of window
ipmebruh_button.pack(side=BOTTOM)








#running window on continuous loop - bc standard window will only be open for a millisecond
root.mainloop()
