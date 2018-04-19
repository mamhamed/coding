import sys
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.words = []

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # map key -> value
        self.dic = {}

        self.word_to_freq = {}
        # map key -> frequency
        self.head = Node(-sys.maxint)
        self.freq_to_node = {0:self.head}
        self.capacity = capacity



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            self.word_to_freq[key] += 1
            node = self.freq_to_node[self.word_to_freq[key]-1]
            node.words.remove(key)

            if self.word_to_freq[key] in self.freq_to_node:
                self.freq_to_node[self.word_to_freq[key]].words.append(key)
            else:
                node = Node(self.word_to_freq[key])
                node.words.append(key)
                prev_node = self.freq_to_node[self.word_to_freq[key]-1]
                tmp = prev_node.next
                node.next = tmp
                node.prev = prev_node
                prev_node.next = node
                self.freq_to_node[self.word_to_freq[key]] = node
            return self.dic[key]

        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.dic[key] = value
            self.get(key)
            return

        if self.capacity == 0:
            return

        if len(self.word_to_freq) >= self.capacity:
            head = self.head
            while len(head.words) == 0:
                head = head.next

            remove_key = head.words.pop(0)
            self.dic.pop(remove_key, None)
            self.word_to_freq.pop(remove_key, None)

        self.dic[key] = value
        self.word_to_freq[key] = 1
        if 1 in self.freq_to_node:
            self.freq_to_node[1].words.append(key)
        else:
            node = Node(1)
            node.words.append(key)
            self.freq_to_node[1] = node
            self.head.next = node
            node.prev = self.head




        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)

def run(ops, data):
    cls = LFUCache(data[0][0])
    i = 1
    for op in ops[1:]:
        d = data[i]
        if op == "put":
            cls.put(d[0],d[1])
        if op == "get":
            print cls.get(d[0])

        i += 1

# run(["LFUCache","put","put","get","put","get","get","put","get","get","get"],
#     [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]])

# run(["LFUCache","put", "get"],
#     [[0],[0,0],[0]])

# run(["LFUCache","put","put","put","put","get"],
#     [[2],[3,1],[2,1],[2,2],[4,4],[2]])

run(["LFUCache","put","put","put","put","get","get"],
    [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]])  # [null,null,null,null,null,-1,3]