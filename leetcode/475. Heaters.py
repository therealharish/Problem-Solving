class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.sort()
        
        def findNextHeater(house):
            low = 0
            high = len(heaters) - 1
            while(low <= high):
                mid = (low + high) // 2
                if heaters[mid] == house:
                    return mid
                elif heaters[mid] > house:
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        
        def findPreviousHeater(house):
            low = 0
            high = len(heaters) - 1
            while(low <= high):
                mid = (low + high) // 2
                if heaters[mid] == house:
                    return mid
                elif heaters[mid] > house:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        
        radius = float('inf')
        for house in houses:
            prev = findPreviousHeater(house)
            next = findNextHeater(house)
            print(house, prev, next)
            if prev == -1:
                prevDistance = float('inf')
            else:
                prevDistance = house - heaters[prev]
            if next == len(heaters):
                nextDistance = float('inf')
            else:
                nextDistance = heaters[next] - house
            radius = min(radius, min(prevDistance, nextDistance))
        return radius
            