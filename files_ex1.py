#!/usr/bin/env python

## Read the file
f = open('file_list.txt')

## Read the lines of the file
for line in f:
  print line.strip()
f.close()

## Create new file
f = open('file_list_new.txt', 'w')
f.close()

## Open new file and append
f = open('file_list_new.txt', 'a')
f.write('This is a line appended to the end.\n')



