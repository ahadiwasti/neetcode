class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def helper(w1,w2):
            if len(w1) != len(w2):
                return False
            count = 0
            for i in range((len(w1))):
                if w1[i] != w2[i]:
                    count+=1

            return count == 1
            
        q = deque()
        q.append((beginWord,1))
        visited = set()
        visited.add(beginWord)

        while q:
            word1,level = q.popleft()
            for word in wordList:
                if word in visited or not helper(word1,word):
                    continue

                if word == endWord:
                    return level+1

                q.append((word,level+1))
                visited.add(word)

        return 0

        
      