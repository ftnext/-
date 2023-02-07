fun main(args: Array<String>) {
    val sumOfMoney = readLine()!!.toInt()
    val count500yen = sumOfMoney / 500
    val restMoney = sumOfMoney % 500
    val count5yen = restMoney / 5
    val joyPoint = 1000 * count500yen + 5 * count5yen
    println(joyPoint)
}
