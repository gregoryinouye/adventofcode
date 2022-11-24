#!/usr/bin/env kotlin

import java.io.FileReader

fun readData(): List<String> {
    return FileReader("./2015-03.txt").readLines()
}

val input = readData().first()

var x: Int = 0
var y: Int = 0
val visited = mutableSetOf<Pair<Int, Int>>(Pair(0, 0))

for (char in input) {
    when (char) {
        '>' -> x++
        '<' -> x--
        '^' -> y++
        'v' -> y--
    }
    visited.add(Pair(x, y))
}

println("Part One: ${visited.size}")
// 2081

visited.clear()
visited.add(Pair(0, 0))
x = 0
y = 0
var x1 = 0
var y1 = 0

for ((index, char) in input.withIndex()) {
    when (char) {
        '>' -> if (index % 2 == 0) x++ else x1++
        '<' -> if (index % 2 == 0) x-- else x1--
        '^' -> if (index % 2 == 0) y++ else y1++
        'v' -> if (index % 2 == 0) y-- else y1--
    }
    if (index % 2 == 0) visited.add(Pair(x, y)) else visited.add(Pair(x1, y1))
}

println("Part Two: ${visited.size}")
// 2341
