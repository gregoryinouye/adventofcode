#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2019/day/1
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readFuelData(): List<String> {
    return FileReader("./2019-01.txt").readLines()
}

val input = readFuelData().map { it.toDouble() }

fun calcFuel(weight: Double): Double {
    return Math.floor(weight / 3) - 2
}

val result: Double = input.fold(0.toDouble()) { acc, curr -> acc + calcFuel(curr) }

println("Part One: ${result.toInt()}")
// 3262358

val result2: Double = input.fold(0.toDouble()) { acc, moduleWeight ->
    var totalFuel = calcFuel(moduleWeight)
    var fuel = calcFuel(totalFuel)
    while (fuel > 0) {
        totalFuel += fuel
        fuel = calcFuel(fuel)
    }
    return@fold acc + totalFuel
}

println("Part Two: ${result2.toInt()}")
// 4890696
