class Solution(object):
    def countVowelSubstrings(self, word):
        vovoo =set('aeiou')  #my life long love sol , settssssss
        count=0
        for i in range(len(word)):
            for j in range(i, len(word)):
                sub=word[i:j+1]
                if set(sub).issubset(vovoo) and all(v in sub for v in vovoo):
                    count+= 1
        return count
