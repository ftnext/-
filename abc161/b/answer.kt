fun main(args: Array<String>) {
    val inputList1 = readLine()!!.split(' ').map { it.toInt() }
    val votes = readLine()!!.split(' ').map { it.toInt() }
    // val typeCountN = inputList1[0]
    val popularCountM = inputList1[1]
    val sumOfVotes = votes.sum()
    val validVotes = votes.filter { it >= sumOfVotes * 1.0 / (4*popularCountM) }
    // println(validVotes)
    // val validVotes = arrayOf<Int>()
    // for (vote in votes) {
    //     if (vote > sumOfVotes / (4*popularCountM))
    //         validVotes = validVotes + vote  // varでないので連結できていない plusAssign?
    // }
    if (validVotes.size >= popularCountM)
        println("Yes")
    else
        println("No")
}
