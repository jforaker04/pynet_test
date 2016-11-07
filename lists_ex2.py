#!/usr/bin/env python

my_list = range(5)
my_list.append('first')
my_list.append('second')

print
print my_list.pop(0)
print
print len(my_list)

my_list.sort()
print my_list
