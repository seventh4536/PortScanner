from http.client import RemoteDisconnected
import socket
import subprocess   


def LocalNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]

print ("Found following IP for LocalHost.")
print (LocalNetworkIp())
print ("Scanning for open ports now...")

 
ip = socket.gethostbyname (socket.gethostname()) 
 
for port in range(65535):      
 
    try:
  
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
 
        serv.bind((ip,port)) 
            
    except:
 
        print('[OPEN] Port open :',port,) 
 
    serv.close()
    
