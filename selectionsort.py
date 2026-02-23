class Solution: 
    def selectionSort( self,arr):
        #1 select current min
        currentmin=0 #save da index
        for i in range(len(arr)):
            currentmin=i
            for j in range(i,len(arr)):
                if arr[j]<arr[currentmin]:
                    arr[j],arr[currentmin]=arr[currentmin],arr[j]
           # print(arr,currentmin)
        return arr
