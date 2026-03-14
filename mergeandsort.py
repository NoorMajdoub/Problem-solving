class Solution(object):
    def merge(self, nums1, m, nums2, n):
            i1=m-1
            i2=n-1
            tracker=len(nums1)-1
            while 0 <= i2 and 0<= i1:
                print(nums1[i1],nums2[i2],i2,i1,tracker)
                if nums2[i2]<nums1[i1]: #he gonna be in the end
                #nums1 bigger so it goes in the end
                    nums1[tracker]=nums1[i1]
                    i1-=1
                else :
                    print("case")
                    nums1[tracker]=nums2[i2]
                    i2-=1
                tracker-=1
            while i2>= 0:
                nums1[tracker]=nums2[i2]
                i2-=1
                tracker-=1
