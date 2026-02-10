class Solution(object):
        def findWords(self, words):
                l={1:list("qwertyuiop"),2:list("zxcvbnm"),3:list("asdfghjkl")}

                ll=[]
                def init(s):
                        p=[]
                        for ss in s.lower():
                            for i,j in l.items():
                                if ss in j:
                                    p.append(i)
                        return len(set(p))==1
                for w in words:
                    if   init(w)==True:
                        ll.append(w)
                return ll
