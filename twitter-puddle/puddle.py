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
                pass
        else:
            p_r = p_r - 1
            if testcase[p_r] >= max_r:
                max_r = testcase[p_r]
            else:
                volume = volume + (max_r - testcase[p_r])
                pass
        pass
    pass

    return volume

testcase_1 = [2,5,1,2,3,4,7,7,6]
testcase_2 = [2,5,1,3,1,2,1,7,7,6]
testcase_3 = [6,1,4,6,7,5,1,6,4]
print "case %s total volume : %s " % (testcase_1, calculate(testcase_1))
print "case %s total volume : %s " % (testcase_2, calculate(testcase_2))
print "case %s total volume : %s " % (testcase_3, calculate(testcase_3))