#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/4
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-04.txt").readLines()
}

data class Location(
    val board: Int,
    val position: Int,
)

val input = readInput()

val bingoNumbers = input.first().split(',')

val cardRows = input.drop(2)

val numbersToLocations = mutableMapOf<Int, MutableList<Location>>()

val boards = mutableListOf<List<Int>>()
val currentBoard = mutableListOf<Int>()

for (row in cardRows) {
    if (row.isEmpty()) {
        boards.add(currentBoard.toList())
        currentBoard.clear()
        continue
    }

    row.trim()
        .replace("\\s+".toRegex(), " ")
        .split(' ')
        .map { it.toInt() }
        .also { currentBoard.addAll(it) }
}

val bingoBoards = List(boards.size) { MutableList(boards.first().size) { 0 } }

for ((i, board) in boards.withIndex()) {
    for ((position, boardNumber) in board.withIndex()) {
        val location = Location(i, position)

        numbersToLocations.get(boardNumber)?.add(location)
            ?: numbersToLocations.put(boardNumber, mutableListOf(location))
    }
}

var bingoIndex = -1

while (checkBoards(bingoBoards) == null) {
    bingoIndex++
    val number = bingoNumbers[bingoIndex]
    for ((board, position) in numbersToLocations[number.toInt()]!!) {
        bingoBoards[board][position] = 1
    }
}

checkBoards(bingoBoards)!!
    .let { sumUnmarkedBoard(boards[it], bingoBoards[it]) }
    .let { it * bingoNumbers[bingoIndex].toInt() }
    .also { println(it) } // 32844

fun checkBoards(boards: List<List<Int>>): Int? {
    for ((i, board) in boards.withIndex()) {
        if (checkBoard(board)) return i
    }
    return null
}

fun checkBoard(board: List<Int>): Boolean {
    val numRows = 5
    val numColumns = board.size / numRows

    // check rows
    for (i in 0..(board.size - 1) step numColumns) {
        if (board.slice(i..i + numColumns - 1).all { it == 1 }) return true
    }

    // check columns
    for (i in 0..numColumns - 1) {
        if (board.slice(i..board.size - 1 step numColumns).all { it == 1 }) return true
    }

    return false
}

fun sumUnmarkedBoard(board: List<Int>, bingoBoard: List<Int>): Int {
    return board.foldIndexed(0) { index, acc, curr -> if (bingoBoard[index] == 1) acc else acc + curr }
}

/**
 * Part 2
 */

val bingoBoards2 = List(boards.size) { MutableList(boards.first().size) { 0 } }

var bingoIndex2 = -1
var lastBoardIndex = -1

while (bingoBoards2.any { !checkBoard(it) }) {
    bingoIndex2++
    val number = bingoNumbers[bingoIndex2]
    for ((board, position) in numbersToLocations[number.toInt()]!!) {
        bingoBoards2[board][position] = 1
    }
    lastBoardIndex = bingoBoards2.indexOfFirst { !checkBoard(it) }.takeIf { it > -1 } ?: lastBoardIndex
}

lastBoardIndex.let { sumUnmarkedBoard(boards[it], bingoBoards2[it]) }
    .let { it * bingoNumbers[bingoIndex2].toInt() }
    .also { println(it) }
