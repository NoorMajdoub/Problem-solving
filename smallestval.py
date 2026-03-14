class Solution(object):
    def smallestNumber(self, n):
                if n< 0:
                    n=n*(-1)
                    l=sorted(list(str(n)),reverse=True)
                    return int(''.join(l))*(-1)
                else:
                    l=sorted(list(str(n)))
                #  print(l)
                    #get the 0 in place
                    if l[0] == '0':
                        for i in range(len(l)):
                            if l[i] != '0':
                                l[0], l[i] = l[i], l[0]
                                break
                    ll=int(''.join(l))
                    return ll
