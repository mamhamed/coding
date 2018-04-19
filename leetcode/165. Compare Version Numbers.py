class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver1 = [int(x) for x in ver1]

        ver2 = version2.split('.')
        ver2 = [int(x) for x in ver2]

        n = min(len(ver1), len(ver2))

        for i in range(n):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1

        if len(ver1) == len(ver2):
            return 0
        elif len(ver1) > len(ver2):
            n = len(ver1) - len(ver2)
            for i in range(n):
                if ver1[len(ver2)+i] > 0:
                    return 1
            return 0
        else:
            n = len(ver2) - len(ver1)
            for i in range(n):
                if ver2[len(ver1)+i] > 0:
                    return -1
            return 0

print Solution().compareVersion("01", "1")
print Solution().compareVersion("1.0", "1")