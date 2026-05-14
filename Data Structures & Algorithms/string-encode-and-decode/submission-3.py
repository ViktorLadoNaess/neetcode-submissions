class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s +=(f'#{len(word)}#{word}')
        return s
    

    def decode(self, s: str) -> List[str]:
        print(s)
        i =0
        result = []
        while i in range(len(s)):
            
            j =i+1
            while s[j] !='#':
                j +=1
   
            word_len= int(s[i+1:j])
            
            word = s[j+1:j+word_len+1]
            print(word)
            i = j+word_len+1
            result.append(word)
        
        return result

    
                
