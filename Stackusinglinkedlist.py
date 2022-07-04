class node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
class Stack:
    def __init__(self):
        self.head=None;

    def isEmpty(self):
        if self.head==None:
            return True;
        else:
            return False;

    def Push(self,data):
        if self.head==None:
            self.head=node(data);
        else:
            newnode=node(data);
            newnode.next=self.head;
            self.head=newnode;
    def Pop(self):
        if(self.isEmpty()):
            return None;
        else:
            popnode=self.head;
            self.head=self.head.next;
            popnode.next=None;
            return popnode.data;
    def ViewStack(self):
        temp=self.head;
        if(self.isEmpty()):
            print("Stack Underflow");
        else:
            while(temp!=None):
                print(temp.data," ",end=" ");
                temp=temp.next;
            return;


def main():
    stack=Stack();
    stack.Push(1);
    stack.Push(2);
    stack.Push(3);

    stack.ViewStack();

    print("\n Poped Elment is:",stack.Pop());

    stack.ViewStack();


if __name__=="__main__":
    main();
