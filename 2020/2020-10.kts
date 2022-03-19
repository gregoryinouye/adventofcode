#/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/10
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-10.txt").readLines()
val input = readData()

var currentJolt: Int = 0
var joltOne: Int = 0
var joltTwo: Int = 0
var joltThree: Int = 1

val adapters = input.map { it.toInt() }.sorted()

for (adapter in adapters) {
    when (adapter - currentJolt) {
        0 -> Unit
        1 -> joltOne++
        2 -> joltTwo++
        3 -> joltThree++
        else -> println("error")
    }

    currentJolt = adapter
}

println("Part One: ${joltOne * joltThree}")
// 2244

/**
 * Part 2
 */

// if there's a gap of three, then both of the adapters are essential
var combinations: Long = 1
var consecutive: Int = 0
var indexOfLastEssential: Int = -1
// var joltOfLastEssential: Int = 0

for ((index, adapter) in adapters.withIndex()) {
    if (index == adapters.size - 1 || adapters[index + 1] - adapter == 3) {
        // current adapter is essential
        // do some calculation
        when (consecutive) {
            1 -> combinations *= 2 // 2^1
            2 -> combinations *= 4 // 2^2
            3 -> combinations *= 7 // 2^3 - 1 since at least one must be used
        }
        println("at index $index multiplying by combination of $consecutive")

        // set essential values
        indexOfLastEssential = index
        consecutive = 0
    }

    // adapter is not essential
    consecutive++
    println("adding consecutive")
}

println("Part 2: $combinations")
// 3947645370368
