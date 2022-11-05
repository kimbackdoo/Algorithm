// common 배열의 개수가 최소 3개이므로
// 해당 배열이 등차수열인지, 등비수열인지 확인 후
// 등차수열이면 해당 배열의 마지막 값 + 공차
// 등비수열이면 해당 배열의 마지막 값 * 공차

class Solution {
    fun solution(common: IntArray): Int {
        val isEqual = common[1] - common[0] == common[2] - common[1]
        val diff = if (isEqual) common[1] - common[0]  else common[1] / common[0]
        return if (isEqual) common.last() + diff else common.last() * diff
    }
}
