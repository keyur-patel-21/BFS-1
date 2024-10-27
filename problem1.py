# Approach:
    # We perform a level order traversal (BFS) on the binary tree using a queue to keep track of nodes at each level.
    # For each level, we pop nodes from the queue, record their values, and add their children to the queue for processing in the next iteration.
    # This way, we build a list of lists where each sublist contains the values of nodes at a given level of the tree.

    # Time Complexity (TC): O(n), where n is the number of nodes in the tree.
    # We visit each node once, so the traversal time is linear in the number of nodes.
    
    # Space Complexity (SC): O(n), for storing the results in the output list and the queue.
    # In the worst case (a full binary tree), the last level could have up to n/2 nodes, so the space used by the queue is proportional to the number of nodes.

class Solution(object):
    def levelOrder(self, root):
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                res.append(level)
        
        return res
