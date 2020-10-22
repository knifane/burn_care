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
num_header=Label(root, text="RULE No.")
iof_header=Label(root, text="INPUT/OUTPUT/FORWARD")
src_ip=Label(root, text="SOURCE IP")
src_port=Label(root, text="SOURCE PORT")
dest_ip=Label(root, text="DESTINATION IP")
dest_port=Label(root, text="DESTINATION PORT")
proto=Label(root, text="PROTOCOL")
accdr=Label(root, text="ACCEPT/DROP")


#1st row of entry
num_entry=Entry(root)
iof_entry=Entry(root)
src_ip_entry=Entry(root)
src_port_entry=Entry(root)
dest_ip_entry=Entry(root)
dest_port_entry=Entry(root)
proto_entry=Entry(root)
accdr_entry=Entry(root)



# .grid and placing by row and column
num_header.grid(row=0, column=0)
iof_header.grid(row=0, column=1)
src_ip.grid(row=0, column=2)
src_port.grid(row=0, column=3)
dest_ip.grid(row=0, column=4)
dest_port.grid(row=0, column=5)
proto.grid(row=0, column=6)
accdr.grid(row=0, column=7)
num_entry.grid(row=1, column=0)
iof_entry.grid(row=1, column=1)
src_ip_entry.grid(row=1, column=2)
src_port_entry.grid(row=1, column=3)
dest_ip_entry.grid(row=1, column=4)
dest_port_entry.grid(row=1, column=5)
proto_entry.grid(row=1, column=6)
accdr_entry.grid(row=1, column=7)





root.mainloop()