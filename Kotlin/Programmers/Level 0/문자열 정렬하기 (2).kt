// 문자열을 모두 소문자로 변경 후, split 메소드를 이용하여 배열로 변환 후
// sorted 메소드를 이용하여 문자 오름차순 정렬 후
// joinToString 메소드를 이용하여 다시 문자열로 변환

class Solution {
    fun solution(my_string: String): String {
        return my_string.lowercase().split("").sorted().joinToString("")
    }
}
