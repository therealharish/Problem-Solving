class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        notLost = []
        lostOne = []
        winSet = set()
        lossSet = set()
        players = set()
        for i in matches:
            win, loss = i
            d[loss] = d.get(loss, 0)+1
        for i in matches:
            win, loss = i
            players.add(win)
            players.add(loss)
        for i in players:
            if i not in d and i not in winSet:
                notLost.append(i)
                winSet.add(i)
            else:
                if(i in d and d[i]==1 and i not in lossSet):
                    lostOne.append(i)
                    lossSet.add(i)
        return [sorted(notLost), sorted(lostOne)]
            
            