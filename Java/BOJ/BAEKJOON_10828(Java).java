import java.util.Scanner;

class Stack {
	private int[] stack;
	private int top;
	
	public Stack(int n) {
		stack = new int[n];
		top = -1;
	}
	
	public void push(int x) {
		stack[++top] = x;
	}
	
	public void pop() {
		if(top==-1) System.out.println(-1);
		else System.out.println(stack[top--]);
	}
	
	public void printSize() {
		System.out.println(top+1);
	}
	
	public void isEmpty() {
		if(top==-1) System.out.println(1);
		else System.out.println(0);
	}
	
	public void printTop() {
		if(top==-1) System.out.println(-1);
		else System.out.println(stack[top]);
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		Stack s = new Stack(n);
		
		for(int i=0; i<n; i++) {
			String command = sc.next();
			
			if(command.equals("push")) {
				int x = sc.nextInt();
				s.push(x);
			}
			else if(command.equals("pop")) s.pop();
			else if(command.equals("size")) s.printSize();
			else if(command.equals("empty")) s.isEmpty();
			else if(command.equals("top")) s.printTop();
		}
		sc.close();
	}
}