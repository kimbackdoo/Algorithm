// numlist를 주어진 조건대로 정렬
// numlist를 순회하면서 해당 숫자가 n과의 뺄셈을 기준으로 오름차순 정렬
// 뺄셈값이 같을 경우 큰수가 앞쪽에 정렬되게 함
// 뺄셈값이 같을 경우 큰수가 앞쪽에 정렬되게 하기 위해 * -1을 하여 계산
import kotlin.math.abs

class Solution {
    fun solution(numlist: IntArray, n: Int): IntArray {
        return numlist
            .sortedWith(compareBy({ abs(it - n) }, { it * -1 }))
            .toIntArray()
    }
}
