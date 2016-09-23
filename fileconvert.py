#! /usr/bin/python
#Written by Jay Lim
#September 23, 2016
#first python script - file converter
from sys import argv

#insert two parameters after filename: (i.e. ./fileconvert.py read.txt write.txt)
script, filename1, filename2 = argv

read = open(filename1)
write = open(filename2,'w')

print "Converting file: %r..." %filename1
print "Creating file: %r..." %filename2

#read a file line by line
#if a line has no trigger words: copy the same line to write
#if a line has a trigger word: replace the trigger word with a different word

l = read.readline()
while(l != ''):
	#hard code what substrings to replace
	if "\t" in l:
		l=l.replace("\t","    ")
	if "\\t" in l:
		l=l.replace("\\t", "\t")
	if "#" in l:
		l=l.replace("#","//")
	write.write(l)
	l=read.readline()
print "Done! Closing files"
read.close()
write.close()
