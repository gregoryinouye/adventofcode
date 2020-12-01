#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/1
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readExpenseReport(): List<String> {
    return FileReader("./2020-01.txt").readLines()
}

val input = readExpenseReport().map { it.toInt() }

val expenses = mutableSetOf<Int>()

for (expense in input) {
    expenses.add(expense)

    if (expenses.contains(2020 - expense)) {
        println(expense * (2020 - expense))
        // 858496
        break
    }
}

/**
 * Part 2
 */

// val sortedExpenses = input.sort().reverse()

// var i = 0
// var j = 1
// var k = 2

// while (sortedExpenses[i] + sortedExpenses[j] + sortedExpenses[k] != 2020) {

// }
