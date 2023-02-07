// TODO: listとmutableListで解いてみる
fun main(args: Array<String>) {
    val ballCountN = readLine()!!.toInt()
    var blueBalls = mutableListOf<Int>()  // mutableListにする必要なし
    var redBalls = mutableListOf<Int>()
    for (x in 1..ballCountN) {
        val line = readLine()!!.split(' ')
        when (line[1]) {
            "B" -> blueBalls.add(line[0].toInt())
            "R" -> redBalls.add(line[0].toInt())
        }
    }
    blueBalls.sort()
    redBalls.sort()
    for (ball in redBalls) println(ball)
    for (ball in blueBalls) println(ball)
}
