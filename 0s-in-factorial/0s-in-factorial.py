def getZeros(n):
    res = 0
    d = 5
    while d <= n:
        res = res + n / d
        d = d * 5
    
    return res

if __name__ == "__main__":
    testcases = [
    (100,24),
    (1000,249),
    (5000,1249),
    ]

    for testcase in testcases:
        num = getZeros(testcase[0])
        if num == testcase[1]:
            print "Currect. In the end of %s!, there are %s 0s." % (testcase[0], num)
        else:
            print "Incurrect. In the end of %s!, there should be %s 0s , result is %s." % (testcase[0], testcase[1], num)
