fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val numbers = readln().split(" ").map { it.toInt() }.sorted()
    val visited = MutableList(n) { false }
    val sb = StringBuilder()

    fun dfs(results: List<Int> = listOf()) {
        if (results.size == m) {
            sb.append(results.joinToString(" "))
            sb.append("\n")
            return
        }

        for (i in numbers.indices) {
            val isDuplicated = i > 0 && numbers[i] == numbers[i - 1] && !visited[i - 1]
            if (visited[i] || isDuplicated) continue

            visited[i] = true
            dfs(results + numbers[i])
            visited[i] = false
        }
    }

    dfs()
    println(sb)
}