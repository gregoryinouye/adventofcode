#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/16
 */

import java.io.FileReader

fun readData(): List<String> = FileReader("./2020-16.txt").readLines()
val input = readData()

val validRanges: Map<String, Pair<Pair<Int, Int>, Pair<Int, Int>>> = input.subList(0, 20)
    .map { it.split(": ", " or ", "-") }
    .associate { (name, start1, end1, start2, end2) ->
        name to Pair(Pair(start1.toInt(), end1.toInt()), Pair(start2.toInt(), end2.toInt()))
    }

val myTicket = input.subList(22, 23)
    .flatMap { ticket -> ticket.split(",").map { it.toInt() } }

val nearbyTickets: List<List<Int>> = input.subList(25, 268)
    .map { ticket -> ticket.split(",").map { it.toInt() } }

var errorRate: Int = 0

nearbyTickets.forEach { ticket ->
    ticket.forEach { value ->
        if (!isValid(value, validRanges)) errorRate += value
    }
}

fun isValid(value: Int, ranges: Map<String, Pair<Pair<Int, Int>, Pair<Int, Int>>>): Boolean {
    for ((range1, range2) in ranges.values) {
        val (start1, end1) = range1
        val (start2, end2) = range2
        if ((value >= start1 && value <= end1) || (value >= start2 && value <= end2)) return true
    }

    return false
}

println("Part One: $errorRate")
// 29878

/**
 * Part 2
 */


fun isValidSet(value: Int, ranges: Map<String, Pair<Pair<Int, Int>, Pair<Int, Int>>>): Set<Int> {
    val valid = mutableSetOf<Int>()

    for ((index, rangePair) in ranges.values.withIndex()) {
        val (start1, end1) = rangePair.first
        val (start2, end2) = rangePair.second
        if ((value >= start1 && value <= end1) || (value >= start2 && value <= end2)) valid.add(index)
    }

    return valid
}

val filteredTickets = nearbyTickets.filter { ticket ->
    ticket.fold(true) {
        acc, curr -> acc && isValid(curr, validRanges)
    }
}

val maxAndMinValues = mutableMapOf<Int, Set<Int>>(
    0 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    1 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    2 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    3 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    4 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    5 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    6 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    7 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    8 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    9 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    10 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    11 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    12 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    13 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    14 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    15 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    16 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    17 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    18 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    19 to setOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
)

filteredTickets.forEach { ticket ->
    ticket.forEachIndexed { index, value ->
        val possible = maxAndMinValues.get(index)!!
        maxAndMinValues.put(index, isValidSet(value, validRanges) intersect possible)
    }
}

println(maxAndMinValues)

println(myTicket[15] * myTicket[5] * myTicket[14] * myTicket[0] * myTicket[17] * myTicket[10])
// 855438643439
