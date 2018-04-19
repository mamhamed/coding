class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N^2)
        # if len(nums) == 0:
        #     return 0
        # longest_at_i = [1] * len(nums)
        #
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             longest_at_i[i] = max(longest_at_i[i], longest_at_i[j]+1)
        #
        # return max(longest_at_i)

        if len(nums) == 0:
            return 0

        X = []
        for i in nums:
            if len(X) == 0:
                X.append([i])
                continue

            for x in X:
                largest_than_all = True
                if x[-1] > i:
                    largest_than_all = False

            if largest_than_all:
                x = self.find_max_len(X)
                x.append(i)
                continue

            for x in X:
                smallest_than_all = True
                if x[0] < i:
                    smallest_than_all = False

            if smallest_than_all:
                X.append([i])
                continue

            x = self.largest_end_element_smaller_than_a_i(X, i)
            x.append(i)



    def largest_end_element_smaller_than_a_i(self, mylist, target):
        m = mylist[0]
        for l in mylist:
            if l[-1] < target and l[-1] < m[-1]:
                m = l
        return m

    def binary_search(self, mylist, target):
        n = len(mylist)
        if n == 0:
            return -1

        if mylist[n/2] == target:
            return n/2
        elif mylist[n/2] < target:
            return n/2 + 1 + self.binary_search(mylist[n/2+1:], target)
        else:
            return self.binary_search(mylist[:n/2], target)

    def find_max_len(self, mylist):
        m = mylist[0]
        for l in mylist:
            if len(l) > len(m):
                m = l

        return m



print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])