#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

char *stack;
int *intStack, top;

void initStack(int len){
	stack = (char*)malloc(sizeof(char)*len);
	intStack = (int*)malloc(sizeof(int)*len);
	top=-1;
}

void push(char ch){
	stack[++top]=ch;
}

char pop(){
	return stack[top--];
}

void intPush(int value){
	intStack[++top]=value;
}

int intPop(){
	return intStack[top--];
}

int isEmpty(){
	return top==-1;
}

int prec(char ch){
	switch(ch){
		case'(': case')': return 0;
		case'+': case'-': return 1;
		case'*': case'/': return 2;
	}
	return -1;
}

void infix_to_postfix(char *exp){
	int i, idx=0, len=strlen(exp);
	char ch, top_op;
	char *tmp = (char*)malloc(sizeof(char)*(len*2));
	memset(tmp, 0, sizeof(char)*(len*2));
	initStack(len);
	for(i=0; i<len; i++){
		ch=exp[i];
		switch(ch){
			case'(':
				push(ch);
				break;
			case')':
				top_op=pop();
				while(top_op!='('){
					tmp[idx++]=top_op;
					tmp[idx++]=' ';
					top_op=pop();
				}
				break;
			case'+': case'-': case'*': case'/':
				while(!isEmpty()&&prec(ch)<=prec(stack[top])){
					tmp[idx++]=pop();
					tmp[idx++]=' ';	
				}
				push(ch);
				break;
			default:
				tmp[idx++]=ch;
				if(exp[i+1] == '+' || exp[i+1] == '-' || exp[i+1] == '*' || exp[i+1] == '/' ||
					exp[i+1] == ')' || exp[i+1] == '\0')
						tmp[idx++] = ' ';
				break;
		}
	}
	while(!isEmpty())
		tmp[idx++]=pop();
	strcpy(exp, tmp);
	free(tmp);
}

int eval(char *exp){
	int op1, op2, i, j, value, cnt=0;
	char ch;
	for(i=0; i<strlen(exp); i++){
		ch=exp[i];
		if('0'<=ch && ch<='9'){
			value=0;
			while(exp[i+cnt]!=' ') cnt++;
			for(j=i; j<i+cnt; j++)
				value=value*10+(exp[j]-'0');
			//value=atoi(&exp[i]); // atoi는 공백이나 숫자가 아닌 문자까지 모두 숫자로 바꿔준다. 
			i+=cnt;
			cnt=0;
			intPush(value);
		}
		else{
			if(ch!=' '){
				op2=intPop();
				op1=intPop();
				switch(ch){
				case'+': intPush(op1+op2); break;
				case'-': intPush(op1-op2); break;
				case'*': intPush(op1*op2); break;
				case'/': intPush(op1/op2); break;
				}	
			}
		}
	}
	return intPop();
}

int main(){
	char exp[MAX];
	int result;
	printf("중위표기 입력 : ");
	scanf("%s", exp);
	infix_to_postfix(exp);
	printf("후위 표기: %s \n", exp);
	result=eval(exp);
	printf("결과값은 %d \n", result);
	free(intStack);
	free(stack);
	return 0;
}
