# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.head = nestedList
        self.listchild = None


    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if self.listchild:
                m = self.listchild
                self.listchild = self.listchild.next
                if not self.listchid:
                    self.head = self.head.next

                return m
            else:
                if self.head.isInteger():
                    m = self.head.getInteger()
                    self.head = self.head.next
                    return m
                else:
                    self.listchild = self.head.getList()
                    m = self.listchild.val
                    self.listchild = self.listchild.next()
                    if not self.listchid:
                        self.head = self.head.next
                    return m

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.listchild:
            return True

        while self.head:
            if self.head.isInteger():
                return True
            else:
                listchild = self.head.getList()
                if listchild:
                    return True
            self.head = self.head.next

        return False


        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())