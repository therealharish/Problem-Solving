class MyCalendarThree:

    def __init__(self):
      self.calendar = {}
        
    def book(self, start: int, end: int) -> int:
      cal = self.calendar
      cal[start] = cal.get(start, 0)+1
      cal[end] = cal.get(end, 0) - 1
      best = 0
      ans = 0
      for x,y in sorted(cal.items()):
        ans+=y
        best = max(best, ans)
      return best
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)