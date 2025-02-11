# platform - leetcode
#link - https://leetcode.com/problems/maximum-depth-of-binary-tree/
# concept - caluclating maximum depth of a tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([root])
        count=0
        while queue:
            size=len(queue)
            count+=1
            for i in range(size):
                first=queue.popleft()
                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)
        return count
        
        