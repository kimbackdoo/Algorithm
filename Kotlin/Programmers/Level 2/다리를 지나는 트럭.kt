class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        val bridgeQueue = ArrayDeque<Int>()
        (1..bridge_length).forEach { bridgeQueue += 0 }
        
        val truckQueue = ArrayDeque<Int>()
        truck_weights.forEach { truckQueue += it }
        
        var answer = 0
        while (bridgeQueue.isNotEmpty()) {
            val truck = bridgeQueue.removeFirst()
            answer += 1
            
            if (truckQueue.isEmpty()) continue
            
            val currentWeight = bridgeQueue.sum() + truckQueue.first()
            bridgeQueue += if (currentWeight <= weight) truckQueue.removeFirst() else 0
        }
        
        return answer
    }
}