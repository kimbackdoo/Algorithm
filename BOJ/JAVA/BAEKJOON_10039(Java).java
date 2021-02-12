import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int score, total=0;
		Scanner sc = new Scanner(System.in);
		
		for(int i=0; i<5; i++) {
			score = sc.nextInt();
			if(score<40) score = 40;
			total += score;
		}
		System.out.println(total/5);
		sc.close();
	}
}