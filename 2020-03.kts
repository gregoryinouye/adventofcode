#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/3
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> {
    return FileReader("./2020-03.txt").readLines()
}

val input = readData()

val slopes = listOf(Pair(3, 1), Pair(1, 1), Pair(5, 1), Pair(7, 1), Pair(1, 2))

var multiple: Long = 1

for ((dx, dy) in slopes) {
    var treeCount = 0
    var x = 0
    var y = 0

    while (y < input.size - 1) {
        x = (dx + x) % input[0].count()
        y += dy
        if (input[y][x] == '#') treeCount++
    }

    println(treeCount)
    multiple *= treeCount
}

// Part One: 268

println(multiple)
// Part Two: 3093068400
