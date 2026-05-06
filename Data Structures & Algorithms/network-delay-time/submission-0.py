class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d, t in times:
            graph[s].append([d,t])
        
        min_heap = []
        visited = set()
        heapq.heappush(min_heap, (0, k))
        t =0
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, time)
            for nei_node, nei_time in graph[node]:
                if nei_node not in visited:
                    heapq.heappush(min_heap, (nei_time+time, nei_node))
                
        return t if len(visited) == n else -1
