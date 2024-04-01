class Solution:
    def Coins(self, nums, amt):
        nums.sort(reverse=True)
        total = 0
        for coin in nums:
            if coin <= amt:
                total += amt // coin
                amt = amt % coin

            if (amt == 0):
                break
            
        
        return total if amt == 0 else -1

print(Solution().Coins([1,2,5],11))

print(Solution().Coins([2],3))

print(Solution().Coins([1],0))

nums = list(map(int,input().split()))
amt= int(input())

print(Solution().Coins(nums,amt))

