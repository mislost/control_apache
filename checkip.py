#1/usr/bin/env python
import re

class checkip(object):
	def __init__(self, ip):
		self.ip = ip
	
	def check_ip(self):
		p = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
		if p.match(self.ip):
			return "True"
		else:
			return "False"
		print self.ip
	
if __name__ == '__main__':
#	i = raw_input('please input IP:')
	app = checkip('192.168.1.1')
	app.check_ip()	
