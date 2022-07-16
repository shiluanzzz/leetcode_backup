# 306. 累加数


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(i,j):
            a=int(num[:i+1])
            b=int(num[i+1:j+1])
            # 前导零
            if (num[0]=="0") or (j>i+1 and num[i+1]=="0"):
                return False
            while True:
                if j==len(num)-1:return True
                c=a+b
                cstr=str(c)
                if j+len(cstr)>len(num):return False
                if num[j+1:j+len(cstr)+1]!=cstr:return False
                else:
                    i,j=j,j+len(cstr)
                    a,b=b,c
        for i in range(len(num)-2):
            for j in range(i+1,len(num)-1):
                if check(i,j):return True
        return False
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().isAdditiveNumber("112358"))