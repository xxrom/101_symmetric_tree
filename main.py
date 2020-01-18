class TreeNode(object):
    def __init__(self, val, leftNode=None, rightNode=None):
        self.val = val
        self.left = leftNode
        self.right = rightNode

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Tree():
    def __init__(self, rootNode):
        self.root = rootNode

    def mirror(self, node=None):
        if node is None:
            return

        # Switch children
        tempNode = node.left
        node.left = node.right
        node.right = tempNode

        if node.left:
            self.mirror(node.left)
        if node.right:
            self.mirror(node.right)

    def printTree(self, queue=None, output=[]):
        # init queue and output
        if queue is None:
            queue = [self.root]
            if self.root != None:
                output = [self.root.val]
        # Exit
        if len(queue) == 0:
            return output

        # Get first element
        node = queue.pop(0)

        if node is not None and node.left != None:
            output.append(node.left.val)
            queue.append(node.left)
        else:
            output.append(None)

        if node is not None and node.right != None:
            queue.append(node.right)
            output.append(node.right.val)
        else:
            output.append(None)

        # Go dipper or return output and exit
        return self.printTree(queue, output)


class Solution():
    """
    :type root: TreeNode
    :rtype: bool
    """

    def isSymmetric(self, root):
        tree = Tree(root)
        treeFirst = tree.printTree()
        print('treeFirst', treeFirst)
        tree.mirror(tree.root)
        treeSecond = tree.printTree()
        print('secondTree', treeSecond)
        print(treeFirst == treeSecond)
        return treeFirst == treeSecond


# tree0 = [1,2,2,3,4,4,3]
# tree1 =  [1,2,2,NULL,3,NULL,3]

initTree0 = TreeNode(1, TreeNode(2, TreeNode(4),  None),
                     TreeNode(2, TreeNode(4), TreeNode(5)))

initTree1 = TreeNode(1, TreeNode(2, TreeNode(5),  TreeNode(4)),
                     TreeNode(2, TreeNode(4), TreeNode(5)))
mySolution = Solution().isSymmetric(initTree0)
print('ans %s' % mySolution)
