#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
import iptc

def say_hi(e):
	table = iptc.Table(iptc.Table.FILTER)
	# table.create_chain("testchain")
	# rule = iptc.Rule()
	# rule.protocol = "tcp"
	# rule.target = iptc.Target(rule, "ACCEPT")
	# match = iptc.Match(rule, "state")
	# chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
	# match.state = "RELATED,ESTABLISHED"
	# rule.add_match(match)
	
	for chain in table.chains:
		# chain.insert_rule(rule)
		print("=" * 30)
		print("Chain", chain.name)
		print("Num_Rules", len(chain.rules))
		for rule in chain.rules:
			print("*" * 30)
			print("Rule",)
			print("proto:\t", rule.protocol)



win = tk.Tk()
win.title("Testing, Testing, 1, 2, 3...")
win.geometry('300x300')
input_str = tk.StringVar()
label = ttk.Label(win, text="Hello, world!!")
button = ttk.Button(win, text="Hola")
button.bind('<Button-1>', say_hi)
input = ttk.Entry(win, textvariable=input_str)
input.pack()
button.pack()
label.pack()

win.mainloop()