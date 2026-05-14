class Solution:

    def encode(self, strs: List[str]) -> str:
        enc= ""
        for word in strs:
            encoded_w=f'#{len(word)}#{word}'
            enc +=encoded_w
        print(enc)
        return enc

    

    def decode(self, s: str) -> List[str]:
        pattern = r'#[1-9]*#'
        dec =[]
        i=0
        while i <len(s):
            i +=1
            j = i
            while s[j] != '#':
                j +=1
            len_word = int(s[i:j])
            print(len_word)
            dec.append(s[j+1:j+1+len_word])
            print(s[j+1:j+1+len_word])
            i =j+len_word+1
        return dec


                
