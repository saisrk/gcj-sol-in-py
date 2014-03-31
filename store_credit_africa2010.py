def creditCalc(tc, noi, items):
    """This Method will take in the credit, total items and all items.
    Then manipulate and send the index of the items need to be 
    bought with the credit in hand
    @param tc: Total credit in hand
    @param noi: Number of items in the store
    @param items: List of values of all items in store
    @return: Tuple specifying the index of two items need to be bought
    """
    new_list = [int(i) for i in items]
    for i in xrange(len(new_list)):
        for j in new_list[i+1:]:
            tot = new_list[i] + j
            if tot == tc:
                return (i+1, ((new_list[i+1:].index(j))+(i+1)+1))
            
    
if __name__ == '__main__':
    with open('A-large-practice.in', 'r') as fp:
        testcases = int(fp.readline())
        for testcase in xrange(testcases):            
            tot_credit = int(fp.readline())
            no_of_items = int(fp.readline())
            items = fp.readline().split()
            result = creditCalc(tot_credit, no_of_items, items)
            print "Case #%d: %d %d" % (testcase+1, result[0], result[1])
