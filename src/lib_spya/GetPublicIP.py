#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A basic python script that goes out to dyndns.org and gets your Public IP Address
# Copyright (C) 2015  babaklava
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
# GetPublicIP.py was written for education purposes only
# It's developer/s decline all responsibility:
#   – in case the tool is used for malicious purposes or in any illegal context;
#   – in case the tool crashes your system or other systems.
#
#

import urllib.request
import urllib.error
import re
import sys


sites = ['http://checkip.dyndns.com/', 'http://whatismyipaddress.com/ip-lookup/', 'http://ip-lookup.net/']

public_ip = []


def getpublic():
    for site in sites:
        try:
            print("Checking with %s" % site)
            request = urllib.request.urlopen(site, timeout=3).read()
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                print("ERROR!", e.reason)
            elif hasattr(e, "code"):
                print("ERROR!", e.code)
        except ConnectionResetError:
            print("ERROR! Connection was reset, trying next site.")
            continue
        except ValueError:
            print("ERROR! Malformed URL, please try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
        else:
            result = re.findall(r'(?:\d{1,3})\.(?:\d{1,3})\.(?:\d{1,3})\.(?:\d{1,3})', str(request))
            for ip in result:
                if ip not in public_ip:
                    public_ip.append(ip)
                    print("Your Public IP Address is: ", public_ip)
                    sys.exit(0)

getpublic()
