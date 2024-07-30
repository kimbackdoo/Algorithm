#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 101
// 전역변수 // 감염된 컴퓨터 수를 구하기 위한 cnt 변수와 탐색됐는지 판단하는 visited 배열 선언
// MAX_VERTICES로 visited 배열의 크기를 고정안하고 입력받은 정점 개수만큼만 배열이 할당되게 동적으로 배열 할당 
int cnt=0, *visited;
typedef struct GraphType {
	int n;
	int adj_mat[MAX_VERTICES][MAX_VERTICES];
} GraphType;

void init(GraphType *g) {
	int i, j;
	g->n = 0;
	for(i=0; i<MAX_VERTICES; i++)
		for(j=0; j<MAX_VERTICES; j++)
			g->adj_mat[i][j] = 0;
}

void insert_vertex(GraphType *g, int v) {
	if(((g->n)+1) > MAX_VERTICES) {
		fprintf(stderr, "그래프 : 정점의 개수 초과");
		return;
	}
	g->n++;
}

void insert_edge(GraphType *g, int start, int end) {
	if(start>=(g->n) || end>=(g->n)) {
		fprintf(stderr, "그래프 : 정점 번호 오류");
		return;
	}
	g->adj_mat[start][end] = 1;
	g->adj_mat[end][start] = 1;
}
// 인접 행렬로 표현된 그래프에 대한 깊이 우선 탐색. 
void dfs_mat(GraphType *g, int v) {
	int w;
	visited[v] = 1;
	for(w=1; w<g->n; w++) {
		if(g->adj_mat[v][w] && !visited[w]){
			cnt++; // 탐색할때마다 cnt 변수 1씩 증가시킨다. 
			dfs_mat(g, w);
		}	
	}	
}

int main() {
	// v:정점개수 e:간선개수 x, y : 컴퓨터 연결을 표시하기 위한 변수 
	int i, v, e, x, y; 
	GraphType *g = malloc(sizeof(GraphType));
	init(g);
	scanf("%d %d", &v, &e); // scanf는 공백 또는 개행을 기준으로 구분 
	for(i=0; i<=v; i++)
		insert_vertex(g, i); // 정점의 개수 즉, g->n은 입력받은 v+1이 된다. 
	visited = (int *)calloc(g->n, sizeof(int)); // visited g->n 만큼 0으로 동적할당
	for(i=0; i<e; i++) {
		scanf("%d %d", &x, &y);
		insert_edge(g, x, y); // 컴퓨터 연결을 표시 
	}
	dfs_mat(g, 1); // 1번 컴퓨터부터 탐색 시작 
	printf("%d \n", cnt);
	free(g); free(visited); // 동적할당을 해제 
	return 0;
}
