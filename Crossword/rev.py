def check(n):
    if n ==0:
        return False
    while n != 1:
        if n % 3 != 0:
            return False
        n = n // 3
    return True

print(check(9))

def change(str):
    length = 0
    for i in str:
        length = length +1
    print(length)

change('hello')

def count(str):
    dict = {}
    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(count('google.com'))

def add(str1, str2):
    t = str1[0]
    t2 = str2[0]
    str2.replace(str2[0], t)
    str1.replace(str1[0], t2)
    str1 = str1 + str2
    return  str1
print(add('abc', 'xyz'))

text = 'abcdefg'
text = text[1:1] + text[:4]
print(text)
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
