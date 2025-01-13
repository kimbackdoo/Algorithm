class Solution {
    fun solution(num: Int): Int {
        if (num == 1) return 0

        var answer = 0
        var n = num.toLong()
        while (n != 1L) {
            n = if (n % 2 == 0L) n / 2 else n * 3 + 1
            answer += 1
            if (answer >= 500) return -1
        }

        return answer
    }
}