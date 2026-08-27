# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        output = []
        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            lev_list = []
            for i in range(len(queue)):
                curr = queue.popleft()
                lev_list.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
            output.append(lev_list)
        return output


