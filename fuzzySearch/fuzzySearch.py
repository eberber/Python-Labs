import re
import numpy as np

def match(my_word, data):
    flag = 0
    payload = []
    string1 = ""
    counter = 0
    num_matches = 0
    #if a single letter does not match, thats one. on a second dont append
    for i in range(len(data)):
        if i >= len(my_word): #make sure word is of same length to compare
            for j in range(len(my_word)):
                string1 += data[(i - len(my_word))+j]
                if my_word[j] != data[(i-len(my_word)) + j]:
                    flag +=1
                    if flag == 2:
                        break
            if flag != 2:
                num_matches+=1
                payload.append(string1)
                if string1 == my_word:
                    break
            string1 = ""
            flag = 0
            counter = 0
        counter +=1
    return payload, num_matches

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    #print (matrix)
    return (matrix[size_x - 1, size_y - 1])

def search(my_word, data):
    string1 = ""
    shift = ""
    payload = []
    dict = {}
    counter = 0
    num_matches = 0
    is_length = 0
    
    for i in range(len(data)):
        string1 += data[i]
        if is_length == len(my_word):
            score = levenshtein(string1, my_word)
            if score <= 1: # within 1 letter deviation
                num_matches += 1
                payload.append(string1)
            elif score == 2: # may be a swap?
                for x in range(len(my_word)):
                    if my_word[x] not in dict.keys() :
                        dict[my_word[x]] += 1
                    if string1[x] not in dict.keys():
                        dict[string1[x]] += 1
                for key, value in dict.items():
                    if value > 1:
                        dict = {} #no swap
                        break
                    elif counter == len(dict):
                        num_matches += 1
                        payload.append(string1)
                    counter += 1
            string1 = ""
            counter = 0
            is_length = 0
        is_length +=1
    return payload, num_matches


with open('small.txt') as file:
    data = file.read().lower()
phrase = input("Enter a phrase to search for: \n")
phrase = phrase.lower()
print("\n Word is : ", phrase, "\n length: \n", len(phrase))
# payload, num_matches = match(phrase, data)
# for i in payload:
#     if i == phrase:
#         print(i)
#         print("Exact match")
#         exit(0)
# print("result \n",payload)
# print('Matches',num_matches)
payload, num_matches = search(phrase, data)
print(payload)
print(num_matches)