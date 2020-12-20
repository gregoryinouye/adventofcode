#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/12
 */

import java.io.FileReader

fun readData(): List<String> = FileReader("./2020-13.txt").readLines()
val input = readData()

val timestamp = input.first().toInt()
val ids = input[1].split(',')
    .mapNotNull { if (it == "x") null else it.toInt() }

var minutes: Int = timestamp - 1
var bus: Int? = null

while (bus == null) {
    minutes++

    for (id in ids) {
        if (minutes % id == 0) {
            bus = id
            break
        }
    }
}

println("Part One: ${bus!! * (minutes - timestamp)}")
// 115

/**
 * Part 2
 */
//val minimum =
val maximum = 41L * 37L * 659L * 23L * 13L * 19L * 29L * 937L * 17L

//var finalTime: Long? = null
////var attempt: Long = 1000000000000
//var attempt: Long = 0
//var time: Long = 0
var base: Long = 0

//val busIdIndexes = mutableListOf<Int>()
//
//val busIds: List<Long> = input[1].split(',')
//    .mapIndexed { index, id ->
//        if (id == "x") {
//            0
//        } else {
//            busIdIndexes.add(index)
//            id.toLong()
//        }
//    }

//val busIdIndexes = mutableListOf<Int>()
//
//val busIds: List<Pair<Long, Int>> = input[1].split(',')
//    .mapIndexedNotNull { index, id ->
//        if (id == "x") null else Pair(id.toLong(), index)
//    }.sortedBy { it.first }
//    .reversed()
//
//var completedPrimes: Long = 1

//val final =
//
//    //busIds
//    listOf(Pair(19L, 3), Pair(17L, 0), Pair(13L, 2))
//        .fold(19L * 17L * 13L) { acc, (prime, index) ->
//            println(acc)
//
//            var multiple: Long = 0
//
//            do {
//                multiple++
//                val remainder = (acc * multiple + index) % prime
//
//            } while (remainder != index.toLong())
//
//            return@fold multiple * acc + index
//        }
//
//println(final)


val busIdIndexes = mutableListOf<Int>()

val busIds: List<Pair<Long, Int>> = input[1].split(',')
    .mapIndexedNotNull { index, id ->
        if (id == "x") null else Pair(id.toLong(), index)
    }.sortedBy { it.first }
    .reversed()

var completedPrimes: Long = 67L
val final =

    //busIds
//    listOf(17L, 0L, 13L, 19L)
    listOf(67L, 7L, 59L, 61L)
        .reduceIndexed { index, acc, prime ->
            println(acc)
            if (prime == 0L) return@reduceIndexed acc

            var multiple: Long = -1

            do {
                multiple++
                val remainder = (acc + multiple * completedPrimes) % prime

                println("acc: $acc, multiple: $multiple, remainder: $remainder, completedPrimes: $completedPrimes, prime: $prime")
            } while (remainder != index.toLong())

            val found = acc + multiple * completedPrimes
            completedPrimes *= prime

            return@reduceIndexed found
        }

println(final)


//val busIdIndexesSorted: List<Int> = busIdIndexes.sortedBy { busIds[it] }.reversed()

// for each number, find the base number that gives the correct remainder

//for (index in busIdIndexesSorted) {
//    val currentPrime: Long = busIds[index] // 937
//    var multiple: Long = -1
//
//    do {
//        multiple++
//        val remainder = (base * multiple) % currentPrime
//
//    } while (remainder != index)
//
//    // set new base number here
//}
//
//println(base)


//val maxId: Int = busIds.maxOrNull()!!
//
//trying@ while (finalTime == null) {
//    attempt++
//
//    time = maxId * attempt - busIdIndexesSorted.first()
//    if (attempt % 10000000.toLong() == 0.toLong()) println(time)
//
//    for (index in busIdIndexesSorted) {
//        if ((time + index.toLong()) % busIds[index].toLong() != 0.toLong()) continue@trying
//    }
//
//    finalTime = time
//}
//
//println("Part Two: $finalTime")
