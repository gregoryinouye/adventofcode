#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/9
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-09.txt").readLines()
}

val input = readInput().map { it.map { Character.getNumericValue(it) } }

input.flatMapIndexed { rowIndex, row ->
    row.mapIndexed { columnIndex, _ ->
        if (isLowPoint(columnIndex, rowIndex, input)) 1 + input[rowIndex][columnIndex] else 0
    }
}
    .sum()
    .also(::println) // 496

fun isLowPoint(column: Int, row: Int, input: List<List<Int>>): Boolean {
    val curr = input[row][column]

    return (row == 0 || input[row - 1][column] > curr) &&
        (column == 0 || input[row][column - 1] > curr) &&
        (row + 1 == input.size || input[row + 1][column] > curr) &&
        (column + 1 == input[0].size || input[row][column + 1] > curr)
}

/**
 * Part 2
 */

val grid = input.map { it.toMutableList() }
val basinSizes = mutableMapOf<Int, Int>()

input.forEachIndexed { rowIndex, row ->
    row.forEachIndexed { columnIndex, _ -> findBasin(columnIndex, rowIndex, null) }
}

basinSizes.map { (_, size) -> size }
    .sortedByDescending { it }
    .take(3)
    .reduce { acc, curr -> acc * curr }
    .also(::println) // 902880

fun findBasin(column: Int, row: Int, basin: Int?) {
    grid.getOrNull(row)
        ?.getOrNull(column)
        ?.takeUnless { it == 9 }
        ?: return

    grid[row][column] = 9

    val currBasin = basin ?: basinSizes.size

    basinSizes.getOrDefault(currBasin, 0)
        .let { basinSizes.put(currBasin, it + 1) }

    findBasin(column, row - 1, currBasin)
    findBasin(column - 1, row, currBasin)
    findBasin(column, row + 1, currBasin)
    findBasin(column + 1, row, currBasin)
}
