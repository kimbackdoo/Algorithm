fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val numbers = readln().split(" ").map { it.toInt() }.sorted()
    val sb = StringBuilder()

    fun dfs(results: List<Int>) {
        if (results.size == m) {
            sb.append(results.joinToString(" "))
            sb.append("\n")
            return
        }

        for (i in 0 until n) {
            dfs(results + numbers[i])
        }
    }

    dfs(listOf())
    println(sb)
}