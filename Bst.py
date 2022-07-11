class node:
    def __init__(self,data):
        self.data=data;
        self.left=self.right=None;

def Insert(root,data):
    if root==None:
        return node(data);
    elif(data<=root.data):
        root.left=Insert(root.left,data);
    elif(data>=root.data):
        root.right=Insert(root.right,data);
    else:
        print("Duplicate key");
    return root;

def Findmaxad(root):
    while(root.right!=None):
        root=root.right;
    return root;

def Deletion(root,data):
    if(root==None):
        return None;
    elif(data>root.data):
        root.right=Deletion(root.right,data);
    elif(data<root.data):
        root.left=Deletion(root.left,data);

    else:
        if(root.right and root.left):
            temp=Findmaxad(root.left);
            root.data=temp.data;
            root.left=Deletion(root.left,root.data);

        elif(root.left==None):
            temp=root;
            root=root.right;
            del temp;

        elif(root.right==None):
            temp=root;
            root=root.left;
            del temp;

        else:
            del root;
            root=None;

    return root;

def Search(root,data):
    if(root==None):
        print("Not found");
        return None;
    elif(data<root.left.data):
        return Search(root.left,data);
    elif(data>root.right.data):
        return Search(root.right,data);
    else:
        return root;




def main():
    root=node(10);

    root=Insert(root,60);
    root = Insert(root, 45);
    root = Insert(root, 25);
    root = Insert(root, 12);

    root=Deletion(root,60);
    



if __name__=="__main__":
    main();
