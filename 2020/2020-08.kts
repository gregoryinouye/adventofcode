#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/8
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-08.txt").readLines()

val input = readData()

var accumulator: Int = 0

var i = 0
val visited = mutableSetOf<Int>()
val possibleChange = mutableSetOf<Int>()

while (i < input.size) {
    if (visited.contains(i)) break
    visited.add(i)

    val instruction = input[i]
    val (cmd, value) = instruction.split(" ")

    if (cmd == "jmp" || cmd == "nop") possibleChange.add(i)

    when (cmd) {
        "acc" -> accumulator += value.toInt()
        "jmp" -> i += value.toInt() - 1
    }

    i++
}

println("Part One: $accumulator")
// 1600

/**
 * Part 2
 */

for (modifyIndex in possibleChange) {
    accumulator = 0
    i = 0
    visited.clear()

    while (i < input.size) {
        if (visited.contains(i)) break
        visited.add(i)

        val instruction = input[i]
        var (cmd, value) = instruction.split(" ")

        if (i == modifyIndex) {
            if (cmd == "jmp") {
                cmd = "nop"
            } else {
                cmd = "jmp"
            }
        }

        when (cmd) {
            "acc" -> accumulator += value.toInt()
            "jmp" -> i += value.toInt() - 1
        }

        i++
    }
    
    if (i == input.size) println("Part Two: $accumulator")
    // 1543
}
