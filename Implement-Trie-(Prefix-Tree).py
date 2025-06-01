class TrieNode:
    def __init__(self, char = ''):
        self.char = char
        self.children = defaultdict(TrieNode)
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode('#')

    def insert(self, word: str) -> None:
        root = self.root

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode(c)
            root = root.children[c]
        root.is_end = True

    def search(self, word: str) -> bool:
        root = self.root

        for c in word:
            if c in root.children:
                root = root.children[c]
            else: return False
        return root.is_end        

    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for c in prefix:
            if c in root.children:
                root = root.children[c]
            else: return False
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)