class Solution(object):
    def findRestaurant(self, l1, l2):
        com=set(l1).intersection(l2)

        
        l=sorted([(x,l1.index(x)+l2.index(x))for x in com],key=lambda x: x[1])
        minit=l[0][1]
        return [x[0] for x in l if x[1]==minit ]
