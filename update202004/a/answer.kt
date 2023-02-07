fun main(args: Array<String>) {
    val inputList = readLine()!!.split(' ').map { it.toInt() }
    val nowS = inputList[0]
    val roomL = inputList[1]
    val roomR = inputList[2]
    when {
        nowS < roomL -> println(roomL)
        roomR < nowS -> println(roomR)
        else -> println(nowS)
    }
}
