import time

print("Opening populations.csv...")
print("Following is read in file using hash tables (Dictionaries in python).")
words = []
Dict = {}
start = time.time()
count = 0
with open('populations.csv', 'r') as myself:
    for word in myself:
        words = word.split(",")
        Dict[words[0]] = words[1]
        count += 1
print("Reading in queries.txt...")
lines = [line.rstrip('\n') for line in open('queries.txt')]
for x in lines:
    if x in Dict.keys():
        print(x, ":", Dict[x])
end = time.time()
print("Execution time in seconds to read and map values: ", end - start)