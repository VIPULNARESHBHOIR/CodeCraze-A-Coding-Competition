
class Solution:
    def Target(self, nums, target):
        flag = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):    #less than n2

                if nums[i] + nums[j] == target:
                    return [i,j]


        return [-1,-1]



print(Solution().Target([0],0))

nums = list(map(int,input().split()))
target= int(input())

print(Solution().Target(nums,target))

