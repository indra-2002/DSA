class Solution:
    def findOrder(self, words):
        # code here
        from collections import defaultdict, deque
        graph=defaultdict(list)
        indegree={ch:0 for word in words for ch in word}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            for j in range(min(len(w1),len(w2))):
               if len(w1)> len(w2) and w1.startswith(w2):
                   return ""
               elif w1[j]!= w2[j]:
                   graph[w1[j]].append(w2[j])
                   indegree[w2[j]]+=1
                   break
        q=deque()
        for i in indegree:
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for i in graph[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return "".join(res) if len(res)==len(indegree) else ""