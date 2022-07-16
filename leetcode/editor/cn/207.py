# 207. {question.title}




# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        DAG=[]
        for i in range(numCourses):
            DAG.append([])
        print(DAG)
        for i in prerequisites:
            DAG[i[0]]=DAG[i[0]].append(i[1])
        visited=[0]*numCourses
        Judged=[0]*numCourses
        # 判断是否有环
        def trip(index,DAG,visited,Judged):
            if visited[index]==1:
                return True
            if Judged[index]==1:
                return False
            visited[index]=1
            Judged[index]=1
            for each in DAG[index]:
                if trip(each,DAG,visited,Judged):
                    return True
            visited[index]=0
            return False
        for each in range(numCourses):
            if trip(each,DAG,visited,Judged):
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a=Solution()
    a.canFinish(2,[[1,0]])
