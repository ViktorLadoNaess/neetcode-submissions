class Solution:

    def encode(self, strs: List[str]) -> str:
        long_list = []
        for word in strs:
            word_len = len(word)
            long_list.append(f'#{word_len}#')
            long_list.append(word)
        
        return ''.join(long_list)
    

    def decode(self, s: str) -> List[str]:
        pattern = r'#[0-9]*#'
        list_of_word=[]
        i=0
        while i < len(s):
            i +=1
            j = i
            while s[j] != "#":
                j +=1
            word_ln = int(s[i:j])
            list_of_word.append(s[j+1:j+1+word_ln])
            i = j+word_ln+1
        
        return list_of_word
                
