class Solution:
    
    def bfs(self,node,v,edges):
        from collections import deque
        q=deque()
        q.append((node,-1))
        v.add(node)
        while q:
            root,parent= q.popleft()
            for neigh in edges[root]:
                if neigh not in v :
                    q.append((neigh,root))
                    v.add(neigh)
                elif neigh !=parent:
                    return True 
        return False

	def isCycle(self, V, edges):
		#Code here
		v=set()
		from collections import deque,defaultdict
		graph=defaultdict(list)
		for i,j in edges:
		    graph[i].append(j)
		    graph[j].append(i)
		for i in range(V):
		    if i not in v:
		        if self.bfs(i,v,graph):
		            return True 
		return False
	
		