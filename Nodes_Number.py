#已知一棵完全二叉树，求其节点的个数
class Node(object):
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

def NodeNum(head):
    if(head == None):
        return 0
    else:
        return judge(head,1,mostleftlevel(head,1))

def judge(node,level, height):
    if (level == height):
        return 1
    if (mostleftlevel(node.right,level+1) == height):
        return (pow(2,(height-level))) + judge(node.right,level+1,height)
    else:
        return (pow(2,(height-level-1))) + judge(node.left,level+1,height)


def mostleftlevel(node,level): #整个树最深的高度
    while(node != None):
        level += 1
        node = node.left
    return level - 1


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    a = NodeNum(head)
    print(a)