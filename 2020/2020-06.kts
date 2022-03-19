#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/6
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-06.txt").readLines()

val input = readData()

var currentQuestions: Set<Char> = emptySet()
var count = 0

for ((index, person) in input.withIndex()) {
    currentQuestions = person.toCharArray() union currentQuestions
    if (person == "" || index == input.size - 1) {
        count += currentQuestions.size
        currentQuestions = emptySet()
    }
}

println("Part One: $count")
// 6596

/**
 * Part 2
 */

count = 0
var unanimousQuestions: Set<Char> = emptySet()

for ((index, person) in input.withIndex()) {
    if (index == 0 || input[index - 1] == "") {
        unanimousQuestions = person.toCharArray().toSet()
    }

    unanimousQuestions = person.toCharArray() intersect unanimousQuestions
    
    if (index == input.size - 1 || input[index + 1] == "") {
        count += unanimousQuestions.size
    }
}

println("Part Two: $count")
// 3219
