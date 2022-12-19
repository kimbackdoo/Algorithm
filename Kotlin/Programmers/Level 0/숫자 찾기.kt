// 주어진 num, k를 모두 문자열로 변환 후, indexOf 메소드를 사용하여 답을 구함
// indexOf의 값은 0부터 시작하므로 의미없는 문자열 "_"을 붙여 답을 구함
class Solution {
    fun solution(num: Int, k: Int): Int {
        return "_$num".indexOf(k.toString())
    }
}
