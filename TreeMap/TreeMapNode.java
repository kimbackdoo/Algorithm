package Assignment;

public class TreeMapNode {
	private final static int LESS = 0;
	private final static int GREATER = 1;
	private Comparable itsKey;
	private Object itsValue;
	protected TreeMapNode nodes[] = new TreeMapNode[2];
	public TreeMapNode(Comparable key, Object value) {
		itsKey = key;
		itsValue = value;
	}
	public Object key() {
		return itsKey;
	}
	public Object find(Comparable key) {
		if (key.compareTo(itsKey) == 0) return itsValue;
		return findSubNodeForKey(selectSubNode(key), key);
	}
	public Object search(Comparable key) {
		if(key.compareTo(itsKey) == 0) return itsKey;
		return findSubNodeForValue(selectSubNode(key), key);
	}
	private int selectSubNode(Comparable key) {
		return (key.compareTo(itsKey) < 0) ? LESS : GREATER;
	}
	private Object findSubNodeForKey(int node, Comparable key) {
		return nodes[node] == null ? null : nodes[node].find(key);
	}
	private Object findSubNodeForValue(int node, Comparable key) {
		return nodes[node] == null ? null : nodes[node].search(key);
	}
	public void add(Comparable key, Object value) {
		if (key.compareTo(itsKey) == 0)
			itsValue = value;
		else
			addSubNode(selectSubNode(key), key, value);
	}
	private void addSubNode(int node, Comparable key, Object value) {
		if (nodes[node] == null)
			nodes[node] = new TreeMapNode(key, value);
		else
			nodes[node].add(key, value);
	}
}