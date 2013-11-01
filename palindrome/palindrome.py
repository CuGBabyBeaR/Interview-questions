import string

def check(str_in):
    _unnecessary = string.punctuation + ' '
    str_in = str_in.lower()
    str_in = str_in.translate(string.maketrans('', ''), _unnecessary)
    length = len(str_in)

    for i in range(0,length/2):
        if str_in[i] != str_in[length - i -1]:
            return False
            pass
        pass
    return True
    pass

testcases = list()
testcases.append("apple")
testcases.append("level")
testcases.append("Madam, I\'m Adam.")
testcases.append("the quick brown fox jumps over the lazy dog")

for case in testcases:
    print "Case \"%s\" is %sa palindrome." % (case, "" if check(case) else "NOT " )
    pass