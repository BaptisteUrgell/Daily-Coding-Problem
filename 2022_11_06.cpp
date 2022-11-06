#include <iostream>
using namespace std;

class Node {
	public:
		int data;
		Node* next;

	 Node(int value, Node* next_ptr) {
		data = value;
		next = next_ptr;
    };
};

class List {
    public:
    Node *head;
	int size;

    List(Node *node){
        head = node;
		size = 0;
		if (head != NULL)
			size++;		
    };

	private:
	void rec_concat(Node *current, Node *end) {
		if (current->next == NULL) {
			current->next = end;
			return;
		}
		else
			return rec_concat(current->next, end);
	};

	private:
	string rec_list_tostring(Node *current, string list_string) {
		list_string += std::to_string(current->data);
		if (current->next == NULL)
			return list_string;
		else {
			list_string += ", ";
			return rec_list_tostring(current->next, list_string);
		}		
	};

	public:
	string to_string() {
        string list_string = "list[";
		if (head != NULL)
			list_string += rec_list_tostring(head, "");
		return list_string += "]";
    };

	void append(int data) {
		Node *end = new Node(data, NULL);
		if (head == NULL)
			head = end;
		else
			rec_concat(head, end);
		size++;
	};

	private:
	void rec_free_nodes(Node *current) {
		if (current->next == NULL)
			return free(current);
		else {
			Node* next = current->next;
			free(current);
			return rec_free_nodes(next);
		}
	};

	public:
	void free_nodes(){
		if (head != NULL)
			rec_free_nodes(head);
		head = NULL;
		return;
	};

    Node* init_pop(Node *current, int k){
        if (k > 0)
            return init_pop(current->next, k-1);
        else
            return current;
    };

	public:
    void pop(int k){
        Node *end = init_pop(head, k-1);
        Node *cur = head;
        Node *prev = NULL;

        while (end->next != NULL) {
            prev = cur;
            cur = cur->next;
            end = end->next; 
        }

        if (prev == NULL){
            head = cur->next;
            free(cur);
        } else {
            prev->next = cur->next;
            free(cur);
        }
    };
};

int main() {
	List *list1 = new List((Node *)NULL);

	list1->append(3);
    list1->append(7);
	list1->append(5);
	
	printf("%s\n",list1->to_string().c_str());
	list1->pop(2);
	printf("%s\n",list1->to_string().c_str());

	list1->free_nodes();
	
	free(list1);
	
	return 0;
};