#!/usr/bin/env python
# coding: utf-8

# In[15]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Student1: Umamaheswarababu Maddela (umama339)
# Student2: Dinesh Sundaramoorthy (dinsu875)


import re
from random import choices
from collections import defaultdict
import text_stats 

def generate_newtext(word_successor, start_word, max_words):
    
    word_dict = word_successor
    cur_word = start_word
    msg = cur_word

    for i in range(max_words):
        # checking if there are no successors
        if not word_dict[cur_word]:
            break

        # choosing the next word
        successors = word_dict[cur_word]
        freq_dict = defaultdict(int)
        for word in successors:
            freq_dict[word] += 1

        total_freq = sum(freq_dict.values())
        
        # calculating probabilities of each successor
        probs = [freq_dict[word]/total_freq for word in successors]

        # choosing the successor at random choice based on weightage(probability)
        cur_word = choices(successors, weights=probs, k=1)[0]
        msg += " " + cur_word

    return msg
    
    

def main(filename, start_word, max_words):  #Ref: https://stackoverflow.com/questions/419163/what-does-if-name-main-do

    content=text_stats.read_file(filename)   #importing read_file() from text_stats.py
    word_successor = text_stats.generate_successor(content)   #importing generate_successor() from text_stats.py
    output = generate_newtext(word_successor, start_word, max_words)
    return output



## To print the output of generate_text.py give only four arguments (generate_text.py, text file name, start_word and max_words)
## To write the output of generate_text.py in a text file give fivr arguments (generate_text.py, text file name, start_word, max_words and output file name)

import sys
import os

if __name__ == '__main__':   #Ref: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    if (len(sys.argv) == 4 or len(sys.argv) == 5):
        path= sys.argv[1]
        start_word = sys.argv[2]
        max_words = int(sys.argv[3])
        if (os.path.exists(path)):
            output = main(path, start_word, max_words)
        else:
            print("Invalid path! Please check the file path and format")

        if (len(sys.argv) == 4):
            print(output)
        elif (len(sys.argv) == 5):
            output_text_file = sys.argv[4]
            with open(output_text_file, 'w', encoding="utf-8") as text_file:
                text_file.write(output)       
        
    else:
        print("Please enter only four or five arguments(program file name, text file name, start word, max words and output file name) ")
 

