// before, after 정렬 후, 순회하면서 다른 값이 있으면 0, 아니면 1 return
// class Solution {
//     fun solution(before: String, after: String): Int {
//         val sortedBefore = before.toList().sorted()
//         val sortedAfter = after.toList().sorted()
//         for (i in sortedBefore.indices) {
//             if (sortedBefore[i] != sortedAfter[i]) return 0
//         }

//         return 1
//     }
// }

// kotlin에서는 list 비교할 수 있음
// list 비교를 통해 before, after가 같은지 다른지 
class Solution {
    fun solution(before: String, after: String): Int {
        return if (before.toList().sorted() == after.toList().sorted()) 1 else 0
    }
}
