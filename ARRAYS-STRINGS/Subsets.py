class Solution:
    def Subset(self, nums):
        res=[]
        subsets=[]

        def helper(i):  #DFS
            #print("res ",res)
            #print("subsets ",subsets)

            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            helper(i + 1)

            subsets.pop()
            helper(i + 1)

        helper(0)

        return res


nums = list(map(int,input().split()))
print(Solution().Subset(nums))