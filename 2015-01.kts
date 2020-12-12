#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2015/day/1
 */

import java.io.FileReader

fun readData(): List<String> {
    return FileReader("./2015-01.txt").readLines()
}

val input = readData().first()

var floor: Int = 0
var enterBasement: Int? = null

for ((index, char) in input.withIndex()) {
    when (char) {
        '(' -> floor++
        ')' -> floor--
    }

    if (floor < 0 && enterBasement == null) enterBasement = index + 1
}

println("Part One: $floor")
// 232

println("Part Two: $enterBasement")
// 1783
