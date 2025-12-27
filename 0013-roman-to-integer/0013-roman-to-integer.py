class Solution:
    def romanToInt(self, s: str) -> int:
        romandict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        prev = 0


        for i in s:
            if romandict[i] > prev:
                sum += romandict[i] - 2 * prev
            else:
                sum += romandict[i]
            prev = romandict[i]

        return sum