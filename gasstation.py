class Solution(object):
    def canCompleteCircuit(self, gas, cost):
            if sum(gas)< sum(cost):#nah no hope
                return -1
            currentsaved = 0
            gotcha = 0

            for i in range(len(gas)):
                #print(gas[i]-cost[i])
                currentsaved+=gas[i]-cost[i]
               # print(currentsaved,gotcha)

                if currentsaved < 0:
                    gotcha=i+1
                    currentsaved=0#refill you used all
            return gotcha

