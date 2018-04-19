class Node(object):
    def __init__(self, char):
        self.char = char
        self.word = ''
        self.next = {}

## my second try
class WordDictionary(object):
    def __init__(self):
        self.root = Node('')

    def addWord(self, word):

        root = self.root
        for c in word:
            if c in root.next:
                root = root.next.get(c)
            else:
                node = Node(c)
                root.next[c] = node
                root = node

        root.word = word

    def search(self, word):
        return self.dfs(word, self.root)

    def dfs(self, word, root):
        for i, c in enumerate(word):
            if c == '.':
                return any([self.dfs(word[i+1:], x) for k, x in root.next.items()])
            else:
                if c not in root.next:
                    return False
                else:
                    root = root.next[c]

        if len(root.word) > 0:
            return True
        else:
            return False


## first try
# class WordDictionary(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = Node('')
#
#     def addWord(self, word):
#         """
#         Adds a word into the data structure.
#         :type word: str
#         :rtype: void
#         """
#         root = self.root
#         nodes = root.next
#         for c in word:
#             n = nodes.get(c)
#             if n is None:
#                 n = Node(c)
#                 root.next[c] = n
#             root = n
#             nodes = root.next
#
#         root.word = word
#
#     def search(self, word):
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         :type word: str
#         :rtype: bool
#         """
#         return self.dfs(word, self.root)
#
#     def dfs(self, word, root):
#         if len(word) == 0:
#             return len(root.word) > 0
#         i = 0
#         for c in word:
#             if c == '.':
#                 nodes = [v for k,v in root.next.items()]
#                 return any([self.dfs(word[i+1:], x) for x in nodes])
#             else:
#                 n = root.next.get(c)
#                 if n is None:
#                     return False
#                 root = n
#             i += 1
#
#         return len(root.word) > 0
#
#         # Your WordDictionary object will be instantiated and called as such:
#         # obj = WordDictionary()
#         # obj.addWord(word)
#         # param_2 = obj.search(word)


def run(ops, data):
    trie = WordDictionary()
    i = 1
    for op in ops[1:]:
        d = data[i][0]
        if op == "addWord":
            trie.addWord(d)
        if op == "search":
            print trie.search(d)

        i += 1


run(["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
)

# run(
#     ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"],
#     [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
# )