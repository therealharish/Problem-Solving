# in notes pg 99
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        forward = [0] * len(arr)
        forward[0] = arr[0]
        for i in range(1, len(arr)):
            if (forward[i - 1] + arr[i] >= arr[i]):
                forward[i] = arr[i] + forward[i - 1]
            else:
                forward[i] = arr[i]

        backward = [0] * len(arr)
        backward[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            if (backward[i + 1] + arr[i] >= arr[i]):
                backward[i] = arr[i] + backward[i + 1]
            else:
                backward[i] = arr[i]

        print(forward, backward)

        maxS = max(forward)
        maxS = max(maxS, max(backward))
        #         these two cases are for when we don't remove any element
        for i in range(1, len(arr) - 1):
            maxS = max(maxS, forward[i - 1] + backward[i + 1])
        return maxS
