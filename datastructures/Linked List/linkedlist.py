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

    def len_list(self):
        curr_node=self.head
        len=0
        while curr_node:
            len+=1
            curr_node=curr_node.next
        return len

    def swap_nodes(self,key1,key2):
        #fetch prev and next for key1
        curr_node1=self.head
        prev1=None
        while curr_node1.data!=key1:
            prev1=curr_node1
            curr_node1=curr_node1.next
        next1=curr_node1.next
        # fetch prev and next for key2
        curr_node2 = self.head
        prev2 = None
        while curr_node2.data != key2:
            prev2 = curr_node2
            curr_node2 = curr_node2.next
        next2 = curr_node2.next
        #swap
        #In case swapping Head and tails
        if not next1 and next2:
            curr_node2.next = next1
            self.head = curr_node2

            prev2.next = curr_node1
            curr_node1.next = None
            return

        #In case we are swapping the head node

        if not prev1:
            curr_node2.next = next1
            self.head=curr_node2

            prev2.next=curr_node1
            curr_node1.next = next2
            return

        #Incase we are swapping the last node
        if not next2:
            prev1.next=curr_node2
            curr_node2.next = next1

            prev2.next = curr_node1
            curr_node1.next = None
            return

        prev1.next=curr_node2
        curr_node2.next=next1

        prev2.next=curr_node1
        curr_node1.next=next2

llist = LinkedList()
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("A")

sw_a,sw_b="A","E"

llist.insert_after_node("D","E")
#llist.delete_node_pos(3)
llist.print_list()

print(f"Swapping Node {sw_a} to {sw_b}")

llist.swap_nodes(sw_a,sw_b)

llist.print_list()
#print(llist.len_list())
