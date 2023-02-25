// id_pw가 db에 있는지 확인하기 위해
// associate 메소드를 사용하여 db를 map으로 변환
// 변환된 db에 id, pw가 있는지 확인하여 해당하는 값 return
class Solution {
    fun solution(id_pw: Array<String>, db: Array<Array<String>>): String {
        val mappedDb = db.associate { it[0] to it[1] }
        val pw = mappedDb[id_pw[0]]

        if (pw == null) return "fail"
        if (pw != id_pw[1]) return "wrong pw"
        return "login"
    }
}
