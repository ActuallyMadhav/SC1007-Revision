class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord
    
    def startsWith(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
