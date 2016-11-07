#!/usr/bin/env python

ip_addr = raw_input("Please enter an IP address, i.e 10.x.x.x: ")
ip_octets = ip_addr.split(".")
ip_octets[-1] = 0

ip_binary = []
ip_binary.append(bin(int(ip_octets[0])))
ip_binary.append(bin(int(ip_octets[1])))
ip_binary.append(bin(int(ip_octets[2])))
ip_binary.append(bin(int(ip_octets[3])))


print
print "{:<12} {:<12} {:<12} {:<12}".format('octet1','octet2','octet3','octet4')
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_octets)
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_binary)
print
