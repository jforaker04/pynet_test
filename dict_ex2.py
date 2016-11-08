#!/usr/bin/env python

net_device = { 
  'ip_addr' :  '10.0.201.72',
  'username' : 'admin',
  'password' : ' inital_pass',
  'vendor' : 'cisco',
  'model' : '5672'
}

print 
for k,v in net_device.items():
  print k,v

net_device['password'] = raw_input("Enter new password: ")
net_device['secret'] = raw_input("Enter new secret: ")

device_type = net_device.get('device_type', 'cisco_ios')
print "\nDefault device type : {}\n".format(device_type)

try:
  device_type = net_device['device_type']
except KeyError:
  print "Device type not found\n"
