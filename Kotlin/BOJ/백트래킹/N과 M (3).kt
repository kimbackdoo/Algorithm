fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val sb = StringBuilder()
    
    fun dfs(results: List<Int>) {
        if (results.size == m) {
            sb.append(results.joinToString(" "))
            sb.append("\n")
            return
        }

        for (number in 1..n) {
            dfs(results + number)
        }
    }

    dfs(listOf())
    println(sb)
}