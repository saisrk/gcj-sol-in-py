def reverse(line):
    """This Method will take the input line, split it 
    and join after reversing
    @param line: The line taken from the file
    @return: The reversed line
    """
    return ' '.join(line.split()[::-1])

try:
    fp = open('B-large-practice.in', 'r')
    testcases = int(fp.readline())
    for tc in xrange(testcases):        
        print "Case #%d: %s" % (tc+1, reverse(fp.readline().strip()))

except Exception:
    print "Unable to work with the file"

finally:
    fp.close()
