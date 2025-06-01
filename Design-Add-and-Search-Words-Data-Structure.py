class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.children = defaultdict(TrieNode)
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('#')

    def addWord(self, word: str) -> None:
        root = self.root

        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode(c)
            root = root.children[c]
        root.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)
        
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)