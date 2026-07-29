class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if magazine.count(char) < ransomNote.count(char):
                return False
        return True
