#
# @lc app=leetcode.cn id=388 lang=python3
#
# [388] 文件的最长绝对路径
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, inputs: str) -> int:
        stack=[]    
        ss=[]
        before=0
        for i in range(0,len(inputs)):
            if inputs[i]=='\n':
                ss.append(inputs[before:i])
                before=i
        ss.append(inputs[before:len(inputs)])
        print(ss)
        ans=0
        for each in ss:
            if not stack:
                stack.append(each)
            else:
                depth=each.count("\t")
                while depth!=len(stack):
                    # 上一个层级到头了 要出栈了
                    path="/".join(stack)
                    if "." in path:
                        print(path)
                        ans=max(ans,len(path)-2*path.count("\n")-2*path.count("\r"))
                    stack.pop()
                stack.append(each)
        path="/".join(stack)
        if "." in path:
            print(path)
            ans=max(ans,len(path)-2*path.count("\n")-2*path.count("\r"))
        return ans
# @lc code=end

print(Solution().lengthLongestPath(
    "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
))