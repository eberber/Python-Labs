import time
import numpy as np

def levenshtein(str1, str2):
    lenX = len(str1) + 1
    lenY = len(str2) + 1
    matrix = np.zeros ((lenX, lenY))
    for x in range(lenX):
        matrix [x, 0] = x
    for y in range(lenY):
        matrix [0, y] = y

    for x in range(1, lenX):
        for y in range(1, lenY):

            if str1[x-1] == str2[y-1]: #if chars match
                matrix [x,y] = min(
                    matrix[x-1, y] + 1, #top
                    matrix[x-1, y-1], #diagonal
                    matrix[x, y-1] + 1 #left
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )

    return (matrix[lenX - 1, lenY - 1])

def search(my_word, data):
    string1 = ""
    payload = []
    index_location = []
    dict = {}
    counter = 0
    num_matches = 0
    is_length = len(my_word) + 1
    operations = 0
    for i in range(len(data)):
        string1 += data[i]
        if i + len(my_word) < len(data):
            for j in range(i + 1, i + is_length):
                string1 += data[j]
                if (len(string1) == len(my_word) + 1) or (len(string1) == len(my_word) - 1) or (len(string1) == len(my_word)):
                    score = levenshtein(string1, my_word)
                    operations +=1
                    #print(string1, "    ", my_word, "\n  XXXXXX \n")
                    if score <= 1:# within 1 letter deviation
                        num_matches += 1
                        payload.append(string1)
                        index_location.append(i)
                    elif score == 2:# may be a swap?
                        for x in range(len(my_word)):
                            if my_word[x] not in dict.keys():
                                dict[my_word[x]] = 1
                            else:
                                dict[my_word[x]] += 1
                        for x in range(len(string1)):
                            if string1[x] not in dict.keys():
                                dict[string1[x]] = 1
                            else:
                                dict[string1[x]] += 1
                        for key, value in dict.items():
                            if value > 2:
                                dict = {} #no swap
                                break
                            elif counter == len(dict):
                                num_matches += 1
                                payload.append(string1)
                                index_location.append(i)
                            counter += 1
                counter = 0
            string1 = ""
    return payload, num_matches, index_location, operations
file = input("Enter file name: ")
with open(file) as file:
    data = file.read().lower()
print("File length: ", len(data))
phrase = input("Enter a phrase to search for: \n")
phrase = phrase.lower()
print("\nWord is : ", phrase, "\nLength: ", len(phrase))
start = time.time()
payload, num_matches, index_location, operations = search(phrase, data)
final = time.time()
for i in range(len(payload)):
    if payload[i] == phrase:
        print("Result: ", payload[i])
        print("Exact match at index: ", index_location[i])
        print("Time: ", final - start)
        print("Operations: ", operations)
        exit(0)
for i in range(len(payload)):
    print("Result: ", payload[i])
    print("Match at index: ", index_location[i])
print('Matches: ', num_matches)
print("Time: ", final - start)
print("Operations: ", operations)
