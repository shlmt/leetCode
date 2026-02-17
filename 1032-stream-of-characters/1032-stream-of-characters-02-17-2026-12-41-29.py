from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        node = self.head
        for l in word:
            node = node.children[l]
        node.is_end = True
    
    def search(self, word):
        node = self.head
        for l in word:
            if l not in node.children:
                return False
            node = node.children[l]
            if node.is_end:
                return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.max_len = max([len(w) for w in words])
        self.stream = ''
        for word in words:
            self.trie.insert(word[::-1]) # for improve runtime - search only one time from the end

    def query(self, letter: str) -> bool:
        # save only the max relevant length, reversed
        self.stream = letter + self.stream
        if len(self.stream) > self.max_len:
            self.stream = self.stream[:self.max_len]
        return self.trie.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)