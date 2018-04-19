class TreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def addNode(self, start, end, node):
        if start >= node.end:
            if node.right is not None:
                return self.addNode(start, end, node.right)
            else:
                node.right = TreeNode(start, end)
                return True
        elif end <= node.start:
            if node.left is not None:
                return self.addNode(start, end, node.left)
            else:
                node.left = TreeNode(start, end)
                return True
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        else:
            return self.addNode(start, end, self.root)


def run(ops, values):
    myCalendar = MyCalendar()
    for i, op in enumerate(ops):
        if op == 'book':
            print myCalendar.book(*values[i])


    print "------"

run(["MyCalendar", "book", "book", "book"], [[], [10, 20], [15, 25], [20, 30]])

# run(["MyCalendar","book","book","book","book","book","book","book","book","book","book"],
#     [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]])

