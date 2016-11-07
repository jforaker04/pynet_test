#!/usr/bin/env python

## Read the file
f = open('file_list.txt')

## Read the lines of the file
for line in f:
  print line.strip()

