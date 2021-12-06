#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/6
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-06.txt").readLines()
}

val fish = readInput().first()
    .split(",")
    .map { it.toInt() }

val fishDayCount = MutableList(9) { 0L }
fish.forEach { fishDayCount[it]++ }

repeat (80) {
    fishDayCount.removeFirst()
        .also {
            fishDayCount.add(it)
            fishDayCount[6] += it
        }
}

println(fishDayCount.sum()) // 377263

/**
 * Part 2
 */

fishDayCount.fill(0L)
fish.forEach { fishDayCount[it]++ }

repeat (256) {
    fishDayCount.removeFirst()
        .also {
            fishDayCount.add(it)
            fishDayCount[6] += it
        }
}

println(fishDayCount.sum()) // 1695929023803
