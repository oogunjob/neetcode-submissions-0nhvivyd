class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # need to create a min heap, that will store the distances
        # with their respecitve coordinates

        # [(3, [0, 0]), (2, [3,2]), ...]

        # need to compute the distances for all of the points

        # time complexity: O(N)
        # space complexity: O(N)
        
        heap = []
        heapq.heapify(heap)

        def computeDistance(x, y):
            z = ((x - 0) ** 2) + ((y - 0) ** 2)
            return math.sqrt(z) 

        for x, y in points:
            distance = computeDistance(x, y)
            heapq.heappush(heap, (distance, [x, y]))

        res = []

        i = 0
        while i < k:
            element = heapq.heappop(heap)
            res.append(element[1])
            i += 1

        return res

        