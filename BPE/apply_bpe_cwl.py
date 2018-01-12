from collections import defaultdict

#sentence = 'the cat is the cat'
#vocab_item = 'cat is'

#This takes in a string of untokenized words and checks for the vocab_item and splits
#if the vocab_item is present, appending a @@ to the vocab_item delimiter and returns
#the whole split as a list
def split_sentence(sentence,vocab_item):
	if sentence == vocab_item or vocab_item not in sentence:
		list_sentence=[]
		list_sentence.append(sentence)
		return list_sentence
	else:
		splits = sentence.split(vocab_item)
		segments = []
		for split in splits[:-1]:
			for segment in [split,vocab_item+'@@']:
				if segment != '':
					segments.append(segment.strip())
		if splits[-1] != '':
			return segments + [splits[-1].strip()]
		else:
			return segments

#import vocabulary output from get_vocab.py and , with keys as lengths of words, 
# and values as tuples of words and their original dict count
with open('training_files/10k/both_vocab_10000.txt', 'r') as fin:
	vocab_length_map = defaultdict(list)
	for line in fin:
		split_count = line.rstrip().split()
		#print(split_count)
		vocab_length_map[len(split_count[0])].append(split_count)
#reads in the file to be parsed by vocab_length_map
#The input file is first made into a list, with each item a line of the input txt
#split_sentence is then called by reverse word length, and reverse count for each value
with open('training_files/english_unparsed_dev.txt','r') as fdata:
	dataset_list = []
	for line in fdata:
		placeholder = []
		placeholder.append(line.rstrip().replace(" ", "_").lower())
		dataset_list.append(placeholder)
	print(dataset_list)
	for key in sorted(vocab_length_map.iterkeys(), reverse=True):
		for word in vocab_length_map[key]:
			print "Word is '%s'" % (word[0])
			for j in range(len(dataset_list)):
				for i in range(len(dataset_list[j])):
					if len(dataset_list[j][i]) > len(word[0]):
						if dataset_list[j][i][-2:] != '@@':
							segmented_sentence = split_sentence(dataset_list[j][i], word[0])
							dataset_list[j] = dataset_list[j][:i]+segmented_sentence+dataset_list[j][i+1:]
print(dataset_list)
#Outputs the resulting list into a file and removes the @@ token
with open('training_files/10k/english_dev_10k_apply_bpe_cwl.txt','wt') as fout:
	for sentence in dataset_list:
		for token in sentence:
			if token[-2:] == '@@':
				fout.write(token[:-2])
				if token != sentence[-1]:
					fout.write(' ')
			else:
				fout.write(token)
				if token != sentence[-1]:
					fout.write(' ')
		fout.write('\n')
							
							