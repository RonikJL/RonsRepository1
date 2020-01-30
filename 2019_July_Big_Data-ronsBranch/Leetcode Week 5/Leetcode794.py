class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        turn = 0
        row = [0] * 3
        col = [0] * 3
        diag = 0
        antiDiag = 0

        for i in range(3):
            for j in range(3):
                if (board[i][j] == "X"):
                    turn += 1
                    row[i] += 1
                    col[j] += 1
                    if (i == j):
                        diag += 1
                    if (i + j == 3 - 1):
                        antiDiag += 1
                elif (board[i][j] == "O"):
                    turn -= 1
                    row[i] -= 1
                    col[j] -= 1
                    if (i == j):
                        diag -= 1
                    if (i + j == 3 - 1):
                        antiDiag -= 1

        xWin = (row[0] == 3 or row[1] == 3 or row[2] == 3 or
                col[0] == 3 or col[1] == 3 or col[2] == 3 or
                diag == 3 or antiDiag == 3)
        oWin = (row[0] == -3 or row[1] == -3 or row[2] == -3 or
                col[0] == -3 or col[1] == -3 or col[2] == -3 or
                diag == -3 or antiDiag == -3)

        if (sum(row) != 0 and sum(row) != 1):
            return False
        if (xWin == True and oWin == True):
            return False
        if ((xWin == False and oWin == False) or (xWin == True and turn == 1) or (oWin == True and turn == 0)):
            return True
        return False