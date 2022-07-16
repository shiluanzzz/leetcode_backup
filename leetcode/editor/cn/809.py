# 809. 情感丰富的文字


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def group(word):
            # abbccc-> [('a',1),('b',2),('c',3)]
            count = 0
            c = None
            res = []
            for i in word:
                if not c:
                    c, count = i, 1
                elif i == c:
                    count += 1
                else:
                    res.append((c, count))
                    c, count = i, 1
            res.append((c, count))
            return res

        s_group = group(s)
        print(s_group)
        ans = 0
        for each in words:
            g = group(each)
            if len(g) != len(s_group):
                continue
            flag = True
            print(g)
            for i in range(len(g)):
                if g[i][0] != s_group[i][0]:
                    flag = False
                    break
                s_num,w_num=s_group[i][1],g[i][1]
                if s_num!=w_num and s_num<3:
                    flag=False
                    break
                if w_num>s_num:
                    flag=False
                    break
            if flag:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().expressiveWords("dddiiiinnssssssoooo",
                                     ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso",
                                      "dinssoo", "dinso"]
                                     ))
    print(Solution().expressiveWords("aaaa",["aaaaa"]))