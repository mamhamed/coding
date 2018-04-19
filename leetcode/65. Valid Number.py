class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        states = [
            {},
            {'blank': 1, 'sign': 2, 'digit': 2, '.': 2},
            {'digit': 2, 'e': 3},
            {'digit': 3},
            {}
        ]

        curr_state = 1
        for c in s:
            if '0' <= c <= '9':
                state = 'digit'
            elif c == '+' or c == '-':
                state = 'sign'
            elif c == ' ':
                state = 'blank'
            else:
                state = c

            if state not in states[curr_state].keys():
                return False

            curr_state = states[curr_state][state]

        return True

print Solution().isNumber("3")
print Solution().isNumber("    3")
print Solution().isNumber("+3")
print Solution().isNumber("-3")
print Solution().isNumber("- 3")
print Solution().isNumber("+3e10")
print Solution().isNumber("+3e10e1")