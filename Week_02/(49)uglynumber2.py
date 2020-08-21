class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set()
        seen.add(1)

        import heapq
        ugly_collections = [2, 3, 5]

        for _ in range(n):

            ugly = heappop(heap)

            for i in ugly_collections:

                new_ugly = ugly * i

                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)

        return ugly
