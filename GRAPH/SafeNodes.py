class Solution:
    def SafeNode(self, graph):

        new_graph = self.Graph(graph)
        safeNodes=[]

        for node in new_graph:
            if not new_graph[node]:
                safeNodes.append(node)

        for node in new_graph:
            if len(new_graph[node]) == 1:
                for req_node in new_graph[node]:
                    if req_node in safeNodes:
                        safeNodes.append(node)


        return sorted(safeNodes)



    def Graph(self, graphs):
        new_graph={}
        for node in range (len(graphs)):
            if node not in new_graph:
                new_graph[node]=[]

            for edges in graphs[node]:
                new_graph[node].append(edges)

            
        return new_graph


s=Solution()
nodes=int(input())
nums = [ list(map(int,input().split())) for _ in range(nodes) ]  

print(s.SafeNode(nums))

#print(s.SafeNode([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
