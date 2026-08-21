class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped=[]
        for i,j in zip(names, heights):
            zipped.append((i,j))
        print(zipped)
        zipped.sort(key= lambda x:x[1], reverse = True)
        print(zipped)
        res = [n for n,_ in zipped]
        return res