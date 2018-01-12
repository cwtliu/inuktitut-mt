from collections import defaultdict, Counter
import Queue
import operator

## SET VARIABLES HERE PLZ
INPUT_FILE = 'both_unparsed_train.txt'
VOCAB_SIZE = 32000
DOC_LENGTH = 266559
OUTPUT_FILE_1 = 'inuk_bpe_train'
OUTPUT_FILE_2 = 'eng_bpe_train'
DUMMY_CHAR = '@@'
END_OF_DOC_CHAR = '@@@'
NEWLINE_CHAR = '~~'
VOCAB_SIZES = [10000,15000,20000,25000,32000]

def write_files(num):
	file1 = True
	index = 0
	for item in dataset_list:
		if file1:
			path = OUTPUT_FILE_1 + str(num) + ".txt"
		else:
			path = OUTPUT_FILE_2 + str(num) + ".txt"
		with open(path, 'aw') as f:
			if item != DUMMY_CHAR:
				if item == END_OF_DOC_CHAR:
					break
				elif item == NEWLINE_CHAR:
					f.write('\n')
					index += 1
				else:
					f.write(item)
					f.write(" ")
		if index > DOC_LENGTH:
			file1 = False

def create_string(file):
	document = file.readlines()
	string = "".join(document)
	string = string.lower()
	return string

def printindexdict():
	for k, v in indexdict.items():
		print("Token: {}\t Indices: {}".format(k, v.keys()))

if __name__ == "__main__":

	with open(INPUT_FILE, 'r') as f:
		
		## Stringify document
		print("Creating docstring...")
		string = create_string(f)
		# print(string)
		
		## Store document as list. '_' for spaces, '@' for newlines
		print("Converting docstring to char-list...")
		dataset_list = []
		for line in string.split('\n'):
			for char in line:
				if char == ' ':
					dataset_list.append('_')
				else:
					dataset_list.append(char)
			dataset_list.append(NEWLINE_CHAR)

		## Special end of document character is '@@'
		dataset_list.pop(len(dataset_list)-1)
		dataset_list[len(dataset_list)-1]=END_OF_DOC_CHAR

		## Index of where token pairs occur
		indexdict = defaultdict(lambda: defaultdict(int))
		
		## Stores all token pairs and counts into a dict
		print("Initializing index and count dicts...")
		for item in xrange(len(dataset_list)-1):
			indexdict[(dataset_list[item],dataset_list[item+1])][item] = 1

		## Counts of token pairs
		countdict = defaultdict(int)
		for k, v in indexdict.items():
			countdict[k]=len(v)

		## Iterate for VOCAB_SIZE iterations
		print("Starting BPE iterations...")
		for num_iterations in xrange(VOCAB_SIZE):
			print("BPE iteration no: {}".format(num_iterations))
			## printindexdict()
			
			## Find max disregarding endlines, exit if no more tokens left to add
			c = countdict.iteritems()
			c = [(k, v) for k, v in c if k[0] != NEWLINE_CHAR and k[1] != NEWLINE_CHAR and k[1] != END_OF_DOC_CHAR and k[0] != k[1]]
			if not c:
				break
			token1, token2 = (max(c, key=operator.itemgetter(1))[0])
			newtoken = token1 + token2
			#print("Token 1: {}".format(token1))
			#print("Token 2: {}".format(token2))
			#print("Attempting to add token {}".format(newtoken))
			if num_iterations == 86:
				print(newtoken)

			## Loop to update counts:
			## For each index where this token pair occurs

			for item in indexdict[(token1,token2)]:
				if item == 0: 
				## Only have to search for forward token
 					plus1 = item+1
					while dataset_list[plus1]==DUMMY_CHAR:
						plus1+=1
					plus2 = plus1+1
					while dataset_list[plus2]==DUMMY_CHAR:
						plus2+=1

					## Subtract count of forward token
					countdict[(dataset_list[plus1],dataset_list[plus2])] -= 1
					#print("Deleting {} at index {}".format((dataset_list[plus1],dataset_list[plus2]), plus1))
					del indexdict[(dataset_list[plus1],dataset_list[plus2])][plus1]

					## Add count of newtoken pair
					countdict[(newtoken,dataset_list[plus2])] += 1
					## Add index of newtoken pair
					indexdict[(newtoken,dataset_list[plus2])][item] = 1
				else:
					minus1 = item-1
					plus1 = item+1
					while dataset_list[minus1]==DUMMY_CHAR:
						minus1-=1
					while dataset_list[plus1]==DUMMY_CHAR:
						plus1+=1
					plus2 = plus1+1
					while dataset_list[plus2]==DUMMY_CHAR:
						plus2+=1

					## Update counts
					if plus2 == END_OF_DOC_CHAR:
						## Subtract count of backward token
						countdict[(dataset_list[minus1],dataset_list[item])] -= 1
						del indexdict[(dataset_list[minus1],dataset_list[item])][minus1]

						## Add count of new backward token
						countdict[(dataset_list[minus1],newtoken)] += 1
						indexdict[(dataset_list[minus1],newtoken)][minus1] = 1
					else:
						## Subtract count of backward token
						countdict[(dataset_list[minus1],dataset_list[item])] -= 1
						## print("Deleting {} at index {}".format((dataset_list[minus1], dataset_list[item]), minus1))
						del indexdict[(dataset_list[minus1],dataset_list[item])][minus1]

						## Subtract count of forward token
						countdict[(dataset_list[plus1],dataset_list[plus2])] -= 1
						## print("Deleting {} at index {}".format((dataset_list[plus1],dataset_list[plus2]), plus1))
						del indexdict[(dataset_list[plus1],dataset_list[plus2])][plus1]

						## Add count of new backward token
						countdict[(dataset_list[minus1],newtoken)] += 1
						# print("Adding {} into indexdict".format((dataset_list[minus1], newtoken)))
						indexdict[(dataset_list[minus1],newtoken)][minus1] = 1

						## Add count of new forward token
						countdict[(newtoken,dataset_list[plus2])] += 1
						# print("Adding {} into indexdict".format((newtoken, dataset_list[plus2])))
						indexdict[(newtoken,dataset_list[plus2])][item] = 1
									
				dataset_list[item] = newtoken
				dataset_list[plus1] = DUMMY_CHAR
			del indexdict[(token1,token2)]
			del countdict[(token1,token2)]
		
			if num_iterations in VOCAB_SIZES:
				print("Writing at iteration {}".format(num_iterations))
				write_files(num_iterations)
