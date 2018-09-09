import time


print("Opening populations.csv...")
print("Following is read in file using dictionaries")
words = []
Dict = {}
count = 0
l1 = []
l2 = []
l3 = []
hun1 = 0.0
hun2 = 0.0
with open('populations.csv', 'r') as myself:
    for word in myself:
        words = word.split(",")
        Dict[words[0]] = words[1]
        l1.append(words[0])
        l3.append(words[1])
        count += 1
l3 = [i.strip('\n') for i in l3]
print("Reading in queries.txt...")
lines = [line.rstrip('\n') for line in open('queries.txt')]
print(type(lines))
print("Starting timer")
z = 0
start = time.time()
for x in lines:
    if x in Dict.keys():
        print(x, ":", Dict[x])
    if z == 100:
        grab = time.time()
        hun1 = grab - start
    z += 1
end = time.time()
final = end - start
print("Execution time in seconds to read and map values: ", final)


print("Starting second data structure: stack")
q = 0
y = 0
print("Starting timer")
start = time.time()
while q < len(lines):
    same = lines[q]
    while y < len(l3):
        if same == l1[y]:
            print(same, ":", l3[y])
        y += 1
    if q == 100:
        grab = time.time()
        hun2 = grab - start
    y = 0
    q += 1
end = time.time()
print("First data struct in seconds: ", final, "Second data struct in seconds: ", end - start)
print("If only 100 values read, data struct 1: ", hun1, "data struct 2: ", hun2)








