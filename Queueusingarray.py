Queue=[];
def isEmpty():
    if(len(Queue)==0):
        return True;
    else:
        return False;
def ViewQueue():
    if(isEmpty()):
        print("Underflow");
        exit();
    print("Queue is: ",end=" ");
    for i in range(len(Queue)):
        print(Queue[i]," ");
def Pop():
    if(isEmpty()):
        print("Underflow");
        exit();
    return Queue.pop(0);

def Push(item):
    Queue.append(item);

def main():
    while(1):
        print("1=Push");
        print("2=Pop");
        print("3=View Queue");
        print("4=Exit");
        x=int(input("Enter your choice"));

        if(x==1):
            item=int(input("Enter the number to be inserted"));
            Push(item);
        if(x==2):
            item=Pop();
            print("Poped item is:",item);
        if(x==3):
            ViewQueue();
        if(x==4):
            exit();

if __name__=="__main__":
   main() ;
