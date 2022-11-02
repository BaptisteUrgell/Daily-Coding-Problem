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

	public:
    void concat(List *list_end) {
        if (head == NULL)
        	head = list_end->head;
		else
			rec_concat(head, list_end->head);
		size += list_end->size;
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

	private:
	Node* rec_pop(Node *current, int index, int start, int end) {
		if (index == start - 1){
			Node *popNode = current->next;
			current->next = rec_pop(current->next, index+1, start, end);
			return popNode;
		}
		if (index == end - 1) {
			Node *keepNode = current->next;
			current->next = NULL;
			return keepNode;
		}
		return rec_pop(current->next, index+1, start, end);
	};

	public:
	List* pop(int start=-1, int end=-1){
		if ((start == -1) && (end == -1)) {
			start = size - 1;
			end = size;
		}
		if (start == -1)
			start = 0;
		if (end == -1)
			end = size;

		Node *newNode = rec_pop(head, 0, start, end);
		List *list_pop = new List((Node *)NULL);
		
		if (start == 0) {
			list_pop->head = head;
			head = newNode;
		} else
			list_pop->head = newNode;			
		return list_pop;
    };
};


Node* intersectPoint(List* list1, List* list2){
	Node* ptr1 = list1->head;
	Node* ptr2 = list2->head;

	if (ptr1 == NULL || ptr2 == NULL)
		return NULL;

	while (ptr1 != ptr2) {
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;

		if (ptr1 == ptr2)
			return ptr1;

		if (ptr1 == NULL)
			ptr1 = list2->head;

		if (ptr2 == NULL)
			ptr2 = list1->head;
	}
	return ptr1;
};

int main() {
	List *list1 = new List((Node *)NULL);
	List *list2 = new List((Node *)NULL);
	List *list3 = new List((Node *)NULL);
	List *poplist;

	list1->append(3);
    list1->append(7);
	list1->append(5);

	list2->append(99);
    list2->append(1);

	list3->append(8);
	list3->append(10);

	list1->concat(list3);
	list2->concat(list3);
	
	List *list4 = new List(intersectPoint(list1, list2));

	printf("%s\n",list1->to_string().c_str());
	printf("%s\n",list2->to_string().c_str());
	printf("%s\n",list4->to_string().c_str());

	poplist = list1->pop(2);
	free(poplist);
	poplist = list2->pop(2);
	free(poplist);

	list1->free_nodes();
	list2->free_nodes();
	list3->free_nodes();
	
	free(list1);
	free(list2);
	free(list3);
	free(list4);
	
	return 0;
};