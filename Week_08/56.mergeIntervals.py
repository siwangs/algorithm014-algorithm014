class Solution:
    def merge(self, seq: List[List[int]]) -> List[List[int]]:
        seq = sorted(seq)
        i = 1
        while i < len(seq):
            if seq[i][0] >= seq[i-1][0] and seq[i][0] <= seq[i-1][1]:
                if seq[i][1] <= seq[i-1][1]:
                    seq.remove(seq[i])
                else:
                    seq[i-1] = [seq[i-1][0], seq[i][1]]
                    seq.remove(seq[i])
            else:
                i += 1
        return seq
