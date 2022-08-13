// 문제에서 요구한대로 출력하면 됨

// fun main(args: Array<String>) {
//     val (a, b) = readLine()!!.split(' ').map(String::toInt)
//     for (i in 1..b) {
//         for (j in 1..a) print("*")
//         println()
//     }
// }

// fun main(args: Array<String>) {
//     val (a, b) = readLine()!!.split(' ').map(String::toInt)
//     repeat(b) {
//         repeat(a) { print("*") }
//         println()
//     }
// }

fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    (1..b).forEach {
        (1..a).forEach { print("*") }
        println()
    }
}
