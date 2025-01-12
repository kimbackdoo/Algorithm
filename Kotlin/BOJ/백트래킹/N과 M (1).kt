fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }

    val numbers = List(n) { it + 1 }
    val visited = MutableList(n) { false }

    fun dfs(results: List<Int>) {
        if (results.size == m) {
            println(results.joinToString(" "))
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
}