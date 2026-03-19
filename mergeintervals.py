class Solution(object):
    def merge(self, intervals):
        res=[]
        lenres=len(res) #aka 0 tf 
        intervals=sorted(intervals,key=lambda x: x[0])
        temp=intervals[0]

        for i in range(len(intervals)-1):
            
            

            
                if intervals[i+1][0]<=temp[1]:
                    #temp [0] is right cause we sorted
                    temp[1]=max(temp[1],intervals[i+1][1])
                else:
                    res.append(temp)
                    temp=intervals[i+1]
            # print(intervals[i+1][0],intervals[i])
        res.append(temp)
        return res
            
