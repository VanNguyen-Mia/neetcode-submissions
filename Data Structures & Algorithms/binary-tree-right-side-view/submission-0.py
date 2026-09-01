# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightside_lst = []
        queue = deque()
        if root:
            queue.append(root)
            rightside_lst.append(root.val)
        
        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            
            if queue:
                rightside_lst.append(queue[0].val)
            level += 1
        
        return rightside_lst