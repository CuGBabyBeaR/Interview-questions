def sOrder(matrix=None, reverse=False):
    if not matrix:
        return
    for l in matrix:
        if reverse:
            for c in l[::-1]:
                print "%4d" % c ,
        else:
            for c in l:
                print "%4d" % c ,
        reverse =  not reverse

def nOrder(matrix=None, reverse=False):
    if not matrix:
        return

    for x in xrange(0,len(matrix[0])):
        if reverse:
            for y in xrange(len(matrix)-1,-1,-1):
                print "%4d" % matrix[y][x],
        else:
            for y in xrange(0,len(matrix)):
                print "%4d" % matrix[y][x],
        reverse =  not reverse

def spiralOrder(matrix=None, clockwise=True, startpoint = "lt"):
    if not matrix:
        return

    startrow = 0
    startcol = 0
    endrow = len(matrix)-1
    endcol =len(matrix[0])-1

    if startpoint == "lt":
        x_start, y_start = 0, 0
        heading = 0 if clockwise else 1
    elif startpoint == "rt":
        x_start, y_start = endcol, 0
        heading = 1 if clockwise else 2
    elif startpoint == "rb":
        x_start, y_start = endcol, endrow
        heading = 2 if clockwise else 3
    elif startpoint == "lb":
        x_start, y_start = 0, endrow
        heading = 3 if clockwise else 0
    else:
        return
    x = x_start
    y = y_start

    flag = True
    while flag:

        for i in xrange(0,5):

            if startrow > endrow:
                flag = False
                break 
            if startcol > endcol:
                flag = False
                break 
                
            if clockwise:
                if heading == 0: # right
                    for x in xrange(startcol, endcol+1):
                        print "%4d" % matrix[y][x],
                    startrow = startrow + 1
                elif heading == 1: # down
                    for y in xrange(startrow,endrow+1):
                        print "%4d" % matrix[y][x],
                    endcol = endcol - 1
                elif heading == 2: # left
                    for x in xrange(endcol,startcol-1,-1):
                        print "%4d" % matrix[y][x],
                    endrow = endrow - 1
                elif heading == 3: # up
                    for y in xrange(endrow,startrow-1,-1):
                        print "%4d" % matrix[y][x],
                    startcol = startcol + 1
                heading = (heading+1) % 4

            else :
                if heading == 0: # right
                    for x in xrange(startcol, endcol+1):
                        print "%4d" % matrix[y][x],
                    endrow = endrow - 1
                elif heading == 1: # down
                    for y in xrange(startrow,endrow+1):
                        print "%4d" % matrix[y][x],
                    startcol = startcol + 1
                elif heading == 2: # left
                    for x in xrange(endcol,startcol-1,-1):
                        print "%4d" % matrix[y][x],
                    startrow = startrow + 1
                elif heading == 3: # up
                    for y in xrange(endrow,startrow-1,-1):
                        print "%4d" % matrix[y][x],
                    endcol = endcol -1
                heading = (heading-1) % 4

if __name__ == "__main__":
    testcase = [
    range(1,5),
    range(5,9),
    range(9,13),
    range(13,17),
    range(17,21),
    range(21,25),
    ]
    for l in testcase:
        for c in l:
            print "%4d" % c ,
        print ""
    print "\n\n====================== S-Order ========================"
    sOrder(testcase)
    print "\n\n================== S-Order reverse ===================="
    sOrder(testcase,True)
    print "\n\n====================== N-Order ========================"
    nOrder(testcase)
    print "\n\n================== N-Order reverse ===================="
    nOrder(testcase,True)
    print "\n\n===== Spiral-Order clockwise right-bottom-started ====="
    spiralOrder(testcase,startpoint="rb")
    print "\n\n==== Spiral-Order anti-clockwise right-top-started ===="
    spiralOrder(testcase,False,"rt")

