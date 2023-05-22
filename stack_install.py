# sử dụng mảng
class Stack1:
    def create_stack():
        stack = []
        return stack
    
    # create an empty stack
    def isEmpty(self,stack):
        return len(stack) == 0
    
    # Add items into the stack
    def push(self, stack, item):
        stack.append(item)
        print("pushed item: "+ item)
        
    # removing an element from the stack
    def pop(self, stack):
        if self.isEmpty():
            return "stack is empty"
        
        return stack.pop()

# stack = create_stack()
# push(stack, str(1))
# push(stack, str(2))
# push(stack, str(3))
# push(stack, str(4))
# print("popped item: " + pop(stack))
# print("stack after popping an element: " + str(stack))

# Sử dụng Linkedlist
class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:

	# Constructor to initialize the root of linked list
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root is None else False

	def push(self, data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
		print ("% d pushed to stack" % (data))

	def pop(self):
		if (self.isEmpty()):
			return float("-inf")
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

	def peek(self):
		if self.isEmpty():
			return float("-inf")
		return self.root.data


# Driver code
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print ("% d popped from stack" % (stack.pop()))
print ("Top element is % d " % (stack.peek()))   

