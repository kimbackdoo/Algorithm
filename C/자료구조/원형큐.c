#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 5

typedef int element;
typedef struct {
	element data[MAX_QUEUE_SIZE];
	int front, rear;
} QueueType;

void error(char *message) {
	fprintf(stderr, "%s\n", message);
	exit(1);
}

void init_queue(QueueType *q) {
	q->front = q->rear = 0;
}

int is_empty(QueueType *q) {
	return (q->front == q->rear);
}

int is_full(QueueType *q) {
	return (q->front == (q->rear + 1) % MAX_QUEUE_SIZE);
}

void queue_print(QueueType *q) {
	if(!is_empty(q)) {
		int i = q->front;
		do {
			i = (i+1)%(MAX_QUEUE_SIZE);
			printf("%d ", q->data[i]);
			if(i == q->rear) break;
		} while(i != q->front);
	}
	printf("\n");
}

void enqueue(QueueType *q, element item) {
	if(is_full(q)) error("Q가 꽉 찼습니다.");
	q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->data[q->rear] = item;
}

int dequeue(QueueType *q) {
	if(is_empty(q)) error("Q가 비었습니다.");
	q->front = (q->front + 1) % MAX_QUEUE_SIZE;
	return q->data[q->front];
}

int main() {
	QueueType queue;
	int item;
	
	init_queue(&queue);
	while(1) {
		printf("입력 : ");
		scanf("%d", &item);
		if(item == 0) dequeue(&queue);
		else enqueue(&queue, item);
		printf("큐 내용 출력 : ");
		queue_print(&queue);
	}
	return 0;
}
