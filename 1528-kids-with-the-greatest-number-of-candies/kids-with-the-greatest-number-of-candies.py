class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        solution = []
        Highest_Candy = max(candies)

        for i in candies:
            if (i + extraCandies >= Highest_Candy):
                solution.append(True)
            else:
                solution.append(False)

        return solution
        