class Solution:
    def maxSumIS(self, Arr, n):
        sum = Arr.copy()
        for i in range(len(Arr)):
            m = Arr[i]
            for j in range(i):
                if (Arr[i] > Arr[j] and m < Arr[i] + sum[j]):
                    m = Arr[i] + sum[j]
            sum[i] = m
        return max(sum)
