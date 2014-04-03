def translate(googlese):
    gle_eng_mapping = {'y': 'a', 'n': 'b', 'f': 'c', 'i': 'd', 'c': 'e',
                       'w': 'f', 'l': 'g', 'b':'h', 'k': 'i' , 'u': 'j',
                       'o': 'k', 'm': 'l', 'x': 'm', 's': 'n', 'e': 'o',
                       'v': 'p', 'z': 'q', 'p': 'r', 'd': 's', 'r': 't',
                       'j': 'u', 'g': 'v', 't': 'w', 'h': 'x', 'a': 'y',
                       'q': 'z', ' ': ' '}
    english = ''
    for each in googlese:
        english = english + gle_eng_mapping[each]

    return english

try:
    with open('A-small-practice.in', 'r') as fp:
        tcs = int(fp.readline())
        for tc in xrange(tcs):
            googlese = fp.readline().strip('\n')
            print "Case #%d: %s" % (tc+1, translate(googlese))
    
except Exception, e:
    print "Exception: ", e
