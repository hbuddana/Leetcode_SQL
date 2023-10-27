"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Create a dictionary to map original nodes to their corresponding cloned nodes.
        oldToNew = {}

        # Define a depth-first search (DFS) function to clone the graph.
        def dfs(node):
            # If the node has already been cloned, return the corresponding cloned node.
            if node in oldToNew:
                return oldToNew[node]

            # Create a new node with the same value as the original node.
            copy = Node(node.val)
            
            # Add the new node to the dictionary to track the mapping.
            oldToNew[node] = copy
            
            # Iterate through the neighbors of the original node and clone them recursively.
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            # Return the cloned node.
            return copy

        # If the input node is not None, start the DFS process to clone the graph.
        # If the input is None, return None to indicate an empty graph.
        return dfs(node) if node else None