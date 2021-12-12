#!/usr/bin/env kotlin

/**
 *
 * https://adventofcode.com/2021/day/12
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-12.txt").readLines()
}

val paths = mutableMapOf<String, MutableSet<String>>()

val input = readInput().map { it.split('-') }
    .forEach { (pointA, pointB) ->
        paths.getOrPut(pointA, { mutableSetOf() })
            .add(pointB)

        paths.getOrPut(pointB, { mutableSetOf() })
            .add(pointA)
    }

val result = mutableListOf<String>()

findPath("start", listOf("start"))
result.count().also(::println) // 3887

fun findPath(name: String, history: List<String>, canVisitSmallTwice: Boolean = false) {
    paths.getOrDefault(name, mutableSetOf())
        .forEach {
            when {
                it == "end" -> result.add(history.plus("end").joinToString(","))
                it == "start" || (isSmallCave(it) && history.contains(it) && !canVisitSmallTwice) -> return@forEach
                isSmallCave(it) && history.contains(it) && canVisitSmallTwice -> findPath(it, history.plus(it), false)
                else -> findPath(it, history.plus(it), canVisitSmallTwice)
            }
        }
}

fun isSmallCave(name: String): Boolean {
    return name.first().isLowerCase()
}

/**
 * Part 2
 */

result.clear()

findPath("start", listOf("start"), true)
result.count().also(::println) // 104834
