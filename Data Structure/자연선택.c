#include<stdio.h>

#define COUNT_MEM 5

char *inputFileName = "data.txt";
char *outFileName[100];
int runNumber;
char minIndex = 0;
char minTemp = 0;
char chkEOF = 0;
int data[COUNT_MEM]; // -1 empty
int temp[COUNT_MEM];
int lastData = -1;
int i;

void main(){
   for(i=0 ; i<COUNT_MEM ; i++){
      data[i] = -1; temp[i] = -1;
   }

   FILE *outFilePointer;
   FILE *inFilePointer = fopen(inputFileName, "rt");
   //1
   for(i=0 ; i<COUNT_MEM && chkEOF!=-1 ; i++){
      chkEOF = fscanf(inFilePointer, "%d", &data[minIndex++]);
   }
   //2
   minIndex = findMin();
   sprintf(outFileName, "run%d.txt", ++runNumber);
   outFilePointer = fopen(outFileName, "wt+");
   fprintf(outFilePointer, "%d ", data[minIndex]);
   lastData = data[minIndex];
   
   while(chkEOF != -1){
      //3
      if(minTemp == COUNT_MEM){
         minIndex = findMin();
         while(minIndex != -1){
            fprintf(outFilePointer, "%d ", data[minIndex]);
            data[minIndex] = -1;
            minIndex = findMin();
         }
         for(i=0 ; i<COUNT_MEM ; i++){
            data[i] = temp[i];
            temp[i] = -1;
            minTemp = 0;
         }
         lastData = 0;
         minIndex = findMin();
         fclose(outFilePointer);
         if(chkEOF != -1){
            sprintf(outFileName, "run%d.txt", ++runNumber);
            outFilePointer = fopen(outFileName, "wt+");
            fprintf(outFilePointer, "%d ", data[minIndex]);
            lastData = data[minIndex];
         }
         continue;
      }
      
      chkEOF = fscanf(inFilePointer, "%d", &data[minIndex]);
      if(chkEOF == -1) break;
      
      //4 5 6
      minIndex = findMin();
      if(data[minIndex] < lastData){
         temp[minTemp++] = data[minIndex];
         data[minIndex] = -1;
         continue;
      }else if(data[minIndex] >= lastData){
         fprintf(outFilePointer, "%d ", data[minIndex]);
         lastData = data[minIndex];
         continue;
      }
   }
   minIndex = findMin();
   while(minIndex != -1){
      data[minIndex] = -1;
      minIndex = findMin();
      if(minIndex != -1)
         fprintf(outFilePointer, "%d ", data[minIndex]);
   }
   fclose(outFilePointer);
   fclose(inFilePointer);
}

int findMin(){
   int j, min=0;
   int empty = 1;
   for(j=1 ; j<COUNT_MEM ; j++){
      if(data[min] == -1){ min++; continue;}
      if(data[j]!=-1 && data[min] > data[j]) min = j;
   }
   
   for(j=0 ; j<COUNT_MEM ; j++){
      if(data[j] != -1) empty = 0;
   }
   if(empty) min = -1;
   
   return min;
}
