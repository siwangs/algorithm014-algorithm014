### 总结：

本周主要讲解的是递归。递归根据不同的形式可以分从两类，分治以及回溯。具体的实现方式稍微有不同，但是都是同一套模板进行实现，稍微做一些微调，但是本质都是是递归的一种。

#### 递归的模板

```python
# Python
def recursion(level, param1, param2, ...):
    # recursion terminator 每次递归的终结条件
    if level > MAX_LEVEL:
	   process_result
	   return

    # process logic in current level
    # 对本层逻辑进行处理，例如添加一个括号。
    process(level, data...)

    # drill down 把 path添加到下一层
    self.recursion(level + 1, p1, ...)
    # reverse the current level status if needed
    # 如果需要，这一层可能做一个不同的选择推倒下一层，直观的理解就是树结构
```

#### 分治：

分治的典型题目是最近的公共祖先，当左右节点都有值的话就是最大的公共祖先。否则的话就把值层层上传

#### 回溯:

回溯的最大特点是会有 path，典型例子，例如括号，全组合等等

### 周作业题解

| 题号                                                                             | 名称         | Github 链接 | 解题心得                      | 已经刷遍数 | 难度 |
| -------------------------------------------------------------------------------- | ------------ | ----------- | ----------------------------- | ---------- | ---- |
| [236](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 最近公共祖先 |             |                               | 1          | 中等 |
| [46](https://leetcode-cn.com/problems/permutations//)                            | 全排列       |             | 使用了迭代 - BFS 手动维护了栈 | 2          | 中等 |
|                                                                                  |              |             |                               |            |      |
|                                                                                  |              |             |                               |            |      |
|                                                                                  |              |             |                               |            |      |
