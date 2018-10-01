import sys
import time
sys.setrecursionlimit(10000)
#GLOBAL
node_id = 0

def horzBoard(slotx, board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == slotx['xCord'] and j == slotx['yCordStart']:
                x = 0
                while j <= slotx['yCordEnd']:
                    board[i][j] = word[x]
                    x += 1
                    j += 1
                break
    return board

def vertBoard(sloty, board, word):
    for j in range(len(board[0])):
        for i in range(len(board)):
            if j == sloty['yCord'] and i == sloty['xCordStart']:
                x = 0
                while i <= sloty['xCordEnd']:
                    board[i][j] = word[x]
                    x += 1
                    i += 1
                break
    return board


def fillBoard(slot, board, word):
    if word == None:
        print('Not possible')
        return

    for s in range(len(slot)):
        if slot[s]['direction'] == 'h':
            horzBoard(slot[s], board, word[s])
        else:
            vertBoard(slot[s],board,word[s])
    for i in range(len(board)):
        print(board[i])
    return board

def solve(slot, relation, words, family, board):
    #one permuatation is possible
    #if first word fits, collision pts match move on
    #print(words)
    for i in range(len(words)):
        if len(words[i]) != slot[i]['Length']:
            return
    for c in relation:
        parentID = c['P']
        parent = words[parentID]
        childID = c['C']
        child = words[childID]
        parenIndex = c['PC']
        childIndex = c['CC']
        if parent[parenIndex] != child[childIndex]:
            return
    return words

def permutations(slot, relation, words, family):
    prev_word = ''
    if len(words) == 0:
        return []
    if len(words) == 1:
        return [words]
    l = []  # empty list that will store current permutation
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(words)):
        m = words[i]
        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = words[:i] + words[i + 1:]
        # Generating all permutations where m is first
        # element
        for p in permutations(slot, relation, remLst, family):
            l.append([m] + p)
    return l


def collision(arr, arr2):
    flag = False
    match = []
    relation = {}
    relList = []
    slot = []
    parent = {}
    child = {}
    family = []
    t = len(arr) + len(arr2)
    graph = [[False for i in range(t)] for j in range(t)]

    for vert in arr2:
        for horz in arr:#x in range of vert and y in range of horz
            if horz['xCord'] in range(vert['xCordStart'], vert['xCordEnd']) and vert['yCord'] in range(horz['yCordStart'], horz['yCordEnd']):
                match.append({horz['ID']:vert['ID']}) #collision between these two found
                #now find where they collide
                #take vert y cord - vert y cord, horizontal
                yHorz = horz['yCordStart']
                yVert = vert['yCord']
                hPoint = yVert - yHorz
                slot.append(hPoint)
                #take horz x cord - vert x cord, vertical
                xHorz = horz['xCord']
                xVert = vert['xCordStart']
                vPoint = xHorz - xVert
                slot.append(vPoint)
                if horz['xCord'] < vert['yCord']: #choose a parent
                    relation.update({'Parent':horz['ID']})
                    relation.update({'Child':vert['ID']})
                    parent.update({'P': horz['ID']})
                    parent.update({'PC': hPoint})
                    child.update({'C': vert['ID']})
                    child.update({'CC': vPoint})
                    parent.update(child.copy())
                    family.append(parent.copy())
                    relList.append(relation.copy())
                    graph[relation['Parent']][relation['Child']] = True
                elif horz['xCord'] >= vert['yCord']:
                    relation.update({'Parent':vert['ID']})
                    relation.update({'Child':horz['ID']})
                    parent.update({'P': vert['ID']})
                    parent.update({'PC': vPoint})
                    child.update({'C': horz['ID']})
                    child.update({'CC': hPoint})
                    parent.update(child.copy())
                    family.append(parent.copy())
                    relList.append(relation.copy())
                    graph[relation['Parent']][relation['Child']] = True

    return match, slot, relList, graph, family

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
            if board[i][j] == '*' :
                length += 1
            if j ==  len(board[0]) - 1 or board[i][j + 1] == '.' :
                if length > 1:
                    start = j - length + 1
                    end = j
                    dicHorz['xCord'] = i
                    dicHorz['yCordStart'] = start
                    dicHorz['yCordEnd'] = end
                    dicHorz['ID'] = node_id
                    dicHorz['Length'] = (end - start) + 1
                    dicHorz['direction'] = 'h'
                    arrHorz.append(dicHorz.copy()) #copy data into array
                    node_id += 1
                length = 0
    length = 0
#vertical word
    for j in range(len(board[0])):
        for i in range(len(board)):
            start = 0 #reset the start place
            if board[i][j] == '*':
                length += 1
            if i == len(board) -1 or board[i + 1][j] == '.' :
                if length > 1:
                    start = i - length + 1
                    end = i
                    dicVert['yCord'] = j
                    dicVert['xCordStart'] = start
                    dicVert['xCordEnd'] = end
                    dicVert['ID'] = node_id
                    node_id += 1
                    dicVert['Length'] = (end - start) + 1
                    dicVert['direction'] = 'v'
                    arrVert.append(dicVert.copy()) #copy data into array
                length = 0
    return [arrHorz, arrVert];

#MAIN
name = input("Enter txt file name only:  ")
try:
    file = open(name + '.txt')
except:
    print("Not a valid file")
#file = open('puzzle1.txt')
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
data = data[col:] #words
print('Words')
for d in range(len(data)):
    print(data[d], 'Len: ', len(data[d]))
val1, val2 = traverse(board)
print('slots')
for s in val1:
    print(s)
for s in val2:
    print(s)
pairs,point, family, graph, together = collision(val1,val2)
collide = {}
#call to perms is a loop
x = 0
#put all slots together
for v in val2:
    val1.append(v)
start = time.time()
answer = None
for p in permutations(val1, together, data, family):
    answer = solve(val1, together, p, family, board)
    if answer != None:
        break
    x += 1
print('\n')
print('Answer' , answer, '\n')
fillBoard(val1, board, answer)
end = time.time()
print('Time: ', end - start)
