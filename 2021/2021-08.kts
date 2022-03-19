#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/8
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-08.txt").readLines()
}

val input = readInput().map { it.split(" | ") }
val easyNumberLengths = setOf(2, 3, 4, 7)

input.flatMap { it.last().split(" ") }
    .count { it.length in easyNumberLengths }
    .also(::println) // 488

/**
 * Part 2
 */

input.map { (patterns, digits) ->
    val mapping = patterns.split(" ")
        .let { buildPatternMapping(it) }

    digits.split(" ")
        .map { mapping[it.toSet()]!! }
        .joinToString("")
        .toInt()
}
    .sum()
    .also(::println) // 1040429

fun buildPatternMapping(patterns: List<String>): Map<Set<Char>, Int> {
    lateinit var oneSet: Set<Char>
    lateinit var fourSet: Set<Char>

    return patterns.sortedBy { it.length }
        .map { it.toSet() }
        .associateWith { patternSet ->
            when (patternSet.size) {
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
                else -> throw RuntimeException("unexpected pattern: $patternSet")
            }
        }
}
