// 주어진 문자열 my_string의 중복을 제거하기 위해 set을 사용
class Solution {
    fun solution(my_string: String): String {
        return my_string.toSet().joinToString("")
    }
}
