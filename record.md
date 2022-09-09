# 算法题刷题记录

- [x](leetcode/editor/cn/x.py)

## 20220909

- [91](leetcode/editor/cn/91.py) 
  - 解码可以从0开始还是从1开始 处理方式不一样，一定要弄懂dp的含义
  - 昨天做的一个秋招题目，A->'0' 这个题目 A->'1'
## 20220908
- [667.优美的排列 II](leetcode/editor/cn/667.py) 完全没思路
- [75.颜色分类](leetcode/editor/cn/75.py) 以前做过今天还是忘记了
- [20220908完美世界笔试](interview/20220908wjmwuijp/002.py)
  - 偶数可以除二，奇数可以变化成2*n+2 或 2*n-2 之间记忆化+递归就行了，好像也是力扣原题

## 20220906

- [828.统计子串中的唯一字符](leetcode/editor/cn/828.py)
    - 数学不会背叛你，不会就是不会- -
- [168](leetcode/editor/cn/168.py) 简单题 wa了一次

## 20220905

- [652](leetcode/editor/cn/652.py)
    - 踩坑：不能直接用str(node)来标记一颗树
    - 使用二叉树的后序遍历或者前序遍历来标记一棵树而不是中序遍历
        - 前序: 根左右 中序：左根右 后序：左右根
- [面试题 01.01.判定字符是否唯一](leetcode/editor/cn/面试题%2001.01.py)
    - 最优解法就是用位运算，但是我不会- -
- [197.上升的温度](leetcode/editor/cn/197.sql)
    - SQL题做的太少了，这个需要用到dateDiff()函数来计算两个日期之间的差值
- [867.转置矩阵](leetcode/editor/cn/867.py) 理清二维矩阵的row,column即可

- [83](leetcode/editor/cn/83.py)
- [110](leetcode/editor/cn/110.py)
- [111](leetcode/editor/cn/111.py)

## 20220904

- [周赛01](leetcode/competition/6167.py) 简单题看懂题意就行
- [周赛02](leetcode/competition/6168.py)
    - 看了解析：记忆化搜索就行了，自己想复杂了，其实也挺抽象的
- [周赛03](leetcode/competition/6169.py)
    - 虽然A了但是自己的写法很垃圾，子数组多一个数字后，如果符合条件可以用或存起来
- [周赛04](leetcode/competition/6170.py)
    - 自己写到后面才发现题目没完全理解，要用两个队列。后面换成2个队列还是有错误，找不出来了
    - 解析里看到了一个更好的写法，可以值得学习一下。

## 20220903

- [646.最长数对链](leetcode/editor/cn/646.py)

    - 没想明白，一看就会，一写就不会
    - 和[435]题目一样

- [435](leetcode/editor/cn/435.py) review

    - 想复杂了，就直接贪心就行了。
    - **列表推导比循环效率高很多**
    - 646的题目也直接用贪心写，比dp更简单。review

## 20220902

- [面试题 04.12](leetcode/editor/cn/面试题%2004.12.py)

    - 主次问题没拆分好

- [257](leetcode/editor/cn/257.py)

- [687](leetcode/editor/cn/687.py)

    - 这种非自顶向下的dfs还要多理解

- [112](leetcode/editor/cn/112.py)  注意节点值可能为负

- [113](leetcode/editor/cn/113.py)  跟112类似，做一个path记录即可，注意list拷贝

- [437](leetcode/editor/cn/437.py)  跟[面试题 04.12](leetcode/editor/cn/面试题%2004.12.py) 类似，主次问题拆分好即可

- [988](leetcode/editor/cn/988.py)  `rewiew` `字典序`

    - ord('~') = 126 可以用在字典序字符串中充当最大值
    - dfs中带路径的pop()

- [124](leetcode/editor/cn/124.py)  `review`

    - 思路对了，实际写起来还有点问题
    - 没看清题目输入的数据情况和限定要求

- [543](leetcode/editor/cn/543.py) 跟124有点像，也是非自顶向下的
