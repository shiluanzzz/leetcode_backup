# 面试题 10.05. 稀疏数组搜索


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findString(self, words: list[str], s: str) -> int:
        words=[i for i in words if i!=""]
        l, r = 0, len(words) - 1
        while l <= r:
            mid = (l + r) // 2
            # if words[mid] == "":
            #     mid = find_mid(l, r, mid)
            #     if mid == -1: return -1
            if words[mid] > s:
                l, r = l, mid - 1
            elif words[mid] < s:
                l, r = mid + 1, r
            else:
                return mid
        return -1

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().findString(words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "at"))