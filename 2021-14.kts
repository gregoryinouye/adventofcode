#!/usr/bin/env kotlin

/**
 *
 * https://adventofcode.com/2021/day/14
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-14.txt").readLines()
}

//val input = readInput()
//
//val polymer = input.first()
//val instructions = input.subList(2, input.size)
//    .map { it.split(" -> ") }
//    .associate { (pair, element) -> pair to element }
//
//fun insert(polymer: String, mapping: Map<String, String>): String {
//    val stringBuilder = StringBuilder()
//    for ((i, char) in polymer.withIndex()) {
//        stringBuilder.append(char)
//        if (i == polymer.length - 1) continue
//        mapping.get("$char${polymer[i + 1]}")
//            ?.also { stringBuilder.append(it[0]) }
//    }
//
//    return stringBuilder.toString()
//}
//
//var result = polymer
//
//repeat(10) { result = insert(result, instructions) }
//val count = mutableMapOf<Char, Int>()
//result.toList()
//    .forEach { char ->
//        count.getOrDefault(char, 0)
//            .also { count.put(char, it + 1) }
//    }
//
//count.toList()
//    .sortedBy { it.second }
//    .let { it.last().second - it.first().second } // 2967

/**
 * Part 2
 */

//val input = readInput()
//
//val polymer = input.first()
//val instructions = input.subList(2, input.size)
//    .map { it.split(" -> ") }
//    .associate { (pair, element) -> pair to element }
//
//val count = mutableMapOf<Char, Long>()
//
//for ((i, char) in polymer.withIndex()) {
////    if (i != 0) continue
//    if (i == polymer.length - 1) continue
//    val polymerPair = "$char${polymer[i + 1]}"
//
//    var result = polymerPair
//    repeat(10) { result = insert(result, instructions) }
//
//    result.toList()
//        .forEach { char ->
//            count.getOrDefault(char, 0L)
//                .also { count.put(char, it + 1L) }
//        }
//}
//
//fun insert(polymer: String, mapping: Map<String, String>, memo: Map<String, Map<String, Long>>): String {
//    val stringBuilder = StringBuilder()
//    for ((i, char) in polymer.withIndex()) {
//        stringBuilder.append(char)
//        if (i == polymer.length - 1) continue
//        mapping.get("$char${polymer[i + 1]}")
//            ?.also { stringBuilder.append(it[0]) }
//    }
//
//    return stringBuilder.toString()
//}
//
//count.toList()
//    .sortedBy { it.second }
//    .let { it.last().second - it.first().second second}

val input = readInput()

val polymer = input.first()
val instructions = input.subList(2, input.size)
    .map { it.split(" -> ") }
    .associate { (pair, element) -> pair to element }

fun insert(polymer: String, mapping: Map<String, String>): String {
    val stringBuilder = StringBuilder()
    for ((i, char) in polymer.withIndex()) {
        stringBuilder.append(char)
        if (i == polymer.length - 1) continue
        mapping.get("$char${polymer[i + 1]}")
            ?.also { stringBuilder.append(it[0]) }
    }

    return stringBuilder.toString()
}

var result = polymer

repeat(10) { result = insert(result, instructions) }
val count = mutableMapOf<Char, Int>()
result.toList()
    .forEach { char ->
        count.getOrDefault(char, 0)
            .also { count.put(char, it + 1) }
    }

count.toList()
    .sortedBy { it.second }
    .let { it.last().second - it.first().second } // 2967

