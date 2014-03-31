def formKeyStrokes(sent):
    """This Method is to identify the proper key strokes made seeing 
    the corresponding alphabet in string. The phonebutton structure 
    is maintained as a dictionary. 
    @param sent: The sentence for which the set of keystrokes must be generated
    @return numstring: The series of key press generated according to sentence
    """
    prev_button = None
    numstring = ''
    pause = ' '
    num_to_alpha_dict = {'2': 'abc', '3': 'def', '4': 'ghi', 
                         '5': 'jkl', '6': 'mno', '7': 'pqrs', 
                         '8': 'tuv', '9': 'wxyz', '0': ' '}
    for each_char in sent:
        for button, alpha_set in num_to_alpha_dict.items():
            if each_char in alpha_set:
                if prev_button == button:
                    numstring = numstring + pause
                key_press_count = alpha_set.index(each_char) + 1
                numstring = numstring + (button * key_press_count)
                prev_button = button
                break
    return numstring

try:
    fp = open('C-small-practice.in', 'r')
    tcs = int(fp.readline())
    for tc in xrange(tcs):
        print "Case #%d: %s" % (tc+1, formKeyStrokes(fp.readline()))

except Exception, e:
    print "Unable to work with the file provided", e

finally:
    fp.close()
