#include <iostream>
#include <string>
using namespace std;


class Node {
    public:
        int data;
        Node *both;

    Node(int value, Node* prev_next) {
        data = value;
        both = prev_next;
    };
};

class List {
    private:
    Node *head;

    public:
    List(Node *node){
        head = node;
    };

    Node* Xor(Node* x, Node* y)
    {
        return (Node *)((uintptr_t)x  ^ (uintptr_t)y);
    };

    void append(int data) {
        Node *prev = NULL;
        Node *current = head;
        Node *next;
        Node *end = new Node(data, NULL);

        if (head == NULL){
            head = end;
        }
        else 
        {
            while (current != NULL)
            {
                next = Xor(prev, current->both);
                prev = current;
                current = next;
            }

            end->both = prev;
            prev->both = Xor(prev->both, end);
        }
    };

    string list_tostring() {
        Node *prev = NULL;
        Node *current = head;
        Node *next;

        string list_string = "list[";

        while (current != NULL) 
        {
            list_string += std::to_string(current->data);
            next = Xor(prev, current->both);
            prev = current;
            current = next;
            if (current != NULL)
                list_string += ", ";
        }
        return list_string + "]";
    };

    Node* get(int index){
        Node *prev = NULL;
        Node *current = head;
        Node *next;
        while ((current != NULL) && (index != 0)) 
        {
            next = Xor(prev, current->both);
            prev = current;
            current = next;
            index--;
        }
        return current;
    };

    void free_nodes(){
        Node *prev = NULL;
        Node *current = head;
        Node *next;

        if (head != NULL)
        {
            while (current != NULL) {
                free(current);
                next = Xor(prev, current->both);
                prev = current;
                current = next;
            }
        }
        head = NULL;
    };
};

int main() {
    List *mylist = new List((Node *)NULL);
    mylist->append(0);
    mylist->append(1);
    mylist->append(2);
    mylist->append(3);
    printf("%s\n",mylist->list_tostring().c_str());
    
    printf("%d\n", mylist->get(2)->data);
    printf("%p\n", mylist->get(-1));

    mylist->free_nodes();
    printf("%s\n",mylist->list_tostring().c_str());
    free(mylist);
    return 0;
}
