#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/7
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-07.txt").readLines()

val input = readData()

val targetBag = "shiny gold"

val rules = mutableMapOf<String, Set<Pair<String, Int>>>()

for (rule in input) {
    val (color, innerBags) = rule.split(" bags contain ")
    val bagList = innerBags.split(", ")
        .filter { !it.contains("other") }
        .map {
            val bag = it.split(" ")
            Pair(bag.subList(1, bag.size - 1).joinToString(" "), bag[0].toInt())
        }
        .toSet()
    rules.put(color, bagList)
}

val validOuterBags = mutableSetOf<String>()

do {
    val previousSize = validOuterBags.size

    for ((outerBag, innerBags) in rules) {
        if (innerBags.any { (bag, _) -> bag in validOuterBags || bag == targetBag }) {
            validOuterBags += outerBag
        }
    }
} while (validOuterBags.size != previousSize)

println("Part One: ${validOuterBags.size}")
// 197

/**
 * Part 2
 */

var count = 0
var bags = mutableListOf<String>(targetBag)

while (!bags.isEmpty()) {
    val list = rules.get(bags.removeFirst())!!
    for ((bag, number) in list) {
        repeat(number) {
            bags.add(bag)
            count++
        }
    }
}

println("Part Two: $count")
// 85324
