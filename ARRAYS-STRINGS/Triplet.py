class Solution:
    def Triplet(self, nums):
        result = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):

                    if nums[i]+ nums[j]+ nums[k] == 0:
                        tuple1 = tuple(sorted([nums[i],nums[j],nums[k]]))
                        result.add(tuple1)
                        

        result=[ list(tup) for tup in result]

        return result


print(Solution().Triplet([-1,0,1,2,-1,-4,4]))

print(Solution().Triplet([0,0,0]))

print(Solution().Triplet([0,1,1]))


nums = list(map(int,input().split()))
print(Solution().Triplet(nums))
