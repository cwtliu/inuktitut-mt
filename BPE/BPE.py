from collections import defaultdict, Counter
import Queue

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

def replace(string, token_list):
    token_list.sort(reverse = True, key = lambda x:len(x))
    for token in token_list:
        index = 0
        checkflag = True
        while index < len(string):
            if string[index] == "$" and checkflag:
                checkflag = False
            elif string[index] == "$" and not(checkflag):
                checkflag = True
            if checkflag and string[index: index + len(token)] == token:
                string = string[0: index] + "$" + string[index: index + len(token)] + "$" + \
                         string[index + len(token): len(string)]
                continue
            index += 1
    return string

if __name__ == "__main__":
    
    ## Input file
    path = 'source_train.txt'
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

        print("Original doc has word counts:")
        #debug_dict(word_dict)

        print("Original doc has char counts:")
        debug_dict(count_dict)

        ## 2. Initialize vocab with each character in original dict of words
        vocab_list = count_dict.keys()
        print(vocab_list)

        ## 3. Scan over every word and obtain pair counts (new dict)
        #pair_dict = get_pair_counts(word_dict)
        pair_dict = countPairs(string)

        ## Get top pair

        ## 4. Update original count dict with all pair counts, subtract old counts


        ## 5. Loop until you reach desired vocab size
        debug_dict(count_dict)
        while len(vocab_list) < vocSize:
            ## Get next top word by count
            max_key, max_value = float("-inf"), float("-inf")
            for key, value in count_dict.items():
                if value > max_value:
                    max_value = value
                    max_key = key

            next_word = max_key
            ## Add word to vocab_dict
            vocab_list.append(next_word)
            #print(vocab_list)

            ## Scan over every word and obtain next bigram counts (new dict)
            new_bigram_dict = defaultdict(int)
            for i in range(len(string)):
                for j in range(0, len(next_word)):
                    if string[i: i + len(next_word)] == next_word:
                        new_bigram_dict[string[i: i + len(next_word) + 1]] += 1
            debug_dict(new_bigram_dict)

            break
            # TODO
            ## Update original count dict with all bigram counts, subtract old counts

    #### BPE Replacement
    dictVoc = ["re", "rec", "rece", "recen", "recent", "ba", "bas", "rg", "rge", "la"]
    string = create_string(open("target_train.txt", 'r'))[0]
    string = string.replace("\n", "_")
    print(dictVoc, string)
    print(replace(string, dictVoc))