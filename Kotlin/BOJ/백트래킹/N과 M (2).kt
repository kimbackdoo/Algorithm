fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }

    fun dfs(results: List<Int>, depth: Int) {
        if (results.size == m) {
            println(results.joinToString(" "))
            return
        }

        for (number in depth..n) {
            dfs(results + number, number + 1)
        }
    }

    dfs(listOf(), 1)
}