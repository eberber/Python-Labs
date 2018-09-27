import numpy

#GLOBAL
node_id = 0

def traverse(board):
    dicHorz = {}
    dicVert = {}
    arrHorz = []
    arrVert = []
    payload = []
    length = 0
    checkpoint = 0
    global node_id

 #horizontal word
    for i in range(len(board)):
        for j in range(len(board[i])):
            start = 0 #reset the start place
            if board[i][j] == '*':
                length += 1
            elif board[i][j] == '.':
                if length > 1:
                    node_id += 1
                    start = j - length
                    end = j -1
                    dicHorz['xCord'] = i
                    dicHorz['yCordStart'] = start
                    dicHorz['yCordEnd'] = end
                    dicHorz['ID'] = node_id
                    arrHorz.append(dicHorz.copy()) #copy data into array
                length = 0

#vertical word
    for j in range(len(board[0])):
        for i in range(len(board)):
            start = 0 #reset the start place
            if board[i][j] == '*':
                length += 1
            elif board[i][j] == '.':
                if length > 1:
                    node_id += 1
                    start = i - length
                    end = i -1
                    dicVert['yCord'] = j
                    dicVert['xCordStart'] = start
                    dicVert['xCordEnd'] = end
                    dicVert['ID'] = node_id
                    arrVert.append(dicVert.copy()) #copy data into array
                length = 0
    return [arrHorz, arrVert];


#MAIN
# name = input("Enter txt file name only:  ")
# try:
#     file = open(name + '.txt')
# except:
#     print("Not a valid file")
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
for i in range(len(board)):
    print(board[i])
val1, val2 = traverse(board)
indexval = 0
# for x in hold:
#     print(x)
for s in val1:
    print(s)
for s in val2:
    print(s)
