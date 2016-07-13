class BinaryTree:
    class Node:
        def __init__(self, l, r, v):
            self.left = l
            self.right = r
            self.value = v

    def __init__(self):
        self.top = None

    def insert(self, x):
        tmp_node = self.top
        new_node = BinaryTree.Node(None, None, x)
        if self.top:
            while(True):
                if x < tmp_node.value:
                    if not tmp_node.left:
                        tmp_node.left = new_node
                        return
                    else:
                        tmp_node = tmp_node.left
                else:
                    if not tmp_node.right:
                        tmp_node.right = new_node
                        return
                    else:
                        tmp_node = tmp_node.right
        else:
            self.top = new_node

    def search(self, x):
        tmp_node = self.top
        while(True):
            if tmp_node:
                if (tmp_node.value == x):
                    return True
                elif(tmp_node.value > x):
                    tmp_node = tmp_node.left
                else:
                    tmp_node = tmp_node.right
            else:
                return False

    def traverse(self, node, arr):
        if node:
            self.traverse(node.left, arr)
            arr.append(node.value)
            self.traverse(node.right, arr)

    def sub_delete(self, tree, value):
        if tree:
            if tree.value == value:
                if not tree.right:
                    return tree.left
                elif not tree.left:
                    return tree.right
                else:
                    ret = tree.left
                    tmp_right = ret
                    while(tmp_right.right):
                        tmp_right = tmp_right.right
                    tmp_right.right = tree.right
                    return ret
            elif value < tree.value:
                tree.left = self.sub_delete(tree.left, value)
                return tree
            else:
                tree.right = self.sub_delete(tree.right, value)
                return tree
        else:
            return None
                
    def delete(self, value):
        if not self.top:
            print 'Not Found: %d' % value
            return
        if self.top.value == value:
            self.top = self.sub_delete(self.top, value)
        elif value < self.top.value:
            self.top.left = self.sub_delete(self.top.left, value)
        else:
            self.top.right = self.sub_delete(self.top.right, value)

    def __str__(self):
        if not self.top:
            return 'BinaryTree()'
        str = 'BinaryTree('
        arr = []
        self.traverse(self.top, arr)
        while(True):
            e = arr.pop(0)
            str += '%d' % e
            if arr:
                str += ', '
            else:
                str += ')'
                break
        return str
                
if __name__ == '__main__':
    import random
    tree = BinaryTree()
    data = [random.randint(0, 100) for x in range(10)]
    print data
    print tree
    for x in data: tree.insert(x)
    print tree
    for x in data:
        print 'search', x, tree.search(x)
        print 'delete', x
        tree.delete(x)
        print 'search', x, tree.search(x)
        print tree
