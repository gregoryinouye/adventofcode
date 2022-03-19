#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/7
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-07.txt").readLines()
}

val input = readInput()
    .first()
    .split(',')
    .map { it.toInt() }
    .sorted()

val positionCount = MutableList(input.last() + 1) { 0 }

input.forEach { index -> positionCount[index]++ }

val cost = positionCount.foldIndexed(Int.MAX_VALUE) { index, acc, _ ->
    getCost(index, positionCount).takeIf { it < acc }
        ?: acc
}

println(cost) // 356992

fun getCost(newPosition: Int, positionCount: List<Int>): Int {
    return positionCount.foldIndexed(0) { index, acc, curr -> Math.abs(newPosition - index) * curr + acc }
}

/**
 * Part 2
 */

val positionCount2 = MutableList(input.last() + 1) { 0 }

input.forEach { index -> positionCount2[index]++ }

val cost2 = positionCount2.foldIndexed(Int.MAX_VALUE) { index, acc, _ ->
    getCost2(index, positionCount2).takeIf { it < acc }
        ?: acc
}

println(cost2) // 101268110

fun getCost2(newPosition: Int, positionCount: List<Int>): Int {
    return positionCount.foldIndexed(0) { index, acc, curr -> getSequenceSum(0, Math.abs(newPosition - index)) * curr + acc }
}

fun getSequenceSum(start: Int, end: Int): Int {
    return (start + end) * (end - start + 1) / 2
}
