def getMinScalarProd(xlist, ylist):
    """This Method will take the two x coordinates and y coordinates and 
    get the Minimum scalar product.
    x = (x1, x2, x3, ..., xn) ; y = (y1, y2, ..., yn)
    scalar product = x1y1 + x2y2 + .... + xnyn
    For minimum we sort the two lists in ascending and descending orders 
    and compute the product respectively.
    @param xlist: The list containing x coordinates
    @param ylist: The list containing y coordinates
    @return min_prod: The minimum scalar product of two coordinates
    """
    sum = 0
    xlist.sort()
    ylist.sort(reverse=True)
    for count in xrange(len(xlist)):
        sum = sum + (xlist[count] * ylist[count])
    return sum

try:
    fp = open('A-large-practice.in', 'r')
    tcs = int(fp.readline())
    for tc in xrange(tcs):
        listcount = fp.readline()
        x_list = [int(i) for i in fp.readline().split()]
        y_list = [int(j) for j in fp.readline().split()]
        print "Case #%d: %d" % (tc+1, getMinScalarProd(x_list, y_list))

except Exception, e:
    print "Unable to read the file", e

finally:
    fp.close()
