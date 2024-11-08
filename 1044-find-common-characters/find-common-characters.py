class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d={}
        for word in range(len(words)):
            for chrs in words[word]:
                # print('chr',chrs,'words',words[word])
                if chrs in d:
                    if word not in d[chrs]:
                        d[chrs][word]=1
                    else:
                        d[chrs][word]+=1
                else:
                    d[chrs]={word:1}
            # print('dict:',d)
        ans=[]
        for char in d:
            if len(d[char])==len(words):
                min_c=101
                for count in d[char]:
                    if d[char][count]<min_c:
                        min_c=d[char][count]
                ans.extend([char for i in range(min_c)])
        
        return ans