// 주어진 문자열을 순회하면서 대문자면 소문자로 변환, 소문자면 대문자로 변환 후 return
class Solution {
    fun solution(my_string: String): String {
        return my_string
            .map { if (it.isUpperCase()) it.lowercase() else it.uppercase() }
            .joinToString("")
    }
}
