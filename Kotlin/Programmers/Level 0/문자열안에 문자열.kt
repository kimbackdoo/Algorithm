// 단지 str2가 str1에 포함되는지 확인하면 됨
// in 연산자를 활용하여 답을 구함

class Solution {
    fun solution(str1: String, str2: String): Int {
        return if (str2 in str1) 1 else 2 
    }
}
