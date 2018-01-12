#Helpful for aligning the text with the English data
numbers = []
curr_chap = 1
prev_verse = -1
curr_verse = 0


curr_count = 0
line_count = 0

with open('OT_Book1_inuk_1.txt', 'r') as f:

    for line in f:
    	line_count += 1
        char = line[:2]
        if not str.isdigit(char):
        	char = char[:1]

        ## Is a duplicate
        if int(char) == curr_verse:
            print("Chap {} Verse {} is a duplicate".format(curr_chap, curr_verse))
            curr_count += 1
            print("Line {}".format(line_count))
        ## Is okay
        elif int(char) == curr_verse + 1:
            curr_verse += 1
            curr_count += 1
        ## Is a new chapter
        elif int(char) == 1:
        	print("Chap {} Verses: {}".format(curr_chap, curr_count))
        	print("Line {}".format(line_count))
        	curr_chap += 1
        	curr_verse = 1
        	curr_count = 1
        ## Is missing
        else:
        	print("Missing chapter {} verse {}".format(curr_chap, curr_verse + 1))
        	curr_verse += 2
        	curr_count += 1
        	print("Line {}".format(line_count))
    print("Chap {} Verses: {}".format(curr_chap, curr_count))

# print(numbers)

