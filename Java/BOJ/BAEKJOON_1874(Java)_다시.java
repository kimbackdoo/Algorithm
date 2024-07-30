import java.util.*;

class Stack {
	private int[] stack;
	private int top;
	
	public Stack(int n) {
		stack = new int[n];
		top = -1;
	}
	
	public void push(int num) {
		stack[++top] = num;
	}
	
	public void pop() {
		top--;
	}
	
	public boolean isEmpty() {
		if(top == -1) return true;
		else return false;
	}
	
	public int peek() {
		return stack[top];
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList<String> al = new ArrayList<String>();
		Stack s = new Stack(n);
		int idx = 0;
		int[] arr = new int[n];
		
		for(int i=0; i<n; i++)
			arr[i] = sc.nextInt();
		
		for(int i=1; i<=n; i++) {
			s.push(i);
			al.add("+");
			while(!s.isEmpty() && arr[idx]==s.peek()) {
				idx++;
				s.pop();
				al.add("-");
			}
		}
		
		if(!s.isEmpty()) System.out.println("NO");
		else
			for(int i=0; i<al.size(); i++)
				System.out.println(al.get(i));
		
		sc.close();
	}
}