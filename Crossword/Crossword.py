import numpy

#GLOBAL
node_id = 0

#def solve(horz , vert, words , collision, answer):
def permutations(slot, together, words, family):
    if len(slot) == 0:
        return []
    #If there is only one element in lst then, only
    #one permuatation is possible
    if len(slot) == 1:
        for x in words:
                if len(x) == slot[0]['Length']: # if word fits
                    flag = True
                    for z in family:
                            if together[0]['C'] == y['ID']:
                                temp = together['PC']
                                temp2 = together['CC']
                                if temp == temp2:
                                    flag = False
                                    break

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
                    family.append(parent.copy())
                    family.append(child.copy())
                    relList.append(relation.copy())
                    graph[relation['Parent']][relation['Child']] = True
                elif horz['xCord'] >= vert['yCord']:
                    relation.update({'Parent':vert['ID']})
                    relation.update({'Child':horz['ID']})
                    parent.update({'P': vert['ID']})
                    parent.update({'PC': vPoint})
                    child.update({'C': horz['ID']})
                    child.update({'CC': hPoint})
                    family.append(parent.copy())
                    family.append(child.copy())
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
    print("Offset point: ",y)
for z in family:
    print(z)
print(graph)
for i in together:
    print(i)
permutations(slot, together, data, family)
#solve(val1 , val2, data , colRelation, None)

