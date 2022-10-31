class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        oneLoc = []
        for i in range(len(nums)):
            if (nums[i] == 1):
                oneLoc.append(i)

        prefixSum = [oneLoc[0]]
        for i in range(1, len(oneLoc)):
            prefixSum.append(oneLoc[i] + prefixSum[i - 1])

        print(oneLoc, prefixSum)

        ans = float('inf')
        ws = 0
        for we in range(len(oneLoc)):
            if ((we - ws + 1) < k):
                continue
            else:
                if (k & 1):
                    mid = ws + k // 2
                    totalMoves = (prefixSum[we] - prefixSum[mid])
                    rightHalf = 0
                    if (mid == 0):
                        rightHalf = 0
                    elif (ws == 0):
                        rightHalf = prefixSum[mid - 1]
                    else:
                        rightHalf = prefixSum[mid - 1] - prefixSum[ws - 1]
                    totalMoves -= rightHalf
                    radius = k // 2
                    saves = radius * (radius + 1)
                else:
                    mid = ws + k // 2 - 1
                    totalMoves = (prefixSum[we] -
                                  prefixSum[mid]) - (oneLoc[mid])
                    rightHalf = 0
                    if (mid == 0):
                        rightHalf = 0
                    elif (ws == 0):
                        rightHalf = prefixSum[mid - 1]
                    else:
                        rightHalf = prefixSum[mid - 1] - prefixSum[ws - 1]
                    totalMoves -= rightHalf

                    radius = mid - ws
                    saves = (radius) * (radius + 1) + (radius + 1)
                res = totalMoves - saves
                ans = min(ans, res)
                ws += 1
        return ans
