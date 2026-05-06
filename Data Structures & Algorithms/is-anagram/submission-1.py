class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) # TC: O(nlogn) SC: O(1)
        # TC: O(n) SC:O(n) solution below:
        if len(s) != len(t): 
            return False
        s_map = Counter(s)
        for ch in t:
            if ch not in s_map:
                return False
            s_map[ch]-=1
            if s_map[ch] == 0:
                del s_map[ch]
        return True 
