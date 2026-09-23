class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
    
class DoublyLL:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data, "--->", end=" ")
                temp=temp.next

l=DoublyLL()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.prev=n
n1.next=n2
l.display()
