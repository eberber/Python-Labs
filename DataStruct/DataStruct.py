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
        #print("Counter for pops.csv: ", count)
with open('queries.txt', 'r') as mapping:
    for store in mapping:
        print(store)
        # for k, v in Dict.items():
        #     print(store, k)
        #     if store == k:
        #         print(k, ":", v)
end = time.time()
print("Execution time in seconds to read and map values: ", end - start)