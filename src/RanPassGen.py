#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A basic python script to generate random password using pycrypto and strings modules.
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
# -------------------------------------------------------------------------------------
# Random Password Generator was written for education purposes only
# It's developer/s decline all responsibility:
#   – in case the tool is used for malicious purposes or in any illegal context;
#   – in case the tool crashes your system or other systems;
#   - in case the tool causes any loss of data or personal information;
# -------------------------------------------------------------------------------------
# * pycrypto is not included with python and will need to be downloaded
#   - pip install pycrypto
#
#
import string
from Crypto.Random import random

print(""" "Random Password Generator" will use:
        "Upper Letters"
        "Lower Letters"
        "Numbers"
        "Underline"
        "Minus"
        "Special Characters"
Please Note: Some websites may impose restrictions on use of certain special characters.
        """)

def ranpassgen():
    char = input("Enter length >> ")
    bits = int(char) * 8
    print("Generating a random password %s characters long or %s bits" % (char, bits))
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(characters) for x in range(int(char)))
    print("Your random password is: ", password)

ranpassgen()

