// 겹친 선분의 길이를 구하면 됨
import kotlin.math.*

class Solution {
    fun solution(lines: Array<IntArray>): Int {
        // 겹치는 선분들만 리스트로 저장
        val tmp = listOfNotNull(
            getOverlappedLine(lines[0], lines[1]),
            getOverlappedLine(lines[0], lines[2]),
            getOverlappedLine(lines[1], lines[2]),
        )
        
        // tmp의 길이가 3이면 즉, 모든 선분이 겹치면 end 값의 최대값 - start 값의 최소값을 return
        if (tmp.size == 3) return tmp.maxOf { it.last() } - tmp.minOf { it.first() }
        // 모든 선분이 겹치지 않으면, 각 end - start 값의 합을 return
        return tmp.sumOf { it.last() - it.first() }
    }
    
    // 두 선분이 겹치는지 확인하는 함수
    private fun isOverlapped(line1: IntArray, line2: IntArray): Boolean {
        return line1[0] <= line2[0] && line2[0] <= line1[1]
    }
    
    // 겹친 선분의 [start, end] 리스트를 반환하는 함수
    private fun getOverlappedLine(line1: IntArray, line2: IntArray): List<Int>? {
        val (sortedLine1, sortedLine2) = arrayOf(line1, line2).sortedBy { it.first() }
        if (!isOverlapped(sortedLine1, sortedLine2)) return null
        return listOf(max(line1[0], line2[0]), min(line1[1], line2[1]))
    }
}

// 배열에 겹치는 선분을 표시하여 정답을 구함
const val MAX_VALUE = 2

class Solution {   
    fun solution(lines: Array<IntArray>): Int {
        // start, end 값의 최소값이 -100, 최대값이 100 이므로 길이가 201인 배열 선언
        val table = IntArray(201)
        // lines 순회
        lines.forEach { (start, end) ->
            // start, end 값이 음수일 수 있고, 최소값이 -100 이므로 start, end에 + 100씩 하여 0부터 시작되도록함
            (start + 100 until end + 100).forEach {
                // table에서 해당 요소가 MAX_VALUE 보다 작으면 겹침 표시
                if (table[it] != MAX_VALUE) table[it]++
            }
        }
        // 겹치는 선분 counting
        return table.count { it == MAX_VALUE }
    }
}
