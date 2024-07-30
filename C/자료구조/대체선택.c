#include <stdio.h>
#define M 5

char *in_fn = "data.txt";
char *out_fn_f = "run%d.txt";
char out_fn[15];
int n_run = 0;
char min_ndx;
char frozen[M] = {0, };
char chk;
int Buffer[M];
int lastKey;
int i;

void main(){
	FILE *ofp;
	FILE *ifp = fopen(in_fn, "rt");
	for(i = 0; i < M; i++)
		if(fscanf(ifp, "%d", &Buffer[i]) == -1)
			frozen[i] = -2;
	new_run:
		sprintf(out_fn, out_fn_f, ++n_run);
		ofp = fopen(out_fn, "wt+");
		for(i = 0; i < M; i++)
			if(frozen[i] != -2)
				frozen[i] = 0;
	repeat:
		chk = 0;
		min_ndx = -1;
		for (i = 0; i < M; i++){
			if(frozen[i] < 0) {
				chk += frozen[i];
				continue;
			}
			if(min_ndx == -1) {
				min_ndx = i;
				continue;
			}
			if(Buffer[min_ndx] > frozen[i]){
				min_ndx = i;
				continue;
			}
		}
		if(min_ndx == -1){
			fclose(ofp);
			if(chk > M * -2)
				goto new_run;
			fclose(ifp);
		}
		else{
			fprintf(ofp, "%d ", Buffer[min_ndx]);
			lastKey = Buffer[min_ndx];
			if(fscanf(ifp, "%d", &Buffer[min_ndx]) == -1)
				frozen[min_ndx] = -2;
			else if(lastKey > Buffer[min_ndx])
				frozen[min_ndx] = -1;
    		goto repeat;
		}
}
