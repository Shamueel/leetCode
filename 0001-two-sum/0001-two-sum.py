class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        print(len(nums))
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    print('append')
                    ans.append(i)
                    ans.append(j)
                    return ans
                    