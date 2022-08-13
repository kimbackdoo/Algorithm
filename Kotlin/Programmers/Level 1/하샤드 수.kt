// x를 문자열로 변환 후, split 연산, sumOf 메소드를 통해 x의 각 자리수의 합을 구함
class Solution {
    fun solution(x: Int): Boolean {
        val total = x.toString().split("").sumOf{ if (it.isNotEmpty()) it.toInt() else 0 }
        return x % total == 0
    }
}

// x를 10으로 나누어가면서 각 자리의 합을 구함
// 숫자 연산이므로 위 풀이보다 압도적으로 빠름
class Solution {
    fun solution(x: Int): Boolean {
        var copyX = x
        var total = 0
        while (copyX > 0) {
            total += copyX % 10
            copyX /= 10
        }
        
        return x % total == 0
    }
}
