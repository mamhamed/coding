import numpy as np

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0:
            return False

        if len(word) == 0:
            return False

        n = len(board)
        m = len(board[0])
        for i in xrange(n):
            for j in xrange(m):
                if self.search_around(board, i, j, word):
                    return True

        return False



    def search_around(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j] != word[0]:
            return False

        if len(word) == 1:
            return True

        flag = False
        tmp = board[i][j]
        board[i][j] = "#"
        for k in [(-1,0), (1,0), (0,1), (0,-1)]:
            flag |= self.search_around(board, i+k[0], j+k[1], word[1:])

        board[i][j] = tmp
        return flag




# board = [
#     ['A','B','C','E'],
#     ['S','F','C','S'],
#     ['A','D','E','E']
# ]
#
# word = "SADFC"

# board = [["a"]]
# word = "a"

# board = [["a", "a"]]
# word = "aa"

board = [["a", "a"]]
word = "aaa"

# board = [["C", "A", "A"],
#          ["A", "A" , "A"],
#          ["B", "C", "D"]]
#
# word = "AAB"

print Solution().exist(board, word)