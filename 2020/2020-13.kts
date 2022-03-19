#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/13
 */

import java.io.FileReader

fun readData(): List<String> = FileReader("./2020-13.txt").readLines()
val input = readData()

val timestamp = input.first().toLong()
val ids = input[1].split(',')
    .map { if (it == "x") null else it.toLong() }

var minutes: Long = timestamp - 1
var bus: Long? = null

while (bus == null) {
    minutes++

    for (id in ids) {
        if (id != null && minutes % id == 0L) {
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

var completedPrimes: Long = ids.firstOrNull { it != null }!!

val partTwo = ids.reduceIndexed { index, acc, prime ->
    if (prime == null) return@reduceIndexed acc

    var multiple: Long = -1

    do {
        multiple++
        val remainder = ((acc ?: 0L) + multiple * completedPrimes) % prime
    } while (remainder != (prime - (index.toLong() % prime)) % prime)

    val found = (acc ?: 0L) + multiple * completedPrimes
    completedPrimes *= prime

    return@reduceIndexed found
}

println("Part Two: $partTwo")
// 756261495958122
