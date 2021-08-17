class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mode_words = defaultdict(list)
        for word in strs:
            mode = ''.join(sorted(list(word)))
            mode_words[mode].append(word)
        
        return list(mode_words.values())
