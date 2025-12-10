class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi=float('-inf')
        l=0
        count={}
        for i in range(len(fruits)):
            if fruits[i] not in count:
                count[fruits[i]]=1
            else:
                count[fruits[i]]+=1
            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            maxi=max(maxi,i-l+1)
        return maxi