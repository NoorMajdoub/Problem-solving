class Solution(object):
    def rotate(self, matrix):
        
        for m in range(0,len(matrix)):
        #matrix[m][m],matrix[len(matrix)-m-1][m]=matrix[len(matrix)-m-1][m],matrix[m][m]
            for i in range (m+1,len(matrix)):
                #matrix[m][i],matrix[len(matrix)-i-1][m]=matrix[len(matrix)-i-1][m],matrix[m][i]
                #print(matrix[m][i],matrix[len(matrix)-i-1][m],matrix[i][m], matrix[m][i])
                matrix[m][i], matrix[i][m] = matrix[i][m], matrix[m][i]
        for m in matrix:
            m.reverse()
            #print("-----")

                
