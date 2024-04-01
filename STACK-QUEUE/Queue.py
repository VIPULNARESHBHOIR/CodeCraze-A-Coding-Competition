front = 0
rear = -1
n = 100
queue=[0 for i in range (n)]

class Solution:

    def enqueue(self,val):
        global front
        global rear 
        global n

        if rear >= n:
            print("Queue is FULL")
        else:
            rear += 1
            queue[rear] = val
        


    def dequeue(self):
        global front
        global rear 
        global n

        if rear == -1:
            return 'Que is Empty'

        ele=queue[front]
        for i in range(0,rear+1):
            queue[i] = queue[i+1]

        queue[rear] = 0  
        rear -= 1

        return ele


    def get(self):
        global front
        global rear 
        global n

        if rear == -1:
            return 'Que is Empty'
        
        return queue[front]



s=Solution()

s.enqueue(42)
s.enqueue(7)
s.enqueue(8)
s.enqueue(9)


print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())

print(queue)

s.enqueue(40)
s.enqueue(7)
s.enqueue(8)
s.enqueue(9)

print(queue)

print(s.get())

