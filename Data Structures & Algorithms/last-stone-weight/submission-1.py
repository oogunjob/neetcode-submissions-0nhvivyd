class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # NEED TO CREATE A MAX HEAP
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        # ITERATE WHILE THE LENGTH IS GREATER THAN 1
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if largest != second_largest:
                heapq.heappush(stones, largest - second_largest)

        stones.append(0)

        return -stones[0]
        