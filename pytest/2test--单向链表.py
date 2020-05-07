print('用单向链表表示十进制整数，求两个正整数的和。'
      '如，1234+34=1268，注意单项链表的方向从前向后，'
      '不允许使用其他数据结构')


class SingleNode(object):
    """
    单向链表节点
    """
    # item用来存放数据
    value = None
    # next指向下一节点
    next = None


class SingleLinkList(object):
    """
    单向链表
    """

    @staticmethod
    def get_link(size):
        """将数字转化为链表"""
        # 初始化要创建的链表
        link = SingleNode()
        # 表示链表的最后一个指针
        last_node = link
        # 创建size个节点并且添加到链表中
        size = str(size)
        for i in size:
            i = int(i)
            value = i
            # 临时节点（生成新的节点）
            node = SingleNode()
            node.value = value
            # 将链表的最后一个指针指向新生成的节点，即链表长度加1
            last_node.next = node
            # 将链表的最后一个指针更新（保持一直作为链表的最后一个节点）
            last_node = node
        return link

    @staticmethod
    def print_link(link):
        """打印链表"""
        if not link:
            return None
        if link.value is None:
            node = link.next
        else:
            node = link

        s = ''
        while node:
            # print(type(node.value))
            ss = str(node.value) + '->'
            s += ss
            node = node.next
        print(s)
        # print(len(s))

    def sum_num(self, a, b):
        """加法运算"""
        if not a:
            return None
        if a.value is None:
            node1 = a.next
        else:
            node1 = a

        if not b:
            return None
        if b.value is None:
            node2 = b.next
        else:
            node2 = b

        s1 = ''
        s2 = ''
        while node1:
            ss = str(node1.value)
            s1 += ss
            node1 = node1.next
        s1 = int(s1)

        while node2:
            ss = str(node2.value)
            s2 += ss
            node2 = node2.next
        s2 = int(s2)

        res = s1 + s2
        res_link = self.get_link(res)
        self.print_link(res_link)


ll = SingleLinkList()
a = ll.get_link(1234)
b = ll.get_link(34)
ll.print_link(a)
ll.print_link(b)
ll.sum_num(a, b)











