class Solution(object):
    def isCovered(self, nums, left, right):
                    counter=[]
                    rr=range(left,right+1)
                    for i in rr:
                        #print(i) pass for all 
                        for r in nums:
                        # print(r) pass cool
                            if i in range(r[0],r[1]+1):
                              #  print(i,r)
                                counter.append(i)
                   # print(counter,list(rr))
                    return set(counter)==set(list(rr))
