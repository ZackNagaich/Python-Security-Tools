#!/usr/bin/python
import os
import socket


host = "10.0.2.15"


#Create socket and bind to public interface
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP
    

sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)

sniffer.bind((host,0))

#Include the IP headers in capture
sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

#IF windows, turn on promiscuous mode 
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

print sniffer.recvfrom(65565)

#Turn of promiscuous mode if on windows
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
    