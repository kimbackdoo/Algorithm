// i부터 j까지 순회하면서 해당 숫자에 k가 포함되어 있는지 counting
// class Solution {
//     fun solution(i: Int, j: Int, k: Int): Int {
//         var answer = 0
//         for (num in i..j) {
//             answer += num.toString().count { it.digitToInt() == k }
//         }

//         return answer
//     }
// }

// i부터 j의 까지 숫자를 나열 후 문자열로 변환
// 문자열에서 k의 개수를 counting
class Solution {
    fun solution(i: Int, j: Int, k: Int): Int {
        return (i..j).joinToString("").count { it.digitToInt() == k }
    }
}
