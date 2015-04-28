#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A basic python script to rapidly ping hosts on the network using multithreading.
#     Copyright (C) 2015  babaklava
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------
# Sping was written for education purposes only
# It's developer/s decline all responsibility:
#	– in case the tool is used for malicious purposes or in any illegal context;
#	– in case the tool crashes your system or other systems.
#
#
import threading
from queue import Queue
import sys
import subprocess
import ipaddress
import time

# Set a print lock
print_lock = threading.Lock()

# create a list that holds all IPs to be pinged
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