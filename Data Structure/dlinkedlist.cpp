#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct DListNode {	// ���߿��� ��� Ÿ��
	element data;
	struct DListNode *llink;
	struct DListNode *rlink;
} DListNode;
// ���� �޽��� ����� ���� �Լ�. 
void error(char *message) {
	fprintf(stderr, "%s\n", message);
}
// ���� ���� ����Ʈ�� �ʱ�ȭ
void init(DListNode *phead) {
	phead->llink = phead;
	phead->rlink = phead;
}
// ���� ���� ����Ʈ�� ��带 ���
void print_dlist(DListNode *phead) {
	DListNode *p;
	for(p=phead->rlink; p!=phead; p=p->rlink)
		printf("<-| %d |-> ", p->data);
	printf("\n");
}
// ���ο� �����͸� ��� before�� �����ʿ� �����Ѵ�.
void dinsert(DListNode *before, element data) {
	DListNode *newnode = (DListNode*)malloc(sizeof(DListNode));
	newnode->data = data;
	newnode->llink = before;
	newnode->rlink = before->rlink;
	before->rlink->llink = newnode;
	before->rlink = newnode;
}
// ��� removed�� �����Ѵ�.
void ddelete(DListNode *head, DListNode *removed) {
	if(removed == head) return;
	removed->llink->rlink = removed->rlink;
	removed->rlink->llink = removed->llink;
	free(removed);
}
// ���ϴ� data�� ã�´�. 
DListNode* search(DListNode *head, element data) {
	DListNode *p;
	for(p=head->rlink; p!=head; p=p->rlink) {
		if(p->data==data)
			return p;
	}
	return NULL;
}
// ���� ���� ����Ʈ �׽�Ʈ ���α׷�
int main(void) {
	int i;
	int menu,before,data;
	DListNode *p;
	DListNode *head = (DListNode*)malloc(sizeof(DListNode));
	init(head);
	for (i=10; i>=1; i--)
		dinsert(head, i);
	while(1){
		system("cls");//ȭ�� Ŭ���� 
		printf("���� ����Ʈ ����\n");
		print_dlist(head);
		printf("-----------------\n");
		printf("1. ����\n");
		printf("2. �߰�\n");
		printf("3. ����\n");
		printf("4. ����\n");
		printf("-----------------\n");
		printf("�۾�����(1~5): ");
		scanf("%d",&menu);
		if(menu==4)
		 break;
		switch(menu) {
			case 1://���ϴ� ��ġ�� ����
				printf("������ ��ġ����(������ ���� ���������� ���Ե�) : ");
				scanf("%d",&before);
				printf("������ ���� ���� : ");
				scanf("%d",&data);
				p=search(head, before);
				if(p==NULL)
					error("������ ��ġ�� ã�� �� �����ϴ�.\n");
				else if(before==data)
					error("������ �����Ͱ� �̹� �����մϴ�.\n");
				else
					dinsert(p, data);
				break;  
			case 2: //����Ʈ�� �������� ������ �߰� 
				printf("�߰��� ���� ���� : ");
				scanf("%d", &data);
				p=search(head, data);
				if(p==NULL)
					dinsert(head->llink, data);
				else
					error("������ �����Ͱ� �̹� �����մϴ�.\n");
				break;
			case 3:
				printf("������ ���ڸ� ���� : ") ;
				scanf("%d", &data);
				p=search(head, data);
				if(p==NULL)
					error("������ �����Ͱ� �����ϴ�.\n");
				else
					ddelete(head, p);  
		}
	}
	return 0;
}