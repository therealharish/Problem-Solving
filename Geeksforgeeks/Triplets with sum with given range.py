class Solution:
    def countTriplets(self, Arr, N, L, R):
        def findPairCount(arr, curr, start, range):
            end = len(arr) - 1
            count = 0
            while (start < end):
                if (arr[curr] + arr[start] + arr[end] < range):
                    count += end - start
                    start += 1
                elif (arr[curr] + arr[start] + arr[end] >= range):
                    end -= 1
            return count

        Arr.sort()
        lowerCount = 0
        higherCount = 0
        for i in range(N - 2):
            if (i > 0 and Arr[i] == Arr[i - 1]):
                continue
            lowerCount += findPairCount(Arr, i, i + 1, L)
            higherCount += findPairCount(Arr, i, i+1, R+1)
        return higherCount - lowerCount