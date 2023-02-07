fun main(args: Array<String>) {
    val string = readLine()!!
    if (string[2] != string[3]) {
        println("No")
        return
    }
    // string[2] == string[3]
    if (string[4] == string[5]) {
        println("Yes")
    } else {
        println("No")
    }
}
