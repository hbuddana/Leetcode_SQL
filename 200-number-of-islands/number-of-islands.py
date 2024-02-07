class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0  # Initialize the count of islands to 0
        visit = set()  # Create a set to keep track of visited cells
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))  # Mark the cell as visited
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            # Explore neighboring cells in all four directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1  # Found a new island, increment the count
                    dfs(r, c)  # Start DFS to explore the island

        return islands

print("This is new message")
