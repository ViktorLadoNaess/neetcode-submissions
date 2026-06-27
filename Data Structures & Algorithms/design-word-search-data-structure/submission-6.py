class Trienode:
    def __init__(self):
        self.children={}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Trienode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c]=Trienode()
            curr = curr.children[c]
        curr.isEnd = True
        return 
            

    def search(self, word: str) -> bool:
        curr = self.root
        n = len(word)
        def dfs(curr,i):
            if i == n:
                return curr.isEnd
            c = word[i]
            if c =='.':
                    return any(dfs(nxt, i+1) for nxt in curr.children.values())                        
            elif not curr.children:
                    return False
            elif not c in curr.children:
                return False
            return dfs(curr.children[c], i+1)
        return dfs(curr, 0)
             

        
