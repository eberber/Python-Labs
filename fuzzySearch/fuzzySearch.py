import re

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


with open('shakespeare.txt') as file:
    data = file.read().lower()
data = re.findall(r"[\S]",data)
phrase = input("Enter a phrase to search for: \n")
phrase = phrase.lower()
print("\n Word is : ", phrase, "\n length: \n", len(phrase))
payload, num_matches = match(phrase, data)
for i in payload:
    if i == phrase:
        print(i)
        print("Exact match")
        exit(0)
print("result \n",payload)
print('Matches',num_matches)
