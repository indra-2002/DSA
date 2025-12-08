class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans=[]
        def backtrack(i,path,evalution,last):
            if i==len(num):
                if evalution==target:
                    ans.append(path)
                return
            for j in range(i,len(num)):
                if j>i and num[i]=="0":
                    break
                curr_str=num[i:j+1]
                curr=int(curr_str)
                if i==0:
                    backtrack(j+1,curr_str,curr,curr)
                else:
                    backtrack(j+1, path + "+" + curr_str, evalution + curr ,curr)
                    backtrack(j+1, path +"-" + curr_str, evalution-curr,-curr)
                    backtrack(j+1, path + "*" + curr_str, evalution -last +last*curr,last*curr)
        backtrack(0,"",0,0)
        return ans
