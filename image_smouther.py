class Solution(object):
    def imageSmoother(self, img):
        def average(img,i,j):
            summer=0
            counter=0
            beging_i=0 if i-1<0 else i-1  #dont let i less than your range in cases where i =0 , cause then cant do the i-1 to get your neighbors before you
            beging_j=0 if j-1<0 else j-1

            for i_t in range(beging_i,min((i+2),len(img))):  #min is also to keep track of limit on the end cause in i==n cant do i+1
                for j_t in range(beging_j,min((j+2),len(img[0]))):
                # print(img[i_t][j_t])
                # print(i_t,j_t)
                    #print("--")
                    summer+=img[i_t][j_t]
                    counter+=1
            return summer//counter
        res = [[0]*len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                    res[i][j]=average(img,i,j)
        return res
    
    
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        
