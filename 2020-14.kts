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

fun calculateBit(bits: String): Long {
    var number = 0L
    var value = 1L
    for (i in bits.count() - 1 downTo 0) {
        when (bits[i]) {
            '0' -> Unit
            '1' -> number += value
        }
        value *= 2L
    }
    return number
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

val sum = mem.values.fold(0L) { acc, binary -> calculateBit(binary) + acc }

println("Part One: $sum")
// 18630548206046

/**
 * Part 2
 */

mem.clear()
val memory = mutableMapOf<Int, Long>()
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

fun calculateMemoryAddress(address: String): List<Int> {
    var addresses = mutableListOf<Int>(0)
    var value = 1
    for (i in address.count() - 1 downTo 0) {
        when (address[i]) {
            '0' -> Unit
            '1' -> addresses = addresses.map { it + value }.toMutableList()
            'X' -> addresses.addAll(addresses.map { it + value })
        }
        value *= 2
    }
    return addresses
}

for ((instruction, value) in input) {
    when (instruction) {
        "mask" -> mask = value
        else -> {
            val (_, address) = instruction.split('[', ']')

            val addresses = calculateMemoryAddress(
                applyMaskToMemoryAddress(mask, Integer.toBinaryString(address.toInt()).padStart(36, '0'))
            )

            addresses.forEach { memory[it] = value.toLong() }
        }
    }
}


//val sum2 = memory.values.reduce { acc, curr -> curr + acc }
val sum2 = memory.values.sum()
println("Part Two: $sum2")

// 650839011558 is too low
// 2973828803353 is too low
// 460498757095247 is incorrect, too high

