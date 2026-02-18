class Solution(object):
    def uniqueMorseRepresentations(self, words):
            l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            def mapit(w,l):
                        final=""
                        for wi in w:
                            final+=l[ord(wi)-ord('a')]
                        return final
                            
            diff=set()
            for w in words:
                diff.add(mapit(w,l)) #counter givesnt el order
            return len(diff)
                
