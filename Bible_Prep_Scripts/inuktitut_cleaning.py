#!/usr/bin/python
# -*- coding: utf-8

# Cleans off the front verse number and removes spaces at the beginning and end of verse

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
            	lines = re.sub('^\d+', '',line)
            	lines1 = re.sub('^ ', '',lines)
            	lines2 = re.sub(' $', '',lines1)
            	#print(lines)
            	#lines = line.lstrip(digits)
            	#print(lines)
                fout.write(lines2)
                #fout.write('\n')
convert(inputname,outputname)
