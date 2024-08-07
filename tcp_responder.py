#!/usr/bin/python3

import socket
import struct
from pprint import pprint

SO_ORIGINAL_DST = 80
SOCKADDR_MIN = 16

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 65535))
s.listen(10)

while True:
    csock, caddr = s.accept()
    csockaddr_in = csock.getsockopt(socket.SOL_IP,SO_ORIGINAL_DST, SOCKADDR_MIN)
    (proto, port, a,b,c,d) = struct.unpack('!HHBBBB', csockaddr_in[:8])
    
    ip = " "
    if socket.htons(proto) == socket.AF_INET : 
          ip = '%d.%d.%d.%d ' % (a,b,c,d) 

    try:
        smallmsg = "Hello {} ({}) on TCP port {} [76bf2bbaa238]\n".format(caddr[0],socket.getnameinfo(caddr,0)[0],port)
        print(smallmsg.strip(),flush=True)
        csock.send(smallmsg.encode())
        csock.shutdown(socket.SHUT_RDWR)
        csock.close()
    except socket.error:
        pass

