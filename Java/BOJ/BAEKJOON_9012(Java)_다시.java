import java.io.*;

class Stack {
	private char[] stack;
	private int top;
	
	public Stack(int len) {
		stack = new char[len];
		top = -1;
	}
	
	public void push(char tmp) {
		stack[++top] = tmp;
	}
	
	public void pop() {
		top--;
	}
	
	public boolean isEmpty() {
		if(top == -1) return true;
		else return false;
	}
}

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for(int i=0; i<t; i++) {
			String ps = br.readLine();
			Stack s = new Stack(ps.length());
			char tmp;
			boolean check = true;
			
			for(int j=0; j<ps.length(); j++) {
				tmp = ps.charAt(j);
				if(tmp == '(') s.push(tmp);
				else {
					if(s.isEmpty()) {
						check = false;
						break;
					}
					s.pop();
				}
			}
			
			if(check && s.isEmpty()) System.out.println("YES");
			else System.out.println("NO");
		}
		br.close();
	}
}