        preLi = [1]
    
        postLi = deque([1])
    
    #print(type(postLi))
        #print(postLi)
        #postLi.appendleft(1)
        #print(postLi)
        #print(postLi[1])
        leftMul=nums[0]
        rightMul=nums[len(nums)-1]
        for i in range(1,len(nums)):
            
            preLi.append(leftMul)
            leftMul *= nums[i]
        #print(preLi)
        #1 2 3 4
        for i in range(len(nums)-2,-1,-1):
            #print('i',i)
            #print(nums[i])
            postLi.appendleft(rightMul)
            rightMul *= nums[i]
            #preLi.append(leftMul*nums[i-1])
            #leftMul *= nums[i-1]
        #print(preLi)
        #print(postLi)
        answer = []
        for i in range(len(nums)):
            answer.append(preLi[i]*postLi[i])
        #print(answer)
        return(answer)
