#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/11
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-11.txt").readLines()
}

val input = readInput()
    .map { it.toList().map { Character.getNumericValue(it) }.toMutableList() }
val result = mutableListOf<Int>()

repeat(100) {
    result.add(step(input))
}
result.sum().also(::println) // 1793

fun step(grid: List<MutableList<Int>>): Int {
    var count = 0

    grid.forEachIndexed { rowIndex, row ->
        row.forEachIndexed { colIndex, energyLevel ->
            if (energyLevel == 9) {
                flash(rowIndex, colIndex, grid)
            } else {
                grid[rowIndex][colIndex]++
            }
        }
    }

    grid.forEachIndexed { rowIndex, row ->
        row.forEachIndexed { colIndex, energyLevel ->
            if (energyLevel > 9) {
                grid[rowIndex][colIndex] = 0
                count += 1
            }
        }
    }

    return count
}

fun flash(row: Int, column: Int, grid: List<MutableList<Int>>) {
    val curr = ++grid[row][column]

    if (curr == 10) {
        if (row > 0 && column > 0) flash(row - 1, column - 1, grid)
        if (row > 0) flash( row - 1, column, grid)
        if (row > 0 && column + 1 < grid[0].size) flash(row - 1, column + 1, grid)
        if (column > 0) flash(row, column - 1, grid)
        if (column + 1 < grid[0].size) flash( row, column + 1, grid)
        if (column > 0 && row + 1 < grid.size) flash( row + 1, column - 1, grid)
        if (row + 1 < grid.size) flash( row + 1, column, grid)
        if (column + 1 < grid[0].size && row + 1 < grid.size) flash( row + 1, column + 1, grid)
    }
}

/**
 * Part 2
 */

val input2 = readInput()
    .map { it.toList().map { Character.getNumericValue(it) }.toMutableList() }

var count = 0

do {
    count++
    val num = step(input2)
} while (num < 100)

println(count) // 247
