#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/15
 */

import java.io.FileReader

fun readData(): List<String> = FileReader("./2020-15.txt").readLines()
val input = readData().first().split(",").map { it.toInt() }

val history = mutableMapOf<Int, Int>()
var turn: Int = 1
var current: Int = 0

for (number in input) {
    current = history.get(number)?.let { turn - it }
        ?: 0
    history.put(number, turn)
    turn++
}

// default heap space of 1GB is too low, 3GB works (export JAVA_OPTS="-Xmx3g")
while (turn < 30_000_000) {
    current = history.get(current)?.let { previousTurn ->
        history.put(current, turn)
        turn - previousTurn
    } ?: 0.also { history.put(current, turn) }
    turn++
    if (turn == 2020) println("Part One: $current")
    // 234
}

println("Part Two: $current")
//8984
