import numpy
#def findChild(x,y,boolean):
def find_star_one(board):
    payload = []
    isHorz = False
    word = 'word'
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '*':
                if((j + 1) < len(board[i]) and board[i][j+1] == '*'): #not out of bounds
                    payload.append(i)
                    payload.append(j)
                    payload.append(True)
                    return payload

def traverse(x, y , bool, board):
    arr = []
    start = 0
    if bool == True: #horizontal word
        for i in range(x,len(board)):
            for j in range(y, len(board[i])):
                if board[i - 1][j] > x and board[i][j] == '*':
                    k = i
                    while k > x : #traverse up within range
                        k = k - 1

    #else:
        # for i in range(x,len(board)):
        #     for j in range(y, len(board[i])):


#MAIN
name = input("Enter txt file name only:  ")
try:
    file = open(name + '.txt')
except:
    print("Not a valid file")
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
star_one = find_star_one(board)
print(star_one)
traverse(star_one[0], star_one[1],star_one[2], board)


