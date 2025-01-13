fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val numbers = readln().split(" ").map { it.toInt() }.sorted()
    val check = HashMap<List<Int>, Boolean>()
    val sb = StringBuilder()

    fun dfs(results: List<Int> = listOf(), depth: Int = 0) {
        if (results.size == m) {
            if (!check.containsKey(results)) {
                check[results] = true
                sb.append(results.joinToString(" "))
                sb.append("\n")
            }
            return
        }

        for (i in depth until n) {
            dfs(results + numbers[i], i)
        }
    }

    dfs()
    println(sb)
}