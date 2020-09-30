def hammingdistance(hex1, hex2):
    x = str(bin(int(hex1, 16))[2:])
    y = str(bin(int(hex2, 16))[2:])
    z = 0
    counter = 0
    if len(x) > len(y):
        y = "{:0>{s}}".format(y, s=len(x))
    elif len(y) > len(x):
        x = "{:0>{s}}".format(x, s=len(y))

    while z < len(x):
        if x[z] != y[z]:
            counter += 1
        z += 1
    return counter