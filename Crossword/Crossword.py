import numpy

file = open('puzzle1.txt')
data = file.readlines()
col = 0
temp = 0
for i in range(len(data)):
    data[i] = list(data[i].strip())
    #print(data[i], i)
    if data[i][0] == '.' or data[i][0] == '*':
        col += 1
    else: temp += 1
board = data[0:col]
data = data[col:]
print(board, '\n')
temp = ''
count = 0
key = 0
value = 0
hash = {}
hash2 = {}
temp1 = 0
temp2 = 0
for x in data:
#    print(x)
    l = len(x)
    t = str(x)
    hash2[t] = l

#print(hash2)

for i in range(len(board)):
    for j in range(len(board[i])):
        #print(board[j] , end = '\n')
        print(board[i][j])
        if board[i][j] == '*': #u see potential start of word
            count = 1 #start counter
            temp1 = j #track start
            q = 1
            print("found star")
            while board[i][j + q] == '*': #while you keep seeing stars
                count +=1 #keep counter going to track length
                temp2 = count #track end
                q += 1
            if count == 1: #no other stars found = no word,  reset
                #print("reset")
                count = 0
            else: # found word
                key += 1
                hash[count] = key #track length and how many words have same length
                for key in hash:
                    if value in hash2.values(): #grab a word that matches that length
                        str = list(hash2.keys())[list(hash2.values()).index(key)]
                        print("here")
                        print(str)
        #print(j)

