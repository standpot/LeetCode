class Solution:
    def isValid(self, s: str) -> bool:
        temp = ""
        for i in range(0, len(s), 1):
            if((s[i] == "(") or (s[i] == "[") or (s[i] == "{")): #open 하는 괄호는 저장
                temp += s[i]
            else:
                if(temp == ""):
                    return False
                else:
                    if ((temp[-1] == "(" and s[i] == ")") or (temp[-1] == "[" and s[i] == "]") or (temp[-1] == "{" and s[i] == "}")): #open 괄호중 가장 최근에 저장 된 것을 비교.
                        temp = temp[:-1] #일치할 시 가장 최근 저장 된 open 괄호는 삭제, 다음으로 가장 최근에 저장 된 값과 비교
                    else:
                        return False 
        if temp == "":
            return True
        else:
            return False