#!/usr/bin/env python

ip_addr = raw_input("Please enter an IP address, i.e 10.x.x.x: ")
ip_octets = ip_addr.split(".")

print
print "{:12} {:12} {:12} {:12}".format(*ip_octets)
print
