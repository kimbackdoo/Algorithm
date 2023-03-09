// 최대공약수, 소인수분해를 구현해야 하는 난이도 있는 문제
// 문제 요구사항대로 구현하면 됨
// a % b가 나누어 떨어지면 유한소수
// b / 최대공약수의 소인수분해 값이 2, 5로만 이루어져 있으면 유한소수
// 나머지는 무한 소수
class Solution {
    fun solution(a: Int, b: Int): Int {
        // a % b가 나누어 떨어지면 유한소수
        val isInt = a % b == 0
        if (isInt) return 1

        val g = gcd(a, b)
        val pfs = primeFactorization(b / g, 2, setOf())
        // b / 최대공약수의 소인수분해 값이 2, 5로만 이루어져 있으면 유한소수
        val isFiniteDecimal = pfs.none { it != 2 && it != 5 }
        // 그 외 경우는 무한소수
        return if (isFiniteDecimal) 1 else 2
    }
    
    // 최대공약수 구하는 함수
    private tailrec fun gcd(a: Int, b: Int): Int = if (a != 0) gcd(b % a, a) else b
    
    // 매개변수의 소인수분해를 구하는 함수
    private tailrec fun primeFactorization(a: Int, divisor: Int, result: Set<Int>): List<Int> {
        if (a < 2) return result.toList()
        if (a % divisor == 0) return primeFactorization(a / divisor, divisor, result.plus(divisor))
        return primeFactorization(a, divisor + 1, result)
    }
}

// tailrec 키워드는 꼬리재귀일 경우 붙일 수 있는 키워드로
// 컴파일 단계에서 재귀함수를 반복문으로 변환해주어 최적화 시켜줌
// 참고
// https://kotlinlang.org/docs/functions.html#tail-recursive-functions
// https://thinkingfactory.tistory.com/457
