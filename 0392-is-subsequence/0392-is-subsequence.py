class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = 0
        count = 0
        for i in range(len(s)):
            
            #print("first loop",s[i])
            for j in range(x,len(t)):
               # print('x =',x)
                #print(t[j])
                if s[i] == t[j] :
                 #   print('j=',j)
                    x = j+1
                    count += 1
                    break
       # print("count",count)
        if count == len(s):
            return True