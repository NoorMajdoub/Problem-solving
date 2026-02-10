class Solution(object):
    def commonChars(self, words):
        common_count = Counter(words[0])
        
        for word in words[1:]:
            common_count &= Counter(word)  #  keep min count for each char
        
        result = list(common_count.elements())
        return result
