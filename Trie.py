from collections import defaultdict


class TreeNode:
    def __init__(self, End=False):
        self.isEnd = End
        self.link = defaultdict()


class Trie:

    def __init__(self):
        self.Trie = TreeNode()

    def insert(self, word: str) -> None:
        node = self.Trie
        for ch in word:
            if ch in node.link:
                node = node.link[ch]
            else:
                n = TreeNode(False)
                node.link[ch] = n
                node = n
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.Trie
        for ch in word:
            if ch in node.link:
                node = node.link[ch]
            else:
                return False
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.Trie
        for ch in prefix:
            if ch in node.link:
                node = node.link[ch]
            else:
                return False
        return True

