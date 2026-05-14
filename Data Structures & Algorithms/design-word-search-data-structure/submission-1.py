class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd= False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]= TrieNode()
            curr=curr.children[c]
        curr.isEnd = True
        return

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            curr = node

            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    # Try every possible child
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.isEnd

        return dfs(0, self.root)

        
