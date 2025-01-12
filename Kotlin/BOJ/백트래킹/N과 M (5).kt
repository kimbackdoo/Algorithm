fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val numbers = readln().split(" ").map { it.toInt() }.sorted()
    val visited = MutableList(n) { false }
    val sb = StringBuilder()

    fun dfs(results: List<Int>) {
        if (results.size == m) {
            sb.append(results.joinToString(" "))
            sb.append("\n")
            return
        }

        for (i in numbers.indices) {
            if (!visited[i]) {
                visited[i] = true
                dfs(results + numbers[i])
                visited[i] = false
            }
        }
    }

    dfs(listOf())
    println(sb)
}