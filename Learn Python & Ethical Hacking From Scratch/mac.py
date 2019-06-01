#!/usr/bin/python3
# NOTE: DO NOT RUN subprocess at host!
import subprocess
# subprocess.call('ifconfig wlan0 down', shell=True)
# subprocess.call('ifconfig wlan0 hw ether 00:11:22:33:44:66', shell=True)
# subprocess.call('ifconfig wlan0 up', shell=True)


from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write report to FILE")
(options, args) = parser.parse_args()

# 用.存取
print(options.filename)

print(args)
