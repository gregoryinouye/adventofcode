#!/usr/bin/env kotlin

/**
 *
 * https://adventofcode.com/2021/day/13
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-13.txt").readLines()
}

val dots = readInput()
val coordinates = mutableSetOf<Pair<Int, Int>>()
val commands = mutableListOf<Pair<String, Int>>()
var isCommand = false

for (dot in dots) {
    if (dot.isEmpty()) {
        isCommand = true
        continue
    }

    if (!isCommand) {
        val (x, y) = dot.split(',').map { it.toInt() }
        coordinates.add(Pair(x, y))
    } else {
        val (direction, value) = dot.split(' ').last().split('=')
        commands.add(Pair(direction, value.toInt()))
    }
}

fun foldCoordinates(command: Pair<String, Int>, coordinates: MutableSet<Pair<Int, Int>>): Set<Pair<Int, Int>> {
    val setB = coordinates.filter { (x, y) -> (x.takeIf { command.first == "x" } ?: y) > command.second }
    coordinates.removeAll { (x, y) -> (x.takeIf { command.first == "x" } ?: y) >= command.second }

    setB.map { (x, y) ->
        val newX = x - (x - command.second) * 2
        val newY = y - (y - command.second) * 2

        if (command.first == "x") {
            Pair(newX, y).also { if (newX < 0) throw RuntimeException("negative X") }
        } else {
            Pair(x, newY).also { if (newY < 0) throw RuntimeException("negative Y") }
        }
    }.let { coordinates.addAll(it) }

    return coordinates
}

// 653

/**
 * Part 2
 */

commands.forEach { foldCoordinates(it, coordinates) }

List(6) { row -> List<String>(39) { col -> if (Pair(col, row) in coordinates) "#" else " " } }
    .forEach { println(it) } // LKREBPRK
