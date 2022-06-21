stack=[];
def isEmpty():
    if(len(stack)==0):
        return True;
    else:
        return False;
def Push(x):
    stack.append(x);
def Pop():
    if(len(stack)==0):
        print("Stack overflow");
        exit();
    else:
        return stack.pop();
def ViewStack():
    if(isEmpty()):
        print("Stack is empty");
        exit();
    for i in range(len(stack)-1,-1,-1):
        print(stack[i],end=" ");


def main():
    while(1):
        print("1=Push");
        print("2=Pop");
        print("3=Print Stack");
        print("4=Exit");
        choice=int(input("Enter your choice"));

        if(choice==1):
            x=int(input("Enter the number to be pushed"));
            Push(x);
        if(choice==2):
            x=Pop();
            print("Poped item is:",x);
        if(choice==3):
            ViewStack();
            print("\n");
        if(choice==4):
            exit();

if __name__=="__main__":
    main();
