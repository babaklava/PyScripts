#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A VERY basic python script to rapidly ping hosts on the network using multithreading.
"""

import threading
from queue import Queue
import sys
import subprocess
import ipaddress
import time

print_lock = threading.Lock()

network = []

# get input from user
try:
    host = input("\nEnter IP/Mask: ")
    network = ipaddress.IPv4Network(host)
except ValueError:
    print("Error the IP Address/Netmask is invalid for IPv4:", host)
except KeyboardInterrupt:
    sys.exit(0)

# count how many IPs were pinged and how many responded
addr_pinged = 0
addr_resp = 0


# the actual function to ping the host from the queue
def sping(ip):
    status, result = subprocess.getstatusoutput("ping -c1 -w1 " + str(ip))
    global addr_pinged
    addr_pinged += 1
    if status == 0:
        global addr_resp
        addr_resp += 1
        with print_lock:
            print("Host", ip, "is up")


# instruction for each worker
def threader():
    while True:
        ip = q.get()
        sping(ip)
        q.task_done()

# setting up empty queue
q = Queue()

# Creating threads, by changing the number in range you will increase amount of threads
for x in range(256):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()

# building the queue
for ip in network:
    q.put(ip)

q.join()

time = str(time.time()-start)
print("Sping done:", addr_pinged, "IP address (", addr_resp, "host up )", "entire job took -", str(time[:3]), "sec")