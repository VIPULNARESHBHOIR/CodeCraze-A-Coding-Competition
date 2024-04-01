class Solution:
    def palindrom(self,str1):
        counter = 0
        left=0
        right=len(str1)-1

        str1 += '$'
        str1 = list(str1)

        while not (left >= right):
            if str1[left] == str1[right]:
                left += 1
                right -= 1
            else:
                str1.insert(right + 1,str1[left])
                left += 1
                counter +=1
                
        return counter



print(Solution().palindrom('abca'))

print(Solution().palindrom('abcdefg'))

print(Solution().palindrom('aaaaa'))

string = str(input())
print(Solution().palindrom(string))