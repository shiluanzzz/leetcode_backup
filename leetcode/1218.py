from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        hash=defaultdict(int)
        for each in arr:
            hash[each]=1
        def get_diff(k):
            if hash.get(k)==0 or hash.get(k)!=1:
                return hash.get(k)
            else:
                ans=get_diff(k+difference)+1
                hash[k]=ans
                return ans
        ans=0
        for k,v in hash.items():
            if v!=1:continue
            else:
                hash[k]=get_diff(k)
                ans=max(ans,hash[k])
        return ans

Solution().longestSubsequence([1,2,3,4],1)