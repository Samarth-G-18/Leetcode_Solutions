class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()

        ulta_word = word[::-1]
        
        return " ".join(ulta_word)        