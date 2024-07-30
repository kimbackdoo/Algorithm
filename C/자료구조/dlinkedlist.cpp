#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct DListNode {	// 이중연결 노드 타입
	element data;
	struct DListNode *llink;
	struct DListNode *rlink;
} DListNode;
// 에러 메시지 출력을 위한 함수. 
void error(char *message) {
	fprintf(stderr, "%s\n", message);
}
// 이중 연결 리스트를 초기화
void init(DListNode *phead) {
	phead->llink = phead;
	phead->rlink = phead;
}
// 이중 연결 리스트의 노드를 출력
void print_dlist(DListNode *phead) {
	DListNode *p;
	for(p=phead->rlink; p!=phead; p=p->rlink)
		printf("<-| %d |-> ", p->data);
	printf("\n");
}
// 새로운 데이터를 노드 before의 오른쪽에 삽입한다.
void dinsert(DListNode *before, element data) {
	DListNode *newnode = (DListNode*)malloc(sizeof(DListNode));
	newnode->data = data;
	newnode->llink = before;
	newnode->rlink = before->rlink;
	before->rlink->llink = newnode;
	before->rlink = newnode;
}
// 노드 removed를 삭제한다.
void ddelete(DListNode *head, DListNode *removed) {
	if(removed == head) return;
	removed->llink->rlink = removed->rlink;
	removed->rlink->llink = removed->llink;
	free(removed);
}
// 원하는 data를 찾는다. 
DListNode* search(DListNode *head, element data) {
	DListNode *p;
	for(p=head->rlink; p!=head; p=p->rlink) {
		if(p->data==data)
			return p;
	}
	return NULL;
}
// 이중 연결 리스트 테스트 프로그램
int main(void) {
	int i;
	int menu,before,data;
	DListNode *p;
	DListNode *head = (DListNode*)malloc(sizeof(DListNode));
	init(head);
	for (i=10; i>=1; i--)
		dinsert(head, i);
	while(1){
		system("cls");//화면 클리어 
		printf("현재 리스트 상태\n");
		print_dlist(head);
		printf("-----------------\n");
		printf("1. 삽입\n");
		printf("2. 추가\n");
		printf("3. 삭제\n");
		printf("4. 종료\n");
		printf("-----------------\n");
		printf("작업선택(1~5): ");
		scanf("%d",&menu);
		if(menu==4)
		 break;
		switch(menu) {
			case 1://원하는 위치에 삽입
				printf("삽입할 위치선택(선택한 숫자 오른쪽으로 삽입됨) : ");
				scanf("%d",&before);
				printf("삽입할 숫자 선택 : ");
				scanf("%d",&data);
				p=search(head, before);
				if(p==NULL)
					error("삽입할 위치를 찾을 수 없습니다.\n");
				else if(before==data)
					error("삽입할 데이터가 이미 존재합니다.\n");
				else
					dinsert(p, data);
				break;  
			case 2: //리스트의 마지막에 데이터 추가 
				printf("추가할 숫자 선택 : ");
				scanf("%d", &data);
				p=search(head, data);
				if(p==NULL)
					dinsert(head->llink, data);
				else
					error("삽입할 데이터가 이미 존재합니다.\n");
				break;
			case 3:
				printf("삭제할 숫자를 선택 : ") ;
				scanf("%d", &data);
				p=search(head, data);
				if(p==NULL)
					error("삭제할 데이터가 없습니다.\n");
				else
					ddelete(head, p);  
		}
	}
	return 0;
}
