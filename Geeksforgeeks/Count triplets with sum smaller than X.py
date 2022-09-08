# in notes 1 pg 12


class Solution:
    def countTriplets(self, arr, n, sumo):
        def findPairCount(curr, start):
            end = len(arr) - 1
            count = 0
            while (start < end):
                if (arr[curr] + arr[start] + arr[end] < sumo):
                    count += end - start
                    start += 1
                elif (arr[curr] + arr[start] + arr[end] >= sumo):
                    end -= 1
            return count

        arr.sort()
        ans = 0
        for i in range(n - 2):
            if (i > 0 and arr[i] == arr[i - 1]):
                continue
            ans += findPairCount(i, i + 1)
        return ans
