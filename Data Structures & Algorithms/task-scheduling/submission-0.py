class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = []
        for val in counts.values():
            heapq.heappush(maxHeap, -val)
        
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                curr = heapq.heappop(maxHeap)
                curr += 1
                if curr:
                    queue.append((curr, time+n))
            if queue:
                if queue[0][1] == time:
                    new, timer = queue.popleft()
                    heapq.heappush(maxHeap, new)
            
        return time

        