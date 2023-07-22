class Node: 
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left = None
        self.right = None

            
class NumArray:
    
    def __init__(self, nums: List[int]):
        self.root = Node(0, len(nums) - 1, 0)
        self.buildSegmentTree(self.root, nums)

    def update(self, index: int, val: int) -> None:
        return self.updateAndReturn(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeTree(self.root, left, right)
        
    def buildSegmentTree(self, node, nums):
        if node.start == node.end:
            node.val = nums[node.start]
            return
        # print(node)
        mid = (node.start + node.end) // 2
        node.left = Node(node.start, mid, 0)
        node.right = Node(mid + 1, node.end, 0)
        print("left", node.left.start, node.left.end)
        print("right", node.right.start, node.right.end)
        self.buildSegmentTree(node.left, nums)
        self.buildSegmentTree(node.right, nums)
        node.val = node.left.val + node.right.val
        
    def updateAndReturn(self, node, index, val):
        if node.start == node.end:
            diff = val - node.val
            node.val = val
            return diff
        mid = (node.start + node.end) // 2
        if index <= mid:
            diff = self.updateAndReturn(node.left, index, val)
        else:
            diff = self.updateAndReturn(node.right, index, val)
        node.val += diff
        return diff

    def sumRangeTree(self, node, left, right):
        if node.start == left and node.end == right:
            return node.val
        mid = (node.start + node.end) // 2
        sum = 0
        if left <= mid:
            sum += self.sumRangeTree(node.left, left, min(mid, right))
        if right > mid:
            sum += self.sumRangeTree(node.right, max(mid + 1, left), right)
        return sum
        
        
        
        
        
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)