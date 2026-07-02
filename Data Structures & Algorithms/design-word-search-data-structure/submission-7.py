class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]= TrieNode()
            curr = curr.children[c]
        curr.isEnd = True 
        return 
    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, i):
            if i == len(word):
                return node.isEnd
            val = word[i]
            if val =='.':
                return any(dfs(node.children[c], i+1) for c,_ in node.children.items())
            else:
                if not val in node.children:
                    return False
                return dfs(node.children[val],i+1)
        return dfs(curr,0)
        
