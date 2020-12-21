#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/13
 */

import java.io.FileReader

fun readData(): List<String> = FileReader("./2020-13.txt").readLines()
val input = readData()

val timestamp = input.first().toLong()
val ids = input[1].split(',')
    .mapNotNull { if (it == "x") null else it.toLong() }

var minutes: Long = timestamp - 1
var bus: Long? = null

while (bus == null) {
    minutes++

    for (id in ids) {
        if (minutes % id == 0L) {
            bus = id
            break
        }
    }
}

println("Part One: ${bus!! * (minutes - timestamp)}")
// 115

/**
 * Part 2
 */

val busIds: List<Pair<Long, Int>> = input[1].split(',')
    .mapIndexedNotNull { index, id ->
        if (id == "x") null else Pair(id.toLong(), index)
    }.sortedBy { it.first }
    .reversed()

var completedPrimes: Long = 1L

val partTwo = busIds.fold(1L) { acc, (prime, index) ->
        var multiple: Long = -1

        do {
            multiple++
            val remainder = (acc + multiple * completedPrimes) % prime
        } while (remainder != (prime - (index.toLong() % prime)) % prime)

        val found = acc + multiple * completedPrimes
        completedPrimes *= prime

        return@fold found
    }

println("Part Two: $partTwo")
// 756261495958122
