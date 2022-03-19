#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/10
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-10.txt").readLines()
}

val input = readInput()
val values = mapOf(')' to 3, ']' to 57, '}' to 1197, '>' to 25137)

input.mapNotNull { parseLine(it) }
    .sumOf { values[it]!! }
    .also(::println) // 166191

fun parseLine(input: String): Char? {
    val stack = mutableListOf<Char>()

    for (paren in input) {
        when (paren) {
            '[', '(', '{', '<' -> stack.add(paren)
            ']' -> if (stack.removeLastOrNull() != '[') return paren
            ')' -> if (stack.removeLastOrNull() != '(') return paren
            '}' -> if (stack.removeLastOrNull() != '{') return paren
            '>' -> if (stack.removeLastOrNull() != '<') return paren
        }
    }
    return null
}

/**
 * Part 2
 */

val points = mutableMapOf(')' to 1, ']' to 2, '}' to 3, '>' to 4)

input.mapNotNull { completeLine(it) }
    .map { it.fold (0L) { acc, char -> 5 * acc + points[char]!! } }
    .sorted()
    .let { it[it.size / 2] }
    .also(::println) // 1152088313

fun completeLine(input: String): List<Char>? {
    val stack = mutableListOf<Char>()

    for (paren in input) {
        when (paren) {
            '[', '(', '{', '<' -> stack.add(paren)
            ']' -> if (stack.removeLastOrNull() != '[') return null
            ')' -> if (stack.removeLastOrNull() != '(') return null
            '}' -> if (stack.removeLastOrNull() != '{') return null
            '>' -> if (stack.removeLastOrNull() != '<') return null
        }
    }

    return stack.map {
        when (it) {
            '[' -> ']'
            '(' -> ')'
            '{' -> '}'
            '<' -> '>'
            else -> throw RuntimeException("error")
        }
    }.reversed()
}
