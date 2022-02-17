class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        if self.head is None:
            print("No elements in the list")
        else:
            curr_node=self.head
            while curr_node:
                print(curr_node.data)
                curr_node=curr_node.next

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_after_node(self,key,data):
        new_node=Node(data)
        curr_node=self.head
        while curr_node:
            if curr_node.data==key:
                next_node=curr_node.next
                curr_node.next=new_node
                new_node.next=next_node
            curr_node=curr_node.next

    def delete_node(self,key):
        curr_node=self.head
        if curr_node.data==key:
            self.head=curr_node.next
            curr_node=None
            return

        prev_node=None
        while curr_node.data!=key:
            prev_node=curr_node
            curr_node=curr_node.next

        if prev_node is None:
            return

        prev_node.next=curr_node.next
        curr_node=None

    def delete_node_pos(self,pos):
        curr_node=self.head
        if pos==0:
            self.head=curr_node.next
            curr_node=None
        index=1
        prev_node=None
        while curr_node and pos!=index:
            prev_node=curr_node
            curr_node=curr_node.next
            index+=1

        if curr_node==None:
            return
        prev_node.next=curr_node.next
        curr_node=None

    def lenlist(self):
        curr_node=self.head
        len=0
        while curr_node:
            len+=1
            curr_node=curr_node.next
        return len

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")
llist.insert_after_node("C","E")
llist.delete_node_pos(3)
llist.print_list()
print(llist.lenlist())
