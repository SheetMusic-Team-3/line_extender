

def line_extendor(file):
    opened = open(file, "r")
    data = [[float(n) for n in line.split()] for line in opened]

    for i in range(len(data)):
        data[i][1] = 0
        data[i][3] = 1

        
