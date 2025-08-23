from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        wordlen=len(words[0])
        totallen=wordlen * len(words)
        wordcount=Counter(words)
        res=[]
        for i in range(wordlen):
            left=i
            curr_count=Counter()
            for j in range(i,len(s)-wordlen+1,wordlen):
                word = s[j:j+wordlen]
                if word in wordcount:
                    curr_count[word]+=1
                    while curr_count[word]> wordcount[word]:
                        leftword=s[left:left+wordlen]
                        curr_count[leftword]-=1
                        left+=wordlen
                    if j+ wordlen - left==totallen:
                        res.append(left)
                else:
                    curr_count.clear()
                    left=j +wordlen
        return res




        