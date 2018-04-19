class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ## second attempt
        if num == target:
            return [num]

        self.res = []
        for i in range(0, len(num)):
            s = num[:i+1]
            d = num[i+1:]
            if s == '0' or (len(s) >= 1 and s[0] != '0'):
                self.dfs(d, s, int(s), int(s), target)

        return self.res

    def dfs(self, remain_digit, so_far_txt, so_far, last, target):
        if so_far == target and remain_digit == "":
            self.res.append(so_far_txt)

        for i in range(0, len(remain_digit)):
            s = remain_digit[:i+1]
            d = remain_digit[i+1:]
            if len(s) == 1 or (len(s) > 1 and s[0] != '0'):
                self.dfs(d, so_far_txt+'+'+s, so_far+int(s), int(s), target)
                self.dfs(d, so_far_txt+'-'+s, so_far-int(s), -int(s), target)
                self.dfs(d, so_far_txt+'*'+s, so_far-last+last*int(s), last*int(s), target)

        return



    #     ## first attempt
    #     res, self.target = [], target
    #     for i in range(1,len(num)+1):
    #         if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
    #             self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
    #     return res
    #
    # def dfs(self, num, temp, cur, last, res):
    #     if not num:
    #         if cur == self.target:
    #             res.append(temp)
    #         return
    #     for i in range(1, len(num)+1):
    #         val = num[:i]
    #         if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
    #             self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
    #             self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
    #             self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)


print Solution().addOperators("123", 6)
print Solution().addOperators("232", 8)
print Solution().addOperators("32", 6)
print Solution().addOperators("105", 5)