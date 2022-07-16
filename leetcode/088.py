# -*- coding:utf-8 -*-
# __author__ = "shitou6"

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从前往后比较
        n1=0
        n2=0
        nums1_copy=nums1.copy()
        nums1[:]=[]

        while(n1<m and n2<n):
            if nums1_copy[n1]<nums2[n2]:
                nums1.append(nums1_copy[n1])
                n1+=1
            else:
                nums1.append(nums2[n2])
                n2+=1
        # 合并最后没加上的
        nums1.extend(nums1_copy[n1:m] if n1<m else nums2[n2:n])
        # 最后这个extend 不能是[n1:] 因为nums1_copy 后面可能还有0
        print(nums1)
        # 输出没问题，但是判题不通过

    def merge2(self, nums1, m: int, nums2, n: int) -> None:
        # 从后往前比较
        end1=m-1
        end2=n-1
        lens=m+n-1
        while(end1>=0 and end2>=0): # 取等是因为第一个数也要比较
            if nums1[end1]>=nums2[end2]:
                nums1[lens]=nums1[end1]
                end1-=1
                lens-=1
            else:
                nums1[lens]=nums2[end2]
                end2-=1
                lens-=1
        # 最后会只会剩下num2
        nums1[:end2+1]=nums2[:end2+1]
        print(nums1)
    def merge3(self,nums1,m,nums2,n):
        nums1[:]=sorted(nums1[:m]+(nums2))

    # review
    def merge4(self,nums1,m,nums2,n):
        # 不原地替换：
        nums1_c=nums1.copy()
        nums1=[]
        a,b=0,0
        while(a<m and b<n):
            if nums1_c[a] < nums2[b]:
                nums1.append(nums1_c[a])
                a+=1
            else:
                nums1.append(nums2[b])
                b+=1
        # 合并剩下的。
        nums1.extend(nums1_c[a:m] if a<m else nums2[b:n])
        print(nums1)

    #review 双指针从后往前
    def merge5(self,nums1,m,nums2,n):
        # pass
        a,b=m-1,n-1
        while(a>=0 and b>=0):
            if nums1[a]>nums2[b]:
                nums1[a+b+1]=nums1[a]
                a-=1
            else:
                nums1[a+b+1]=nums2[b]
                b-=1
        print(nums1)
        nums1[:b+1]=nums2[:b+1]
        print(nums1)

S=Solution()

S.merge5([1,2,2,0,],3,[1],1)
