class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        sol=[]
        ans=[]
        def backtrack(start):
            if start==len(digits):
                ans.append("".join(sol[:]))
                return
            
            for j in dic[digits[start]]:
                sol.append(j)
                backtrack(start+1)
                sol.pop()
        backtrack(0)
        return ans


