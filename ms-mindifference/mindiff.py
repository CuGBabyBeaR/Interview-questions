# Basically, depending on the sorting algorithm

def mindiff(array):
    arr = sorted(array)
    minvalue = abs(arr[1] - arr[0])

    for i in xrange(1,len(arr)-2):
        diff = abs(arr[i+1] - arr[i])
        if minvalue > diff :
            minvalue = diff
            pass
        pass
    pass

    return minvalue

testcase_1 = [32,4,1,2,45,6,7,543,2]
testcase_2 = [-23,-1,-4,-2,-53,-2,-123]
testcase_3 = [234,334,-233,-412,-543,-2345,534,-76,-346,432]

print "Case %s , min diff is : %s." % (testcase_1, mindiff(testcase_1))
print "Case %s , min diff is : %s." % (testcase_2, mindiff(testcase_2))
print "Case %s , min diff is : %s." % (testcase_3, mindiff(testcase_3))
