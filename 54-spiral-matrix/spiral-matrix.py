
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the result.
        res = []
        
        # Initialize pointers for the boundaries of the matrix.
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        # Loop while there are elements within the boundaries.
        while left < right and bottom > top:

            # Traverse the top row from left to right and add elements to the result.
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse the rightmost column from top to bottom and add elements to the result.
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check if there are more elements to be added.
            if not (left < right and top < bottom):
                break

            # Traverse the bottom row from right to left and add elements to the result.
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse the leftmost column from bottom to top and add elements to the result.
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        # Return the result list containing elements in spiral order.
        return res

