class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        bfs = [([], nums)]
        while bfs:
            print(bfs)
            pre, nex = bfs.pop(0)
            if len(nex) == 1:
                ans.append(pre + nex)
            else:
                for i in range(len(nex)):
                    bfs.append((pre + [nex[i]], nex[:i] + nex[i + 1:]))
        return ans
