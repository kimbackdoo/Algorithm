// A를 순회하면서 문제에서 주어진대로 A를 밀고,
// B를 찾으면 해당 index return, 아니면 -1 return

// class Solution {
//     fun solution(A: String, B: String): Int {
//         // A와 B가 같으면 0 return
//         if (A == B) return 0

//         var tmp = A
//         // A 순회
//         for (i in 1..A.length + 1) {
//             // A 문자열 밀기
//             tmp = tmp.last() + tmp.dropLast(1)
//             // B랑 같으면 i return
//             if (tmp == B) return i
//         }
        
//         // B랑 같아지지 않으면 -1 return
//         return -1
//     }
// }

// (B + B)에서 A를 찾고, 해당 index return, 못찾으면 -1 return
class Solution {
    fun solution(A: String, B: String): Int = (B + B).indexOf(A)
}
