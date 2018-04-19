import numpy as np
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.arr = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        mypick = -1
        cnt = 0
        for i in xrange(len(self.arr)):
            if self.arr[i] == target:
                if mypick == -1:
                    mypick, cnt = i, 1
                else:
                    cnt += 1
                    if np.random.randint(cnt)+1 == cnt:
                        mypick = i

        return mypick


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)


def run(ops, vals):
    g = Solution(vals[0][0])
    i = 1
    for op in ops[1:]:
        val = vals[i][0]
        if op == 'pick':
            return g.pick(val)


dic = {}
for k in range(100):
    a = run(["Solution","pick"],
            [[[1,2,3,3,3]],[3]])
    dic[a] = dic.get(a, 0) + 1

print dic

#
# run(["Solution","pick"],
#     [[[1]],[1]])