#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/8
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-08.txt").readLines()
}

val input = readInput()
    .map { it.split(" | ") }
    .map { it.last() }
    .map { it.split(" ") }

val easyNumberSizes = setOf(2, 3, 4, 7)

val count = input.fold(0) { acc, curr -> acc + curr.filter { it.length in easyNumberSizes }.size }

println(count) // 488

/**
 * Part 2
 */

val input2 = readInput().map { it.split(" | ") }

val sum = input2.map { (patterns, digits) ->
    val mapping = patterns.split(' ')
        .let { getPatternMapping(it) }

    digits.split(" ")
        .map { mapping[it.toSet()]!! }
        .joinToString("")
        .toInt()
}.sum()

println(sum) // 1040429

fun getPatternMapping(patterns: List<String>): Map<Set<Char>, Int> {
    lateinit var oneSet: Set<Char>
    lateinit var fourSet: Set<Char>
    val result = mutableMapOf<Set<Char>, Int>()

    patterns.sortedBy { it.length }
        .forEach { pattern ->
            val patternSet = pattern.toSet()
            when (pattern.length) {
                2 -> 1.also { oneSet = patternSet }
                3 -> 7
                4 -> 4.also { fourSet = patternSet }
                5 -> when {
                    (patternSet intersect oneSet).size == 2 -> 3
                    (patternSet intersect fourSet).size == 2 -> 2
                    else -> 5
                }
                6 -> when {
                    (patternSet intersect oneSet).size == 1 -> 6
                    (patternSet intersect fourSet).size == 4 -> 9
                    else -> 0
                }
                7 -> 8
                else -> throw RuntimeException("unexpected pattern: $pattern")
            }.also { result.put(patternSet, it) }
        }

    return result
}
