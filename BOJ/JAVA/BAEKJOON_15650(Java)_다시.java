import java.util.Scanner;

public class Main {
	static int n, m;
	static int[] list = new int[9];
	static int[] check = new int[9];
	
	static void dfs(int idx, int cnt) {
		if(cnt == m) {
			for(int i=0; i<m; i++)
				System.out.print(list[i] + " ");
			System.out.println();
			return;
		}
		
		for(int i=idx+1; i<=n; i++) {
			if(check[i]==1) continue;
			check[i] = 1;
			list[cnt] = i;
			dfs(i, cnt+1);
			check[i] = 0;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		
		dfs(0, 0);
		
		sc.close();
	}
}