def find_center(arr):
    sums = []
    sums.append(map(sum, [[r[col] for r in arr] for col in range(0,len(arr))])) # get the sum in Y deriction
    sums.append(map(sum, arr))                                                  # get the sum in X deriction
    
    center = [float(sum((sum_[i]*i for i in range(0,len(sum_))))) / sum(sum_) for sum_ in sums] 
    # calculation of 2 weighted means 

    return center
    pass

testcase_1 = [
[1,3,2,4,5], # 15
[2,4,3,2,1], # 12
[5,7,3,4,1], # 20
[7,6,8,5,4], # 30
[6,5,4,3,5], # 23
]
#21,25,20,18,16
print "Case 1 point of equilibrium is %s " %  (find_center(testcase_1))

