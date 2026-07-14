class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res =[]
        def dfs(i,parts):
            if len(parts) == 4:
                if i != len(s):
                        return
                for j in parts:
                    if len(j)>3:
                        return

                res.append('.'.join(parts))
                return
            for x in range(1,4):
                print(x)
                print(i+x)
                print(s[i:i+x])
                segment = s[i:i+x]
                if len(segment) > 1 and segment[0] == "0":
                    continue
                if i+x> len(s):
                    continue
                if int(segment)<= 255:
                    parts.append(segment)
                    dfs(i+x, parts)
                    parts.pop()
        dfs(0,[]) 
        return res
