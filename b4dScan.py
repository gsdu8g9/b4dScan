#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
______  _____ ___________________
___  /_ __  // /______  /__  ___/_____________ ________ ®
__  __ \_  // /__  __  / _____ \ _  ___/_  __ `/__  __ \
_  /_/ //__  __// /_/ /  ____/ / / /__  / /_/ / _  / / /
/_.___/   /_/   \__,_/   /____/  \___/  \__,_/  /_/ /_/   - v0.1

This is a simple port scanner made in python 3.3
over 'Tor' proxy socks5 - module required PySocks

Easy step to install required module is, type in the Terminal:

    :$ pip3 install PySocks

or download manually from here http://sourceforge.net/projects/pysocks/


    Author: b4d_tR1p - (b4d_tR1p@me.com)
    GitHub: https://github.com/b4dtR1p/b4dScan


    Copyright® 2014 Alessandro Pucci - @b4d_tR1p

    GitHub: https://github.com/b4dtR1p/b4dScan

Date  : January 2014
Licence : GPL v3 or any later version

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import print_function

__author__ = 'b4d_tR1p - (b4d_tR1p@me.com)'
__version__ = '0.1'
__licence__ = 'GPL-v3'

import socket, socks, sys
from datetime import datetime

# Python 3 compatibility hack

if sys.version_info[:2] >= (3, 0):
  import urllib.request
  user_input = input
  urllib = urllib.request.urlopen


else:
  import urllib2
  from urllib2 import urlopen
  user_input = raw_input
  urllib = urllib2.urlopen


ini = datetime.now()

class b4dScan():

	def __init__(self, host=None):
		self.host = host

	def Target(self, host=None):
		self.host = str(user_input('Enter a remote host name here: '))
		return host

	def Scan(self, tor):
		host = self.host
		for port in range(1, 1024):
			if tor == 1:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050, True)
				socket.socket = socks.socksocket
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.5)
			result = sock.connect_ex((host, port))
			if result == 0:
				print ('Port {}: \t Open'.format(port) + ' \t Service: \t' + socket.getservbyport(port))
				return port
			sock.close()

	def HttpRequest(self, tor):
		if tor == 1:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050, True)
			socket.socket = socks.socksocket
		host = ('http://www.' + self.host)
		r = urllib(host)
		print (r.info())
		return r.info()
		print (r.getcode())
		return r.getcode()

fin = datetime.now()

tot = fin - ini

def Choice():
	choice = int(user_input('Choose your entry: '))
	return choice

def main():
	print ('''\n

  _       ___     _ _____
 | |     /   |   | /  __/
 | |__  / /| | __| \ `--.  ___ __ _ _ __ ®
 | '_ \/ /_| |/ _` |`--. \/ __/ _` | '_ \
 | |_) \___  | (_| /\__/ / (_| (_| | | | |
 |.____/   \_/\__,_\____/ \___\___|__| |_|

    1) Scan
    2) Scan over Tor proxy
    3) HttpRequest
    4) HttpRequest over Tor proxy
    5) TotalScan
    6) TotalScan over Tor proxy
    7) Exit

		''')
	b = b4dScan()
	c = Choice()
	b.Target()
	print ('... please wait, get info from', b.host)
	if c == 1:
		b.Scan(0)
	elif c == 2:
		b.Scan(1)
	elif c == 3:
		b.HttpRequest(0)
	elif c == 4:
		b.HttpRequest(1)
	elif c == 5:
		(b.Scan(0), b.HttpRequest(0))
	elif c == 6:
		(b.Scan(1), b.HttpRequest(1))
	elif c == 7:
		print ('Tnks for using b4dScan, bye bye!')
	else:
		print ('Get a right entry, like 1, 2 or 3\n')
		main()


if __name__ == '__main__':
	main()
	print ('Scanning finished in: ', tot)
