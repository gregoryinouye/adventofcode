#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/2
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readDirections(): List<String> {
    return FileReader("./2021-02.txt").readLines()
}

val input = readDirections()

var x = 0
var z = 0

input.forEach { instruction ->
    val direction = instruction.split(' ')[0]
    val magnitude = instruction.split(' ')[1].toInt()
    when (direction) {
        "forward" -> x += magnitude
        "down" -> z += magnitude
        "up" -> z -= magnitude
    }
}

println(x * z) // 1635930

/**
 * Part 2
 */

x = 0
z = 0
var aim = 0

input.forEach { instruction ->
    val direction = instruction.split(' ')[0]
    val magnitude = instruction.split(' ')[1].toInt()
    when (direction) {
        "forward" -> {
            x += magnitude
            z += (magnitude * aim)
        }
        "down" -> aim += magnitude
        "up" -> aim -= magnitude
    }
}

println(x * z) // 1781819478
