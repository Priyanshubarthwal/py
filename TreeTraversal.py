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

def PreOrder(root):
    if root==None:
        return ;
    print(root.data,end=" ");
    PreOrder(root.left);
    PreOrder(root.right);

def InOrder(root):
    if root==None:
        return ;
    InOrder(root.left);
    print(root.data,end=" ");
    InOrder(root.right);

def PostOrder(root):
    if root==None:
        return ;
    PostOrder(root.left);
    PostOrder(root.right);
    print(root.data,end=" ");



def main():
    root = node(10);

    root = Insert(root, 60);
    root = Insert(root, 45);
    root = Insert(root, 25);
    root = Insert(root, 12);
    root = Insert(root, 61);
    root = Insert(root, 19);
    root = Insert(root, 92);
    root = Insert(root, 55);

    print("PreOrder traversal is:",end=" ");PreOrder(root);
    print("\nInOrder traversal is:",end=" ");InOrder(root);
    print("\nPostOrder traversal is:",end=" ");PostOrder(root);





if __name__ == "__main__":
    main();
