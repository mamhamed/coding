"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

def knows(a, b):
    # if a == 0 and b == 1:
    #     return False
    # if a == 1 and b == 0:
    #     return True

    return False

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        if n == 1:
            return 0

        nums = range(n)

        while len(nums) >= 2:
            a = nums.pop()
            b = nums.pop()
            if knows(a, b):
                nums.append(b)
            else:
                nums.append(a)

        c = nums[-1]
        print c
        for v in range(n):
            if c != v:
                if not knows(c, v) and knows(v, c):
                    continue
                else:
                    return -1

        return c

print Solution().findCelebrity(2)