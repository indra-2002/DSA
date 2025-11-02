class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        from collections import defaultdict, deque
        pattern_map=defaultdict(list)
        for word in wordset:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                pattern_map[pattern].append(word)
        q=deque()
        q.append((beginWord,1))
        visited=set()
        while q:
            word, steps = q.popleft()
            if word== endWord:
                return steps
            for i in range(len(word)):               
                pattern=word[:i]+ "*" + word[i+1:]
                for neigh in pattern_map[pattern]:
                    if neigh not in visited:
                        q.append((neigh,steps+1))
                        visited.add(neigh)
                
        return 0