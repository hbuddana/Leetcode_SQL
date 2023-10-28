class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        # Define two sets to store cells that can flow to the Pacific and Atlantic oceans.
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # Define a DFS function to mark reachable cells.
        def dfs(r, c, ocean_reachable):
            # Mark the current cell as reachable.
            ocean_reachable.add((r, c))
            
            # Define the four possible directions: up, down, left, and right.
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # Check if the new cell is within the bounds of the grid.
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    # Check if the new cell is not already marked as reachable and
                    # if its height is greater than or equal to the current cell's height.
                    if (new_r, new_c) not in ocean_reachable and heights[new_r][new_c] >= heights[r][c]:
                        # Recursively explore the new cell.
                        dfs(new_r, new_c, ocean_reachable)
        
        # Perform DFS from the left and top edges (Pacific Ocean).
        for r in range(rows):
            dfs(r, 0, pacific_reachable)
        for c in range(cols):
            dfs(0, c, pacific_reachable)
        
        # Perform DFS from the right and bottom edges (Atlantic Ocean).
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable)
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable)
        
        # Find the intersection of cells that can flow to both oceans.
        result = list(pacific_reachable.intersection(atlantic_reachable))
        
        return result     
