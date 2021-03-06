class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {
            5: 0,
            10: 0
        }

        for bill in bills:

            if bill == 5:

                money[5] += 1

            elif bill == 10 and money[5] != 0:

                money[5] -= 1
                money[10] += 1

            elif bill == 20 and money[5] != 0 and money[10] != 0:

                money[5] -= 1
                money[10] -= 1

            elif bill == 20 and money[5] >= 3:

                money[5] -= 3

            else:

                return False

        return True
