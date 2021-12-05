#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/5
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-05.txt").readLines()
}

data class Coordinate(
    val x: Int,
    val y: Int,
)

val input = readInput()
    .map { it.split(",", " -> ") }
    .map { (x1, y1, x2, y2) -> listOf(Coordinate(x1.toInt(), y1.toInt()), Coordinate(x2.toInt(), y2.toInt())) }

val horizontalsAndVerticals = mutableListOf<List<Coordinate>>()
val diagonals = mutableListOf<List<Coordinate>>()
val vents = mutableSetOf<Coordinate>()
val intersections = mutableSetOf<Coordinate>()

input.forEach {
    if (it.first().x == it.last().x || it.first().y == it.last().y) {
        horizontalsAndVerticals.add(it)
    } else {
        diagonals.add(it)
    }
}

for (line in horizontalsAndVerticals) {
    getCoordinates(line).forEach { coordinate ->
        val isNewCoordinate = vents.add(coordinate)
        if (!isNewCoordinate) intersections.add(coordinate)
    }
}

println(intersections.size) // 8111

fun getCoordinates(line: List<Coordinate>): Set<Coordinate> {
    var xStart = line.first().x
    var yStart = line.first().y

    val xEnd = line.last().x
    val yEnd = line.last().y

    val dx = getIncrement(xStart, xEnd)
    val dy = getIncrement(yStart, yEnd)

    val coordinates = mutableSetOf<Coordinate>(Coordinate(xStart, yStart))

    while (xStart != xEnd || yStart != yEnd) {
        xStart += dx
        yStart += dy
        coordinates.add(Coordinate(xStart, yStart))
    }

    return coordinates
}

fun getIncrement(a: Int, b: Int): Int {
    return when {
        a < b -> 1
        a > b -> -1
        else -> 0
    }
}

/**
 * Part 2
 */

for (line in diagonals) {
    getCoordinates(line).forEach { coordinate ->
        val isNewCoordinate = vents.add(coordinate)
        if (!isNewCoordinate) intersections.add(coordinate)
    }
}

println(intersections.size) // 22088
