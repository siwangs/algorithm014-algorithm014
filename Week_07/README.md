### 第六周总结：

#### Trie Tree

-   基于字符串前缀的关键字树，本质属于 N-array 树。
-   每个节点最多包含 26 个子节点，并且边缘将每个父节点与其子节点相连。
-   我们需要将每个键的最后一个节点标记为单词节点的末尾。

##### Trie 常见操作

-   插入
    -   输入键的每个字符都作为一个单独的 Trie 节点插入。
    -   关键特征作为子数组的索引。
    -   时间复杂度 O (k), K 是索引长度。
-   搜索
    -   比较字符并向下移动。
    -   到达字符串的结尾。（终止条件）
    -   在 Trie 中找不到索引。（终止条件）
    -   时间复杂度 O (k), K 是索引长度。

#### 并查集

它跟踪被划分为多个不相交（不重叠）子集的元素集。

##### 并查集的操作

-   查找：确定特定元素在哪一个子集中
-   合并：把两个子集合并为一个子集

#### 双向 BFS

它运行两个同时搜索以查找从源到目标顶点的最小路径。

-   从源顶点向目标顶点正向搜索。
-   从目标顶点向源顶点的向后搜索。
-   当两个图形相交时，搜索终止。

使用场景：

初始状态和目标状态都是唯一的且已经完全定义，两个方向上的分支因子完全相同。

#### 高级搜索：

**在每个步骤中，它根据值 f 选择一个节点，该值 f 是等于两个其他参数 g 和 h 之和的参数。在每个步骤中，它选择具有最低 f 的节点/单元，并处理该节点/单元。**

优化路径查找和图形遍历。
典型问题：考虑一个有很多障碍的正方形网格，我们得到了一个起始单元和一个目标单元。我们希望从起始单元格尽快到达目标单元格

#### 红黑树

二叉搜索树，每个节点有多一维的属性，颜色。

数据结构例子

```python
class TreeNode {
	TreeNode left;
	TreeNode right;
	int val;
	boolean color;
}
```

##### 红黑树特征：

-   每个节点都是红色或黑色。
-   每片叶子都是黑色的。
-   如果节点为红色，则其两个子节点均为黑色。
-   从节点到后代叶子的每个简单路径都包含相同数量的黑色节点。

### 周作业题解

| 题号                                                                             | 名称                                                                                              | Github 链接 | 解题心得 | 已经刷遍数 | 难度 |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------- | -------- | ---------- | ---- |
| [208](https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description) | [208. Implement Trie (Prefix Tree)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/) |             |          | 1          | 中等 |
| [2](https://leetcode-cn.com/problems/generate-parentheses/)                      | 22.[生成括弧](https://leetcode-cn.com/problems/generate-parentheses/)                             |             |          | 1          | 中等 |
| [70](https://leetcode-cn.com/problems/climbing-stairs/)                          | [70.climbing stairs](https://leetcode-cn.com/problems/climbing-stairs/)                           |             |          | 1          | Easy |
|                                                                                  |                                                                                                   |             |          |            |      |
|                                                                                  |                                                                                                   |             |          |            |      |
