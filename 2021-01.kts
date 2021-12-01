#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/1
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readDepths(): List<String> {
    return FileReader("./2021-01.txt").readLines()
}

val input = readDepths().map { it.toInt() }

var count = 0
input.reduce { acc, curr -> curr.also { if (acc < curr) count++ } }

println(count) // 1502

/**
 * Part 2
 */

val result = input.reduceIndexed { index, acc, curr ->
    if (index < 3) return@reduceIndexed 0
    if (curr > input[index - 3]) acc + 1 else acc
}

println(result) // 1538
