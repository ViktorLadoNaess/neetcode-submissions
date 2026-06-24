class TrieNode:
    def __init__(self):
        self.children ={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr = curr.children[c]
        curr.isEnd=True 
        return

    def search(self, word: str) -> bool:

        curr = self.root
        def dfs(curr, i):
            if i == len(word):
                return curr.isEnd
            if word[i] =='.':
                return any(dfs(curr.children[c],i+1) for c in curr.children)
            else:
                if word[i] not in curr.children:
                    return False
                return dfs(curr.children[word[i]],i+1)
        return dfs(curr,0)
