import sys
sys.setrecursionlimit(10000)
#GLOBAL
node_id = 0
def horzBoard(slotx, board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == slot['xCord'] and j == slot['yCordStart']:
                x = 0
                while j < slot['yCordEnd']:
                    board[i][j] = word[x]
                    x += 1
                    j += 1
                break
    for i in range(len(board)):
        print(board[i])
    return board


def vertBoard(sloty, board, word):
    for j in range(len(board[0])):
        for i in range(len(board)):
            if j == slot['yCord'] and i == slot['xCordStart']:
                x = 0
                while i < slot['xCordEnd']:
                    board[i][j] = word[x]
                    x += 1
                    i += 1
                break
    for i in range(len(board)):
        print(board[i])
    return board

def solve(slot, relation, words, family, board):
    #one permuatation is possible
    #if first word fits, collision pts match move on
    for f in range(len(relation)):
        for s in range(len(slot)):
            if f['P'] == slot[s]['ID']:
                for w in range(len(words)):
                    if len(words[w]) == s['Length']:
                        #now does child fit?
                        for sl in range(len(slot)):
                            if f['C'] == slot[sl]['ID']:
                                for wl in range(len(words)):
                                    if len(words[wl]) == sl['Length']:
                                        #check offset
                                        if words[w][f['PC']] == words[wl][f['CC']]:
                                            #add word to board, first parent
                                            if 'xCord' in slot[s]:
                                                return horzBoard(slot[s], board, words[w])
                                            elif 'yCord' in slot[s]:
                                                return vertBoard(slot[s], board, words[w])
                                            #add child
                                            if 'xCord' in slot[sl]:
                                                return horzBoard(slot[sl], board, words[wl])
                                            elif 'yCord' in slot[sl]:
                                                return vertBoard(slot[sl], board, words[wl])
                                        else: return #check another loop




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
    print(graph)

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
            if board[i][j] == '*':
                length += 1
            elif board[i][j] == '.':
                if length > 1:
                    start = j - length
                    end = j -1
                    dicHorz['xCord'] = i
                    dicHorz['yCordStart'] = start
                    dicHorz['yCordEnd'] = end
                    dicHorz['ID'] = node_id
                    dicHorz['Length'] = end - start
                    arrHorz.append(dicHorz.copy()) #copy data into array
                    node_id += 1
                length = 0

#vertical word
    for j in range(len(board[0])):
        for i in range(len(board)):
            start = 0 #reset the start place
            if board[i][j] == '*':
                length += 1
            elif board[i][j] == '.':
                if length > 1:
                    start = i - length
                    end = i -1
                    dicVert['yCord'] = j
                    dicVert['xCordStart'] = start
                    dicVert['xCordEnd'] = end
                    dicVert['ID'] = node_id
                    node_id += 1
                    dicVert['Length'] = end - start
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
data = data[col:] #words
for i in range(len(board)):
    print(board[i])
for d in range(len(data)):
    print(data[d], 'Len: ', len(data[d]))
val1, val2 = traverse(board)
for s in val1:
    print(s)
for s in val2:
    print(s)
pairs,slot, family, graph, together = collision(val1,val2)
collide = {}
print(type(slot))
for x in pairs:
     print('Collision ID pairs: ', x)
for y in slot:
    print("Offset point: ", y)
print('Relation')
for z in family:
    print(z)
print('Together')
for i in together:
    print(i)
#call to perms is a loop
x = 0
for p in permutations(slot, together, data, family):
    print(p)
    print('\n DONE  \n', x )
    solve(slot, together, p, family, board)
    x += 1

#solve(val1 , val2, data , colRelation, None)

