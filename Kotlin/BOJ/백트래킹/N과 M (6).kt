fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val numbers = readln().split(" ").map { it.toInt() }.sorted()
    val sb = StringBuilder()

    fun dfs(results: List<Int>, depth: Int) {
        if (results.size == m) {
            sb.append(results.joinToString(" "))
            sb.append("\n")
            return
        }

        for (i in depth until n) {
            dfs(results + numbers[i], i + 1)
        }
    }

    dfs(listOf(), 0)
    println(sb)
}