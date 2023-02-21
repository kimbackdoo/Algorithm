// 주어진 bin1, bin2를 10진수로 변환 후, 덧셈 결과를 2진수로 변환
class Solution {
    fun solution(bin1: String, bin2: String): String {
        return (bin1.toInt(2) + bin2.toInt(2)).toString(2)
    }
}
