
#include <bits/stdc++.h>
using namespace std;

struct Node {
	int val;
	struct Node* next;
	Node(int x)
	{
		val = x;
		next = NULL;
	}
};

class LinkedlistIS {

public:
	Node* head;
	Node* sorted;

	void push(int val)
	{
		Node* newnode = new Node(val);
		newnode->next = head;
		head = newnode;
	}

	void insertionSort(Node* headref)
	{
		// Initialize sorted linked list
		sorted = NULL;
		Node* current = headref;
		while (current != NULL) {
			
			Node* next = current->next;
			sortedInsert(current);
			current = next;
		}
		head = sorted;
	}
	void sortedInsert(Node* newnode)
	{
		/* Special case for the head end */
		if (sorted == NULL || sorted->val >= newnode->val) {
			newnode->next = sorted;
			sorted = newnode;
		}
		else {
			Node* current = sorted;
			while (current->next != NULL
				&& current->next->val < newnode->val) {
				current = current->next;
			}
			newnode->next = current->next;
			current->next = newnode;
		}
	}
	void printlist(Node* head)
	{
		while (head != NULL) {
			cout << head->val << " ";
			head = head->next;
		}
	}
};
