# Burncare

A GUI for iptables that manages firewallrules in Linux, using Python programming language. Constructed with Tkinter.

# Prerequisites

 - Python 3
		 - sudo apt install python3.6
 - Update Linux packages
		 - apt update -y && apt upgrade -y && apt dist-upgrade
 - Python Iptables
		 - ip3 install --upgrade python-iptables

# Installation
		 - cd /opt
		 - git clone https://github.com/knifane/burn_care.git

# Create a symbolic link
		- cd /bin
		- ln -s /opt/burn_care/burncare.py Burncare
 
