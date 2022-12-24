// s1, s2의 교집합을 구함
// class Solution {
//     fun solution(s1: Array<String>, s2: Array<String>): Int {
//         val s1Set = s1.toSet()
//         val s2Set = s2.toSet()
//         return s1Set.intersect(s2Set).size
//     }
// }

// count 메소드를 이용하여 교집합 구함
class Solution {
    fun solution(s1: Array<String>, s2: Array<String>): Int {
        // :: 의미는 참조를 뜻함
        // 즉, s1.count { s2.contains(it) } 와 같음
        return s1.count(s2::contains)
    }
}
