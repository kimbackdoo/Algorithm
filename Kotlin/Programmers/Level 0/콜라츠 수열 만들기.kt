class Solution {
    fun solution(n: Int): List<Int> {
        var target = n
        val answer = mutableListOf<Int>(target)
        while (target != 1) {
            if (target % 2 == 0) target /= 2
            else target = target * 3 + 1
            answer += target
        }
        
        return answer
    }
}