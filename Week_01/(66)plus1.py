class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        left = len(digits) - 1
        while left >= 0:

            if digits[left] < 9:
                digits[left] += 1
                break
            digits[left] = 0
            if left == 0 and digits[left] == 0:
                digits = [1] + digits
            left -= 1

        return digits
