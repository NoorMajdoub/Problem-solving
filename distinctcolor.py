class Solution(object):
    def queryResults(self, limit, queries):
        hashit = {}           #ball:color
        colorcount ={}      #colro_feq
        res = []

        for ball, color in queries:
            # il ball already with cooor
            if ball in hashit:
                oldcolor = hashit[ball]
                colorcount[oldcolor] -= 1
                if colorcount[oldcolor] == 0:
                    del colorcount[oldcolor]


            # you add color
            hashit[ball] = color
            colorcount[color] = colorcount.get(color, 0) + 1
            res.append(len(colorcount))
        return res
