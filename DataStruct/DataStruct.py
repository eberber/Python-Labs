import time

print("Opening populations.csv...")
print("Following is read in file using dictionaries")
words = []
Dict = {}
count = 0
with open('populations.csv', 'r') as myself:
    for word in myself:
        words = word.split(",")
        Dict[words[0]] = words[1]
        count += 1
print("Reading in queries.txt...")
lines = [line.rstrip('\n') for line in open('queries.txt')]
# print("Starting timer")
# start = time.time()
# for x in lines:
#     if x in Dict.keys():
#         print(x, ":", Dict[x])
# end = time.time()
# print("Execution time in seconds to read and map values: ", end - start)
print("Starting second data structure: sets")
ds2 = set([])
with open('populations.csv', 'r') as myself:
    for word in myself:
        ds2 = word.split(",")
with open('queries.txt', 'r') as query:
    for look in query:
        print(ds2[0])
        if look in ds2[0]:
            print(look, ":", ds2[1])







