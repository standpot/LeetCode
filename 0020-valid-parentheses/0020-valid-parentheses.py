class Solution:
    def isValid(self, s: str) -> bool:
        temp = ""
        for i in range(0, len(s), 1):
            if((s[i] == "(") or (s[i] == "[") or (s[i] == "{")):
                temp += s[i]
            else:
                if(temp == ""):
                    return False
                else:
                    if ((temp[-1] == "(" and s[i] == ")") or (temp[-1] == "[" and s[i] == "]") or (temp[-1] == "{" and s[i] == "}")):
                        temp = temp[:-1]
                    else:
                        return False
        if temp == "":
            return True
        else:
            return False