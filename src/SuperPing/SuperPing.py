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
# SuperPing.py was written for education purposes only
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


class SuperPing(object):
    def __init__(self):
        # count how many IPs were pinged and how many responded
        self.addr_resp = 0
        self.addr_pinged = 0
        # Set a print lock
        self.print_lock = threading.Lock()
        # setting up empty queue
        self.q = Queue()

    def main(self, netip):
        import time

        # create a list that holds all IPs to be pinged
        network = []

        # verify user input
        try:
            network = ipaddress.IPv4Network(netip)
        except ValueError:
            print("Error the IP Address/Netmask is invalid for IPv4:", netip)
        except KeyboardInterrupt:
            sys.exit(0)

        # Creating threads (by changing the number in range you will increase amount of threads)
        for i in range(256):
            t = threading.Thread(target=self.threader)
            t.daemon = True
            t.start()

        self.start = time.time()

        # building the queue
        for ip in network:
            self.q.put(ip)

        self.q.join()

        time = str(time.time() - self.start)
        print("SuperPing finished:", self.addr_pinged, "IP address pinged (", self.addr_resp, "responded )", "entire job took -",
              str(time[:3]), "sec")

    # the actual function to ping the host from the queue
    def sping(self, ip):
        status, result = subprocess.getstatusoutput("ping -c1 -w1 " + str(ip))
        self.addr_pinged += 1
        if status == 0:
            self.addr_resp += 1
            with self.print_lock:
                print("Host", ip, "responded")

    # instruction for each worker
    def threader(self):
        while True:
            ip = self.q.get()
            self.sping(ip)
            self.q.task_done()

if __name__ == '__main__':
    sping = SuperPing()
    ip_input = input("Enter (IP Address/Mask): ")
    sping.main(ip_input)