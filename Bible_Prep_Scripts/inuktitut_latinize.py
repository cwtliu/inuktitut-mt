#!/usr/bin/python
# -*- coding: utf-8

# Replaces Inuktitut symbols with latinized equivalent, specific to our dataset

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
            	if any(i.isdigit() for i in line):	
            		m = re.search(r"[0-9]:[0-9]*-[0-9]",line) #removes the commentary -- but still have to manually remove the annotations
            		if m is None:
                		for word in line.split():
                			s = 0
                			for i in word:
                				if i.isdigit():
                				    if s == 0:
                				        s = 1
                				if i == '-':
                				    s = 0
                			if s == 1:
                				fout.write('\n')
                			x = word
                			x = x.replace(" "," ")
                			x=x.replace("ᐁ","ai")
                			x=x.replace("ᐃ","i")
                			x=x.replace("ᐅ","u")
                			x=x.replace("ᐊ","a")
                			x=x.replace("ᐯ","pai")
                			x=x.replace("ᐱ","pi")
                			x=x.replace("ᐲ", "pii")
                			x=x.replace("ᐳ", "pu")
                			x=x.replace("ᐴ", "puu")
                			x=x.replace("ᐸ", "pa")
                			x=x.replace("ᐹ", "paa")
                			x=x.replace("ᑌ", "tai")
                			x=x.replace("ᑎ", "ti")
                			x=x.replace("ᑏ", "tii")
                			x=x.replace("ᑐ", "tu")
                			x=x.replace("ᑑ", "tuu")
                			x=x.replace("ᑕ", "ta")
                			x=x.replace("ᑖ", "taa")
                			x=x.replace("ᑫ", "kai")
                			x=x.replace("ᑭ", "ki")
                			x=x.replace("ᑮ", "kii")
                			x=x.replace("ᑯ", "ku")
                			x=x.replace("ᑰ", "kuu")
                			x=x.replace("ᑲ", "ka")
                			x=x.replace("ᑳ", "kaa")
                			x=x.replace("ᒉ", "gai")
                			x=x.replace("ᒋ", "gi")
                			x=x.replace("ᒌ", "gii")
                			x=x.replace("ᒍ", "gu")
                			x=x.replace("ᒎ", "guu")
                			x=x.replace("ᒐ", "ga")
                			x=x.replace("ᒑ", "gaa")
                			x=x.replace("ᒣ", "mai")
                			x=x.replace("ᒥ", "mi")
                			x=x.replace("ᒦ", "mii")
                			x=x.replace("ᒤ","mii")
                			x=x.replace("ᒧ", "mu")
                			x=x.replace("ᒨ", "muu")
                			x=x.replace("ᒪ", "ma")
                			x=x.replace("ᒫ", "maa")
                			x=x.replace("ᓀ", "nai")
                			x=x.replace("ᓂ", "ni")
                			x=x.replace("ᓃ", "nii")
                			x=x.replace("ᓄ", "nu")
                			x=x.replace("ᓅ", "nuu")
                			x=x.replace("ᓇ", "na")
                			x=x.replace("ᓈ", "naa")
                			x=x.replace("ᓭ", "sai")
                			x=x.replace("ᓯ", "si")
                			x=x.replace("ᓰ", "sii")
                			x=x.replace("ᓱ", "su")
                			x=x.replace("ᓲ", "suu")
                			x=x.replace("ᓴ", "sa")
                			x=x.replace("ᓵ", "saa")
                			x=x.replace("ᓓ", "lai")
                			x=x.replace("ᓕ", "li")
                			x=x.replace("ᓖ", "lii")
                			x=x.replace("ᓗ", "lu")
                			x=x.replace("ᓘ", "luu")
                			x=x.replace("ᓚ", "la")
                			x=x.replace("ᓛ", "laa")
                			x=x.replace("ᔦ", "jai")
                			x=x.replace("ᔨ", "ji")
                			x=x.replace("ᔩ", "jii")
                			x=x.replace("ᔪ", "ju")
                			x=x.replace("ᔫ", "juu")
                			x=x.replace("ᔭ", "ja")
                			x=x.replace("ᔮ", "jaa")
                			x=x.replace("ᕓ", "vai")
                			x=x.replace("ᕕ", "vi")
                			x=x.replace("ᕖ", "vii")
                			x=x.replace("ᕗ", "vu")
                			x=x.replace("ᕘ", "vuu")
                			x=x.replace("ᕙ", "va")
                			x=x.replace("ᕚ", "vaa")
                			x=x.replace("ᕃ", "rai")
                			x=x.replace("ᕆ", "ri")
                			x=x.replace("ᕇ", "rii")
                			x=x.replace("ᕈ", "ru")
                			x=x.replace("ᕉ", "ruu")
                			x=x.replace("ᕋ", "ra")
                			x=x.replace("ᕌ", "raa")
                			x=x.replace("ᙯ", "qai")
                			x=x.replace("ᕿ", "qi")
                			x=x.replace("ᖀ", "qii")
                			x=x.replace("ᖁ", "qu")
                			x=x.replace("ᖂ", "quu")
                			x=x.replace("ᖃ", "qa")
                			x=x.replace("ᖄ", "qaa")
                			x=x.replace("ᙰ", "ngai")
                			x=x.replace("ᖏ", "ngi")
                			x=x.replace("ᖐ", "ngii")
                			x=x.replace("ᖑ", "ngu")
                			x=x.replace("ᖒ", "nguu")
                			x=x.replace("ᖓ", "nga")
                			x=x.replace("ᖔ", "ngaa")
                			x=x.replace("ᑉ", "p")
                			x=x.replace("ᑦ", "t")
                			x=x.replace("ᒃ", "k")
                			x=x.replace("ᒡ", "g")
                			x=x.replace("ᒻ", "m")
                			x=x.replace("ᓐ", "n")
                			x=x.replace("ᔅ", "s")
                			x=x.replace("ᓪ", "l")
                			x=x.replace("ᔾ", "j")
                			x=x.replace("ᕝ", "v")
                			x=x.replace("ᕐ", "r")
                			x=x.replace("ᖅ", "q")
                			x=x.replace("ᖕ", "ng")
                			#print word,
                			#print x
                			fout.write(x)
            				fout.write(' ')
                		#fout.write('.')
convert(inputname,outputname)



