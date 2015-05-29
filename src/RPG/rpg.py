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
# rpg.py was written for education purposes only
# It's developer/s decline all responsibility:
#   – in case the tool is used for malicious purposes or in any illegal context;
#   – in case the tool crashes your system or other systems;
#   - in case the tool causes any loss of data or personal information;
#
#
import string
import argparse
from Crypto.Random import random


class RandomPasswordGenerator(object):
    """ Random Password Generator (RPG) Securely generate a random password. """
    def __init__(self):
        self.ascii_lower = string.ascii_lowercase
        self.ascii_upper = string.ascii_uppercase
        self.special = string.punctuation
        self.digits = string.digits

    def ranpassgen(self, passlen, lower, upper, spec, dig):

        """ Constructs a random password using the provided parameters.

        :param passlen: the length of the password to be generated
        :param lower: use lower case characters in the password
        :param upper: use upper case characters in the password
        :param spec: use special characters in the password
        :param dig: use digits in the password
        :return: Returns randomly generated password
        """
        char_set = []

        if lower is True:
            char_set.append(self.ascii_lower)

        if upper is True:
            char_set.append(self.ascii_upper)

        if spec is True:
            char_set.append(self.special)

        if dig is True:
            char_set.append(self.digits)

        characters = "".join(char_set[:4])
        password = "".join(random.choice(characters) for i in range(int(passlen)))

        return password

if __name__ == '__main__':
    rpg = RandomPasswordGenerator()

    parser = argparse.ArgumentParser(usage="python3 rpg.py <passlen> [<args>]", add_help=False)

    req = parser.add_argument_group("Required")
    req.add_argument("passlen", help="Password Length.", type=int)

    group = parser.add_argument_group("Optional")
    group.add_argument("-h", "--help", help="Show this Help Message.", action="help")
    group.add_argument("-l", "--lower", help="Use lower case letters.", action="count")
    group.add_argument("-u", "--upper", help="Use upper case letters.", action="count")
    group.add_argument("-s", "--special", help="Use special characters (includes '-').", action="count")
    group.add_argument("-d", "--digits", help="Use numbers.", action="count")

    args = parser.parse_args()

    args_list = []
    arg_count = 0
    pass_len = args.passlen

    if args.lower is not None:
        args_list.append(True)
        arg_count += 1
    else:
        args_list.append(False)

    if args.upper is not None:
        args_list.append(True)
        arg_count += 1
    else:
        args_list.append(False)

    if args.special is not None:
        args_list.append(True)
        arg_count += 1
    else:
        args_list.append(False)

    if args.digits is not None:
        args_list.append(True)
        arg_count += 1
    else:
        args_list.append(False)

    if arg_count is not 0:
        print(rpg.ranpassgen(pass_len, args_list[0], args_list[1], args_list[2], args_list[3]))
    else:
        print(rpg.ranpassgen(pass_len, lower=True, upper=True, spec=True, dig=True))
