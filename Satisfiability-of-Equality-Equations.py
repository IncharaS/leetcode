from typing import List
from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = defaultdict(str)

        # Initialize each variable to be its own parent
        for ch in range(26):
            parent[chr(ord('a') + ch)] = chr(ord('a') + ch)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        # First pass: process '=='
        for string in equations:
            element1 = string[0]
            eq = string[1]
            element2 = string[3]

            if eq == '=':
                root_1 = find(element1)
                root_2 = find(element2)
                parent[root_1] = root_2

        # Second pass: process '!='
        for string in equations:
            element1 = string[0]
            eq = string[1]
            element2 = string[3]

            root_1 = find(element1)
            root_2 = find(element2)

            if eq == '!' and root_1 == root_2:
                return False

        return True
