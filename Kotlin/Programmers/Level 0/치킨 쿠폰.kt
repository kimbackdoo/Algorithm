// 주어진 chicken 값을 10으로 나누면서 남은 쿠폰을 구하고,
// 주문한 치킨의 양을 더해나감
class Solution {
    fun solution(chicken: Int): Int {
        var answer = 0
        var coupon = chicken
        while (coupon >= 10) {
            answer += coupon / 10
            coupon = coupon / 10 + coupon % 10
        }

        return answer
    }
}
