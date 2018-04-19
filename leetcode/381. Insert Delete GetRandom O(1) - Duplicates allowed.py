import numpy as np
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.arr = []
        self.cnt = 0


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if len(self.arr) > self.cnt:
            self.arr[self.cnt] = val
        else:
            self.arr.append(val)
        if val in self.data:
            self.data[val].add(self.cnt)
            self.cnt += 1
            return False
        else:
            self.data[val] = set([self.cnt])
            self.cnt += 1
            return True


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            ind = self.data[val].pop()
            if len(self.data[val]) == 0:
                self.data.pop(val, None)
            if ind == self.cnt-1:
                self.cnt -= 1
                return
            if self.cnt == 1:
                return True
            last_elem = self.arr[self.cnt-1]  # replace the empty spot with last element in arr
            self.arr[ind] = last_elem
            if len(self.data[last_elem]) > 0:
                self.data[last_elem].remove(self.cnt-1)
                self.data[last_elem].add(ind)
            self.cnt -= 1
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        ind = np.random.randint(low=0, high=self.cnt)
        return self.arr[ind]



        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()

def run(ops, nums):
    for i in range(len(ops)):
        op = ops[i]
        a = nums[i]
        if op == "RandomizedCollection":
            print "---"
            g = RandomizedCollection()
        elif op == "insert":
            print g.insert(a[0])
        elif op == "remove":
            print g.remove(a[0])
        elif op == "getRandom":
            print g.getRandom()
#
# run(["RandomizedCollection", "insert", "remove", "insert"],
#     [[], [1], [1], [1], []])

# run(["RandomizedCollection", "insert", "insert", "remove", "insert", "remove", "getRandom"],
#     [[], [0], [1], [0], [2], [1], []])
#
# run(["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"],
#     [[],[4],[3],[4],[2],[4],[4],[3],[4],[4]])
#
# run(["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","getRandom","getRandom","getRandom","getRandom"],
#     [[],[0],[1],[2],[3],[3],[2],[3],[0],[],[],[],[]])

run(["RandomizedCollection","insert","insert","insert","insert","insert","insert","remove","remove","remove","insert","remove"],
    [[],[9],[9],[1],[1],[2],[1],[2],[1],[1],[9],[1]])