#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/14
 */

import java.io.FileReader

fun readData(): List<String> = FileReader("./2020-14.txt").readLines()
val input = readData().map { it.split(" = ") }

fun applyMask(mask: String, memory: String): String {
    var ans: String = ""
    for (i in 0..mask.count() - 1) {
        ans += when (mask[i]) {
            '1' -> '1'
            '0' -> '0'
            else -> memory[i]
        }
    }
    return ans
}

val mem = mutableMapOf<Int, String>()
var mask: String = ""

for ((instruction, value) in input) {
    when (instruction) {
        "mask" -> mask = value
        else -> {
            val (_, address) = instruction.split('[', ']')
            mem[address.toInt()] = applyMask(
                mask,
                Integer.toBinaryString(value.toInt()).padStart(36, '0'),
            )
        }
    }
}

val sum = mem.values.fold(0L) { acc, binary -> binary.toLong(2) + acc }

println("Part One: $sum")
// 18630548206046

/**
 * Part 2
 */

mem.clear()
val memory = mutableMapOf<Long, Long>()
mask = ""

fun applyMaskToMemoryAddress(mask: String, memory: String): String {
    var ans: String = ""
    for (i in 0..mask.count() - 1) {
        ans += when (mask[i]) {
            '1' -> '1'
            'X' -> 'X'
            else -> memory[i]
        }
    }
    return ans
}

fun calculateMemoryAddress(address: String): List<Long> {
    var addresses = mutableListOf<Long>(0L)
    var value = 1L
    for (i in address.count() - 1 downTo 0) {
        when (address[i]) {
            '0' -> Unit
            '1' -> addresses = addresses.map { it + value }.toMutableList()
            'X' -> addresses.addAll(addresses.map { it + value })
        }
        value *= 2L
    }
    return addresses
}

for ((instruction, value) in input) {
    when (instruction) {
        "mask" -> mask = value
        else -> {
            val (_, address) = instruction.split('[', ']')

            applyMaskToMemoryAddress(mask, Integer.toBinaryString(address.toInt()).padStart(36, '0'))
                .let { calculateMemoryAddress(it) }
                .forEach { memory[it] = value.toLong() }
        }
    }
}

val sum2 = memory.values.sum()
println("Part Two: $sum2")
// 4254673508445
