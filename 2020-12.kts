#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/12
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> = FileReader("./2020-12.txt").readLines()
val input = readData()

fun calculateManhattanDistance(x: Int, y: Int): Int = Math.abs(x) + Math.abs(y)

fun calculatePosition(
    instructions: List<String>,
    initialDx: Int,
    initialDy: Int,
    shouldMoveShip: Boolean
): Pair<Int, Int> {
    var x: Int = 0
    var y: Int = 0
    var dx: Int = initialDx
    var dy: Int = initialDy

    for (instruction in instructions) {
        val direction = instruction[0]
        val magnitude = instruction.substring(1).toInt()

        when (direction) {
            'N' -> if (shouldMoveShip) y += magnitude else dy += magnitude
            'S' -> if (shouldMoveShip) y -= magnitude else dy -= magnitude
            'E' -> if (shouldMoveShip) x += magnitude else dx += magnitude
            'W' -> if (shouldMoveShip) x -= magnitude else dx -= magnitude
            'L' -> {
                val turns: Int = (magnitude / 90) % 4
                repeat(turns) {
                    val oldX = dx
                    dx = -dy
                    dy = oldX
                }
            }
            'R' -> {
                val turns: Int = (magnitude / 90) % 4
                repeat(turns) {
                    val oldX = dx
                    dx = dy
                    dy = -oldX
                }
            }
            'F' -> {
                repeat(magnitude) {
                    x += dx
                    y += dy
                }
            }
        }
    }
    return Pair(x, y)
}

val (x1, y1) = calculatePosition(input, 1, 0, true)
println("Part One: ${calculateManhattanDistance(x1, y1)}")
// 319

/**
 * Part 2
 */

val (x2, y2) = calculatePosition(input, 10, 1, false)
println("Part Two: ${calculateManhattanDistance(x2, y2)}")
// 50157
