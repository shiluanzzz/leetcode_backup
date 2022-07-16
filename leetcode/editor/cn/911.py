# 911. 在线选举


# leetcode submit region begin(Prohibit modification and deletion)
class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        person_num = len(set(persons))
        person_count = [[0] * len(times) for i in range(person_num)]
        for i, v in enumerate(times):
            for person_id, person_num in enumerate(person_count):
                if i != 0:
                    add = person_count[person_id][i - 1]
                else:
                    add = 0
                if person_id == persons[i]:
                    add += 1
                person_count[person_id][i] = add
        print(person_count)
        self.count = person_count
        self.times = times

    def q(self, t: int) -> int:
        # print("times",self.times)
        index = 0
        for i in range(len(self.times)):
            if self.times[i] == t:
                index = i
                break
            if self.times[i] > t:
                index = max(i - 1, index)
                break
        # 最后
        if t>self.times[-1]: index = len(self.times) - 1
        print(t, "->", index)
        max_count, max_index = self.count[0][index], 0
        for i in range(1,len(self.count)):
            if self.count[i][index] > max_count:
                max_count, max_index = self.count[i][index], i
            elif self.count[i][index] == max_count:
                ## 平票，往前找判断这两个人
                k = index-1
                while k > -1:
                    a, b = self.count[i][k], self.count[max_index][k]
                    if a < b:
                        max_index = i
                        break
                    elif a > b:
                        break
                    else:
                        pass
                    k -= 1
            else:
                pass
        return max_index



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a=TopVotedCandidate([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
    print(a.q(3))
    print(a.q(12))
    print(a.q(25))
    print(a.q(15))
    print(a.q(24))
    print(a.q(8))

