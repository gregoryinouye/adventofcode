#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/5
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-05.txt").readLines()

val input = readData()

fun calculateSeatId(row: Int, col: Int): Int = row * 8 + col

fun calculateSeat(seatString: String, start: Int, end: Int): Int {
    var low = start
    var high = end

    for (bisect in seatString) {
        val average = (low + high).toDouble() / 2

        when (bisect) {
            'F', 'L' -> high = Math.floor(average).toInt()
            'B', 'R' -> low = Math.ceil(average).toInt()
        }
    }

    if (high != low) println("error")
    return low
}

val rowAndCol = input.map { Pair(it.substring(0, 7), it.substring(7)) }

var maxId = 0
val seatIds = mutableSetOf<Int>()

for ((rowString, colString) in rowAndCol) {
    val row = calculateSeat(rowString, 0, 127)
    val col = calculateSeat(colString, 0, 7)
    val seatId = calculateSeatId(row, col)

    if (seatId > maxId) maxId = seatId
    seatIds.add(seatId)
}
println("Part One: $maxId")
// 904

/**
 * Part 2
 */

for (i in maxId downTo 0) {
    if (!seatIds.contains(i)) {
        println("Part Two: $i")
        // 669
        break
    }
}
