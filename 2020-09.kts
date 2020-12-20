#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/9
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-09.txt").readLines()
val input = readData()

val numbers = mutableMapOf<Long, MutableSet<Int>>()

for ((index, numberString) in input.withIndex()) {
    val number = numberString.toLong()

    numbers.get(number)
        ?.let { it += index }
        ?: numbers.put(number, mutableSetOf(index))

    if (index <= 25) continue

    var foundPair = false
    for (i in index downTo index - 25) {
        val targetNumber = number - input[i].toLong()
        if (numbers.containsKey(targetNumber)) {
            foundPair = true
            break
        }
    }

    if (!foundPair) {
        println("Part One: $number")
        // 776203571
        break
    }
}

/**
 * Part 2
 */

val searchNumber: Long = 776203571

// sliding window solution
var sum: Long = 0
var start: Int = 0
var end: Int = 0

while (sum != searchNumber) {
    when {
        sum > searchNumber -> {
            sum -= input[start].toLong()
            start++
        }

        sum < searchNumber -> {
            sum += input[end].toLong()
            end++
        }
    }
}

val range = input.subList(start, end).map { it.toLong() }.toSet()
println("Part Two: ${range.minOrNull()!! + range.maxOrNull()!!}")
// 104800569

// iterative solution
// var numberList = mutableListOf<Long>()

// for (index in input.size - 1 downTo 0) {
//     val number = input[index].toLong()

//     if (number >= searchNumber) continue

//     numberList = numberList.mapNotNull { (it + number).takeIf { it <= searchNumber } }
//         .toMutableList()
//         .add(number)

//     val foundIndex = numberList.indexOf(searchNumber)
    
//     if (foundIndex > -1) {
//         val range = input.subList(start, end).map { it.toLong() }.toSet()
//         println("Part Two: ${range.minOrNull()!! + range.maxOrNull()!!}")
//         break
//     }
// }
