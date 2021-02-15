from socket import *
import hashlib
Server = "vayu.iitd.ac.in"
server_port = 80
clientsocket = socket(AF_INET, SOCK_STREAM) 
clientsocket.connect((Server,server_port))
path  = "GET /big.txt HTTP/1.1\r\nHost: vayu.iitd.ac.in\r\nConnection: keep-alive\r\nRange: bytes=0-999\r\n\r\nr\n\r\n"

f = open("c:/Users/kddha/Desktop/sem/sem5/col334/ass3.1.txt",'w')
state0 = True #before \r
state1 = False #after \r
state2 = False  #after \r\n
state3 = False     #after \r\n\r
state4 = False      #after \r\n\r\n
size = 6488666
initial = 0
while(initial<size):
    final = initial+100
    if(size-initial<100):
        final = size
    clientsocket.send((f"GET /big.txt HTTP/1.1\r\nHost: vayu.iitd.ac.in\r\nConnection: keep-alive\r\nRange: bytes={initial}-{final}\r\n\r\nr\n\r\n").encode())
    initial = initial + 1000
    l = clientsocket.recv(1000)
    char = l.decode()
    i = 0
    while(i<len(char)):
        
        if(state0==True and char[i] == "\r"):
            #print("state 0-1" )
            state0 = False
            state1 = True
            i= i+1
        elif(state1==True and char[i] == "\n"):
            #print("state 1-2" )
            state1 = False
            state2 = True
            i= i+1
        elif(state2==True and char[i] == "\r"):
            #print("state 2-3" )
            state2 = False
            state3 = True
            
            if(char[i+1] == "\n"):
                #print("state 3-4" )
                state3 = False
                state4 = True
                i = i+2
            else:
                #print("state 3-0" )
                state0  = True
                state3  = False
        elif(state4==True):
            f.write(char[i])
            #print(char)
            i = i+1
        else:
            #print("state x-0" )
            state0 = True
            state1 = False
            state2 = False
            state3 = False
            State4 = False
            i = i+1
clientsocket.close()
f.close()
checksum = hashlib.md5((open("c:/Users/kddha/Desktop/sem/sem5/col334/ass3.1.txt",'r').read()).encode()).hexdigest()
if(checksum=="70a4b9f4707d258f559f91615297a3ec"):
    print("mathched")
else:
    print(checksum)
    print("not matched")