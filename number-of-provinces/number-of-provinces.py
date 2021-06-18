from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        queue = deque([])
        provinces = 0
        
        for city in range(len(isConnected)):   #O(N)
            if city in visited:
                continue
            visited.add(city)
            queue.append(city)
            while queue:
                v_city = queue.popleft()
                for nbr in range(len(isConnected[0])):    #O(N)
                    if nbr not in visited and isConnected[v_city][nbr] == 1:
                        queue.append(nbr)
                        visited.add(nbr)
            provinces += 1
        return provinces
        