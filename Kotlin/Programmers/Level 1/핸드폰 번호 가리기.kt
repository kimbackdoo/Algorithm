// substring 메소드를 이용하여 번호 뒤 4자리를 자른 후, padStart 메소드를 활용하여 앞자리에 *를 붙임
// class Solution {
//     fun solution(phone_number: String): String {
//         val length = phone_number.length
//         return phone_number.substring(length - 4).padStart(length, '*')
//     }
// }

// takeLast 메소드를 이용하여 번호 뒤 자리를 구함
class Solution {
    fun solution(phone_number: String): String {
        val length = phone_number.length
        return phone_number.takeLast(4).padStart(length, '*')
    }
}
