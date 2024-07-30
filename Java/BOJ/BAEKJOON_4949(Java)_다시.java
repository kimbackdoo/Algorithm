import java.util.Scanner;

class Stack {
	private char[] stack;
	private int top;
	
	public Stack(int len) {
		stack = new char[len];
		top = -1;
	}
	
	public void push(char ch) {
		stack[++top] = ch;
	}
	
	public void pop() {
		top--;
	}
	
	public char peek() {
		return stack[top];
	}
	
	public boolean isEmpty() {
		if(top == -1) return true;
		else return false;
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		
		char ch;
		while(!str.equals(".")) {
			Stack s = new Stack(str.length());
			for(int i=0; i<str.length(); i++) {
				ch = str.charAt(i);
				if(ch=='(' || ch=='[') s.push(ch);
				else if(ch==')' || ch==']'){
					if(s.isEmpty() || (s.peek()=='(' && ch==']') || (s.peek()=='[' && ch==')')) {
						s.push(ch);
						break;
					}
					s.pop();
				}
			}
			if(s.isEmpty()) System.out.println("yes");
			else System.out.println("no");
			str = sc.nextLine();
		}
		sc.close();
	}
}