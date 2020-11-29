#!/usr/bin/env python
#coding=utf-8

import socket
import time
import os
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

HOST = ip
PORT = 2332
cmd = "ip addr|grep " + str(ip)
a = os.popen(cmd).read()
network_card = a.split(' ')[-1].split('\n')[0]
#Configure socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    request = conn.recv(1024)
    method = request.split(' ')[0]
    src  = request.split(' ')[1]

    print 'Connect by: ', addr

    if method == 'GET':
        if src.split('/')[1] == 'latency':
            print str(src.split('/')[2])
            print str(network_card)
            cmd1 = "tc qdisc add dev " + str(network_card) + " root netem delay " + str(src.split('/')[2])
            cmd2 = "tc qdisc del dev " + str(network_card) + " root netem"
            #print cmd2
            #print cmd1
            tmp = os.popen(cmd2)  
            time.sleep(1) 
            tmp = os.popen(cmd1)   
        else:
            continue
    
    else:
        continue

    conn.sendall(b'ok')
    
    conn.close()
