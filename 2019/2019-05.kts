#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2019/day/5
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readOpCodes(): List<String> {
    return FileReader("./2019-05.txt").readLines()
}

val input = readOpCodes()
    .first()
    .split(",")
    .map { it.toInt() }

class IntcodeComputer {
    lateinit var code: MutableList<Int>

    // Opcode 1 adds together numbers read from two positions and
    // stores the result in a third position.
    private fun add(position: Int) {
        val aPosition = code[position + 1]
        val bPosition = code[position + 2]
        val savePosition = code[position + 3]
        code[savePosition] = code[aPosition] + code[bPosition]
    }

    // Opcode 2 works exactly like opcode 1, except it multiplies
    // the two inputs instead of adding them
    private fun multiply(position: Int) {
        val aPosition = code[position + 1]
        val bPosition = code[position + 2]
        val savePosition = code[position + 3]
        code[savePosition] = code[aPosition] * code[bPosition]
    }

    // Opcode 3 takes a single integer as input and saves it to the
    // position given by its only parameter. For example, the instruction
    // 3,50 would take an input value and store it at address 50.
    private fun save(position: Int) {
        val savePosition = code[position + 1]
    }

    fun run(input: List<Int>): Int {
        code = input.toMutableList()
        var position = 0

        while (code[position] != 99) {
            when (code[position]) {
                1 -> add(position)
                2 -> multiply(position)
                3 -> save(position)
                99 -> break
                else -> throw RuntimeException("unknown op code")
            }
            position += 4
        }

        return code[0]
    }
}

val computer = IntcodeComputer()

println("Part One: ${computer.run(input)}") // 6730673

for (noun in 0..99) {
    for (verb in 0..99) {
        val modifiedInput = input.toMutableList()
        modifiedInput[1] = noun
        modifiedInput[2] = verb

        if (computer.run(modifiedInput) == 19690720) {
            println("Part Two: ${100 * noun + verb}") // 3749
            break
        }
    }
}
