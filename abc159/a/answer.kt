fun main(args: Array<String>) {
    val inputList = readLine()!!.split(' ').map { it.toInt() }
    val evenCount = inputList[0]
    val oddCount = inputList[1]
    // evenCountから2つ選ぶ
    val selectFromEven = evenCount * (evenCount-1) / 2
    // oddCountから2つ選ぶ
    val selectFromOdd = oddCount * (oddCount-1) / 2
    val totalSelectCount = selectFromEven + selectFromOdd
    println(totalSelectCount.toString())
}
