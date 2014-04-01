import math

def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
    
def findSqPalindrome(start, end):
    count = 0
    for number in xrange(start, end+1):
        if palindrome(number):
            sqrt = math.sqrt(number)
            if not sqrt.is_integer():
                continue
            if palindrome(int(sqrt)):               
                count += 1

    return count
        
try:
    with open('C-large-practice-1.in', 'r') as fp:
        tcs = int(fp.readline())
        for tc in xrange(tcs):
            start, end = [int(i) for i in fp.readline().split()]
            print "Case #%d: %d" % (tc+1, findSqPalindrome(start, end))

except Exception, e:
    print "Exception occurred", e
