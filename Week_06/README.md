### 总结：

#### 动态规划解题框架

-   一般形式：求最值
-   本质：穷举
-   优化：穷举有很多重叠的子问题，需要用记忆化搜索或者 DP table 来优化穷举过程
-   动态规划特点：一定会具备最优子结构，重叠子问题
-   确定状态转移方程

### 伪代码模板

```python
# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)
```

### 周作业题解

| 题号                                                     | 名称                                                                   | Github 链接 | 解题心得 | 已经刷遍数 | 难度 |
| -------------------------------------------------------- | ---------------------------------------------------------------------- | ----------- | -------- | ---------- | ---- |
| [64](https://leetcode-cn.com/problems/minimum-path-sum/) | [Minimum Path Sum](https://leetcode-cn.com/problems/minimum-path-sum/) |             |          | 1          | 中等 |
| [91](https://leetcode-cn.com/problems/decode-ways/)      | [Decode Ways](https://leetcode-cn.com/problems/decode-ways/)           |             |          | 1          | 中等 |
|                                                          |                                                                        |             |          |            |      |
|                                                          |                                                                        |             |          |            |      |
|                                                          |                                                                        |             |          |            |      |
