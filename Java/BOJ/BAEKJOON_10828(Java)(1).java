import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		Stack<Integer> s = new Stack<Integer>();
		
		for(int i=0; i<n; i++) {
			String command = sc.next();
			
			if(command.equals("push")) {
				int x = sc.nextInt();
				s.push(x);
			}
			
			else if(command.equals("pop"))
				System.out.println(s.isEmpty() ? -1 : s.pop());
			
			else if(command.equals("size"))
				System.out.println(s.size());
			
			else if(command.equals("empty"))
				System.out.println(s.isEmpty() ? 1 : 0);
			
			else if(command.equals("top"))
				System.out.println(s.isEmpty() ? -1 : s.peek());
		}
		sc.close();
	}
}