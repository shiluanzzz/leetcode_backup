# 89. 格雷编码


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def grayCode(self, n: int) -> list[int]:
        target=pow(2,n)
        # 2 00 01
        # 4 00 10 11 01
        # 8 00 10 110 1110 1111 111 11 01
        # 16
        l=["00","10"]
        r=["11","01"]
        if n==1:return [0,1]
        if n==2:return [0,1,3,2]
        while len(l)!=target/2:
            t="1"*(len(r)+1)
            r.insert(0,t)
            l.append(t[:-1]+'0')
        ans=[]
        for i in l:
            ans.append(int(i,2))
        for k in r:
            ans.append(int(k,2))
        return ans
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().grayCode(3))