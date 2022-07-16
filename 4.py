class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        lens=len(nums1)+len(nums2)
        i,j=0,0
        count=0
        self.ans=[]
        while i<=len(nums1) and j<=len(nums2) and count<lens//2:
            # print(i,j)
            now_num=-1
            if i==len(nums1):
                now_num=nums2[j] 
                j+=1
            elif j==len(nums2):
                now_num=nums1[i]
                i+=1
            else:
                if nums1[i]>nums2[j]:
                    now_num=nums2[j]
                    j+=1
                else:
                    now_num=nums1[i]
                    i+=1
            print(now_num)
            count+=1
            if count==lens//2:
                if lens%2==1:
                    return now_num
                else:
                    if len(self.ans)!=0:
                        self.ans.append(now_num)
                        return sum(self.ans)/2
                    else:
                        count-=1
                        self.ans.append(now_num)
print(Solution().findMedianSortedArrays([1,2],[3,4]))