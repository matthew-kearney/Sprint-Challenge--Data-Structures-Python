class BSTNode:
     def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None

     def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


     def contains(self, target):
        if self.value == target:
             return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                # if self.left.value == target:
                #     return True
                else:
                     return self.left.contains(target)
                    
            else: 
                if not self.right:
                    return False
                # if self.right.value == target:
                #     return True
                else:
                    return self.right.contains(target)