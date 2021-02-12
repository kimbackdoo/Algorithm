package Assignment;

public class TreeMapTest {
	public static void main(String[] args) {
		TreeMap Start = new TreeMap();
		Start.add("Martin", "martin");
		Start.add("Bob", "bob");
		Start.add("Robin", "robin");
		Start.add("Alan", "Alan");
		Start.add("Don", "don");
		Start.add("Paul", "paul");
		Start.add("Sam", "sam");
		System.out.println("----- visitAll() ----");
		Start.visitAll(Start.topNode);
		System.out.println("----- search -----");
		Start.search("Robin");
		Start.search("Sam");
		Start.search("JeaHun");
	}
}
