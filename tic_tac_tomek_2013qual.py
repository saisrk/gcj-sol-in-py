def checkResult(board):
    """This Method will check the result of the board that is presented.
    The methods checks each row, each column and both diagonals for the 
    X, O players winning.
    @param board: The dictionary which depicts the board and player status
    @return: Returns X won, O won or Neutral
    """
    null_count = 0
    res_string = ''
    for row in board.keys():
        if ((board[row].count('X') == 3 and board[row].count('T') == 1) or (board[row].count('X') == 4)):
            return "X won"
        elif ((board[row].count('O') == 3 and board[row].count('T') == 1) or (board[row].count('O') == 4)):
            return "O won"
        null_count = null_count + board[row].count('.')

    for i in xrange(4):
        for j in xrange(1, 5):
            res_string = res_string + board[j][i]
        if ((res_string.count('X') == 3 and res_string.count('T') == 1) or (res_string.count('X') == 4)):
            return "X won"
        elif ((res_string.count('O') == 3 and res_string.count('T') == 1) or (res_string.count('O') == 4)): 
            return "O won"
        res_string = ''

    diagonal1 = board[1][0] + board[2][1] + board[3][2] + board[4][3]
    diagonal2 = board[4][0] + board[3][1] + board[2][2] + board[1][3]

    if ((diagonal1.count('X') == 3 and diagonal1.count('T') == 1) or (diagonal1.count('X') == 4)):
        return "X won"
    elif ((diagonal1.count('O') == 3 and diagonal1.count('T') == 1) or (diagonal1.count('O') == 4)):
        return "O won"
    elif ((diagonal2.count('X') == 3 and diagonal2.count('T') == 1) or (diagonal2.count('X') == 4)):
        return "X won"
    elif ((diagonal2.count('O') == 3 and diagonal2.count('T') == 1) or (diagonal2.count('O') == 4)):
        return "O won"

    if null_count > 0:
        return "Game has not completed"
    else:
        return "Draw"

try:
    ttt_board = {}
    fp = open('A-large-practice.in', 'r')
    tcs = int(fp.readline())
    for tc in xrange(tcs):
        for row in xrange(4):
            data = fp.readline().strip()
            if len(data) == 0:
                data = fp.readline().strip()
            ttt_board[row+1] = data
        print "Case #%d: %s" % (tc+1, checkResult(ttt_board))

except Exception, e:
    print "Exception has occurred", e

finally:
    fp.close()
