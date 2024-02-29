#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Student1: Umamaheswarababu Maddela (umama339)
# Student2: Dinesh Sundaramoorthy (dinsu875)

# reading the text file
def read_file(filename):
    with open(filename, "r", encoding="utf8") as file:
        content = file.read()
    return content

# preprocess the content of the text file
def preprocess(content):
    import string
    for char in string.punctuation:
        content=content.replace(char,' ')
    content = content.lower()
    word_list = content.split()
    return word_list

# To print a frequency table for alphabetic letters, ordered from the most common to the least
def frequent_letters(content):
    content = content.lower()
    alphabet_counts = {}
    for char in content:
        if char.isalpha():
            alphabet_counts[char] = alphabet_counts.get(char, 0) + 1
    result=sorted(alphabet_counts.items(), key=lambda x: x[1], reverse=True)
    print_output = "Frequency table \n"
    for alphabet, count in result:
        print_output += f"{alphabet}: {count} \n"
    return print_output   

# To print the number of words that the text contains, according to some definition of words.
def count_words(content):
    word_list = preprocess(content)
    num_words = len(word_list)
    print_output = f"The number words in the file is {num_words} \n"
    return print_output

# To print the number of unique words that the text contains, according to this definition.
def unique_words(content):
    word_list = preprocess(content)
    word_set=set(word_list)
    num_unique_words = len(word_set)
    print_output = f"The number of unique words in the file is {num_unique_words} \n"
    return print_output


#  To print the five most commonly used words, their frequency and the words that most commonly follow them
def common_words(content):
    word_list = preprocess(content)
    count={}
    for word in word_list:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    sorted_words=dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
    
    # five most common words
    top_five =list(sorted_words)[:5]
    print_output = "Five most commonly used words \n"
    print_output += "\n"
    follow_words={}
    for i in range(len(word_list)-1):
        if word_list[i] in top_five:
            if word_list[i] in follow_words:
                follow_words[word_list[i]].append(word_list[i+1])
            else:
                follow_words[word_list[i]] = [word_list[i+1]]
    for word in top_five:
        dict_count={}
        for i in follow_words[word]:
            if i in dict_count:
                dict_count[i]+=1
            else:
                dict_count[i]=1
                
        # dictionary of most following words in descending order
        sorted_3=dict(sorted(dict_count.items(), key=lambda x:x[1], reverse=True))
        print_output += f"{word} ({sorted_words[word]} occurances) \n"
        for key, value in list(sorted_3.items())[0:3]:
            print_output += f"-- {key},  {value} \n"
        print_output += "\n"
        dict_count={}
    return print_output

def generate_successor(content):
    from collections import defaultdict
    
    word_list = preprocess(content)
    successor_dict = defaultdict(list)
    
    # building dictionary of successors
    for i in range(len(word_list)-1):
        successor_dict[word_list[i]].append(word_list[i+1])
        
    return successor_dict
    
    
    


## To print the output of text_stats.py give only two arguments (text_stats.py and text file name)
## To write the output of text_stats.py in a text file give three arguments (text_stats.py, text file name and output file name)

import sys
import os

if __name__ == '__main__':     #Ref:https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    if (len(sys.argv) == 2 or len(sys.argv) == 3):
        path= sys.argv[1]
        if (os.path.exists(path)):
            content=read_file(path)
            output = frequent_letters(content)
            output += "\n"
            output += count_words(content)
            output += "\n"
            output += unique_words(content)
            output += "\n"
            output += common_words(content)
            
        else:
            print("Invalid path! Please check the file path and format")

        if (len(sys.argv) == 2):
            print(output)
        elif (len(sys.argv) == 3):
            output_text_file = sys.argv[2]
            with open(output_text_file, 'w', encoding="utf-8") as text_file:
                text_file.write(output)       
        
    else:
        print("Please enter only two or three arguments(program file name, text file name and output file name) ")
 

