#!/usr/bin/env python3

import tkinter as tk

#FUNCTIONS
def button_press():
    global row_of_boxes
    # Dictionary to save placements of input on interface for a single row
    row_of_boxes = {}
    row_of_boxes = {'input_output_forward_entry' : input_output_forward_entry, 
                'source_ip_entry' : source_ip_entry,
                'dest_ip_entry' :  dest_ip_entry,
                'protocol_entry' : protocol_entry,
                'source_port_entry' : source_port_entry, 
                'dest_port_entry' : dest_port_entry,
                'accept_or_drop_entry' : accept_or_drop_entry}
    # Add row to table_of_rules list
    # table_of_rules.append(row_of_boxes)
    rule={}
    chain_box=''
    chain_box=row_of_boxes['input_output_forward_entry'] 
    rule['input_output_forward']=chain_box.get()
    chain_box=row_of_boxes['source_ip_entry']
    rule['source_ip']=chain_box.get()
    chain_box=row_of_boxes['source_port_entry']
    rule['source_port']=chain_box.get()
    chain_box=row_of_boxes['dest_ip_entry']
    rule['dest_ip']=chain_box.get()
    chain_box=row_of_boxes['dest_port_entry']
    rule['dest_port']=chain_box.get()
    chain_box=row_of_boxes['protocol_entry']
    rule['protocol']=chain_box.get()
    chain_box=row_of_boxes['accept_or_drop_entry']
    rule['accept_or_drop']=chain_box.get()
    print(rule)

#GUI
window = tk.Tk()
window.title("SEVEN BUTTONS!!")

global top_frame
top_frame = tk.Frame()
top_frame.grid(row=0, column=0, sticky="nsew")
top_frame.configure(bg="#4e4f50")
top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
top_frame.columnconfigure(2, weight=1)
top_frame.columnconfigure(3, weight=1)
top_frame.columnconfigure(4, weight=1)
top_frame.columnconfigure(5, weight=1)
top_frame.columnconfigure(6, weight=1)
top_frame.columnconfigure(7, weight=1)
top_frame.rowconfigure(2, weight=1)

#rule num column header and enty box
rule_header = tk.Label(top_frame, text='  RULE No.  ', font="bold", bg="#4e4f50", fg="white")
rule_header.grid(row=0, column=0)
#input/output/fowrward column header and entry box
input_output_forward = tk.Label(top_frame, text='  INPUT/OUTPUT/FORWARD  ', font="bold", fg ="white", bg="#4e4f50")
input_output_forward.grid(row=0, column=1)
#Source IP column header and entry box
source_ip = tk.Label(top_frame, text='  SOURCE IP  ', font="bold", bg="#4e4f50", fg="white")
source_ip.grid(row=0, column=2)
#Source port column header and entry box
source_port = tk.Label(top_frame, text='  SOURCE PORT  ', font="bold", bg="#4e4f50", fg="white")
source_port.grid(row=0, column=3)
#Destination IP column header and entry box
destination_ip = tk.Label(top_frame, text='  DESTINATION IP  ', font="bold", bg="#4e4f50", fg="white")
destination_ip.grid(row=0, column=4)
#Destination port column header and entry box
destination_port = tk.Label(top_frame, text='  DESTINATION PORT  ', font="bold", bg="#4e4f50", fg="white")
destination_port.grid(row=0, column=5)
#Protocol column header and drop down box
protocol = tk.Label(top_frame, text='  PROTOCOL  ', font="bold", bg="#4e4f50", fg="white")
protocol.grid(row=0, column=6)
#Accept or Drop column header and drop down box
accept_or_drop_label = tk.Label(top_frame, text='  ACCEPT OR DROP  ', font="bold", bg="#4e4f50", fg="white")
accept_or_drop_label.grid(row=0, column=7)

button = tk.Button(window, text="Print Me!", command = button_press)

#COLUMN0
rule_counter=1
new_rule=tk.Label(top_frame, text=rule_counter)
new_rule.grid(row=1, column=0,ipady=10)
#COLUMN1
input_output_forward_entry=tk.Entry(top_frame, width=14)
input_output_forward_entry.grid(row=1,column=1)
#COLUMN2
source_ip_entry=tk.Entry(top_frame, width=14)
source_ip_entry.grid(row=1,column=2)
#COLUMN3
source_port_entry=tk.Entry(top_frame, width=7)
source_port_entry.grid(row=1,column=3)
#COLUMN4
dest_ip_entry=tk.Entry(top_frame, width=14)
dest_ip_entry.grid(row=1,column=4)
#COLUMN5
dest_port_entry=tk.Entry(top_frame, width=7)
dest_port_entry.grid(row=1,column=5)
#COLUMN6
protocol_entry=tk.Entry(top_frame, width=7)
protocol_entry.grid(row=1,column=6)
#COLUMN7
accept_or_drop_entry=tk.Entry(top_frame, width=7)
accept_or_drop_entry.grid(row=1,column=7)



button.grid()


window.mainloop()