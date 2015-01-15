#!/usr/bin/env python

import os

class Input(object):
	def __init__(self, ip):
		self.ip = ip

	def Input_ip(self):
		f = open('hosts.allow', 'a+')
		f.write(self.ip+'\n')
		f.close()

if __name__  == '__main__':
	app = Input('192.168.1.111')
	app.Input_ip()

	
				
