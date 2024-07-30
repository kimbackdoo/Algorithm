import java.util.StringTokenizer;
import java.io.*;

public class Main {
	static int n, m;
	static int[] list;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static void dfs(int cnt) throws IOException {
		if(cnt == m) {
			for(int i=0; i<m; i++)
				bw.write(String.valueOf(list[i]) + " ");
			bw.newLine();
			return;
		}
		
		for(int i=1; i<=n; i++) {
			if(cnt!=0 && list[cnt-1]>i) continue;
			list[cnt] = i;
			dfs(cnt+1);
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		list = new int[m];
		dfs(0);
		
		br.close();
		bw.flush();
		bw.close();
	}
}