from PIL import Image
import time
import queue


class Hman(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __eq__(self, other):
        return 0

    def __lt__(self, other):
        if type(self) == str:
            return self
        return 0

    def children(self):
        return self.left, self.right


def create_freq_table():
    img = Image.open("flag.bmp")
    #img.show()
    width, height = img.size
    px = img.load()
    count_bits = 0
    dict = {}
    total = 0
    for x in range(width):
     for y in range(height):
        #print(px[x,y]) #gives rgb value at each pt
        r, g, b = px[x, y]# 100, 0 , 200

        if r in dict.keys():
            dict[r] += 1
        else:
            dict[r] = 1
        if g in dict.keys():
            dict[g] += 1
        else:
            dict[g] = 1
        if b in dict.keys():
            dict[b] += 1
        else:
            dict[b] = 1
        count_bits += 1
    count_bits = count_bits * 24
    compare = dict
    for i in dict.values():
        total += i
    temp = 0
    tuple = ()
    list = []
    for i, j in dict.items():
        dict[i] = j/total
        temp += dict[i]
        tuple = (dict[i], i)
        list.append(tuple)
    return list, compare, count_bits


def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             # and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = Hman(l, r)        # 2b. create internal node with children
        p.put((l[0]+r[0], node)) # 2c. add new node to queue
        #print('HERE', l,r)
    return p.get()               # 3. tree is complete - return root node


# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], Hman):
        walk_tree(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],Hman):
        walk_tree(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return code


def compress(code):
    img = Image.open("flag.bmp")
    width, height = img.size
    px = img.load()
    bit_list = []
    for x in range(width):
        for y in range(height):
            r, g, b = px[x, y]
            if r in code.keys():
                bit_list.append(code[r])
            if g in code.keys():
                bit_list.append(code[g])
            if b in code.keys():
                bit_list.append(code[b])
    f = open("result.txt", "w+")
    total_compress_bits = 0
    for k in bit_list:
        f.write("%s" % k)
        total_compress_bits += len(k)
    return total_compress_bits


def compression_ratio(compare, code):
    avg_bits = 0.0
    for i, j in compare.items():
        if i in code.keys():
           avg_bits += j * len(code[i])
    return avg_bits


def decompress(file):
    #read in the file and map the bits using the table
    with open(file, "r") as f:
        contents = f.read()
        print(contents)


freq, compare, count_bits = create_freq_table()

"""freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'),
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'),
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z')]"""

node = create_tree(freq)
code = walk_tree(node)
total_compress_bits = compress(code)
avg_bits = compression_ratio(compare, code)

print("RGB          FREQUENCY        BIT MAP")
print("_____________________________________")
for i in sorted(freq, reverse=True):
    print(i[1], '   {:6.20f}'.format(i[0]), code[i[1]])
print("\nRequired bits for fixed length: ", count_bits)
print("Required bits for Compression: ", total_compress_bits)
avg_bits = (8-avg_bits)/8 * 100
avg_bits = 100 - avg_bits
print("Compression Ratio: ", round(avg_bits, 2), "%")