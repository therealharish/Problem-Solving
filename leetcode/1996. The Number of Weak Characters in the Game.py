class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        count = 0
        properties.sort()
        l = [properties[-1][0], properties[-1][1]]
        last = 0
        for i in range(len(properties) - 2, -1, -1):
            if (properties[i][0] < l[0]):
                if (properties[i][1] < l[1]):
                    count += 1
                else:
                    l[0] = properties[i][0]
                    last = l[1]
                    l[1] = max(l[1], properties[i][1])
            elif (properties[i][0] == l[0]):
                if last > properties[i][1]:
                    count += 1

        return count
