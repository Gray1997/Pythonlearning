class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board_check = set()

        for i  in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cur = board[i][j]
                if (i, cur) in board_check or (cur,j) in board_check or (i/3, j/3, cur) in board_check:
                    return False
                board_check.add((i,cur))
                board_check.add((cur,j))
                board_check.add((i/3, j/3, cur))

        return True