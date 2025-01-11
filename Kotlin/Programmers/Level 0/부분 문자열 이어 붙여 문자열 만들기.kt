class Solution {
    fun solution(my_strings: Array<String>, parts: Array<IntArray>): String {
        return my_strings
            .mapIndexed { index, string -> string.slice(parts[index][0] .. parts[index][1]) }
            .joinToString("")
    }
}