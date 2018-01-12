from collections import defaultdict, Counter
import Queue
import operator

def countPairs(string):
    pairDict = defaultdict(int)
    for i in range(len(string) - 1):
        if string[i] not in blockCharacters and string[i + 1] not in blockCharacters:
            pairDict[(string[i: i + 2])] += 1
    return pairDict

def count_nchar_tokens(string, n):
    nchar_dict = defaultdict(int)
    for i in range(len(string) - n + 1):
        nchar_dict[string[i:i+n]] += 1
    return Counter(nchar_dict)

def create_word_and_count_dicts(file):
    # Stringify document
    document = file.readlines()
    ## Strip whitespace
    document = list(map(str.strip, document))
    ## Join all lines 
    document = " ".join(document)
    ## Split by word
    document = document.split(" ")
    ## Append EOW character (I think the BPE paper calls for this? Not sure)
    document = map(lambda x: x + '_', document)
    ## Transform list into dict with counts
    return Counter(document), Counter("".join(document))

def create_string(file):
    # Stringify document
    document = file.readlines()
    string = ""
    for i in document:
        string += i
    string = string.lower()
    characters_dict = Counter(string)
    return string, characters_dict


## Can use this function to take a dictionary and print contents in a nice way
def debug_dict(d):
    for k, v in d.items():
        print("{}\t:{}".format(k, v))
    print("")

def get_pair_counts(d):
    newcountdict = defaultdict(int)
    for k, v in d.items():
        for i in range(len(k) - 1):
            newcountdict[k[i:i+2]] += v
    return newcountdict

def clean(dictionary):
    for key, value in dictionary.items():
        if key in blockCharacters:
            del(dictionary[key])

if __name__ == "__main__":
    
    ## Input file
    path = 'english_unparsed_dev.txt'
    with open(path, 'r') as f:
        ## Parameters
        #vocSize = 32000
        vocSize = 20
        # 1. Create dict of words : counts, and bigrams : counts
        # We will iterate over the word dict every time we need to search for new bigrams
        # instead of iterating over the whole document for efficiency.
        # We will maintain the bigram count dict to determine next vocab token.
        #word_dict, count_dict = create_word_and_count_dicts(f)
        string, count_dict = create_string(f)

        blockCharacters = ["\n", "\t", "_"]
        #clean(count_dict)

        #print("Original doc has word counts:")
        #debug_dict(word_dict)

        #print("Original doc has char counts:")
        debug_dict(count_dict)

        ## 2. Initialize vocab with each character in original dict of words
        vocab_list = count_dict.keys()
        #print(vocab_list)

        ## 3. Scan over every word and obtain pair counts (new dict)
        #pair_dict = get_pair_counts(word_dict)
        pair_dict = countPairs(string)
        #print(pair_dict)
        ## 3b. store entire training data as a list (inefficient)
        dataset_list = []
        for line in string.split('\n'):
            for char in line:
                if char == ' ':
                    dataset_list.append('_')
                else:
                    dataset_list.append(char)
                dataset_list.append('@')
       # print(dataset_list) #creates the dataset
        
        ## Count dataset
        countdict = defaultdict(int)
        #stores all pairs and counts into a dict
        for item in range(len(dataset_list)-1):
        	if (dataset_list[item],dataset_list[item+1]) not in countdict:
        		countdict[(dataset_list[item],dataset_list[item+1])] = 1
        	else:
        		countdict[(dataset_list[item],dataset_list[item+1])] += 1
       # print(countdict)
        
        for i in range(1000):
        	## Get top pair
        	c = countdict.iteritems()
        	c = [(k, v) for k, v in c if k[0] != '@' and k[1] != '@' ] 
        	token1, token2 = (max(c, key=operator.itemgetter(1))[0]) #won't work because of endlines
        	newtoken = ''.join([token1, token2])
        	#print(newtoken)
        	## 4. Update original count dict with all pair counts, subtract old counts
    		for item in range(len(dataset_list)-2):
    			if item < len(dataset_list):
        			if dataset_list[item] == token1 and dataset_list[item+1] == token2:
        				if item == 0:
        					countdict[(dataset_list[item+1],dataset_list[item+2])] -= 1
        					countdict[(newtoken,dataset_list[item+2])] += 1
        				elif item == len(dataset_list)-2:
        					countdict[(dataset_list[item-1],dataset_list[item])] -= 1
        					countdict[(dataset_list[item-1],newtoken)] += 1
        				else:
        					#print(item)
        					#print(len(dataset_list))
        					countdict[(dataset_list[item-1],dataset_list[item])] -= 1
        					countdict[(dataset_list[item+1],dataset_list[item+2])] -= 1
        					countdict[(dataset_list[item-1],newtoken)] += 1
        					countdict[(newtoken,dataset_list[item+2])] += 1
        				dataset_list[item] = newtoken
        				dataset_list.pop(item+1)
        	del countdict[(token1,token2)]
        	#print(dataset_list)
        	#print(countdict)
        #dataset_list = ' '.join(dataset_list)
        #dataset_list = dataset_list.split('@')
        with open('dataset_list.txt','wt') as fout:
        	for item in dataset_list:
        		if item == '@':
        			fout.write('\n')
        		else:
        			fout.write(item)
        			fout.write(' ')
        d = {k:v for k, v in countdict.iteritems() if v > 0}
        
        count = Counter(dataset_list)
        with open('bpe_brute_vocab.txt','wt') as fout:
        	for k in count.keys():
        		if k is not '@':
        			fout.write(k)
        			fout.write("\n")
        	fout.close()
        #debug_dict(countdict)
        