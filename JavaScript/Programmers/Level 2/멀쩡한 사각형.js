// 문제를 보면 가로 w만큼, 세로 h만큼 대각선이 지남 즉, (w + h) 만큼 사각형을 사용하지 못함
// 이때 대각선은 w, h의 최대공약수만큼 꼭지점을 지나기 때문에 w, h의 최대공약수 만큼 겹치는 부분이 생김
// 따라서 W * h - (w + h - gcd(w, h))라는 식을 세울 수 있음

function gcd(a, b) { // 최대공약수 구현, 유클리드 호제법
    while (a) {
        [a, b] = [b % a, a]; // 구조분해할당 문법을 이용하여 최대공약수를 구함
    }
    
    return b;
}

function solution(w, h) {
    return w * h - (w + h - gcd(w, h)); // 위 공식 적용
}
