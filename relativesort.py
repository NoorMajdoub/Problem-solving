class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        hashit = {}
        for i, el in enumerate(arr2):  #did index but this is coole
            hashit[el] = i
        def helper(el):
            if el in hashit:
                return hashit[el]
            else:
                return len(arr2) + el #instead of inf
        arr1.sort(key=helper) #key heple is giving the priority
        return arr1
