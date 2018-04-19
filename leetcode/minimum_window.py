#Given a collection T of characters and a string S, find the minimum window in S which will contain all the characters in T
#For example,
#S = "this is a test string"
#T = "tist"
#The minimum window is "t stri"

import numpy as np

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mymap = {}  # location of characters in s
        for i in t:
            mymap[i] = []

        miss = list(t) # keep the list of missing character

        start = 0
        end = len(s)
        for i in range(len(s)):
            char = s[i]
            if char in t:
                if char in miss:
                    miss.remove(char)
                elif mymap[char] != []:
                    mymap[char].pop(0)
                mymap[char].append(i)

            if miss == []:
                maximum = max([x[-1] for x in mymap.values()])
                minimum = min([x[0] for x in mymap.values()])

                if maximum - minimum + 1 < end - start + 1:
                    end = maximum
                    start = minimum

        if miss != []:
            return ""
        else:
            return s[start:end+1]




S = "ADOBECODEBANC"
T = "ABC"

#S = "this is a test string"
#T = "tist"

#S = "aa"
#T = "aa"

all_window = []

print Solution().minWindow(S,T)
