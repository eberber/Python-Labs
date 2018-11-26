from  PIL import Image
import time
#def freq_table(point):


img = Image.open("powercat.bmp")
#img.show()
width, height = img.size
px = img.load()
count_bits = 0
for x in range(width):
 for y in range(height):
    print(px[x,y]) #gives rgb value at each pt
    count_bits+=1
count_bits = count_bits * 24
print("Required bits for fixed length: ", count_bits)
t = px[0,0]
print(t)