// filterIndexed 메소드를 사용하여 code의 배수 요소들만 filtering
class Solution {
    fun solution(cipher: String, code: Int): String {
        return cipher.filterIndexed { index, _ -> (index + 1) % code == 0 }
    }
}
