fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val sb = StringBuilder()

    fun dfs(results: List<Int>, depth: Int) {
        if (results.size == m) {
            sb.append(results.joinToString(" "))
            sb.append("\n")
            return
        }

        for (number in depth..n) {
            dfs(results + number, number)
        }
    }

    dfs(listOf(), 1)
    println(sb)
}