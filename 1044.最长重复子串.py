#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#

# @lc code=start
from operator import le


class Solution:
    def longestDupSubstring(self, s: str) -> str:

        arr = [ord(char) - ord("a") for char in s]
        adv = 26 #进制

        def check(length): 
            #从下标0开始长度为length的子串中，
            #利用哈希编码的方式看有没有相同的子串。
            key = 0
            aL = adv**(length-1)
            for j in range(length):
                key = key * adv + arr[j]
            # key 字符串s[:lens]的哈希编码
            # 在此基础上求解剩下的长度为lens的编码
            # 为了防止哈希碰撞，在做一次哈希
            table = {hash(key)}
            for i in range(1, len(arr)-length+1):
                key = (key - arr[i-1] * aL) * adv + arr[i+length-1]
                # 为了防止哈希碰撞，在做一次哈希
                hash_key = hash(key)
                if hash_key in table:
                    return i
                table.add(hash_key)
            return -1
        # 求解的是最长的重复子串 二分找这个长度
        start = length = 0
        left, right = 1, len(s)
        while left <= right:
            mid = (right - left) // 2 + left
            idx = check(mid)
            if idx != -1:
                start = idx
                length = mid
                left = mid + 1
            else:
                right = mid - 1
        return s[start:start+length]


# @lc code=end

print(Solution().longestDupSubstring("bananananan"))