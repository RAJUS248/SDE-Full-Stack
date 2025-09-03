from collections import deque

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class Trees:

    def __init__(self):
        self.root = None
    
    def createBinaryTree(self):
        # level 1
        self.root = Node(1)

        # level 2
        self.root.left = Node(2)
        self.root.right = Node(3)

        # level 3 
        self.root.left.left = Node(4)
        self.root.left.right = Node (5)
        self.root.right.left = Node(6)
        self.root.right.right = Node (7)

    # Display the tree nodes in Pre-order 
    def printBinaryTree(self, node: Node): # 1: function parameters
        
        # 2 Loop termination condition
        if (node == None):
            print(" None ")    
            return
        
        # 3 Work
        print(f" {node.data} ")

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        self.printBinaryTree(node.left)

        # Recursively visit the right sub tree
        self.printBinaryTree(node.right)

        # 5 return nothing

 # Display the tree nodes in Pre-order 
    def CountNodes(self, node: Node)-> int: # 1: function parameters
        
        # 2 Loop termination condition
        if (node == None):
            print(" None ")    
            return 0
        
       
        print(f" {node.data} ")

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        leftCount = self.CountNodes(node.left)

        # Recursively visit the right sub tree
        rightCount = self.CountNodes(node.right)

         # 3 Work
        TotalCount = leftCount + rightCount + 1
        return TotalCount  # return 
    
        # return (1+ leftCount(node.left) + rightCount(node.right))

    def FindMax(self, node: Node)-> int: # 1: function parameters
        
        # 2 Loop termination condition
        if (node == None):
            print(" None ")    
            return 0
        
       
        print(f" {node.data} ")

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        leftMax = self.FindMax(node.left)

        # Recursively visit the right sub tree
        rightMax = self.FindMax(node.right)

         # 3 Work
        maxValue = max(leftMax, rightMax)
        maxValue = max(maxValue, node.data)
        return maxValue
    














    
    def FindMin(self, node: Node)-> int: # 1: function parameters
        
        # 2 Loop termination condition
        if (node == None):
            print(" None ")    
            return 0
        
       
        print(f" {node.data} ")

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        leftMin = self.FindMin(node.left)

        # Recursively visit the right sub tree
        leftMin = self.FindMin(node.right)

         # 3 Work
        minValue = min(leftMin, leftMin)
        minValue = min(minValue, node.data)
        return minValue

    def GetSum(self, node: Node)-> int: # 1: function parameters
        
        # 2 Loop termination condition
        if (node == None):
            print(" None ")    
            return 0
        
       
        print(f" {node.data} ")

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        leftSum = self.GetSum(node.left)

        # Recursively visit the right sub tree
        rightSum = self.GetSum(node.right)

         # 3 Work
        totalSum = leftSum + rightSum + node.data
        return totalSum

    def GetSumOfLeafNodes(self, node: Node)-> int: # 1: function parameters
       # Edge case Tree is empty
        if (node == None):
            return 0
        
        # 2 Loop termination condition
        if (node.left == None and node.right == None):
            return node.data
       
        print(f" {node.data} ")

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        leftSum = self.GetSumOfLeafNodes(node.left)

        # Recursively visit the right sub tree
        rightSum = self.GetSumOfLeafNodes(node.right)

         # 3 Work        
        leafNodesSum = leftSum + rightSum         
        return leafNodesSum
    
    def GetLeafNodesMax(self, node: Node)-> int: # 1: function parameters
        
        if (node == None):
            return 0
        
        # 2 Loop termination condition
        if (node.left == None and node.right == None):
            return node.data
       
        print(f" {node.data} ")

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        leftLeafNodeMax = self.GetLeafNodesMax(node.left)

        # Recursively visit the right sub tree
        rightLeafNodeMax = self.GetLeafNodesMax(node.right)

         # 3 Work        
        leafNodeMax = max(leftLeafNodeMax, rightLeafNodeMax)      
        return leafNodeMax
    
    def IsBinaryTreeBalanced(self, node: Node)-> bool:
        if (node == None):
            return True
        
        leftTreeCount = self.CountNodes(node.left)
        rightTreeCount = self.CountNodes(node.right)

        difference = abs(leftTreeCount - rightTreeCount)
        
        if (difference > 1):
            return False
        else:
            return True

    def Search(self, node: Node, key: int)-> bool: # 1: function parameters
        
        # 2 Loop termination condition
        if (node == None):            
            return False

        # 4 D & C strategy 
        # Recursively visit the left sub tree
        isFoundInLeftSubTree = self.Search(node.left, key)

        # Recursively visit the right sub tree
        isFoundInRightSubTree = self.Search(node.right, key)

        if (node.data == key or isFoundInLeftSubTree or isFoundInRightSubTree):
            return True
        else:
            return False

    def GetHeightOfBinaryTree(self, node: Node)-> int:
        if (node == None):
            return 0
        
        leftNodeHeight = self.GetHeightOfBinaryTree(node.left)
        rightNodeHeight = self.GetHeightOfBinaryTree(node.right)

        maxHeight = max(leftNodeHeight, rightNodeHeight)
        maxHeight = maxHeight + 1  # self count 
        return maxHeight

    def LevelOrderTraversal(self, node: Node):
        if (node == None):
            return
        
        queue = deque()
        queue.append(node)

        while not queue:
            nexNode = queue.popleft()
            print(f" {nexNode.data} ")

            if nexNode.left != None:
                queue.append(nexNode.left)
            
            if nexNode.right != None:
                queue.append(nexNode.right)

    def isBSTNotWorkingAlways(self, node: Node) -> bool:
        # termination
        if (node == None):
            return True
        
        # traversal D & C
        leftMax = self.FindMax(node.left)
        rightMin = self.FindMin(node.right)

        # Work
        if (node.data > leftMax and node.data < rightMin):
            return True
        else:
            return False
    
    def isBST(self, node: Node, maxValue, minValue) -> bool:
        # termination
        if (node == None):
            return True
        
        # Result for the sub-problem 
        if (node.data >= minValue or node.data <= maxValue):
            return True

        # traversal D & C
        isLeftBST = self.isBST(node.left, maxValue, node.data)
        isRightBST = self.isBST(node.right, node.data, minValue)
        return isLeftBST and isRightBST


    def getLeftMostChildValue(self, node:Node) -> int:
        if (node == None):
            return 0
    
        currentNode = node
        while currentNode.left != None:
            currentNode = currentNode.left
        
        return currentNode.data
    
    def getRighttMostChildValue(self, node:Node) -> int:
        if (node == None):
            return 0
    
        currentNode = node
        while currentNode.right != None:
            currentNode = currentNode.right
        
        return currentNode.data

    

myTree = Trees()
myTree.createBinaryTree()
myTree.printBinaryTree(myTree.root)

print(f"Number of nodes in the BT = {myTree.CountNodes(myTree.root)}")

print(f"Max value in BT = {myTree.FindMax(myTree.root)}")

print(f"Min value in BT= {myTree.FindMin(myTree.root)}")

print(f"Sum of all nodes in BT = {myTree.GetSum(myTree.root)}")

print(f"Sum of leaft nodes in BT = {myTree.GetSumOfLeafNodes(myTree.root)}")

print(f"Sum of leaft nodes in BT = {myTree.GetLeafNodesMax(myTree.root)}")

print(f"Search key 2 is it present = {myTree.Search(myTree.root, 2)}")
print(f"Search key 100 is it present = {myTree.Search(myTree.root, 100)}")

print(f"Height of the BT = {myTree.GetHeightOfBinaryTree(myTree.root)}")

print(f"Is this BT = {myTree.isBST(myTree.root)}")

print(f"Left most child value  = {myTree.getLeftMostChildValue(myTree.root)}")

print(f"Right most child value  = {myTree.getRighttMostChildValue(myTree.root)}")





        
        




