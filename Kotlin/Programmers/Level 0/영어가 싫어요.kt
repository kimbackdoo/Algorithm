// HashMap을 이용하여 zero ~ nine을 0 ~ 9로 매핑시킨 후
// 순회하면서 replace 메소드를 이용하여 문자열 변환
// class Solution {
//     fun solution(numbers: String): Long {
//         var answer = numbers
//         val hashMap = hashMapOf(
//                 "zero" to "0",
//                 "one" to "1",
//                 "two" to "2",
//                 "three" to "3",
//                 "four" to "4",
//                 "five" to "5",
//                 "six" to "6",
//                 "seven" to "7",
//                 "eight" to "8",
//                 "nine" to "9",
//         )
//         for (entry in hashMap) {
//             val (key, value) = entry
//             answer = answer.replace(key, value)
//         }
//         return answer.toLong()
//     }
// }

// 함수형 프로그래밍을 이용하여 풀이
class Solution {
    fun solution(numbers: String): Long {
        return numbers
            .replace("zero", "0")
            .replace("one", "1")
            .replace("two", "2")
            .replace("three", "3")
            .replace("four", "4")
            .replace("five", "5")
            .replace("six", "6")
            .replace("seven", "7")
            .replace("eight", "8")
            .replace("nine", "9")
            .toLong()
    }
}
