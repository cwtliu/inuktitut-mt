#!/usr/bin/python
# -*- coding: utf-8

# Appends a line with annotations to the previous verse

# For ASCII Encoding/Decoding of Inuktitut Syllabary
import io
import codecs
import unicodedata
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

inputname = 'input name'
outputname = 'output name'
def convert(inputname,outputname):
    with codecs.open(inputname, encoding='utf-8') as fin:
        with open(outputname,'wt') as fout:
            for line in fin:
            	#if any(i.isdigit() for i in line):	
            	m = re.search(r"[0-9]:[0-9]",line) #removes the commentary -- but still have to manually remove the annotations
            	if m is None:
            		fout.write('\n')
                	for word in line.split():
                		x = word
                		fout.write(x)
            			fout.write(' ')
            	if m:
            		#print(line)
            		for word in line.split():
            			x = word
            			fout.write(x)
            			fout.write(' ')
convert(inputname,outputname)
