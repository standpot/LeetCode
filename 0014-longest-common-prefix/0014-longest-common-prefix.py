class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in strs[1:]:
            temp = ""
            temp2 = 0
            for j in prefix:
                if temp2 < len(i) and j == i[temp2]:
                    temp += j
                    temp2 += 1
                else:
                    break
            prefix = temp

        return prefix