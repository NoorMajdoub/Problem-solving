class Solution(object):
    def findWinners(self, matches):
                counter_looser=Counter([m[1] for m in matches])
                looser,winner=[],list(set(sum(matches,[])))
                for m in matches:
                    if m[1] in winner:
                        winner.remove(m[1]) 
                        if counter_looser[m[1]]==1:
                            looser.append(m[1]) #must be lost one match
                return sorted(winner),sorted(looser)
