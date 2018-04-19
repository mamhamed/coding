import numpy as np
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) <= 0:
            return words

        if maxWidth == 0:
            return words

        justified = []
        ptr = 0
        while ptr < len(words):
            n = 0
            arr = []
            while ptr < len(words) and n+len(words[ptr]) <= maxWidth:
                arr.append(words[ptr])
                n += len(words[ptr])+1
                ptr += 1
            justified.append(arr)

        for i in range(len(justified)-1):
            arr = justified[i]
            extra_white_space = maxWidth - sum([len(x) for x in arr]) - len(arr) + 1

            extra_space = ' '
            added_space = 0
            i = 0
            while added_space < extra_white_space:
                if len(arr) > 1:
                    arr[i%(len(arr)-1)] += ' '
                else:
                    arr[i%len(arr)] += ' '
                i += 1
                added_space += 1

        for_last = maxWidth - sum([len(x) for x in justified[-1]]) - len(justified[-1]) + 1
        extra_space = ''
        for _ in range(for_last):
            extra_space += ' '
        justified[-1][-1] = justified[-1][-1] + extra_space
        for i in range(len(justified)):
            justified[i] = ' '.join(justified[i])

        return justified


# print Solution().fullJustify([""], 0)
# print Solution().fullJustify(["a"], 1)
# print Solution().fullJustify(["a", "b", "c", "d"], 1)
# print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print Solution().fullJustify(["Listen","to","many,","speak","to","a","few."], 6)