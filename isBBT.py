#判断一棵树是否为平衡二叉树
class Node(object):
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

class ReturnData(object):
    def __init__(self,isBalance,height):
        self.isBalance = isBalance
        self.height = height

def judge(head):
    if (head == None):
        return ReturnData(True,0)
    leftData = judge(head.left)
    if not leftData.isBalance:   #如果左边不平衡
        return ReturnData(False, 0)
    rightData = judge(head.right)
    if not rightData.isBalance:  #如果右边不平衡
        return ReturnData(False, 0)
    if (abs(leftData.height-rightData.height)>1):  #计算两边的高度差
        return ReturnData(False, 0)
    return ReturnData(True, (max(leftData.height,rightData.height)+1))

def isBalance(head):
    return judge(head).isBalance


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.right = Node(4)
    head.right.right = Node(5)
    a = isBalance(head)
    print(a)