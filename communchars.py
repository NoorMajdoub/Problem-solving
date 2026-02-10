class Solution(object):
    def commonChars(self, words):
        common_count = Counter(words[0])
        
        for word in words[1:]:
            common_count &= Counter(word)  # "&" keeps min count for each character
        
        result = list(common_count.elements())
        return result
