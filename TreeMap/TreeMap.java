package Assignment;

public class TreeMap {
	TreeMapNode topNode = null;
	public void add(Comparable key, Object value) {
		if (topNode == null)
			topNode = new TreeMapNode(key, value);
		else
			topNode.add(key, value);
	}
	public Object get(Comparable key) {
		return topNode == null ? null : topNode.find(key);
	}
	public void visitAll(TreeMapNode topNode) {
		if(topNode != null) {
			System.out.print(topNode.key() + "\n");
			visitAll(topNode.nodes[0]);
			visitAll(topNode.nodes[1]);
		}
	}
	public Object search(Comparable key) {
		if(topNode == null)
				System.out.println("null");
		else {
			if(topNode.search(key) == null)
				System.out.println("not found");
			else
				System.out.println(topNode.search(key));
		}
		return 0;
	}
}
