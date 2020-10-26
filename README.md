# Burncare

A GUI for iptables that manages firewallrules in Linux, using Python programming language. Constructed with Tkinter.

# Prerequisites
![linux prerequisites gif](https://github.com/knifane/burn_care/blob/main/images/Linux%20prereqs_1.mp4)

 - Python 3
	- sudo apt install python3.6
 - Update Linux packages (note: may take a long time, depending on the current state of your system)
	- apt update -y && apt upgrade -y && apt dist-upgrade
 - Python Iptables
	- pip3 install --upgrade python-iptables
- Please note in order to run Burncare, you must have sudo privileges.

# Installation
		 - cd /opt
		 - git clone https://github.com/knifane/burn_care.git

# Create a symbolic link
		- cd /bin
		- ln -s /opt/burn_care/burncare.py Burncare
 
