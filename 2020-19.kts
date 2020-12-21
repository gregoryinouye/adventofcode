#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/19
 */

import java.io.FileReader

fun readData(): List<String> = FileReader("./2020-19.txt").readLines()
val input = readData()

val rules = mutableMapOf<String, List<String>>()
val messages = mutableListOf<String>()
var isRule = true

for (line in input) {
    if (line == "") {
        isRule = false
        continue
    }

    if (isRule) {
        val rule = line.split(": ", " ")
        val ruleName = rule[0]
        val ruleComponents = rule.subList(1, rule.size)
            .map { if (it.contains('\"') it.split(")[1] else it) }
        rules.put(ruleName, ruleComponents)
    } else {
        messages.add(line)
    }
}

println(rules)

