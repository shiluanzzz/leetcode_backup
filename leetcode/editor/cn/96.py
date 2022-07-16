
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    d={}
    def numTrees(self, n: int) -> int:
        return self.count(1,n)
    def count(self,left,right):
        id="{}-{}".format(left,right)
        if id in self.d:
            return self.d[id]
        if left>right:
            return 1
        ans=0
        for i in range(left,right+1):
            l=self.count(left,i-1)
            r=self.count(i+1,right)
            ans+=l*r
        self.d[id]=ans
        return ans
# leetcode submit region end(Prohibit modification and deletion)
