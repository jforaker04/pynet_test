#!/usr/bin/env python

def openfile(filename):
  with open(filename) as f:
    return f.read()

def find_serial(show_version):
  serial_number = ''
  for line in show_version.splitlines():
    if 'Processor board ID' in line:
      _, serial_number = line.split("Processor board ID")
  return serial_number

my_file = "show_version.txt"
show_version = openfile(my_file)
serial_number = find_serial(show_version)

print serial_number
