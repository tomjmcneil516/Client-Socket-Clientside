import socket
import sys

lshostname = socket.gethostbyname(sys.argv[1])
lsport = int(sys.argv[2])

HNS_file =  open("PROJ2-HNS.txt", 'r')      
RESOLVED_file = open("RESOLVED.txt", 'w+')

for word in HNS_file:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    domain_name = word.rstrip().lower()  

    cs.connect((lshostname, lsport))
    cs.sendall(domain_name.encode('utf-8'))
    try:
        data = cs.recv(4096)
        RESOLVED_file.write(data.decode('utf-8') + "\n")
    except :
        print("timeout")
    
HNS_file.close()
RESOLVED_file.close()

    
        


