#!/usr/bin/env python3

#importing tkinter
from tkinter import *
#importing iptc for a more "elegant" code
import iptc
#imporing subprocess: allows you to spawn new processes, connect to input/output/error
#pipes and obtain their return codes
import subprocess

#creating a window - create a variable - Tk = tkinter
root = Tk()

#creating window title
root.title("Burn Care")

#window color and size
root.configure(bg="#4e4f50")
root.minsize(1200, 450)


#1-adding label - text or image - to main root window
#subtitle_label = Label(root, text = "CURRENT IPTABLE RULES", font="bold", fg="white", bg="#4e4f50")

#front facing GUI
global top_frame
top_frame = LabelFrame(root)
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
rule_header = Label(top_frame, text='  RULE No.  ', font="bold", bg="#4e4f50", fg="white")
rule_header.grid(row=0, column=0)
#input/output/fowrward column header and entry box
input_output_forward = Label(top_frame, text='  INPUT/OUTPUT/FORWARD  ', font="bold", fg ="white", bg="#4e4f50")
input_output_forward.grid(row=0, column=1)
#Source IP column header and entry box
source_ip = Label(top_frame, text='  SOURCE IP  ', font="bold", bg="#4e4f50", fg="white")
source_ip.grid(row=0, column=2)
#Source port column header and entry box
source_port = Label(top_frame, text='  SOURCE PORT  ', font="bold", bg="#4e4f50", fg="white")
source_port.grid(row=0, column=3)
#Destination IP column header and entry box
destination_ip = Label(top_frame, text='  DESTINATION IP  ', font="bold", bg="#4e4f50", fg="white")
destination_ip.grid(row=0, column=4)
#Destination port column header and entry box
destination_port = Label(top_frame, text='  DESTINATION PORT  ', font="bold", bg="#4e4f50", fg="white")
destination_port.grid(row=0, column=5)
#Protocol column header and drop down box
protocol = Label(top_frame, text='  PROTOCOL  ', font="bold", bg="#4e4f50", fg="white")
protocol.grid(row=0, column=6)
#Accept or Drop column header and drop down box
accept_or_drop_label = Label(top_frame, text='  ACCEPT OR DROP  ', font="bold", bg="#4e4f50", fg="white")
accept_or_drop_label.grid(row=0, column=7)


#Bottom frame containing the "Add Rule", "Remove Rule", and "Save" buttons
global bottom_frame
bottom_frame = LabelFrame(root, bg="#4e4f50")
bottom_frame.grid(row=1, column=0, sticky='se', padx=20, pady=20)

global bottom_center_frame
bottom_center_frame = LabelFrame(root, bg="#4e4f50")
bottom_center_frame.grid(row=1, column=0, sticky='s', padx=20, pady=20)
#Remove rule button
remove_rule_button = Button(bottom_center_frame, text='Remove Rule', font="bold", bg="#4e4f50", fg="white")
remove_rule_button.grid(row=0, column=1)
# remove_rule_button.bind("<Button-1>", Remove_Rules)   
# Remove Rule Entry Box
global remove_rule_entry_box
remove_rule_button.grid(row=0, column=1)
remove_rule_entry_box = Entry(bottom_center_frame, width=12, bg="#4e4f50", fg="white")
remove_rule_entry_box.grid(row=0, column=2, ipady=5)    
#Save button
save_button = Button(bottom_frame, text='Save', font="bold", bg="#4e4f50", fg="white")
save_button.grid(row=0, column=2)
# save_button.bind("<Button-1>", Save_Rules)
#Show Rules Button
show_current_rules = Button(bottom_frame, text='View Current Rules', font="bold", bg="#4e4f50", fg="white")
show_current_rules.grid(row=0, column=0)
# show_current_rules.bind("<Button-1>", Show_Rules)    
#Bottom left frame for "Delete All" button
global bottom_left_frame
bottom_left_frame = LabelFrame(root, bg="#4e4f50") 
bottom_left_frame.grid(row=1, column=0, sticky='sw', padx=20, pady=20)
# Delete All Rules button
delete_all_rules = Button(bottom_left_frame, text='Delete All', font="bold", bg="#4e4f50", fg="white")
delete_all_rules.grid(row=0, column=0)
# delete_all_rules.bind("<Button-1>", Remove_All_Rules)

#THIS PART IS CONFUSING AND NEEDS TO BE PICKED APART!
rule_counter=0
table_of_rules = []
row_count = 0
class App(object):
    #Function to create a new rule row
    def new_row(self):
        global rule_counter
        global table_of_rules
        global row_count
        rule_counter += 1 
        new_rule = Label(top_frame, text=rule_counter, font="bold", bg="#4e4f50", fg="white")
        new_rule.grid(column=0, ipady=10)
        
        global input_output_forward_options
        input_output_forward_options = StringVar()
        input_output_forward_options.set("INPUT")
        global input_output_forward_button
        input_output_forward_button = OptionMenu(top_frame, input_output_forward_options, "INPUT", "OUTPUT", "FORWARD")
        input_output_forward_button.config(bg="#4e4f50", fg="white", width=9)
        input_output_forward_button.grid(column=1)

        global source_ip_entry_box 
        source_ip_entry_box = Entry(top_frame, width=14)
        source_ip_entry_box.config(bg="#4e4f50", fg="white")
        source_ip_entry_box.grid(column=2)

        global source_port_entry_box 
        source_port_entry_box = Entry(top_frame, width=7)
        source_port_entry_box.config(bg="#4e4f50", fg="white")
        source_port_entry_box.grid(column=3)

        global destination_ip_entry_box 
        destination_ip_entry_box = Entry(top_frame, width=14)
        destination_ip_entry_box.config(bg="#4e4f50", fg="white")
        destination_ip_entry_box.grid(column=4)

        global destination_port_entry_box 
        destination_port_entry_box = Entry(top_frame, width=7)
        destination_port_entry_box.config(bg="#4e4f50", fg="white")
        destination_port_entry_box.grid(column=5)

        global protocol_options 
        protocol_options = StringVar()
        protocol_options.set("tcp")
        global protocol_button 
        protocol_button = OptionMenu(top_frame, protocol_options, "tcp", "udp", "icmp")
        protocol_button.config(bg="#4e4f50", fg="white", width=5)
        protocol_button.grid(column=6)

        global accept_or_drop_options
        accept_or_drop_options = StringVar()
        accept_or_drop_options.set("ACCEPT")
        global accept_or_drop_button 
        accept_or_drop_button = OptionMenu(top_frame, accept_or_drop_options, "ACCEPT", "DROP")
        accept_or_drop_button.config(bg="#4e4f50", fg="white", width=7)
        accept_or_drop_button.grid(column=7)

        self.num_rows += 1
        new_rule.grid(column=0, row=self.num_rows, sticky='WE')
        input_output_forward_button.grid(column=1, row=self.num_rows)
        source_ip_entry_box.grid(column=2, row=self.num_rows)
        source_port_entry_box.grid(column=3, row=self.num_rows)
        destination_ip_entry_box.grid(column=4, row=self.num_rows)
        destination_port_entry_box.grid(column=5, row=self.num_rows)
        protocol_button.grid(column=6, row=self.num_rows)
        accept_or_drop_button.grid(column=7, row=self.num_rows)
        row_count += 1

        global row_of_boxes
        # Dictionary to save placements of input on interface for a single row
        row_of_boxes = {}
        row_of_boxes = {'input_output_forward_options' : input_output_forward_options, 
                    'source_ip_entry_box' : source_ip_entry_box,
                    'destination_ip_entry_box' :  destination_ip_entry_box,
                    'protocol_options' : protocol_options,
                    'source_port_entry_box' : source_port_entry_box, 
                    'destination_port_entry_box' : destination_port_entry_box,
                    'accept_or_drop_options' : accept_or_drop_options}
        # Add row to table_of_rules list
        table_of_rules.append(row_of_boxes)
        #print(table_of_rules)

    #Function for linking new rows to the "Add Rule" button
    def __init__(self):
        self.num_rows = 1
        #Auto run function at start
        self.new_row()
        add_rule_button = Button(bottom_center_frame, text='New Rule', font="bold", bg="#4e4f50", fg="white", command=self.new_row)
        add_rule_button.grid(row=0, column=0)



#3 - command for the button click
def button():
    #4- .config makes a change to something - in this case, have the print show up in GUI, not command line
    #print("ipmebruh is a made-up command, duh.") - this just prints in command line
    ipmebruh_button.config(text="Refresh") #-> this just replaces button text
    #5- testing iptc code and having output display in GUI
    # table = iptc.Table(iptc.Table.FILTER)
    # print table.name
    
    #trying to print in main window once button cmd is called
    content_label = Label(root, text="ipmebruh isn't a real command, duh") #everytime button is hit, line will repeat
    content_label.grid()

#2-putting in a button, styling it, and fitting it with a command (just the name to call it)
ipmebruh_button = Button(root, text ="ipmebruh", fg="white", bg="#4e4f50", command=button)


#1-"calling" the label - default is center top
#subtitle_label.grid()

#2-calling the button - placing at bottom of window
ipmebruh_button.grid(sticky="S")

app = App()

#running window on continuous loop - bc standard window will only be open for a millisecond
root.mainloop()