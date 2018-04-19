import sys
class Node(object):
    def __init__(self):
        self.words = set([])
        self.next = Node
        self.prev = Node


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_to_freq = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.freq_to_node = {0: self.head, sys.maxint: self.tail}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.word_to_freq:
            # remove the word from frequency chain
            current_freq_node = self.freq_to_node[self.word_to_freq[key]]
            current_freq_node.words.remove(key)
            self.word_to_freq[key] += 1
            if self.word_to_freq[key] in self.freq_to_node:
                node = self.freq_to_node[self.word_to_freq[key]]
                node.words.add(key)
            else:
                node = Node()
                node.words.add(key)
                tmp_node = current_freq_node.next
                current_freq_node.next = node
                node.prev = current_freq_node
                node.next = tmp_node
                tmp_node.prev = node
                self.freq_to_node[self.word_to_freq[key]] = node
        else:
            self.word_to_freq[key] = 1
            if 1 in self.freq_to_node:
                self.freq_to_node[1].words.add(key)
            else:
                node = Node()
                node.words.add(key)
                self.head.next = node
                node.prev = self.head
                node.next = self.tail
                self.tail.prev = node
                self.freq_to_node[1] = node

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.word_to_freq:
            if self.word_to_freq[key] == 1:
                self.word_to_freq.pop(key, None)
                self.freq_to_node[1].words.remove(key)
            else:
                self.freq_to_node[self.word_to_freq[key]].words.remove(key)
                self.word_to_freq[key] -= 1
                self.freq_to_node[self.word_to_freq[key]].words.add(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if len(self.word_to_freq) == 0:
            return ""

        tail = self.tail.prev
        while tail is not None:
            if len(tail.words) > 0:
                return next(iter(tail.words))
            else:
                tail = tail.prev

        return ""


    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if len(self.word_to_freq) == 0:
            return ""

        head = self.head.next
        while head is not None:
            if len(head.words) > 0:
                return next(iter(head.words))
            else:
                head = head.next

        return ""



            # Your AllOne object will be instantiated and called as such:
            # obj = AllOne()
            # obj.inc(key)
            # obj.dec(key)
            # param_3 = obj.getMaxKey()
            # param_4 = obj.getMinKey()


def run(ops, data):
    cls = AllOne()
    i = 1
    for op in ops[1:]:
        d = data[i]
        if op == "inc":
            cls.inc(d[0])
        if op == "dec":
            cls.dec(d[0])
        if op == "getMaxKey":
            print cls.getMaxKey()
        if op == "getMinKey":
            print cls.getMinKey()

        i += 1


run(["AllOne","getMaxKey","getMinKey"],
    [[],[],[]])

run(["AllOne","inc","inc","inc","getMaxKey","inc","dec","getMaxKey","getMinKey"],
    [[],["1"],["2"],["1"],[],["2"],["1"],[],[]])

run(["AllOne","inc","getMaxKey","getMinKey"],
    [[],["hello"],[],[]])