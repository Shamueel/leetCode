class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapal = {} #occurance : how many alphabet of that occurance
        mapal2 = {}
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        for i , st in enumerate(s):
            if st in mapal:
                mapal[st] +=1
            else:
                mapal[st] = 1
        for i , st in enumerate(t):
            if st in mapal2:
                mapal2[st] +=1
            else:
                mapal2[st] = 1
        print(mapal)
        print(mapal2)
        if len(mapal) != len(mapal2):
            print("length no equal")
            return False
        else:
            return True
        '''
        arr = list(mapal.values())
        print(type(arr))
        print(arr)
        bar = list(mapal2.values())
        x=arr
        y=bar
        for i in range(len(arr)):
            for j in range(len(bar)):
                if arr[i] == bar[j]:
                    print('match')
                    print('i',i)
                    print('j',j)
                    arr.pop(i)
                    bar.pop(j)
                    print(arr)
                    print(bar)
        '''
                
            
                
            
            
        
        
       