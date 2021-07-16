
#!/bin/python3

import sys
import socket
import subprocess
from datetime import datetime as dt

#clear the screen
subprocess.call('clear', shell=True)

#ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer) #returns hostname of the machine

	
#Add pretty banner
print("-" * 40)
print("Please wait, scanning remote host", remoteServerIP)
print("scanner by: Gbolahan Olaleru (klattasium)")
print("-" * 40)


t1 = dt.now() #check time the scan started

#using range function to specify ports it will scan all ports between 1 and 1024)
#also put in some error handling for catching errors
try:
	for port in range(1,1024):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port)) #returns error indicator
		print("Checking connection {}".format(port))
		if result == 0:
			print("Port {}:  open".format(port))
		sock.close
		
except socket.error:
	print("Couldn't connect to server")
	sys.exit()
	
except keyboardInterrupt:
	print("You pressed CTRL + C.")
	sys.exit()
	
except socker.gaierror:
	print("Hostname could not be resolved. Exit")
	sys.exit()

#checking Time Again
t2 = dt.now()

#Difference between time, to see the time elapsed during scan
total = t2 - t1

#printting the information to screen 
print("Scanning Completed in: ", total)