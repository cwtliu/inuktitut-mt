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

#updates new pair counts
def update_pair_counts(d):
    newcountdict = defaultdict(int)
    for k, v in d.items():
        for i in range(len(k) - 1):
            newcountdict[k[i:i+2]] += v
    return newcountdict

if __name__ == "__main__":
    
    ## Input file
    path = 'test1'
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
        #debug_dict(count_dict)

        ## 2. Initialize vocab with each character in original dict of words
        vocab_list = count_dict.keys()
        print(vocab_list)

        ## 3. Scan over every word and obtain pair counts (new dict)
        #pair_dict = get_pair_counts(word_dict)
        pair_dict = countPairs(string)
        print(pair_dict)
        
        ## Get top pair
        merge_token = max(pair_dict.iteritems(), key=operator.itemgetter(1)) #FIGURE OUT OUR TIEBREAKER PLAN FOR 2+ MAXIMUMS
        print(merge_token)
        
        ## 3b. store entire training data as a list (inefficient)
        dataset_list = []
        for line in string.split('\n'):
        	for char in line:
        		dataset_list.append(char)
        	dataset_list.append('&')
        print(dataset_list) #creates the dataset
        tupledict = defaultdict()
        #stores all pairs and counts into a dict
        for item in range(len(dataset_list)-1):
        	if dataset_list[item] not in tupledict:
        		tupledict.setdefault(dataset_list[item],[])
        		tupledict[dataset_list[item]].append([dataset_list[item+1],1])
        	else:
        		flag = 0
        		for iter in range(len(tupledict[dataset_list[item]])):
        			if dataset_list[item+1] == tupledict[dataset_list[item]][iter][0]:
        				tupledict[dataset_list[item]][iter][1]+=1
        			else:
        				flag+=1
        		if flag == len(tupledict[dataset_list[item]]):
        			tupledict[dataset_list[item]].append([dataset_list[item+1],1])
        print(tupledict)
        
        
        tripledict = defaultdict()
        #stores all pairs and counts into a dict
        for item in range(len(dataset_list)-2):
        	if dataset_list[item] not in tripledict:
        		tripledict.setdefault(dataset_list[item],[])
        		tripledict[dataset_list[item]].append([dataset_list[item+1],dataset_list[item+2],1])
        	else:
        		flag = 0
        		for iter in range(len(tripledict[dataset_list[item]])):
        			if dataset_list[item+1] == tripledict[dataset_list[item]][iter][0] and dataset_list[item+2] == tripledict[dataset_list[item]][iter][1]:
        				tripledict[dataset_list[item]][iter][2]+=1
        			else:
        				flag+=1
        		if flag == len(tripledict[dataset_list[item]]):
        			tripledict[dataset_list[item]].append([dataset_list[item+1],dataset_list[item+2],1])
        print(tripledict)
        
        #WRAP THROUGH NUM ITERATIONS (TODO)
        #return largest pair tokens: token1, token2
        token1, max_value = float("-inf"), float("-inf")
        for key, value in tupledict.items():
            for i in range(len(value)):
            	if value[i][1] > max_value:
                	max_value = value[i][1]
                	token2 = value[i][0]
                	token1 = key
    	print(token1)
    	print(token2)
    	print(max_value)

        
        ## 4. Update original count dict with all pair counts, subtract old counts
        #add new merged tokens
        newtoken = ''.join([token1, token2])
        tripledict.setdefault(newtoken,[])
        #if token1 is in the left
        #look to the right two after token
        for i in range(len(tripledict[token1])):
        	print('yes')
        	print(tripledict[token1][i][0])
        	if tripledict[token1][i][0] == token2:
        		print(tripledict[token1][i][1])
        		tripledict[newtoken].append([tripledict[token1][i][2],tripledict[token1][i][1],tripledict[token1][i][2]])
        	#del tripledict[token1][i]
        #if token1 is to the right of an entry, decrement by 1 each time (O(n))
        #increment by 1 pair of left token and new merged right token
      #  for key, value in countdict.items():
      #  	print(key)
      #  	print(value)
      #  	for j in range(len(value)):
      #  		print(value[j][0])
      #  		if token1 == value[j][0]:
      #  			print(value[j][0])
      #  			print(value[j][1])
      #  			countdict[key].append([newtoken,value[j][1]])
        			#del countdict[key][j]
        	#	print(j)
        		#print(token1 == countdict[token2][j][token1])
        			#print(token1)
        			#print(countdict[token2][i][0])
        print(tripledict)
        	

        ## 5. Loop until you reach desired vocab size
        #debug_dict(count_dict)
        while len(vocab_list) < vocSize:
            ## Get next top word by count
            max_key, max_value = float("-inf"), float("-inf")
            for key, value in count_dict.items():
                if value > max_value:
                    max_value = value
                    max_key = key
            #print("max key is "+key)

            next_word = max_key
            ## Add word to vocab_dict
            vocab_list.append(next_word)
            #print(vocab_list)

            #print(next_word, "that was next word")
            ## Scan over every word and obtain next bigram counts (new dict)
            new_bigram_dict = defaultdict(int)
            for i in range(len(string)):
                for j in range(0, len(next_word)):
                    if string[i: i + len(next_word)] == next_word:
                        new_bigram_dict[string[i: i + len(next_word) + 1]] += 1
            #print("new bigram dict is ")
            #print(new_bigram_dict)
            debug_dict(new_bigram_dict)

            break
            # TODO
            ## Update original count dict with all bigram counts, subtract old counts