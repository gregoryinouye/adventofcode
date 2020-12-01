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

val sortedExpenses = input.sorted().reversed()

for (i in 0..sortedExpenses.size - 1) {
    for (j in i + 1..sortedExpenses.size - 1) {
        for (k in j + 1..sortedExpenses.size - 1) {
            if (sortedExpenses[i] + sortedExpenses[j] + sortedExpenses[k] == 2020) {
                println(sortedExpenses[i] * sortedExpenses[j] * sortedExpenses[k])
                // 263819430
                break
            }
        }
    }
}
