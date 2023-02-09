#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @project: PYTHON_DataStructureAndAlgorithmAnalysis
# @File: 01_无序列表_链表.py
# @user: zx
# @Author: 张鑫
# @Email: xin_zhang0113@tju.edu.cn
# @create-time: 2023/1/12 17:19
# @Software: PyCharm

class Node:
    """
    功能说明：
        Node类，节点必须包含列表元素，我们称之为节点的数据变量。其次，节点必须保存指向下一个节点的引用
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    """
    功能说明：
        无序列表UnorderedList类构造方法，包含指向第一个节点的引用
    """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        # 1.创建一个新节点，将元素作为其数据
        temp = Node(item)
        # 2.将新节点的next引用指向当前列表中的第一个节点
        temp.setNext(self.head)
        # 3.修改列表的头节点，使其指向新创建的节点
        self.head = temp

    def length(self):
        # 初始化列表的头节点
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


if __name__ == "__main__":
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    data = mylist.search(17)
    print(data)
