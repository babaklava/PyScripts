#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A basic python script that scrapes a site's URLs
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
# URLfinder.py was written for education purposes only
# It's developer/s decline all responsibility:
#   – in case the tool is used for malicious purposes or in any illegal context;
#   – in case the tool crashes your system or other systems.
#
#
import re
import urllib.request
import urllib.error


def urlfinder():
    try:
        usrinput = input("Enter URL to start scraping >> ")
        print("Looking for URLs in", usrinput)
        website = urllib.request.urlopen(usrinput).read()
        links = re.findall(r'(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)[\'"]?(?:[^\'" >]+)', str(website))
        for link in links:
            print(link)
    except ValueError:
        print("*** Looks like a typo, please try again. ***\n")
        return urlfinder()
    except urllib.error.URLError:
        print("*** Looks like a typo, please try again. ***\n")
        return urlfinder()

urlfinder()
