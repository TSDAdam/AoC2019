values = ''
layers = []
layer = []
image = []
width = 25
height = 6
pixels_per_layer = width * height

f = open('d:/8.in.txt', 'r')
for line in f:
    for c in line:
        values += c

first = 0
last = pixels_per_layer

for i in range(0, int(len(values) / pixels_per_layer)):
    layers.append(values[first:last])
    first = last
    last += pixels_per_layer


for i in range(0, pixels_per_layer):
    thispixel = " "
    for n in range(0, len(layers)):
        if layers[n][i] == '0':
            thispixel = ' . '
            break
        elif layers[n][i] == '1':
            thispixel = " 0 "
            break
    image.append(thispixel)


first = 0
last = width 
print("") 
for row in range(0, height):
    thisrow = "".join(image[first:last])
    print(thisrow)
    first = last
    last += width