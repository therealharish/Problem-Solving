# # class Solution:
# #     def sortColors(self, nums: List[int]) -> None:
# #       x = nums.count(0)
# #       y = nums.count(1)
# #       z = nums.count(2)
# #       xx = [0]*x
# #       yy = [1]*y
# #       zz = [2]*z

# #       xx.extend(yy)
# #       xx.extend(zz)

# #       nums[:] = xx

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#       low = 0
#       high = len(nums) -1
#       mid = 0
#       while(mid<=high):
#         if(nums[mid] == 0):
#           nums[low], nums[mid] = nums[mid], nums[low]
#           low+=1
#           mid+=1
#         elif(nums[mid] ==1):
#           mid+=1
#         elif(nums[mid] ==2):
#           nums[mid], nums[high] = nums[high], nums[mid]
#           high-=1

#         #


# IN COPY 1 PG 17
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        left = 0
        right = len(arr) - 1
        i = 0
        while (i <= right):
            if (arr[i] == 1):
                i += 1
            elif (arr[i] == 0):
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
                i += 1
            else:
                arr[right], arr[i] = arr[i], arr[right]
                right -= 1
        return arr