from subprocess import Popen, PIPE, STDOUT
import re
import subprocess



def proc_put(proc, cmd, filename = None):
	print cmd

	while True:
		line = proc.stdout.readline()
		if not line:
			print line

			if not filename:
				with open(filename, 'a+') as f:
					f.write(line)
	
		else:
			break
	

class Unit(object):
	def __init__(self):
		pass

	def restore(self):
		cmd = 'purple_restore -l {} -D {}'.format()
		proc = self.proc_spawn(cmd)

	def proc_spawn(self, cmd):
		proc = Popen(cmd, stdin = None, stdout = PIPE, stderr = STDOUT, bufsize = 0, universal_newlines = True, shell = True)
	
		return proc
		

class Usb(object):

	def __init__(self, usb_string = None):
		self.setting(usb_string)

	def setting(self, usb_string):
		if  'Attach' in usb_string:
			match_ret = re.compile('.+Attach\s*(?P<PRODUCT>\w+)\s*.+UDID = (?P<UDID>\w+).+device ID = (?P<DEVICE_ID>\d).+location ID = (?P<LOCATION_ID>\w+).+product ID = (?P<PRODUCT_ID>\w+).+', re.M)
			match_ret = match_ret.match(usb_string)

			self.product = match_ret.group('PRODUCT')
			self.udid = match_ret.group('UDID')
			self.device_id = match_ret.group('DEVICE_ID')
			self.location_id = match_ret.group('LOCATION_ID')
			self.product_id = match_ret.group('PRODUCT_ID')
		else:
			self.product = None
			self.udid = None
			self.device_id = None
			self.location_id = None
			self.product_id = None
		
	@classmethod
	def iter_usb(cls):
		iter_count = 0
		usb_list = []
		while iter_count < 3:
			output = subprocess.check_output('mobdev list', shell = True)
			if  'Attach' in output:
				print output
				for usb_str in re.finditer('.+Attach.+', output, flags = re.M):
					usb = Usb(usb_str.string)
					usb_list.append(usb)
				break
			else:
				iter_count = iter_count + 1

		return usb_list

if __name__ == '__main__':
	usb_l = Usb.iter_usb()
	print usb_l
