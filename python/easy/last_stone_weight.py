# 1046. Last Stone Weight

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while stones and len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2:
                continue
            
            else:
                dif = abs(stone1 - stone2)
                heapq.heappush(stones, 0-dif)

        
        return 0 if not stones else abs(stones[0])