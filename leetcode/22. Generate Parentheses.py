class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ''

        pars_arr = [('(', n-1, n)]
        final = []

        while len(pars_arr) > 0:
            par, left, right = pars_arr.pop()
            if left == right == 0:
                final.append(par)
            else:
                if left > 0:
                    pars_arr.append((par+'(', left-1, right))
                if left < right:
                    pars_arr.append((par+')', left, right-1))

        return final

print Solution().generateParenthesis(3)