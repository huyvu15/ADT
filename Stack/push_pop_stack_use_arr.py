class MyStack:
    
  def __init__(self):
    self.arr=[]
    
  #Function to push an integer into the stack.
  def push(self,data):
    #add code here
    self.arr.append(data)
    
  def isEmpty(self):
    return len(self.arr) == 0
  #Function to remove an item from top of the stack.
  def pop(self):
    #add code here
    if self.isEmpty():
      return -1;
    return self.arr.pop()
        

if __name__=='__main__':
  #Add code here
  n = int(input())
  a = MyStack()
  
  c = []
  
  for i in range(n):
    operation = input().split()
    if operation[0] == "push":
        a.push(int(operation[1]))
    elif operation[0] == "pop":
        # print(a.pop(), end=" ")
        c.append(a.pop())
    
  for i in c:
    print(i, end = " ")