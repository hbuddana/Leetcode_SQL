class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for i in nums:
            squares.append(i*i)
        return sorted(squares)

        