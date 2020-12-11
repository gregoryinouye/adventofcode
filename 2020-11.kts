#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/11
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-11.txt").readLines()
val input = readData().map { it.toCharArray() }
val input2 = readData().map { it.toCharArray() }

fun shouldEmptySeat(row: Int, col: Int): Boolean {
    var occupied: Int = 0
    for (x in Math.max(0, col - 1)..Math.min(col + 1, input[0].count() - 1)) {
        for (y in Math.max(0, row - 1)..Math.min(row + 1, input.count() - 1)) {
            when {
                y == row && x == col -> Unit
                input[y][x] == '#' -> occupied++
            }
        }
    }
    return occupied >= 4
}

fun shouldOccupySeat(row: Int, col: Int): Boolean {
    for (x in Math.max(0, col - 1)..Math.min(col + 1, input[0].count() - 1)) {
        for (y in Math.max(0, row - 1)..Math.min(row + 1, input.count() - 1)) {
            when {
                y == row && x == col -> Unit
                input[y][x] == '#' -> return false
            }
        }
    }
    return true
}

do {
    val coordinates = mutableSetOf<Pair<Int, Int>>()

    for ((row, rowData) in input.withIndex()) {
        for ((col, chair) in rowData.withIndex()) {
            val flipSeat = when (chair) {
                'L' -> shouldOccupySeat(row, col)
                '#' -> shouldEmptySeat(row, col)
                else -> false
            }
            if (flipSeat) coordinates.add(Pair(row, col))
        }
    }

    for ((row, col) in coordinates) {
        input[row][col] = if (input[row][col] == 'L') '#' else 'L'
    }

} while (coordinates.size > 0)

var count: Int = 0
for (row in input) {
    for (char in row) {
        if (char == '#') count++
    }
}

println("Part One: $count")
// 2412

/**
 * Part 2
 */

fun shouldEmptySeatWithVision(row: Int, col: Int): Boolean {
    var occupied: Int = 0
    for (x in Math.max(0, col - 1)..Math.min(col + 1, input2[0].count() - 1)) {
        for (y in Math.max(0, row - 1)..Math.min(row + 1, input2.count() - 1)) {
            when {
                y == row && x == col -> Unit
                input2[y][x] == '#' -> occupied++
                input2[y][x] == '.' -> {
                    val dx = x - col
                    val dy = y - row

                    var newX = x + dx
                    var newY = y + dy

                    while (newX >= 0 && newY >= 0 && newX <= input2[0].count() - 1 && newY <= input2.count() - 1) {
                        when (input2[newY][newX]) {
                            '#' -> {
                                occupied++
                                break
                            }
                            '.' -> {
                                newX += dx
                                newY += dy
                            }
                            'L' -> break
                        }
                    } 
                }
            }
        }
    }
    return occupied >= 5
}

fun shouldOccupySeatWithVision(row: Int, col: Int): Boolean {
    for (x in Math.max(0, col - 1)..Math.min(col + 1, input2[0].count() - 1)) {
        for (y in Math.max(0, row - 1)..Math.min(row + 1, input2.count() - 1)) {
            when {
                y == row && x == col -> Unit
                input2[y][x] == '#' -> return false
                input2[y][x] == '.' -> {
                    val dx = x - col
                    val dy = y - row

                    var newX = x + dx
                    var newY = y + dy

                    while (newX >= 0 && newY >= 0 && newX <= input2[0].count() - 1 && newY <= input2.count() - 1) {
                        when (input2[newY][newX]) {
                            '#' -> return false
                            
                            '.' -> {
                                newX += dx
                                newY += dy
                            }

                            'L' -> break
                        }
                    }
                }
            }
        }
    }
    return true
}

do {
    val coordinates = mutableSetOf<Pair<Int, Int>>()

    for ((row, rowData) in input2.withIndex()) {
        for ((col, chair) in rowData.withIndex()) {
            val flipSeat = when (chair) {
                'L' -> shouldOccupySeatWithVision(row, col)
                '#' -> shouldEmptySeatWithVision(row, col)
                else -> false
            }

            if (flipSeat) coordinates.add(Pair(row, col))
        }
    }

    for ((row, col) in coordinates) {
        input2[row][col] = if (input2[row][col] == 'L') '#' else 'L'
    }

} while (coordinates.size > 0)

var count2 = 0
for (row in input2) {
    for (char in row) {
        if (char == '#') count2++
    }
}

println("Part Two: $count2")
// 2176
