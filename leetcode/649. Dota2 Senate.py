class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        def bisectLeft(arr, target):
            l = 0
            r = len(arr)-1
            while l < r:
                mid = (l+r)//2
                if arr[mid] < target:
                    l = mid+1
                else:
                    r = mid
            return l if arr[l] >= target else l+1
        
        senate = list(senate)
        print(senate)
        d = {
            'R': [],
            'D': []
        }
        n = len(senate)
        for i, ele in enumerate(senate):
            d[ele].append(i)
            
        print(d)
        while d['R'] and d['D']:
            i = 0
            while(i<n and d['R'] and d['D']):
                # print(i)
                if senate[i] == 'R':
                    index = bisectLeft(d["D"], i)
                    if index < len(d['D']):
                        p = d['D'].pop(index)
                    else:
                        p = d['D'].pop(0)
                    senate[p] = 0
                elif senate[i] == 'D':
                    index = bisectLeft(d["R"], i)
                    if index < len(d['R']):
                        p = d['R'].pop(index)
                    else:
                        p = d['R'].pop(0)
                    senate[p] = 0
                i+=1
                # print(d)

        return 'Radiant' if d['R'] else 'Dire'       
    
# tabulate it
