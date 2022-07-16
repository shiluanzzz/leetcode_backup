# -*- coding:utf-8 -*-
# __author__ = "shitou6"

class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针 首，末
        q=0
        p=len(s)-1
        while q<p:
            s[q],s[p]=s[p],s[q]
            q,p=q+1,p-1
            print(s)
if __name__ == '__main__':
    S=Solution()
    S.reverseString(["h","e","l","l","o"])