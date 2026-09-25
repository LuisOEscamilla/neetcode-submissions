class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = defaultdict(list)
        minHeap = []
        for x, y in points:
            currDist = ((x ** 2) + (y ** 2)) ** 0.5
            distances[currDist] += [[x,y]]
            minHeap.append(currDist)
        
        heapq.heapify(minHeap)
        results = []
        for _ in range(k):
            dist = heapq.heappop(minHeap)
            currCoords = distances[dist][0]
            del distances[dist][0]
            results.append(currCoords)

        return results
