class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        left=0
        right=len(s)-1
        chars=list(s)
        while(left<right):
            if(chars[left] in vowels):
                if(chars[right] in vowels):
                    chars[left],chars[right]=chars[right],chars[left]
                    left+=1
                    right-=1
                else:
                    right-=1
            else:
                left+=1
        return ''.join(chars)

