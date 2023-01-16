// 주어진 문자열에서 num1, num2 요소를 swap 하면 됨
class Solution {
    fun solution(my_string: String, num1: Int, num2: Int): String {
        val tmp = my_string[num1]

        val answer = my_string.toCharArray()
        answer[num1] = answer[num2]
        answer[num2] = tmp
        return answer.joinToString("")
    }
}
