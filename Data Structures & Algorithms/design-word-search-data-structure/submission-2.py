class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            c = word[i]
            if c == '.':
                # wildcard: try every child
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # normal char: must follow that exact path
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)
        
        return dfs(self.root, 0)