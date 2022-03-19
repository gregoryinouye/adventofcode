#!/usr/bin/env kotlin

/**
 *
 * https://adventofcode.com/2021/day/15
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.util.PriorityQueue

fun readInput(): List<String> {
    return FileReader("./2021-15.txt").readLines()
}

//val input = readInput().map { it.toList().map { Character.getNumericValue(it) } }
//val visited = mutableSetOf<Pair<Int, Int>>()
//val start = Pair(0, 0)
//val distance = mutableMapOf<Pair<Int, Int>, Int>(start to 0)
//
//fun getNeighbors(coordinate: Pair<Int, Int>): List<Pair<Int, Int>> {
//    val result = mutableListOf<Pair<Int, Int>>()
//    val (x, y) = coordinate
//    if (x > 0) result.add(Pair(x - 1, y))
//    if (x < input[0].size - 1) result.add(Pair(x + 1, y))
//    if (y > 0) result.add(Pair(x, y - 1))
//    if (y < input.size - 1) result.add(Pair(x, y + 1))
//
//    return result.toList()
//}
//
//fun getRisk(coordinate: Pair<Int, Int>): Int {
//    return input[coordinate.second][coordinate.first]
//}
//
//fun calculateRiskPaths(coordinate: Pair<Int, Int>) {
//    if (visited.contains(coordinate)) return
//    val neighbors = getNeighbors(coordinate)
////        .filter { it !in visited }
////        .also { println("$it: ${it.map { distance[it] }}") }
////        .sortedBy { distance[it] ?: Int.MAX_VALUE }.also { println(it) }
//    val totalRisk = distance.get(coordinate)!!
////    println("$coordinate totalRisk: $totalRisk")
//
//    neighbors.forEach { neighbor ->
//        val curr = distance.getOrDefault(neighbor, Int.MAX_VALUE)
//        (getRisk(neighbor) + totalRisk).takeIf { it < curr }
//            ?.also { distance.put(neighbor, it)
////                println("$neighbor saving new distance $it")
//            }
//    }
//
//    visited.add(coordinate)
//}
//
//
//calculateRiskPaths(start)
//
//while (distance.entries.filter { (coordinate, _) -> coordinate !in visited }.isNotEmpty()) {
//    distance.entries.filter { (coordinate, _) -> coordinate !in visited }
//        .sortedBy { it.value }
//        .firstOrNull()
//        ?.also { calculateRiskPaths(it.key) }
//}
////distance.also(::println)
//distance.get(Pair(input[0].size - 1, input.size - 1)).also(::println)

/**
 * Part 2
 */

val input = readInput().map { it.toList().map { Character.getNumericValue(it) } }
val visited = mutableSetOf<Pair<Int, Int>>()
val queue = PriorityQueue<Pair<Pair<Int, Int>, Int>>(compareBy<Pair<Pair<Int, Int>, Int>> { it.second } )
val start = Pair(0, 0)
val distance = mutableMapOf<Pair<Int, Int>, Int>(start to 0)

fun getNeighbors(coordinate: Pair<Int, Int>): List<Pair<Int, Int>> {
    val result = mutableListOf<Pair<Int, Int>>()
    val (x, y) = coordinate
    if (x > 0) result.add(Pair(x - 1, y))
    if (x < input[0].size * 5 - 1) result.add(Pair(x + 1, y))
    if (y > 0) result.add(Pair(x, y - 1))
    if (y < input.size * 5 - 1) result.add(Pair(x, y + 1))

    return result.toList()
}

fun getRisk(coordinate: Pair<Int, Int>): Int {
    return ((input[coordinate.second % input.size][coordinate.first % input[0].size] + coordinate.second / input.size + coordinate.first / input[0].size) % 10) + (((input[coordinate.second % input.size][coordinate.first % input[0].size] + coordinate.second / input.size + coordinate.first / input[0].size) / 10))
}

fun calculateRiskPaths(coordinate: Pair<Int, Int>) {
    if (visited.contains(coordinate)) return
    val neighbors = getNeighbors(coordinate)
        .filter { it !in visited }
    val totalRisk = distance.get(coordinate)!!

    neighbors.forEach { neighbor ->
        val curr = distance.getOrDefault(neighbor, Int.MAX_VALUE)
        (getRisk(neighbor) + totalRisk).takeIf { it < curr }
            ?.also {
                distance.put(neighbor, it)
                queue.add(Pair(neighbor, it))
            }
    }

    visited.add(coordinate)
}


calculateRiskPaths(start)

while (queue.isNotEmpty()) {
    if (visited.size % 100 == 0) println(visited.size)
    queue.poll()
        .let { (coordinate, _) -> calculateRiskPaths(coordinate) }
}
distance.get(Pair(input[0].size * 5 - 1, input.size * 5 - 1)).also(::println)
