str = 'morning'
t =''
t1 = ''
dup = ''
dict= {}
for i in range(len(str)):
    t = str[i]
    print(t)
    dict[t] = 1
    if t in dict.keys():
        hold = dict.get(t)
        dict.get() = hold +1
for j in dict.items():
    if dict.values() == 1:
        print(dict.keys())