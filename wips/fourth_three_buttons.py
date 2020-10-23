#!/usr/bin/env python3

import tkinter as tk
import subprocess
import iptc

rule_counter=0
table_of_rules = []
row_count = 0
window = tk.Tk()
window.title("Burncare")

subtitle_label = tk.Label(window, text = "CURRENT IPTABLE RULES", font="bold", fg="white", bg="#4e4f50")
subtitle_label.grid(row=0)
process = subprocess.Popen(["sudo iptables -L"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
current,stderr_current = process.communicate()
current_label = tk.Label(window, text=current,font="bold", fg="white", bg="#4e4f50")
current_label.grid(row=1)

class App(object):
    #GUI-----------------------------------------|
    

    global top_frame
    top_frame = tk.Frame(bg="#4e4f50")    
    top_frame.configure()
    top_frame.grid(row=2, column=0, sticky="nsew")

    top_frame.columnconfigure(0, weight=1)
    top_frame.columnconfigure(1, weight=1)
    top_frame.columnconfigure(2, weight=1)
    top_frame.columnconfigure(3, weight=1)
    top_frame.columnconfigure(4, weight=1)
    top_frame.columnconfigure(5, weight=1)
    top_frame.columnconfigure(6, weight=1)
    top_frame.columnconfigure(7, weight=1)
    top_frame.rowconfigure(2, weight=1)

    #Function for linking new rows to the "Add Rule" button
    def __init__(self):
        

        self.num_rows = 1
        #Auto run function at start
        self.new_row()
        add_rule_button = tk.Button(bottom_center_frame, text='New Rule', font="bold", bg="#4e4f50", fg="white", command=self.new_row)
        add_rule_button.grid(row=0, column=0)
   
        #Update button
        update_button = tk.Button(bottom_center_frame, text="Update", command = self.button_press, font="bold", bg="#4e4f50", fg="white")
        update_button.grid(row=0, column=2)


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
    accept_or_drop_label = tk.Label(top_frame, text='  ACCEPT/DROP  ', font="bold", bg="#4e4f50", fg="white")
    accept_or_drop_label.grid(row=0, column=7)

 #Function to create a new rule row
    def new_row(self):
        global rule_counter
        global table_of_rules
        global row_count
        #COLUMN0
        rule_counter += 1 
        new_rule = tk.Label(top_frame, text=rule_counter, font="bold", bg="#4e4f50", fg="white")
        new_rule.grid(column=0, ipady=10)
        #COLUMN1
        global input_output_forward_options
        input_output_forward_options = tk.StringVar()
        input_output_forward_options.set("INPUT")
        global input_output_forward_button
        input_output_forward_button = tk.OptionMenu(top_frame, input_output_forward_options, "INPUT", "OUTPUT", "FORWARD")
        input_output_forward_button.config(bg="#4e4f50", fg="white", width=14)
        input_output_forward_button.grid(column=1)
        #COLUMN2
        global source_ip_entry
        source_ip_entry = tk.Entry(top_frame, width=14)
        source_ip_entry.config(bg="#4e4f50", fg="white")
        source_ip_entry.grid(column=2)
        #COLUMN3
        global source_port_entry
        source_port_entry = tk.Entry(top_frame, width=7)
        source_port_entry.config(bg="#4e4f50", fg="white")
        source_port_entry.grid(column=3)
        #COLUMN4
        global dest_ip_entry
        dest_ip_entry= tk.Entry(top_frame, width=14)
        dest_ip_entry.config(bg="#4e4f50", fg="white")
        dest_ip_entry.grid(column=4)
        #COLUMN5
        global dest_port_entry
        dest_port_entry = tk.Entry(top_frame, width=7)
        dest_port_entry.config(bg="#4e4f50", fg="white")
        dest_port_entry.grid(column=5)
        #COLUMN6
        global protocol_options 
        protocol_options = tk.StringVar()
        protocol_options.set("tcp")
        global protocol_button 
        protocol_button = tk.OptionMenu(top_frame, protocol_options, "tcp", "udp", "icmp")
        protocol_button.config(bg="#4e4f50", fg="white", width=7)
        protocol_button.grid(column=6)
        #COLUMN7
        global accept_or_drop_options
        accept_or_drop_options = tk.StringVar()
        accept_or_drop_options.set("ACCEPT")
        global accept_or_drop_button 
        accept_or_drop_button = tk.OptionMenu(top_frame, accept_or_drop_options, "ACCEPT", "DROP")
        accept_or_drop_button.config(bg="#4e4f50", fg="white", width=7)
        accept_or_drop_button.grid(column=7)

        self.num_rows += 1
        new_rule.grid(column=0, row=self.num_rows, sticky='WE')
        input_output_forward_button.grid(column=1, row=self.num_rows)
        source_ip_entry.grid(column=2, row=self.num_rows)
        source_port_entry.grid(column=3, row=self.num_rows)
        dest_ip_entry.grid(column=4, row=self.num_rows)
        dest_port_entry.grid(column=5, row=self.num_rows)
        protocol_button.grid(column=6, row=self.num_rows)
        accept_or_drop_button.grid(column=7, row=self.num_rows)
        row_count += 1

        global row_of_boxes
        # Dictionary to save placements of input on interface for a single row
        row_of_boxes = {}
        row_of_boxes = {'input_output_forward_button' : input_output_forward_button, 
                    'source_ip_entry' : source_ip_entry,
                    'dest_ip_entry' :  dest_ip_entry,
                    'protocol_button' : protocol_button,
                    'source_port_entry' : source_port_entry, 
                    'dest_port_entry' : dest_port_entry,
                    'accept_or_drop_button' : accept_or_drop_button}
        # Add row to table_of_rules list
        table_of_rules.append(row_of_boxes)
        #print(table_of_rules)

    
    #FUNCTION FOR UPDATE BUTTON---------|
    def button_press(self):
        global row_of_boxes
        # Dictionary to save placements of input on interface for a single row
        row_of_boxes = {}
        row_of_boxes = {'input_output_forward_options' : input_output_forward_options, 
                    'source_ip_entry' : source_ip_entry,
                    'dest_ip_entry' :  dest_ip_entry,
                    'protocol_options' : protocol_options,
                    'source_port_entry' : source_port_entry, 
                    'dest_port_entry' : dest_port_entry,
                    'accept_or_drop_options' : accept_or_drop_options}
        # Add row to table_of_rules list
        # table_of_rules.append(row_of_boxes)
        rule={}
        chain_box=''
        chain_box=row_of_boxes['protocol_options']
        rule['protocol']=chain_box.get()        
        chain_box=row_of_boxes['input_output_forward_options'] 
        rule['input_output_forward']=chain_box.get()
        chain_box=row_of_boxes['source_ip_entry']
        rule['source_ip']=chain_box.get()
        chain_box=row_of_boxes['source_port_entry']
        rule['source_port']=chain_box.get()
        chain_box=row_of_boxes['dest_ip_entry']
        rule['dest_ip']=chain_box.get()
        chain_box=row_of_boxes['dest_port_entry']
        rule['dest_port']=chain_box.get()

        chain_box=row_of_boxes['accept_or_drop_options']
        rule['accept_or_drop']=chain_box.get()
        #print(rule['protocol']) #------>SANITY CHECK
        # print(f"sudo iptables -A {rule['input_output_forward']} -p {rule['protocol']} -s {rule['source_ip']} --sport {rule['source_port']} -d {rule['dest_ip']} --dport {rule['dest_port']} -j {rule['accept_or_drop']}")
        
        process = subprocess.Popen([f"sudo iptables -A {rule['input_output_forward']} -p {rule['protocol']} -s {rule['source_ip']} --sport {rule['source_port']} -d {rule['dest_ip']} --dport {rule['dest_port']} -j {rule['accept_or_drop']}"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        output, stderr_output = process.communicate()

        global current_label
        current_label.destroy()
        updated_process = subprocess.Popen(["sudo iptables -L"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        current,stderr_current = updated_process.communicate()
        current_label = tk.Label(window, text=current,font="bold", fg="white", bg="#4e4f50")
        current_label.grid(row=1)

        #print(output)
        #---END OF FUNCTION FOR UPDATE BUTTON-------|

    # --------------DELETE ALL FUNCTION --------------|    
    def delete_all():
        # table=iptc.Table(iptc.Table.FILTER)
        # table.flush()
        # table.refresh() 
        global current_label
        current_label.destroy()
        cleared_process = subprocess.Popen(["sudo iptables -F && sudo iptables -L"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        current,stderr_current = cleared_process.communicate()
        current_label = tk.Label(window, text=current,font="bold", fg="white", bg="#4e4f50")
        current_label.grid(row=1)

    #----------END OF DELETE ALL FUNCTION ----------------|

    #BUTTONS FRAMES FOR BUTTONS
   #Bottom frame containing the "Add Rule", "Remove Rule", and "Save" buttons
    global bottom_frame
    bottom_frame = tk.LabelFrame(window, bg="#4e4f50")
    bottom_frame.grid(row=3, column=0, sticky='se', padx=20, pady=20)

    global bottom_center_frame
    bottom_center_frame = tk.LabelFrame(window, bg="#4e4f50")
    bottom_center_frame.grid(row=3, column=0, sticky='s', padx=20, pady=20)
    # #Remove rule button
    # remove_rule_button = Button(bottom_center_frame, text='Remove Rule', font="bold", bg="#353535", fg="#80FF00")
    # remove_rule_button.grid(row=0, column=1)
    # remove_rule_button.bind("<Button-1>", Remove_Rules)   
    # # Remove Rule Entry Box
    # global remove_rule_entry_box
    # remove_rule_button.grid(row=0, column=1)
    # remove_rule_entry_box = Entry(bottom_center_frame, width=12, bg="#353535", fg="#80FF00")
    # remove_rule_entry_box.grid(row=0, column=2, ipady=5)    

    #delete all button
    delete_all=tk.Button(bottom_frame, text='Delete All', font="bold", bg="#4e4f50", fg="white", command=delete_all)
    delete_all.grid(row=0, column=0)


    # global bottom_left_frame
    # bottom_left_frame = LabelFrame(root, bg="#353535") 
    # bottom_left_frame.grid(row=1, column=0, sticky='sw', padx=20, pady=20)
    # # Delete All Rules button
    # delete_all_rules = Button(bottom_left_frame, text='Delete All', font="bold", bg="#353535", fg="#80FF00")
    # delete_all_rules.grid(row=0, column=0)
    # delete_all_rules.bind("<Button-1>", Remove_All_Rules)

    # --------------end of GUI---------------------|
    
   

   

app = App()
window.mainloop()


