class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            sorted_string = ''.join(sorted(str))
            if sorted_string in dict.keys():
                dict[sorted_string].append(str)
            else:
                dict[sorted_string] = [str]
        res = [value for value in dict.values()]
        return res