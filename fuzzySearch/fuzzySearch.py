def shiftTable(pattern):
    table = []
    map = {}
    alphabet = []
    patt = []
    # m is len of pattern
    for i in range(len(pattern)):
        patt.append(pattern)
        if pattern[i] not in map.keys():
            map.update({pattern[i] : 1})
    for key in map:
        alphabet.append(key)
    print(alphabet)
    for i in range(len(pattern) - 1):
        table[i] = len(pattern)
        for j in range(len(pattern) - 2):
            table[patt[j]] = len(pattern) - 1 - j
    print(pattern)
    return table

with open('dictionary.txt') as file:
    data = file.read()
print(data)
phrase = input("Enter a phrase to search for: ")
print("Word is : ", phrase, "\n length: ", len(phrase))
shiftTable(phrase)