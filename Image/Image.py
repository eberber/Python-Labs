from PIL import Image
import time
import queue
#AUTHOR: Edgar Berber
compare_me = []
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

def create_freq_table(file_path):
    img = Image.open(file_path, 'r')
    #img.show()
    width, height = img.size
    px = img.load()
    count_bits = 0
    dict = {}
    total = 0
    w = range(width)
    h = range(height)
    for x in w:
     for y in h:
        #print(px[x,y]) #gives rgb value at each pt
        r, g, b = px[x, y]
        compare_me.append(r)
        compare_me.append(g)
        compare_me.append(b)
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
    return list, compare, count_bits, file_path


def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    # create node from freq table, add to queue
        p.put(value)
    while p.qsize() > 1:
        l, r = p.get(), p.get()  # remove two smallest nodes, priority queue sorts at each get
        node = Hman(l, r)        # create internal node OBJECT with children
        p.put((l[0]+r[0], node)) # add new node object to queue using the combined frequencies of the l and r
    return p.get()               # return root node

# Recursively assign bit value to each rgb number
def encode(node, bits="", code={}):
    if isinstance(node[1].left[1], Hman):
        encode(node[1].left, bits+"0", code)
    else:
        code[node[1].left[1]] = bits+"0"
    if isinstance(node[1].right[1],Hman):
        encode(node[1].right, bits+"1", code)
    else:
        code[node[1].right[1]] = bits+"1"
    return code

def compress(code, file_path):
    img = Image.open(file_path)
    width, height = img.size
    px = img.load()
    bit_list = []
    w = range(width)
    h = range(height)
    for x in w:
        for y in h:
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
        f.write("%s\n" % k)
        total_compress_bits += len(k)
    return total_compress_bits

def compression_ratio(compare, code):
    avg_bits = 0.0
    for i, j in compare.items():
        if i in code.keys():
           avg_bits += j * len(code[i])
    return avg_bits

def decompress(file, code, file_path):
    #read in the file and map the bits using the table
    list = []
    with open(file, "r") as f:
        for line in f:
            for i, j in code.items():
                if line.rstrip() == j:
                    list.append(i) #we know all bits are unique so on match break
                    break
    img = Image.open(file_path)
    width, height = img.size
    w = range(width)
    h = range(height)
    count = 0
    img.show()
    px = img.load()
    for i in w:
        for j in h: #grab each pixel and replace it with the rgb values from our list
            px[i,j] = (list[count], list[count+1], list[count+2]) #order should be the same
            count += 3 #change this value to a 1 for proof the image displayed was modified
    img.show()
    return list

#default path
file_path = "C:/Users/eberber97/Documents/Projects/Python-Labs/Image/colors.bmp" #input("Enter image path: ")
start = int(round(time.time() * 1000))
freq, compare, count_bits, file_path = create_freq_table(file_path)

node = create_tree(freq)
code = encode(node)
total_compress_bits = compress(code, file_path)
avg_bits = compression_ratio(compare, code)
file = "result.txt"
rgb_point_list = decompress(file, code, file_path)
end = int(round(time.time() * 1000))
time = end - start

print("\nRGB          FREQUENCY        BIT MAP")
print("_____________________________________")
for i in sorted(freq, reverse=True):
    print(i[1], '   {:6.20f}'.format(i[0]), code[i[1]])
print("\nRequired bits for fixed length: ", count_bits)
print("Required bits for Compression: ", total_compress_bits)
avg_bits = (8-avg_bits)/8 * 100 #8 bits per component of pixel, gives % compressed
avg_bits = 100 - avg_bits #take % compressed - original (always 100%)
print("Compression Ratio: ", round(avg_bits, 2), "%")
#time = int(time/1000.0)
print("Time for execution in msecs: ", time)
print("NOTE: The first image displayed was the original, the second was the image AFTER compression and decompression")