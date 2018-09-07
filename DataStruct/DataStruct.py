import time

print("Opening populations.csv...")
print("Following is read in file using hash tables (Dictionaries in python).")
words = []
Dict = {}
start =  time.time()
with open('populations.csv', 'r') as myself:
    for word in myself:
        words = word.split(",")
        Dict[words[0]] = words[1]
for k, v in Dict.items():
    print(k, ":", v)
end = time.time()
print("Execution time in seconds to read and map values: ", end - start)