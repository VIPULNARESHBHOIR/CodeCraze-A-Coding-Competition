class Solution:
    def LargeMaze(self,blocked, src, dest):
        if not blocked:
            return True
            
        block = 0
        opt=[-1,-1]
        dircetions=[[1,0],[0,1],[0,-1],[-1,0]]
        for m in range (1000000*1000000):
            for dircetion in dircetions:
                k,l = src
                i,j = dircetion
                p1,p2= i+k , l+j

                if [p1,p2] not in blocked and [p1,p2] > src:
                    src = [p1, p2]

                elif [p1,p2] in blocked:
                    block += 1

            if block == len(blocked):
                return False

            if src == dest :
                return True

            block = 0
        
        return False


#print(Solution().LargeMaze([[0,1],[1,0]],[0,0],[2,0]))
#print(Solution().LargeMaze([],[0,0],[999999,999999]))

s=Solution()
nodes=int(input())
blocked = [ list(map(int,input().split())) for _ in range(nodes) ] 
src = list(map(int,input().split()))
dest = list(map(int,input().split()))

print(s.LargeMaze(blocked,src,dest))