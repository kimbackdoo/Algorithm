#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode {
	element data;
	struct ListNode *link;
} ListNode;

void error(char *message) {
	fprintf(stderr, "%s\n", message);
}

ListNode* insert_first(ListNode *head, element value) {
	ListNode *p = (ListNode*)malloc(sizeof(ListNode));
	p->data = value;
	p->link = head;
	head = p;
	return head;
}

ListNode* insert(ListNode *head, ListNode* pre, element value) {
	ListNode *p = (ListNode*)malloc(sizeof(ListNode));
	p->data = value;
	p->link = pre->link;
	pre->link = p;
	return head;
}

ListNode* delete_first(ListNode *head) {
	ListNode *removed;
	if(head==NULL) return NULL;
	removed = head;
	head = removed->link;
	free(removed);
	return head;
}

ListNode* delete_node(ListNode *head, ListNode* pre) {
	ListNode *removed;
	removed = pre->link;
	pre->link = removed->link;
	free(removed);
	return head;
}

void print_list(ListNode *head) {
	ListNode *p;
	for(p=head; p!=NULL; p=p->link)
		printf("%d->", p->data);
	printf("\b\b  \n");
}

int isValue(ListNode* head, element value) {
	ListNode *p;
	for(p=head; p!=NULL; p=p->link)
		if(p->data==value)
			return 1;
	return 0;		
}

ListNode* find_pre(ListNode *head, element value, int mode) {
	ListNode *p, *pre;
	pre = head;
	if(mode==1) {
		if(!isValue(head, value)) {
			for(p=head; p!=NULL; pre=p, p=p->link)
				if(p->data > value)
					return pre;
			if(pre->data<value)	
				return pre;
		}
	}
	else {
		if(isValue(head, value))
			for(p=head; p!=NULL; pre=p, p=p->link)
				if(p->data==value)
					return pre;
	}
	return NULL;
}

int main() {
	ListNode *head = NULL;
	ListNode *pre = NULL;
	element value;
	int menu;
	for(int i=10; 1<=i; i--)
		head = insert_first(head, i);
	while(1) {
		print_list(head);
		printf("1. 삽입 \n2. 삭제 \n3. 종료 \n메뉴를 선택하세요 : ");
		scanf("%d", &menu);
		if(menu==3) break;
		switch(menu) {
			case 1:
				printf("삽입할 데이터는? ");
				scanf("%d", &value);
				pre = find_pre(head, value, 1);
				/* error */
				if(pre==head && head->data > value)
						head = insert_first(head, value);
				else if(pre==NULL)
					error("데이터가 이미 존재합니다.\n");
				else
					insert(head, pre, value);
				break;
			case 2:
				printf("삭제할 데이터를 선택 : ");
				scanf("%d", &value);
				pre = find_pre(head, value, 2);
				/* error */
				if(pre==head && value!=head->link->data)
					   head=delete_first(head);
				else if(pre==NULL)
					error("삭제할 데이터가 없습니다.\n");
				else
					delete_node(head, pre);
				break;
			default:
				printf("잘못된 번호입니다.\n");
				break; 
		}
	}
	return 0;
}
