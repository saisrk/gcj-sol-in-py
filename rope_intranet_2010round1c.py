def getNoOfIntersections(wlist):
    """This Method will calculate the number of intersections in a ingenius way.
    The comparison is done in dual fashion after sorting and in each intersection
    the count is increased.
    @param wlist: The list containing the points
    @return intersections: Number of times lines meeting
    """
    intersections = 0
    if len(wlist) < 2:
        return intersections

    wlist.sort(key=lambda x: x[0])
    for i in xrange(len(wlist)):
        for each in wlist[i+1:]:
            if wlist[i][0] < each[0] and wlist[i][1] < each[1]:
                continue
            if wlist[i][0] < each[0] and wlist[i][1] > each[1]:
                intersections += 1
            elif wlist[i][0] > each[0] and wlist[i][1] < each[1]:
                intersections += 1

    return intersections

try:
    fp = open('A-large-practice.in', 'r')
    tcs = int(fp.readline())
    for tc in xrange(tcs):
        wire_list = []
        no_of_wires = int(fp.readline())
        for wire_ct in xrange(no_of_wires):
            wire_list.append([int(i) for i in fp.readline().strip().split()])
        print "Case #%d: %d" % (tc+1, getNoOfIntersections(wire_list))

except Exception, e:
    print "Exception Occurred", e

finally:
    fp.close()
