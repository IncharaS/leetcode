from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        \\\
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        \\\
        if endWord not in wordList:
            return 0

        
        # Initialize the queue and visited set
        queue = deque([beginWord])
        visited = set([beginWord])
        wordSet = set(wordList)
        
        # Perform BFS
        count = 1  # We start from beginWord, so count starts at 1
        while queue:
            # Process all nodes (words) at the current level
            level_size = len(queue)
            for _ in range(level_size):
                word = queue.popleft()
                
                # If the word matches the endWord, return the count (number of steps)
                if word == endWord:
                    return count
                
                # Try all possible single-letter transformations
                for i in range(len(word)):
                    for letter in \abcdefghijklmnopqrstuvwxyz\:
                        new_word = word[:i] + letter + word[i+1:]
                        
                        # If the new word is in the wordList and has not been visited yet
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
                            wordSet.remove(new_word)
            
            # Increment the count for the next level in BFS
            count += 1

        # If the endWord is not found, return 0
        return 0
