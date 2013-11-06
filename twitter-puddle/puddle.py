# CuGBabyBeaR

def calculate(testcase):
    p_l = 0 
    p_r = len(testcase) - 1
    max_l = testcase[p_l]
    max_r = testcase[p_r]

    volume = 0
    while p_r > p_l :
        if max_l < max_r:
            p_l = p_l + 1
            if testcase[p_l] >= max_l:
                max_l = testcase[p_l]
            else:
                volume = volume + (max_l - testcase[p_l])
        else:
            p_r = p_r - 1
            if testcase[p_r] >= max_r:
                max_r = testcase[p_r]
            else:
                volume = volume + (max_r - testcase[p_r])

    return volume

if __name__ == '__main__':
    testcases = [
    ([1,0,1], 1),
    ([2,0,1], 1),
    ([0,1,0,1,0], 1),
    ([1,0,1,0], 1),
    ([1,0,1,2,0,2], 3),
    ([2,5,1,2,3,4,7,7,6],10),
    ([2,5,1,3,1,2,1,7,7,6],17),
    ([6,1,4,6,7,5,1,6,4],13),
    ([2,5,1,2,3,4,7,7,6],10),
    ([5,1,0,1],1),
    ([2,5,1,2,3,4,7,7,6,3,5], 12),
    ]

    for testcase in testcases:
        v = calculate(testcase[0])
        if v == testcase[1]:
            print "Correct: %s total volume is : %s" % (testcase[0],v)
        else:
            print "Incorrect: %s total volume is : %s , shoule be %s" % (testcase[0],v,testcase[1])

