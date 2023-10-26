class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

    # Create a new matrix with the same dimensions as the original matrix
        new_matrix = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                # Copy elements from the original matrix to the new matrix with rotation
                new_matrix[j][n - 1 - i] = matrix[i][j]

        # Copy the rotated elements back to the original matrix (in-place)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]

        return new_matrix
            