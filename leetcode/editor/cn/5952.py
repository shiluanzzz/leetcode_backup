import collections


class Solution:
    def countPoints(self, rings: str) -> int:
        def add(origin,new_color):
            print(origin,new_color)
            ans=""
            origin+=new_color
            if "R" in origin:
                ans+="R"
            if "G" in origin:
                ans+="G"
            if "B" in origin:
                ans+="B"
            return ans
        data=collections.defaultdict(str)
        n=len(rings)//2
        for i in range(0,len(rings),2):
            data[int(rings[i+1])]=add(data[int(rings[i+1])],rings[i])
        ans=0
        for k,v in data.items():
            if v=="RGB":
                ans+=1
        return ans

if __name__ == '__main__':
