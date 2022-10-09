class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
      s = 0
      front = [0]
      for i in range(k):
        front.append(front[-1]+cardPoints[i])

      rear = [0]
      for i in range(k):
        rear.append(rear[-1] + len(cardPoints)-i-1)

      print(front, rear)

      for i in range(k):
        c = front[i] + rear[k-i]
        s = max(c, s)

      return s
        
