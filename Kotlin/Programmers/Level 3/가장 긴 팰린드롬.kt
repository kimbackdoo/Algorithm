import kotlin.math.max

class Solution {
    fun solution(s: String): Int {
        var answer = 1
        for (i in s.indices) {
            answer = max(answer, palindromeLength(s, i - 1, i + 1))
            answer = max(answer, palindromeLength(s, i, i + 1))
        }

        return answer
    }

    fun palindromeLength(s: String, left: Int, right: Int): Int {
        var l = left
        var r = right
        while (0 <= l && r < s.length && s[l] == s[r]) {
            l -= 1
            r += 1
        }

        return r - l - 1
    }
}